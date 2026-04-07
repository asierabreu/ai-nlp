import type { NextPage } from "next";
import Head from "next/head";
import Header from "@/components/Header";
import Footer from "@/components/Footer";

const Contact: NextPage = () => {
  return (
    <>
      <Head>
        <title>Contact | AI/NLP Portfolio</title>
        <meta name="description" content="Get in touch about collaborations, questions, or contributions." />
      </Head>

      <div className="min-h-screen flex flex-col">
        <Header />

        <main className="flex-1 max-w-2xl mx-auto px-4 sm:px-6 lg:px-8 py-16 w-full">
          <div className="animate-slide-up">
            <h1 className="text-4xl font-bold text-gray-900 dark:text-white mb-4">
              Contact
            </h1>
            <p className="text-lg text-gray-600 dark:text-gray-400 mb-10">
              Interested in collaborating or have questions about the projects? Reach out!
            </p>

            <div className="space-y-4">
              {[
                {
                  label: "GitHub",
                  value: "@asierabreu",
                  href: "https://github.com/asierabreu",
                  icon: "💻",
                },
                {
                  label: "Repository",
                  value: "asierabreu/ai-nlp",
                  href: "https://github.com/asierabreu/ai-nlp",
                  icon: "📦",
                },
                {
                  label: "Issues",
                  value: "Open an issue",
                  href: "https://github.com/asierabreu/ai-nlp/issues",
                  icon: "🐛",
                },
              ].map((item) => (
                <a
                  key={item.label}
                  href={item.href}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="card flex items-center gap-4 p-5 hover:border-brand-300 dark:hover:border-brand-700 transition-colors"
                >
                  <span className="text-2xl">{item.icon}</span>
                  <div>
                    <div className="text-sm text-gray-500 dark:text-gray-400">
                      {item.label}
                    </div>
                    <div className="font-medium text-gray-900 dark:text-white">
                      {item.value}
                    </div>
                  </div>
                  <span className="ml-auto text-brand-500">→</span>
                </a>
              ))}
            </div>
          </div>
        </main>

        <Footer />
      </div>
    </>
  );
};

export default Contact;
