import { NextResponse } from "next/server";
import { fetchRepoStats } from "@/lib/github";

export const revalidate = 3600; // Revalidate every hour

export async function GET() {
  const data = await fetchRepoStats();

  if (!data) {
    return NextResponse.json(
      { error: "Failed to fetch GitHub data" },
      { status: 503 }
    );
  }

  return NextResponse.json({
    stars: data.stargazers_count,
    forks: data.forks_count,
    issues: data.open_issues_count,
    language: data.language,
    updated_at: data.updated_at,
    url: data.html_url,
  });
}
