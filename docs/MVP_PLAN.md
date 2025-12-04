# ConTech1 MVP Plan - Fastest Path to Version 1

## Goal: Get a working product in 1-2 weeks

## Architecture: Web App (Fastest MVP)

```
┌─────────────────────────────────────┐
│   Web Browser (Any Device)          │
│   Simple HTML/JavaScript UI         │
└──────────────┬──────────────────────┘
               │ HTTP
               ▼
┌─────────────────────────────────────┐
│   FastAPI Backend (Python)          │
│   - Handles AI queries              │
│   - Manages tool calls              │
│   - Returns results                 │
└──────────────┬──────────────────────┘
               │
       ┌───────┴───────┐
       │               │
       ▼               ▼
┌─────────────┐  ┌─────────────┐
│  AI Model   │  │ Swift Tools │
│  (GPT-4/    │  │ (via API/  │
│   Claude)   │  │  CLI)       │
└─────────────┘  └─────────────┘
```

## Why This Approach?

✅ **Fastest to build** - Web is simpler than desktop apps
✅ **Works everywhere** - Mac, Windows, iPhone, Android
✅ **Easy to iterate** - Change code, refresh browser
✅ **Can run locally** - Test on your machine first
✅ **Easy to deploy** - Deploy to web when ready
✅ **Can wrap later** - Turn into desktop app with Electron if needed

## MVP Features (Version 1)

1. **Chat Interface**
   - User types question
   - AI responds
   - Shows tool usage

2. **Integrated Tools**
   - Proposal Generator (start with this)
   - Simple Takeoff (add second)
   - Material Calculator (custom Python tool)

3. **Basic UI**
   - Simple, clean chat interface
   - Show when tools are used
   - Display results

## Tech Stack

**Backend:**
- FastAPI (Python) - Fast, modern, easy
- OpenAI/Anthropic API - For AI model
- Your Swift tools - Via API or CLI

**Frontend:**
- Simple HTML/CSS/JavaScript (start simple!)
- Can upgrade to React later if needed

**Deployment:**
- Local first (run on your Mac)
- Deploy to Vercel/Railway later (free tiers available)

## Timeline

**Week 1:**
- Day 1-2: Set up FastAPI backend with AI integration
- Day 3-4: Add Proposal Generator tool
- Day 5: Build simple web UI
- Day 6-7: Test and iterate

**Week 2:**
- Add more tools
- Improve UI
- Add custom Python tools
- Deploy to web

## Next Steps

1. Build backend API
2. Create simple web UI
3. Integrate first tool (Proposal Generator)
4. Test end-to-end
5. Iterate!

