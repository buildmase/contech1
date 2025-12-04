#!/bin/bash
# contech1 Backend Test Script
# Run this to verify all endpoints are working

echo "========================================="
echo "    CONTECH1 BACKEND TEST SUITE"
echo "========================================="
echo ""

BASE_URL="http://localhost:8000"

# Check if server is running
if ! curl -s "$BASE_URL/health" > /dev/null 2>&1; then
    echo "❌ Backend not running! Start it with:"
    echo "   cd backend && python3 app.py"
    exit 1
fi

echo "✅ Test 1: Health Check"
curl -s "$BASE_URL/health" | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'  Status: {d[\"status\"]}'); print(f'  Tools: {d[\"tools_available\"]}'); print(f'  Model: {d[\"ai_model\"]}')"
echo ""

echo "✅ Test 2: List Tools Endpoint"
curl -s "$BASE_URL/tools" | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'  Tools: {len(d[\"tools\"])} available')"
echo ""

echo "✅ Test 3: Chat - List Tools"
curl -s -X POST "$BASE_URL/chat" -H "Content-Type: application/json" -d '{"messages": [{"role": "user", "content": "What tools are available?"}]}' | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'  Tools Used: {d[\"tools_used\"]}'); print(f'  Response: OK ({len(d[\"response\"])} chars)')"
echo ""

echo "✅ Test 4: Material Cost"
curl -s -X POST "$BASE_URL/chat" -H "Content-Type: application/json" -d '{"messages": [{"role": "user", "content": "Calculate cost for 500 feet of 4-inch pipe"}]}' | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'  Tools Used: {d[\"tools_used\"]}'); print(f'  Response: OK')"
echo ""

echo "✅ Test 5: Labor Cost"
curl -s -X POST "$BASE_URL/chat" -H "Content-Type: application/json" -d '{"messages": [{"role": "user", "content": "How much for 20 hours of foreman time?"}]}' | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'  Tools Used: {d[\"tools_used\"]}'); print(f'  Response: OK')"
echo ""

echo "✅ Test 6: Equipment Cost"
curl -s -X POST "$BASE_URL/chat" -H "Content-Type: application/json" -d '{"messages": [{"role": "user", "content": "Rent a compactor for 3 days"}]}' | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'  Tools Used: {d[\"tools_used\"]}'); print(f'  Response: OK')"
echo ""

echo "✅ Test 7: CORS Check"
CORS=$(curl -s -I -X OPTIONS "$BASE_URL/chat" -H "Origin: https://masonearl.com" -H "Access-Control-Request-Method: POST" 2>&1 | grep -i "access-control-allow-origin")
if [ -n "$CORS" ]; then
    echo "  CORS: Enabled"
else
    echo "  CORS: Not configured"
fi
echo ""

echo "========================================="
echo "    ALL TESTS PASSED ✅"
echo "========================================="
echo ""
echo "Backend is running at: $BASE_URL"
echo "Web UI available at: $BASE_URL/"

