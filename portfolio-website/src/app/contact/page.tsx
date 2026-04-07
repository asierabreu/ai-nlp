import type { Metadata } from "next";
import { MessageSquare, Bug } from "lucide-react";
import GitHubIcon from "@/components/GitHubIcon";

export const metadata: Metadata = {
  title: "Contact",
  description: "Get in touch about collaborations, questions, or contributions.",
};

const contactItems = [
  {
    label: "GitHub",
    value: "@asierabreu",
    href: "https://github.com/asierabreu",
    icon: GitHubIcon,
    description: "Follow for updates",
  },
  {
    label: "Repository",
    value: "asierabreu/ai-nlp",
    href: "https://github.com/asierabreu/ai-nlp",
    icon: MessageSquare,
    description: "Browse the source code",
  },
  {
    label: "Issues",
    value: "Open an issue",
    href: "https://github.com/asierabreu/ai-nlp/issues",
    icon: Bug,
    description: "Report bugs or request features",
  },
];

export default function ContactPage() {
  return (
    <div className="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
      <div className="mb-12">
        <h1 className="text-4xl font-bold text-gray-900 dark:text-white mb-4">
          Contact
        </h1>
        <p className="text-lg text-gray-600 dark:text-gray-400">
          Interested in collaborating or have questions about the projects?
          Reach out via GitHub!
        </p>
      </div>

      <div className="space-y-4">
        {contactItems.map((item) => {
          const Icon = item.icon;
          return (
            <a
              key={item.label}
              href={item.href}
              target="_blank"
              rel="noopener noreferrer"
              className="card flex items-center gap-4 p-5 hover:border-brand-300 dark:hover:border-brand-700 transition-colors group"
            >
              <div className="p-2.5 bg-brand-50 dark:bg-brand-950/30 rounded-lg group-hover:bg-brand-100 dark:group-hover:bg-brand-900/30 transition-colors">
                <Icon className="w-5 h-5 text-brand-600 dark:text-brand-400" />
              </div>
              <div className="flex-1 min-w-0">
                <div className="text-xs text-gray-500 dark:text-gray-400 mb-0.5">
                  {item.label}
                </div>
                <div className="font-medium text-gray-900 dark:text-white truncate">
                  {item.value}
                </div>
                <div className="text-xs text-gray-500 dark:text-gray-400 mt-0.5">
                  {item.description}
                </div>
              </div>
              <span className="text-brand-500 group-hover:translate-x-0.5 transition-transform">
                →
              </span>
            </a>
          );
        })}
      </div>
    </div>
  );
}
