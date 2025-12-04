# Deploying ConTech1 to masonearl.com

## Overview

ConTech1 consists of two parts:
1. **Frontend**: HTML page on masonearl.com (already added)
2. **Backend**: FastAPI server (needs to be deployed)

## Deployment Steps

### Option 1: Vercel (Recommended - Easiest)

1. **Install Vercel CLI:**
```bash
npm i -g vercel
```

2. **Deploy backend:**
```bash
cd backend
vercel
```

3. **Update API URL in contech1.html:**
   - Change `API_URL` to your Vercel deployment URL
   - Example: `https://contech1-backend.vercel.app/chat`

4. **Deploy frontend (masonearl.com):**
   - Commit changes to git
   - Push to your repository
   - Your hosting will auto-deploy

### Option 2: Railway (Free Tier Available)

1. **Sign up at railway.app**
2. **Create new project**
3. **Connect GitHub repo** (or deploy from CLI)
4. **Set environment variables:**
   - `OPENAI_API_KEY=your-key`
5. **Railway auto-detects FastAPI**
6. **Update API URL in contech1.html**

### Option 3: Render (Free Tier Available)

1. **Sign up at render.com**
2. **Create new Web Service**
3. **Connect GitHub repo**
4. **Settings:**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app:app --host 0.0.0.0 --port $PORT`
5. **Set environment variables**
6. **Deploy**

## Backend Configuration

### Create vercel.json (for Vercel)

```json
{
  "version": 2,
  "builds": [
    {
      "src": "backend/app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "backend/app.py"
    }
  ]
}
```

### Environment Variables Needed

- `OPENAI_API_KEY` - Your OpenAI API key

## Testing Locally First

1. **Run backend locally:**
```bash
cd backend
python app.py
```

2. **Update contech1.html API_URL to:**
```javascript
const API_URL = 'http://localhost:8000/chat';
```

3. **Test in browser:**
   - Open `pages/contech1.html` locally
   - Try asking questions

4. **Once working, deploy backend**

## Post-Deployment Checklist

- [ ] Backend deployed and accessible
- [ ] API_URL updated in contech1.html
- [ ] CORS configured correctly
- [ ] Environment variables set
- [ ] Test end-to-end on live site
- [ ] Update API_URL to production URL

## Troubleshooting

**CORS Errors:**
- Make sure backend allows your domain
- Update `allow_origins` in app.py

**API Not Found:**
- Check backend URL is correct
- Verify backend is running
- Check browser console for errors

**Environment Variables:**
- Make sure OPENAI_API_KEY is set
- Restart backend after setting vars

