import type { Metadata } from "next";
import ProjectCard from "@/components/ProjectCard";
import AnimatedSection from "@/components/AnimatedSection";
import projectsData from "@/content/projects.json";
import type { Project } from "@/lib/types";

export const metadata: Metadata = {
  title: "Projects",
  description:
    "All AI/NLP portfolio projects — knowledge graphs, LLM fine-tuning, and more.",
};

const projects = projectsData.projects as Project[];

const statusOrder: Record<Project["status"], number> = {
  active: 0,
  wip: 1,
  planned: 2,
};

const sortedProjects = [...projects].sort(
  (a, b) => statusOrder[a.status] - statusOrder[b.status]
);

export default function ProjectsPage() {
  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
      <AnimatedSection>
        <div className="mb-12">
          <h1 className="text-4xl font-bold text-gray-900 dark:text-white mb-4">
            All Projects
          </h1>
          <p className="text-lg text-gray-600 dark:text-gray-400 max-w-2xl">
            A complete listing of AI/NLP projects spanning knowledge graph
            extraction, parameter-efficient LLM fine-tuning, and interactive
            demos.
          </p>
        </div>
      </AnimatedSection>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {sortedProjects.map((project, i) => (
          <AnimatedSection key={project.id} delay={i * 0.05}>
            <ProjectCard project={project} />
          </AnimatedSection>
        ))}
      </div>
    </div>
  );
}
