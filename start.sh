#!/bin/bash

# ConTech1 Startup Script
# Run this to start the construction AI assistant

echo "🏗️  Starting ConTech1 Construction AI Assistant..."
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "⚠️  No .env file found!"
    echo "Creating .env file - please add your OPENAI_API_KEY"
    echo "OPENAI_API_KEY=your-key-here" > .env
    echo ""
    echo "Edit .env and add your API key, then run this script again."
    exit 1
fi

# Load environment variables
export $(cat .env | xargs)

# Check if API key is set
if [ "$OPENAI_API_KEY" = "your-key-here" ] || [ -z "$OPENAI_API_KEY" ]; then
    echo "⚠️  Please set your OPENAI_API_KEY in .env file"
    exit 1
fi

# Start the server
echo "✅ Starting server on http://localhost:8000"
echo "📱 Open in your browser: http://localhost:8000"
echo ""
cd backend
python app.py

