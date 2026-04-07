"use client";

import { motion } from "framer-motion";
import Link from "next/link";
import { ArrowRight, Sparkles } from "lucide-react";
import GitHubIcon from "./GitHubIcon";

export default function Hero() {
  return (
    <section className="relative py-24 px-4 sm:px-6 lg:px-8 overflow-hidden">
      {/* Background gradient */}
      <div className="absolute inset-0 bg-gradient-to-br from-brand-50 via-white to-purple-50 dark:from-gray-950 dark:via-gray-950 dark:to-brand-950/20 -z-10" />

      {/* Decorative blobs */}
      <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-brand-200/20 dark:bg-brand-900/10 rounded-full blur-3xl -z-10 translate-x-1/3 -translate-y-1/4" />
      <div className="absolute bottom-0 left-0 w-[400px] h-[400px] bg-purple-200/20 dark:bg-purple-900/10 rounded-full blur-3xl -z-10 -translate-x-1/3 translate-y-1/4" />

      <div className="max-w-4xl mx-auto text-center">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
        >
          <div className="inline-flex items-center gap-2 px-4 py-2 bg-brand-100 dark:bg-brand-900/30 text-brand-700 dark:text-brand-300 rounded-full text-sm font-medium mb-6">
            <Sparkles className="w-4 h-4" />
            <span>NLP · Knowledge Graphs · LLM Fine-Tuning</span>
          </div>
        </motion.div>

        <motion.h1
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, delay: 0.1 }}
          className="text-5xl sm:text-6xl font-bold text-gray-900 dark:text-white mb-6 leading-tight"
        >
          AI/NLP{" "}
          <span className="text-transparent bg-clip-text bg-gradient-to-r from-brand-600 to-purple-600">
            Portfolio
          </span>
        </motion.h1>

        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, delay: 0.2 }}
          className="text-xl text-gray-600 dark:text-gray-400 mb-10 max-w-2xl mx-auto leading-relaxed"
        >
          A collection of open-source projects exploring natural language
          processing, knowledge graph construction, and large language model
          fine-tuning.
        </motion.p>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, delay: 0.3 }}
          className="flex flex-wrap items-center justify-center gap-4"
        >
          <Link href="/projects" className="btn-primary">
            Explore Projects
            <ArrowRight className="w-4 h-4" />
          </Link>
          <a
            href="https://github.com/asierabreu/ai-nlp"
            target="_blank"
            rel="noopener noreferrer"
            className="btn-secondary"
          >
            <GitHubIcon className="w-4 h-4" />
            View on GitHub
          </a>
        </motion.div>
      </div>
    </section>
  );
}
