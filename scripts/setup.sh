#!/bin/bash

# Setup script for Webservice Test Sandbox
echo "🚀 Setting up Webservice Test Sandbox..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is required but not installed."
    exit 1
fi

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install -e .

# Install Node.js dependencies
echo "📦 Installing Node.js dependencies..."
npm install

echo "✅ Setup complete!"
echo ""
echo "To start the application:"
echo "Development mode:"
echo "  just run-dev        # Both services in development"
echo "  just run-backend    # Backend only"
echo "  just run-frontend   # Frontend only"
echo ""
echo "Production mode (Docker):"
echo "  just build          # Build Docker images"
echo "  just start          # Start with Docker Compose"
echo "  just start-bg       # Start in background"
echo "  just stop           # Stop services"
echo ""
echo "To run tests:"
echo "  just test           # Run all tests"
echo "  pytest             # Run Python tests"
