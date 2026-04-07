import type { Metadata } from "next";
import Hero from "@/components/Hero";
import ProjectCard from "@/components/ProjectCard";
import TechStack from "@/components/TechStack";
import AnimatedSection from "@/components/AnimatedSection";
import projectsData from "@/content/projects.json";
import type { Project } from "@/lib/types";

export const metadata: Metadata = {
  title: "AI/NLP Portfolio",
  description:
    "Portfolio showcasing AI/NLP projects: knowledge graphs, LLM fine-tuning, and more.",
};

const projects = projectsData.projects as Project[];

const stats = [
  { value: "5", label: "Projects" },
  { value: "3+", label: "NLP Frameworks" },
  { value: "LoRA", label: "Fine-Tuning Method" },
  { value: "MIT", label: "License" },
];

export default function HomePage() {
  return (
    <>
      <Hero />

      {/* Stats */}
      <AnimatedSection>
        <section className="border-y border-gray-200 dark:border-gray-800 bg-gray-50 dark:bg-gray-900/50">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
            <div className="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
              {stats.map((stat) => (
                <div key={stat.label}>
                  <div className="text-3xl font-bold text-brand-600 dark:text-brand-400 font-mono">
                    {stat.value}
                  </div>
                  <div className="text-sm text-gray-600 dark:text-gray-400 mt-1">
                    {stat.label}
                  </div>
                </div>
              ))}
            </div>
          </div>
        </section>
      </AnimatedSection>

      {/* Featured Projects */}
      <AnimatedSection>
        <section id="projects" className="py-16">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="text-center mb-12">
              <h2 className="section-title mb-4">Featured Projects</h2>
              <p className="text-lg text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">
                Explore AI/NLP projects spanning knowledge graph extraction, LLM
                fine-tuning, and interactive demos.
              </p>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {projects.map((project, i) => (
                <AnimatedSection key={project.id} delay={i * 0.05}>
                  <ProjectCard project={project} />
                </AnimatedSection>
              ))}
            </div>
          </div>
        </section>
      </AnimatedSection>

      {/* Tech Stack */}
      <AnimatedSection>
        <TechStack />
      </AnimatedSection>
    </>
  );
}
