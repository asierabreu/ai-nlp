/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  images: {
    remotePatterns: [],
  },
  // Standalone output bundles only the files needed to run the server,
  // which is required for the production Docker image.
  output: 'standalone',
};

module.exports = nextConfig;
