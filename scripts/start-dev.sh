#!/bin/bash

# Development startup script for Webservice Test Sandbox
echo "🚀 Starting Webservice Test Sandbox in development mode..."

# Check if backend is already running
if curl -s http://localhost:8080/healthz > /dev/null 2>&1; then
    echo "⚠️  Backend is already running on port 8080"
else
    echo "🔧 Starting backend API..."
    python -m backend.main &
    BACKEND_PID=$!
    echo "Backend started with PID: $BACKEND_PID"
fi

# Check if frontend is already running
if curl -s http://localhost:3000 > /dev/null 2>&1; then
    echo "⚠️  Frontend is already running on port 3000"
else
    echo "🔧 Starting frontend application..."
    cd frontend && npm run dev &
    FRONTEND_PID=$!
    echo "Frontend started with PID: $FRONTEND_PID"
fi

# Wait for services to be ready
echo "⏳ Waiting for services to be ready..."
sleep 5

# Check if services are running
if curl -s http://localhost:8080/healthz > /dev/null 2>&1; then
    echo "✅ Backend is ready at http://localhost:8080"
else
    echo "❌ Backend failed to start"
fi

if curl -s http://localhost:3000 > /dev/null 2>&1; then
    echo "✅ Frontend is ready at http://localhost:3000"
else
    echo "❌ Frontend failed to start"
fi

echo ""
echo "🎉 Development environment is ready!"
echo "   Frontend: http://localhost:3000"
echo "   Backend:  http://localhost:8080"
echo ""
echo "Press Ctrl+C to stop all services"

# Wait for user interrupt
trap 'echo "🛑 Stopping services..."; kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; exit 0' INT
wait
