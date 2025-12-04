# Quick Start Guide - Get Running in 10 Minutes

## Step 1: Install Dependencies

```bash
cd "/Users/masdawg/Desktop/Brain/Mason/1. Projects/1. Code/Models/ConTech1"
pip install fastapi uvicorn openai python-dotenv
```

## Step 2: Get API Key

1. Sign up for OpenAI API: https://platform.openai.com
2. Get your API key
3. Create `.env` file:
```bash
echo "OPENAI_API_KEY=your-key-here" > .env
```

## Step 3: Run the Server

```bash
cd backend
python app.py
```

## Step 4: Open in Browser

Go to: http://localhost:8000

## Step 5: Test It!

Try asking:
- "Generate a proposal for a 1000ft waterline project"
- "Calculate materials for 500 feet of 4-inch pipe"
- "What tools do you have available?"

## What You'll See

- Simple chat interface
- AI responds to your questions
- Shows when tools are used
- Works in any browser!

## Next: Integrate Your Swift Tools

1. Add Proposal Generator integration
2. Add Simple Takeoff
3. Add more custom tools

## Deployment (Later)

When ready to deploy:
- Vercel (free tier)
- Railway (free tier)
- Render (free tier)

All support FastAPI!

