# Test contech1 - Quick Guide

## Start the Backend

```bash
cd "/Users/masdawg/Desktop/Brain/Mason/1. Projects/1. Code/Models/ConTech1/backend"
python app.py
```

You should see:
```
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

## Test the Tools

### Option 1: Use the Web Interface
1. Open `pages/contech1.html` in your browser
2. Or go to: http://localhost:8000 (if backend serves the UI)

### Option 2: Test via API Directly

**Test tool listing:**
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "What tools are available?"}]}'
```

**Test material cost calculation:**
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "Calculate the cost for 1000 feet of 4-inch pipe"}]}'
```

**Test labor cost:**
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "How much will 40 hours of operator time cost?"}]}'
```

## What to Expect

✅ **Tools should work:**
- List available tools
- Calculate material costs
- Calculate labor costs
- Calculate equipment costs
- Generate full project estimates

✅ **AI should:**
- Understand natural language
- Choose the right tool automatically
- Explain results simply
- Show which tools were used

## Troubleshooting

**Backend won't start:**
- Check API key is set: `cat backend/.env`
- Check dependencies: `pip install -r requirements.txt`

**Tools not working:**
- Check backend logs for errors
- Verify API key is valid
- Check browser console for CORS errors

**API errors:**
- Make sure backend is running on port 8000
- Check CORS settings in `backend/app.py`
- Verify API URL in `contech1.html`

## Next Steps

Once tools are working:
1. ✅ Test all 7 tools
2. ✅ Try complex queries
3. ✅ Integrate Swift tools (Proposal Generator, etc.)
4. ✅ Load real pricing data
5. ✅ Deploy to production

