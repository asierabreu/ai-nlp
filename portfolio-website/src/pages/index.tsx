import type { GetStaticProps, NextPage } from "next";
import Head from "next/head";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import ProjectGrid from "@/components/ProjectGrid";
import type { Project } from "@/components/ProjectCard";
import projectsMetadata from "../../public/projects-metadata.json";

interface HomeProps {
  projects: Project[];
}

const Home: NextPage<HomeProps> = ({ projects }) => {
  return (
    <>
      <Head>
        <title>AI/NLP Portfolio</title>
        <meta
          name="description"
          content="Portfolio showcasing AI/NLP projects: knowledge graphs, LLM fine-tuning, and more."
        />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <div className="min-h-screen flex flex-col">
        <Header />

        <main className="flex-1">
          {/* Hero Section */}
          <section className="relative py-24 px-4 sm:px-6 lg:px-8 overflow-hidden">
            {/* Background gradient */}
            <div className="absolute inset-0 bg-gradient-to-br from-brand-50 via-white to-purple-50 dark:from-gray-950 dark:via-gray-950 dark:to-brand-950/20 -z-10" />

            <div className="max-w-4xl mx-auto text-center animate-slide-up">
              <div className="inline-flex items-center gap-2 px-4 py-2 bg-brand-100 dark:bg-brand-900/30 text-brand-700 dark:text-brand-300 rounded-full text-sm font-medium mb-6">
                <span>🤖</span>
                <span>NLP · Knowledge Graphs · LLM Fine-Tuning</span>
              </div>

              <h1 className="text-5xl sm:text-6xl font-bold text-gray-900 dark:text-white mb-6 leading-tight">
                AI/NLP{" "}
                <span className="text-transparent bg-clip-text bg-gradient-to-r from-brand-600 to-purple-600">
                  Portfolio
                </span>
              </h1>

              <p className="text-xl text-gray-600 dark:text-gray-400 mb-10 max-w-2xl mx-auto leading-relaxed">
                A collection of open-source projects exploring natural language
                processing, knowledge graph construction, and large language
                model fine-tuning.
              </p>

              <div className="flex flex-wrap items-center justify-center gap-4">
                <a href="#projects" className="btn-primary">
                  Explore Projects
                </a>
                <a
                  href="https://github.com/asierabreu/ai-nlp"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="btn-secondary"
                >
                  View on GitHub
                </a>
              </div>
            </div>
          </section>

          {/* Stats */}
          <section className="border-y border-gray-200 dark:border-gray-800 bg-gray-50 dark:bg-gray-900/50">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
              <div className="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
                {[
                  { value: "5", label: "Projects" },
                  { value: "3+", label: "NLP Frameworks" },
                  { value: "LoRA", label: "Fine-Tuning Method" },
                  { value: "MIT", label: "License" },
                ].map((stat) => (
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

          {/* Projects Grid */}
          <div id="projects">
            <ProjectGrid
              projects={projects}
              title="Featured Projects"
              subtitle="Explore AI/NLP projects spanning knowledge graph extraction, LLM fine-tuning, and interactive demos."
            />
          </div>

          {/* Tech Stack */}
          <section className="py-16 bg-gray-50 dark:bg-gray-900/50">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
              <h2 className="section-title text-center mb-12">Tech Stack</h2>
              <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
                {[
                  { category: "Frontend", items: ["Next.js", "React", "TypeScript", "Tailwind CSS"] },
                  { category: "NLP", items: ["spaCy", "Transformers", "NLTK", "FAISS"] },
                  { category: "LLM", items: ["PyTorch", "LoRA/QLoRA", "Weights & Biases", "PEFT"] },
                  { category: "Backend", items: ["FastAPI", "Neo4j", "Docker", "GitHub Actions"] },
                ].map((stack) => (
                  <div key={stack.category} className="card p-5">
                    <h3 className="font-semibold text-gray-900 dark:text-white mb-3">
                      {stack.category}
                    </h3>
                    <ul className="space-y-1">
                      {stack.items.map((item) => (
                        <li
                          key={item}
                          className="text-sm text-gray-600 dark:text-gray-400 font-mono"
                        >
                          {item}
                        </li>
                      ))}
                    </ul>
                  </div>
                ))}
              </div>
            </div>
          </section>
        </main>

        <Footer />
      </div>
    </>
  );
};

export const getStaticProps: GetStaticProps<HomeProps> = async () => {
  return {
    props: {
      projects: projectsMetadata.projects as Project[],
    },
  };
};

export default Home;
