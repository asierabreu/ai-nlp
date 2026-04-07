/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  images: {
    domains: [],
  },
  // Standalone output bundles only the files needed to run the server,
  // which is required for the production Docker image.
  output: 'standalone',
  // Enable static exports for GitHub Pages (uncomment if needed)
  // output: 'export',
};

module.exports = nextConfig;
