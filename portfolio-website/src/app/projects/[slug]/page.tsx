import type { Metadata } from "next";
import { notFound } from "next/navigation";
import Link from "next/link";
import { ExternalLink, FileText, ArrowLeft, CheckCircle2 } from "lucide-react";
import GitHubIcon from "@/components/GitHubIcon";
import projectsData from "@/content/projects.json";
import type { Project } from "@/lib/types";

const projects = projectsData.projects as Project[];

interface Props {
  params: { slug: string };
}

export function generateStaticParams() {
  return projects.map((p) => ({ slug: p.slug }));
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const project = projects.find((p) => p.slug === params.slug);
  if (!project) return { title: "Project Not Found" };
  return {
    title: project.title,
    description: project.description,
  };
}

const statusColors = {
  active: "bg-green-100 text-green-800 dark:bg-green-900/30 dark:text-green-400",
  wip: "bg-yellow-100 text-yellow-800 dark:bg-yellow-900/30 dark:text-yellow-400",
  planned: "bg-gray-100 text-gray-600 dark:bg-gray-800 dark:text-gray-400",
};

const statusLabels = {
  active: "Active",
  wip: "In Progress",
  planned: "Planned",
};

export default function ProjectPage({ params }: Props) {
  const project = projects.find((p) => p.slug === params.slug);
  if (!project) notFound();

  return (
    <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
      {/* Back */}
      <Link
        href="/projects"
        className="inline-flex items-center gap-1.5 text-sm text-gray-600 dark:text-gray-400 hover:text-brand-600 dark:hover:text-brand-400 transition-colors mb-8"
      >
        <ArrowLeft className="w-4 h-4" />
        Back to Projects
      </Link>

      {/* Header */}
      <div className="mb-8">
        <div className="flex items-start gap-4 mb-4">
          <span className="text-5xl">{project.emoji}</span>
          <div>
            <h1 className="text-3xl font-bold text-gray-900 dark:text-white mb-2">
              {project.title}
            </h1>
            <span
              className={`text-xs font-medium px-2.5 py-1 rounded-full ${statusColors[project.status]}`}
            >
              {statusLabels[project.status]}
            </span>
          </div>
        </div>

        {/* Tags */}
        <div className="flex flex-wrap gap-2">
          {project.tags.map((tag) => (
            <span key={tag} className="tag">
              {tag}
            </span>
          ))}
        </div>
      </div>

      {/* Description */}
      <div className="prose prose-gray dark:prose-invert max-w-none mb-8">
        <p className="text-lg text-gray-600 dark:text-gray-400 leading-relaxed">
          {project.longDescription ?? project.description}
        </p>
      </div>

      {/* Highlights */}
      {project.highlights && project.highlights.length > 0 && (
        <div className="card p-6 mb-8">
          <h2 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">
            Key Features
          </h2>
          <ul className="space-y-2">
            {project.highlights.map((h) => (
              <li
                key={h}
                className="flex items-start gap-2 text-gray-700 dark:text-gray-300"
              >
                <CheckCircle2 className="w-4 h-4 text-brand-500 mt-0.5 shrink-0" />
                <span className="text-sm">{h}</span>
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Links */}
      <div className="flex flex-wrap gap-3">
        <a
          href={project.githubUrl}
          target="_blank"
          rel="noopener noreferrer"
          className="btn-primary"
        >
          <GitHubIcon className="w-4 h-4" />
          View on GitHub
        </a>
        {project.demoUrl && project.demoUrl !== "#" && (
          <a
            href={project.demoUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="btn-secondary"
          >
            <ExternalLink className="w-4 h-4" />
            Live Demo
          </a>
        )}
        {project.docsUrl && (
          <a
            href={project.docsUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="btn-secondary"
          >
            <FileText className="w-4 h-4" />
            Documentation
          </a>
        )}
      </div>
    </div>
  );
}
