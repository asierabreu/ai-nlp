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
              <li>
                <a href="#nlp-kg" className="hover:text-brand-600 dark:hover:text-brand-400 transition-colors">
                  NLP Knowledge Graph
                </a>
              </li>
              <li>
                <a href="#llm-toolkit" className="hover:text-brand-600 dark:hover:text-brand-400 transition-colors">
                  LLM Fine-Tuning Toolkit
                </a>
              </li>
              <li>
                <a href="#domain-llm" className="hover:text-brand-600 dark:hover:text-brand-400 transition-colors">
                  Domain-Specific LLM
                </a>
              </li>
              <li>
                <a href="#text2kg" className="hover:text-brand-600 dark:hover:text-brand-400 transition-colors">
                  Text-to-KG Demo
                </a>
              </li>
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
                  className="hover:text-brand-600 dark:hover:text-brand-400 transition-colors"
                >
                  GitHub Repository
                </a>
              </li>
              <li>
                <a href="/about" className="hover:text-brand-600 dark:hover:text-brand-400 transition-colors">
                  About
                </a>
              </li>
              <li>
                <a href="/contact" className="hover:text-brand-600 dark:hover:text-brand-400 transition-colors">
                  Contact
                </a>
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
