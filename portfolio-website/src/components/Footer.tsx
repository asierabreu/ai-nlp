import Link from "next/link";
import GitHubIcon from "./GitHubIcon";

export default function Footer() {
  return (
    <footer className="border-t border-gray-200 dark:border-gray-800 mt-24">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {/* Brand */}
          <div>
            <h3 className="text-lg font-bold text-brand-600 dark:text-brand-400 font-mono mb-3">
              AI/NLP Portfolio
            </h3>
            <p className="text-sm text-gray-600 dark:text-gray-400 leading-relaxed">
              Showcasing cutting-edge work in Natural Language Processing,
              Knowledge Graphs, and LLM fine-tuning.
            </p>
          </div>

          {/* Projects */}
          <div>
            <h4 className="font-semibold text-gray-900 dark:text-white mb-3">
              Projects
            </h4>
            <ul className="space-y-2 text-sm text-gray-600 dark:text-gray-400">
              {[
                { href: "/projects/nlp-knowledge-graph", label: "NLP Knowledge Graph" },
                { href: "/projects/llm-fine-tuning-toolkit", label: "LLM Fine-Tuning Toolkit" },
                { href: "/projects/domain-specific-llm", label: "Domain-Specific LLM" },
                { href: "/projects/text2kg-demo", label: "Text-to-KG Demo" },
                { href: "/projects/nlp-annotation-tool", label: "NLP Annotation Tool" },
              ].map((item) => (
                <li key={item.href}>
                  <Link
                    href={item.href}
                    className="hover:text-brand-600 dark:hover:text-brand-400 transition-colors"
                  >
                    {item.label}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          {/* Links */}
          <div>
            <h4 className="font-semibold text-gray-900 dark:text-white mb-3">
              Links
            </h4>
            <ul className="space-y-2 text-sm text-gray-600 dark:text-gray-400">
              <li>
                <a
                  href="https://github.com/asierabreu/ai-nlp"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-1.5 hover:text-brand-600 dark:hover:text-brand-400 transition-colors"
                >
                  <GitHubIcon className="w-3.5 h-3.5" />
                  GitHub Repository
                </a>
              </li>
              <li>
                <Link
                  href="/projects"
                  className="hover:text-brand-600 dark:hover:text-brand-400 transition-colors"
                >
                  All Projects
                </Link>
              </li>
              <li>
                <Link
                  href="/contact"
                  className="hover:text-brand-600 dark:hover:text-brand-400 transition-colors"
                >
                  Contact
                </Link>
              </li>
            </ul>
          </div>
        </div>

        <div className="mt-8 pt-8 border-t border-gray-200 dark:border-gray-800 text-center text-sm text-gray-500 dark:text-gray-500">
          <p>© {new Date().getFullYear()} AI/NLP Portfolio. MIT License.</p>
        </div>
      </div>
    </footer>
  );
}
