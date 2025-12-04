# Troubleshooting contech1

## Backend Not Responding

### Check if backend is running:
```bash
lsof -i :8000
# Should show python process
```

### Start the backend:
```bash
cd "/Users/masdawg/Desktop/Brain/Mason/1. Code/Models/ConTech1/backend"
python3 app.py
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Test backend directly:
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "Hello"}]}'
```

Should return JSON with `response` and `tools_used` fields.

## Frontend Errors

### CORS Error
- **Symptom**: "Failed to fetch" or CORS error in console
- **Fix**: Make sure backend CORS allows your origin
- **Check**: Open browser console (F12) and look for CORS errors

### Connection Refused
- **Symptom**: "Cannot connect" error
- **Fix**: Backend not running - start it with `python3 app.py`

### API URL Wrong
- **Symptom**: 404 or wrong endpoint
- **Fix**: Check `API_URL` in `contech1.html` matches backend URL
- **Default**: `http://localhost:8000/chat`

## Common Issues

### Port 8000 Already in Use
```bash
# Find what's using port 8000
lsof -i :8000

# Kill it
kill -9 <PID>

# Or use different port (update app.py)
```

### API Key Not Working
```bash
# Check API key is set
cat backend/.env

# Test API key
python3 -c "from dotenv import load_dotenv; from pathlib import Path; import os; load_dotenv(Path('backend/.env')); print(os.getenv('OPENAI_API_KEY')[:20])"
```

### Dependencies Missing
```bash
pip3 install -r requirements.txt
```

## Debug Mode

### Check Backend Logs
```bash
# If running in background
tail -f /tmp/contech1.log

# Or check server output
python3 app.py
# (runs in foreground, shows all logs)
```

### Check Browser Console
1. Open `contech1.html` in browser
2. Press F12 (Developer Tools)
3. Go to Console tab
4. Look for errors when sending message

### Test API Directly
```bash
# Test tool listing
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "What tools are available?"}]}'

# Test material cost
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "Calculate cost for 1000ft of 4-inch pipe"}]}'
```

## Quick Fixes

### Restart Everything
```bash
# Kill backend
lsof -ti:8000 | xargs kill -9

# Start fresh
cd "/Users/masdawg/Desktop/Brain/Mason/1. Projects/1. Code/Models/ConTech1/backend"
python3 app.py
```

### Clear Browser Cache
- Hard refresh: Cmd+Shift+R (Mac) or Ctrl+Shift+R (Windows)
- Or clear cache in browser settings

### Check File Paths
- Make sure `backend/.env` exists with API key
- Make sure `tools/estimating_tools.py` exists
- Make sure all files are in correct locations

## Still Not Working?

1. Check backend is running: `lsof -i :8000`
2. Check API key: `cat backend/.env`
3. Check browser console for errors
4. Test API directly with curl
5. Check backend logs for errors

