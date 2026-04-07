export interface Project {
  id: string;
  title: string;
  description: string;
  longDescription?: string;
  emoji: string;
  tags: string[];
  githubUrl: string;
  demoUrl?: string;
  docsUrl?: string;
  status: "active" | "wip" | "planned";
}

export default function ProjectCard({ project }: { project: Project }) {
  const statusColors = {
    active: "bg-green-100 text-green-800 dark:bg-green-900/30 dark:text-green-400",
    wip: "bg-yellow-100 text-yellow-800 dark:bg-yellow-900/30 dark:text-yellow-400",
    planned: "bg-gray-100 text-gray-600 dark:bg-gray-800 dark:text-gray-400",
  };

  const statusLabels = {
    active: "Active",
    wip: "In Progress",
    planned: "Planned",
  };

  return (
    <div className="card p-6 flex flex-col gap-4 animate-fade-in">
      {/* Header */}
      <div className="flex items-start justify-between gap-3">
        <div className="flex items-center gap-3">
          <span className="text-3xl">{project.emoji}</span>
          <h3 className="text-lg font-semibold text-gray-900 dark:text-white leading-snug">
            {project.title}
          </h3>
        </div>
        <span
          className={`text-xs font-medium px-2 py-1 rounded-full shrink-0 ${statusColors[project.status]}`}
        >
          {statusLabels[project.status]}
        </span>
      </div>

      {/* Description */}
      <p className="text-sm text-gray-600 dark:text-gray-400 leading-relaxed flex-1">
        {project.description}
      </p>

      {/* Tags */}
      <div className="flex flex-wrap gap-2">
        {project.tags.map((tag) => (
          <span
            key={tag}
            className="text-xs px-2 py-1 bg-brand-50 dark:bg-brand-950/50 text-brand-700 dark:text-brand-300 rounded-md font-mono"
          >
            {tag}
          </span>
        ))}
      </div>

      {/* Links */}
      <div className="flex items-center gap-3 pt-2 border-t border-gray-100 dark:border-gray-800">
        <a
          href={project.githubUrl}
          target="_blank"
          rel="noopener noreferrer"
          className="text-sm font-medium text-brand-600 dark:text-brand-400 hover:underline"
        >
          GitHub →
        </a>
        {project.demoUrl && (
          <a
            href={project.demoUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="text-sm font-medium text-gray-600 dark:text-gray-400 hover:underline"
          >
            Demo →
          </a>
        )}
        {project.docsUrl && (
          <a
            href={project.docsUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="text-sm font-medium text-gray-600 dark:text-gray-400 hover:underline"
          >
            Docs →
          </a>
        )}
      </div>
    </div>
  );
}
