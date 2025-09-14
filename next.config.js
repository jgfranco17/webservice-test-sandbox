/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  async rewrites() {
    return [
      {
        source: "/api/:path*",
        destination: "http://backend-primary:8080/:path*",
      },
    ];
  },
};

module.exports = nextConfig;
