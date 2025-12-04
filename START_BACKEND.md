# Start contech1 Backend

## Quick Start

```bash
cd "/Users/masdawg/Desktop/Brain/Mason/1. Projects/1. Code/Models/ConTech1/backend"
python app.py
```

The backend will start on: http://localhost:8000

## Test It

Open your browser to: http://localhost:8000

Or use the frontend at: `pages/contech1.html` (make sure API_URL is set to `http://localhost:8000/chat`)

## Troubleshooting

**Port already in use:**
```bash
# Find what's using port 8000
lsof -i :8000

# Kill it or use a different port
python app.py --port 8001
```

**Missing dependencies:**
```bash
pip install -r ../requirements.txt
```

**API key not set:**
```bash
export OPENAI_API_KEY=your-key-here
# Or create .env file in backend/ directory
```

