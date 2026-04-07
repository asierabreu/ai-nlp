import type { Metadata } from "next";
import "./globals.css";
import { Providers } from "@/components/Providers";
import NavBar from "@/components/NavBar";
import Footer from "@/components/Footer";

export const metadata: Metadata = {
  title: {
    default: "AI/NLP Portfolio",
    template: "%s | AI/NLP Portfolio",
  },
  description:
    "Portfolio showcasing AI/NLP projects: knowledge graphs, LLM fine-tuning, and more.",
  keywords: ["AI", "NLP", "machine learning", "knowledge graphs", "LLM", "fine-tuning"],
  authors: [{ name: "asierabreu" }],
  openGraph: {
    type: "website",
    locale: "en_US",
    url: "https://github.com/asierabreu/ai-nlp",
    siteName: "AI/NLP Portfolio",
    title: "AI/NLP Portfolio",
    description:
      "Portfolio showcasing AI/NLP projects: knowledge graphs, LLM fine-tuning, and more.",
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body>
        <Providers>
          <div className="min-h-screen flex flex-col">
            <NavBar />
            <main className="flex-1">{children}</main>
            <Footer />
          </div>
        </Providers>
      </body>
    </html>
  );
}
