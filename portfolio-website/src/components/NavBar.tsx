"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useState } from "react";
import { Menu, X } from "lucide-react";
import GitHubIcon from "./GitHubIcon";
import DarkModeToggle from "./DarkModeToggle";

const navLinks = [
  { href: "/", label: "Home" },
  { href: "/projects", label: "Projects" },
  { href: "/contact", label: "Contact" },
];

export default function NavBar() {
  const pathname = usePathname();
  const [menuOpen, setMenuOpen] = useState(false);

  return (
    <header className="sticky top-0 z-50 w-full border-b border-gray-200 dark:border-gray-800 bg-white/80 dark:bg-gray-950/80 backdrop-blur-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <Link
            href="/"
            className="text-xl font-bold text-brand-600 dark:text-brand-400 font-mono"
          >
            AI/NLP Portfolio
          </Link>

          {/* Desktop Navigation */}
          <nav className="hidden md:flex items-center gap-6">
            {navLinks.map((link) => (
              <Link
                key={link.href}
                href={link.href}
                className={`text-sm font-medium transition-colors ${
                  pathname === link.href
                    ? "text-brand-600 dark:text-brand-400"
                    : "text-gray-600 dark:text-gray-400 hover:text-brand-600 dark:hover:text-brand-400"
                }`}
              >
                {link.label}
              </Link>
            ))}
          </nav>

          {/* Actions */}
          <div className="flex items-center gap-3">
            <DarkModeToggle />
            <a
              href="https://github.com/asierabreu/ai-nlp"
              target="_blank"
              rel="noopener noreferrer"
              className="hidden sm:inline-flex btn-secondary text-sm py-2 px-4"
              aria-label="View on GitHub"
            >
              <GitHubIcon className="w-4 h-4" />
              <span className="hidden sm:inline">GitHub</span>
            </a>

            {/* Mobile menu button */}
            <button
              onClick={() => setMenuOpen(!menuOpen)}
              className="md:hidden p-2 rounded-lg text-gray-600 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"
              aria-label="Toggle mobile menu"
            >
              {menuOpen ? (
                <X className="w-5 h-5" />
              ) : (
                <Menu className="w-5 h-5" />
              )}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile Navigation */}
      {menuOpen && (
        <div className="md:hidden border-t border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-950">
          <nav className="max-w-7xl mx-auto px-4 py-3 flex flex-col gap-1">
            {navLinks.map((link) => (
              <Link
                key={link.href}
                href={link.href}
                onClick={() => setMenuOpen(false)}
                className={`px-3 py-2 rounded-lg text-sm font-medium transition-colors ${
                  pathname === link.href
                    ? "bg-brand-50 dark:bg-brand-950/30 text-brand-600 dark:text-brand-400"
                    : "text-gray-600 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800"
                }`}
              >
                {link.label}
              </Link>
            ))}
            <a
              href="https://github.com/asierabreu/ai-nlp"
              target="_blank"
              rel="noopener noreferrer"
              className="px-3 py-2 rounded-lg text-sm font-medium text-gray-600 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 flex items-center gap-2"
            >
              <GitHubIcon className="w-4 h-4" />
              GitHub
            </a>
          </nav>
        </div>
      )}
    </header>
  );
}
