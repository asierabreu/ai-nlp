const stacks = [
  {
    category: "Frontend",
    items: ["Next.js", "React", "TypeScript", "Tailwind CSS"],
    icon: "🎨",
  },
  {
    category: "NLP",
    items: ["spaCy", "Transformers", "NLTK", "FAISS"],
    icon: "🧠",
  },
  {
    category: "LLM",
    items: ["PyTorch", "LoRA/QLoRA", "Weights & Biases", "PEFT"],
    icon: "🤖",
  },
  {
    category: "Backend",
    items: ["FastAPI", "Neo4j", "Docker", "GitHub Actions"],
    icon: "⚙️",
  },
];

export default function TechStack() {
  return (
    <section className="py-16 bg-gray-50 dark:bg-gray-900/50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <h2 className="section-title mb-4">Tech Stack</h2>
          <p className="text-lg text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">
            Modern tools and frameworks powering the portfolio projects.
          </p>
        </div>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
          {stacks.map((stack) => (
            <div
              key={stack.category}
              className="card p-5 hover:border-brand-200 dark:hover:border-brand-800"
            >
              <div className="flex items-center gap-2 mb-3">
                <span className="text-xl">{stack.icon}</span>
                <h3 className="font-semibold text-gray-900 dark:text-white">
                  {stack.category}
                </h3>
              </div>
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
  );
}
