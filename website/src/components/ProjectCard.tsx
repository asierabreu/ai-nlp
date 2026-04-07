import Link from "next/link";
import { ExternalLink, FileText } from "lucide-react";
import GitHubIcon from "./GitHubIcon";
import type { Project } from "@/lib/types";

export type { Project };

export default function ProjectCard({ project }: { project: Project }) {
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

  return (
    <div className="card p-6 flex flex-col gap-4 group hover:-translate-y-1 hover:border-brand-200 dark:hover:border-brand-800">
      {/* Header */}
      <div className="flex items-start justify-between gap-3">
        <div className="flex items-center gap-3">
          <span className="text-3xl">{project.emoji}</span>
          <h3 className="text-lg font-semibold text-gray-900 dark:text-white leading-snug">
            {project.title}
          </h3>
        </div>
        <span
          className={`text-xs font-medium px-2 py-1 rounded-full shrink-0 ${statusColors[project.status]}`}
        >
          {statusLabels[project.status]}
        </span>
      </div>

      {/* Description */}
      <p className="text-sm text-gray-600 dark:text-gray-400 leading-relaxed flex-1">
        {project.description}
      </p>

      {/* Tags */}
      <div className="flex flex-wrap gap-2">
        {project.tags.map((tag) => (
          <span key={tag} className="tag">
            {tag}
          </span>
        ))}
      </div>

      {/* Links */}
      <div className="flex items-center gap-3 pt-2 border-t border-gray-100 dark:border-gray-800">
        {project.slug && (
          <Link
            href={`/projects/${project.slug}`}
            className="text-sm font-medium text-brand-600 dark:text-brand-400 hover:underline"
          >
            Details →
          </Link>
        )}
        <a
          href={project.githubUrl}
          target="_blank"
          rel="noopener noreferrer"
          className="inline-flex items-center gap-1 text-sm font-medium text-gray-600 dark:text-gray-400 hover:text-brand-600 dark:hover:text-brand-400 transition-colors"
          aria-label="View on GitHub"
        >
          <GitHubIcon className="w-3.5 h-3.5" />
          GitHub
        </a>
        {project.demoUrl && (
          <a
            href={project.demoUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-1 text-sm font-medium text-gray-600 dark:text-gray-400 hover:text-brand-600 dark:hover:text-brand-400 transition-colors"
          >
            <ExternalLink className="w-3.5 h-3.5" />
            Demo
          </a>
        )}
        {project.docsUrl && (
          <a
            href={project.docsUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-1 text-sm font-medium text-gray-600 dark:text-gray-400 hover:text-brand-600 dark:hover:text-brand-400 transition-colors"
          >
            <FileText className="w-3.5 h-3.5" />
            Docs
          </a>
        )}
      </div>
    </div>
  );
}
