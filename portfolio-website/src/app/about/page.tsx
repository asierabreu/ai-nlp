import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "About",
  description:
    "About the AI/NLP portfolio — skills, background, and research interests.",
};

const skills = [
  {
    category: "NLP",
    items: [
      "Named Entity Recognition",
      "Relation Extraction",
      "Text Classification",
      "Semantic Search",
    ],
  },
  {
    category: "LLM",
    items: [
      "Fine-Tuning (LoRA/QLoRA)",
      "Prompt Engineering",
      "RAG Systems",
      "Model Evaluation",
    ],
  },
  {
    category: "ML Engineering",
    items: [
      "PyTorch",
      "Hugging Face",
      "Experiment Tracking",
      "Model Deployment",
    ],
  },
  {
    category: "Infrastructure",
    items: ["Docker", "GitHub Actions", "FastAPI", "Neo4j"],
  },
];

const interests = [
  "Automated knowledge graph construction from unstructured text",
  "Parameter-efficient fine-tuning of large language models (LoRA, QLoRA)",
  "Domain adaptation and specialization of LLMs",
  "Information extraction: NER, relation extraction, event detection",
  "Graph neural networks for knowledge representation",
];

export default function AboutPage() {
  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
      {/* Hero */}
      <div className="mb-14">
        <h1 className="text-4xl font-bold text-gray-900 dark:text-white mb-4">
          About
        </h1>
        <p className="text-lg text-gray-600 dark:text-gray-400 leading-relaxed max-w-2xl">
          This portfolio showcases applied research and engineering projects at
          the intersection of Natural Language Processing, Knowledge Graphs, and
          Large Language Models. Each project is designed to be practical,
          reproducible, and production-ready.
        </p>
      </div>

      {/* Skills */}
      <section className="mb-14">
        <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">
          Skills & Technologies
        </h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
          {skills.map((skill) => (
            <div key={skill.category} className="card p-5">
              <h3 className="font-semibold text-brand-600 dark:text-brand-400 mb-3">
                {skill.category}
              </h3>
              <ul className="space-y-1">
                {skill.items.map((item) => (
                  <li
                    key={item}
                    className="text-sm text-gray-700 dark:text-gray-300 flex items-center gap-2"
                  >
                    <span className="w-1.5 h-1.5 rounded-full bg-brand-500 shrink-0" />
                    {item}
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </section>

      {/* Research Interests */}
      <section>
        <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-4">
          Research Interests
        </h2>
        <ul className="space-y-3 text-gray-600 dark:text-gray-400">
          {interests.map((interest) => (
            <li key={interest} className="flex items-start gap-3">
              <span className="text-brand-500 mt-0.5">→</span>
              <span>{interest}</span>
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
}
