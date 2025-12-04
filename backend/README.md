# ConTech1 Backend

FastAPI backend for the construction AI assistant.

## Quick Start

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Set up API key:**
```bash
export OPENAI_API_KEY="your-key-here"
# Or create a .env file with: OPENAI_API_KEY=your-key-here
```

3. **Run the server:**
```bash
python app.py
# Or: uvicorn app:app --reload
```

4. **Open in browser:**
```
http://localhost:8000
```

## What It Does

- Serves a web UI (simple chat interface)
- Handles AI queries via `/chat` endpoint
- Automatically uses construction tools when needed
- Returns results to user

## Next Steps

1. Integrate your actual Swift tools
2. Add more tools
3. Improve UI
4. Deploy to web

