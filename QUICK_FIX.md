# Quick Fix for "Failed to fetch" Error

## The Problem
The page can't connect to the backend. This happens when:
1. Page is opened via `file://` protocol (double-clicking HTML file)
2. Backend isn't running
3. CORS blocking the connection

## Solution: Access via Local Server

### Option 1: Use Python's Built-in Server (Easiest)

```bash
cd "/Users/masdawg/Desktop/Brain/Mason/1. Projects/1. Code/1. Websites/masonearl.com"
python3 -m http.server 8080
```

Then open: **http://localhost:8080/pages/contech1.html**

### Option 2: Use VS Code Live Server
1. Install "Live Server" extension in VS Code
2. Right-click `contech1.html`
3. Select "Open with Live Server"
4. Page opens at `http://localhost:5500/pages/contech1.html`

### Option 3: Make Sure Backend is Running

```bash
# Check if backend is running
lsof -i :8000

# If not running, start it:
cd "/Users/masdawg/Desktop/Brain/Mason/1. Projects/1. Code/Models/ConTech1/backend"
python3 app.py
```

## Why This Happens

Browsers block `file://` pages from making HTTP requests to `localhost` for security. You need to serve the page via HTTP (`http://localhost`).

## Test It Works

1. Start backend: `python3 app.py` (in backend folder)
2. Start web server: `python3 -m http.server 8080` (in masonearl.com folder)
3. Open: http://localhost:8080/pages/contech1.html
4. Try: "What tools are available?"

Should work! ✅

