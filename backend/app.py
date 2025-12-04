"""
contech1 Backend - FastAPI Server
Action-based construction AI assistant with integrated tools
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import List, Optional
import os
import sys
from pathlib import Path
from openai import OpenAI
import json
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
env_path = Path(__file__).parent / ".env"
load_dotenv(env_path)
logger.info(f"Loaded .env from: {env_path}")

# Add tools directory to path
sys.path.append(str(Path(__file__).parent.parent / "tools"))

# Import estimating tools
try:
    from estimating_tools import (
        calculate_material_cost,
        calculate_labor_cost,
        calculate_equipment_cost,
        estimate_project_cost
    )
except ImportError:
    # If tools not available, define stubs
    def calculate_material_cost(*args, **kwargs):
        return {"error": "Estimating tools not loaded"}
    def calculate_labor_cost(*args, **kwargs):
        return {"error": "Estimating tools not loaded"}
    def calculate_equipment_cost(*args, **kwargs):
        return {"error": "Estimating tools not loaded"}
    def estimate_project_cost(*args, **kwargs):
        return {"error": "Estimating tools not loaded"}

app = FastAPI(title="contech1 - Construction AI Assistant")

# Allow CORS for web frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://masonearl.com",
        "http://localhost:8000",
        "http://localhost:8080",  # Python http.server
        "http://localhost:5500",  # VS Code Live Server
        "http://127.0.0.1:5500",  # VS Code Live Server
        "http://127.0.0.1:8000",
        "http://127.0.0.1:8080",
        "*"  # Allow all for development, restrict in production
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize AI client
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    logger.error("OPENAI_API_KEY not found in environment variables!")
    raise ValueError("OPENAI_API_KEY not set. Please set it in backend/.env file")
    
client = OpenAI(api_key=api_key)
logger.info("OpenAI client initialized successfully")

# Request/Response models
class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[ChatMessage]

class ChatResponse(BaseModel):
    response: str
    tools_used: List[str] = []

# Define your construction tools
def get_construction_tools():
    """Define available construction tools"""
    return [
        {
            "type": "function",
            "function": {
                "name": "list_available_tools",
                "description": "Lists all available construction tools and what they do in simple language. Use when user asks what tools are available, what can you do, or what are my options.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "generate_proposal",
                "description": "Generates a construction proposal PDF. Use when user asks to create, generate, or build a proposal for a construction project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_name": {"type": "string", "description": "Name of the construction project"},
                        "client_name": {"type": "string", "description": "Name of the client"},
                        "project_description": {"type": "string", "description": "Description of the work"},
                        "materials": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of materials needed"
                        },
                        "labor_hours": {"type": "number", "description": "Total labor hours"},
                        "total_cost": {"type": "number", "description": "Total project cost"}
                    },
                    "required": ["project_name", "client_name", "total_cost"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "calculate_materials",
                "description": "Calculates material quantities needed for a project. Use when user asks about quantities, materials needed, or takeoffs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "material_type": {"type": "string", "description": "Type of material (pipe, wire, conduit, etc.)"},
                        "length_ft": {"type": "number", "description": "Length in feet"},
                        "diameter_inches": {"type": "number", "description": "Diameter in inches if applicable"}
                    },
                    "required": ["material_type", "length_ft"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "calculate_material_cost",
                "description": "Calculates material cost using real pricing data. Use when user asks about material costs, pricing, or cost estimates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "material_type": {"type": "string", "description": "Type of material (pipe, concrete, rebar, etc.)"},
                        "quantity": {"type": "number", "description": "Quantity needed"},
                        "size": {"type": "string", "description": "Size specification (e.g., '4' for 4-inch pipe, '3000_psi' for concrete)"}
                    },
                    "required": ["material_type", "quantity"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "calculate_labor_cost",
                "description": "Calculates labor cost based on labor rates. Use when user asks about labor costs, crew costs, or hourly rates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "labor_type": {"type": "string", "description": "Type of laborer (operator, laborer, foreman, electrician, ironworker)"},
                        "hours": {"type": "number", "description": "Number of hours"}
                    },
                    "required": ["labor_type", "hours"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "calculate_equipment_cost",
                "description": "Calculates equipment rental cost. Use when user asks about equipment costs or rental rates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "equipment_type": {"type": "string", "description": "Type of equipment (excavator, auger, compactor)"},
                        "days": {"type": "number", "description": "Number of days needed"}
                    },
                    "required": ["equipment_type", "days"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "estimate_project_cost",
                "description": "Creates a complete project cost estimate with materials, labor, equipment, and markup. Use when user asks for a full estimate, project cost, or bid estimate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "materials": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "type": {"type": "string"},
                                    "quantity": {"type": "number"},
                                    "size": {"type": "string"}
                                }
                            },
                            "description": "List of materials with type, quantity, and size"
                        },
                        "labor": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "type": {"type": "string"},
                                    "hours": {"type": "number"}
                                }
                            },
                            "description": "List of labor with type and hours"
                        },
                        "equipment": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "type": {"type": "string"},
                                    "days": {"type": "number"}
                                }
                            },
                            "description": "Optional list of equipment with type and days"
                        },
                        "markup": {"type": "number", "description": "Markup percentage as decimal (default 0.15 for 15%)"}
                    },
                    "required": ["materials", "labor"]
                }
            }
        }
    ]

# Tool execution functions
def execute_tool(tool_name: str, parameters: dict):
    """Execute a construction tool"""
    
    if tool_name == "list_available_tools":
        # Return available tools in simple, straightforward language
        return {
            "status": "success",
            "tools": [
                {
                    "name": "Generate Proposal",
                    "description": "Creates a construction proposal PDF with project details, materials, labor, and costs.",
                    "example": "Generate a proposal for a 1000ft waterline project"
                },
                {
                    "name": "Calculate Material Quantities",
                    "description": "Figures out how much material you need for a project (like pipe, wire, or concrete).",
                    "example": "How much 4-inch pipe do I need for 500 feet?"
                },
                {
                    "name": "Calculate Material Cost",
                    "description": "Tells you how much materials will cost using real pricing data.",
                    "example": "What's the cost for 1000 feet of 4-inch pipe?"
                },
                {
                    "name": "Calculate Labor Cost",
                    "description": "Calculates how much labor will cost based on hourly rates for operators, laborers, foremen, electricians, etc.",
                    "example": "How much will 40 hours of operator time cost?"
                },
                {
                    "name": "Calculate Equipment Cost",
                    "description": "Figures out equipment rental costs for excavators, augers, compactors, etc.",
                    "example": "How much does it cost to rent an excavator for 5 days?"
                },
                {
                    "name": "Full Project Estimate",
                    "description": "Creates a complete project cost estimate with materials, labor, equipment, and markup all included.",
                    "example": "Give me a full estimate for installing 1000ft of waterline"
                }
            ],
            "summary": "I have 6 tools available: proposal generation, material calculations, cost estimates, labor costs, equipment costs, and full project estimates. Just tell me what you need and I'll use the right tool."
        }
    
    elif tool_name == "generate_proposal":
        # TODO: Call your actual Proposal Generator Swift tool
        # For now, return mock response
        return {
            "status": "success",
            "message": f"Proposal generated for {parameters.get('project_name')}",
            "pdf_path": f"/proposals/{parameters.get('project_name')}.pdf"
        }
    
    elif tool_name == "calculate_materials":
        # Custom Python tool - calculate materials
        material_type = parameters.get("material_type", "")
        length_ft = parameters.get("length_ft", 0)
        diameter = parameters.get("diameter_inches", 0)
        
        # Simple calculation logic
        if material_type.lower() == "pipe":
            # Add 10% waste factor
            quantity = length_ft * 1.1
            return {
                "status": "success",
                "material_type": material_type,
                "quantity": round(quantity, 2),
                "unit": "feet",
                "waste_factor": "10%"
            }
        else:
            return {
                "status": "success",
                "material_type": material_type,
                "quantity": length_ft,
                "unit": "feet"
            }
    
    elif tool_name == "calculate_material_cost":
        # Use estimating tools
        result = calculate_material_cost(
            parameters.get("material_type"),
            parameters.get("quantity"),
            parameters.get("size")
        )
        return {"status": "success", **result}
    
    elif tool_name == "calculate_labor_cost":
        # Use estimating tools
        result = calculate_labor_cost(
            parameters.get("labor_type"),
            parameters.get("hours")
        )
        return {"status": "success", **result}
    
    elif tool_name == "calculate_equipment_cost":
        # Use estimating tools
        result = calculate_equipment_cost(
            parameters.get("equipment_type"),
            parameters.get("days")
        )
        return {"status": "success", **result}
    
    elif tool_name == "estimate_project_cost":
        # Use estimating tools for full project estimate
        result = estimate_project_cost(
            parameters.get("materials", []),
            parameters.get("labor", []),
            parameters.get("equipment", []),
            parameters.get("markup", 0.15)
        )
        return {"status": "success", **result}
    
    else:
        logger.warning(f"Unknown tool requested: {tool_name}")
        return {"status": "error", "message": f"Unknown tool: {tool_name}"}

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return {
        "status": "healthy",
        "service": "contech1",
        "tools_available": 7,
        "ai_model": "gpt-4o-mini"
    }

# List tools endpoint
@app.get("/tools")
async def list_tools():
    """List all available tools"""
    return {
        "tools": [
            {"name": "list_available_tools", "description": "Lists all available construction tools"},
            {"name": "generate_proposal", "description": "Generates a construction proposal PDF"},
            {"name": "calculate_materials", "description": "Calculates material quantities needed"},
            {"name": "calculate_material_cost", "description": "Calculates material costs using real pricing"},
            {"name": "calculate_labor_cost", "description": "Calculates labor costs based on hourly rates"},
            {"name": "calculate_equipment_cost", "description": "Calculates equipment rental costs"},
            {"name": "estimate_project_cost", "description": "Creates a complete project cost estimate"}
        ]
    }

@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the web UI"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>contech1 - Construction AI Assistant</title>
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background: #f5f5f5;
            }
            .chat-container {
                background: white;
                border-radius: 8px;
                padding: 20px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            .messages {
                height: 400px;
                overflow-y: auto;
                margin-bottom: 20px;
                padding: 10px;
                background: #fafafa;
                border-radius: 4px;
            }
            .message {
                margin: 10px 0;
                padding: 10px;
                border-radius: 4px;
            }
            .user {
                background: #007bff;
                color: white;
                text-align: right;
            }
            .assistant {
                background: #e9ecef;
            }
            .tool-used {
                background: #fff3cd;
                border-left: 3px solid #ffc107;
                padding: 5px 10px;
                margin: 5px 0;
                font-size: 0.9em;
            }
            input {
                width: 70%;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 4px;
            }
            button {
                padding: 10px 20px;
                background: #007bff;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
            button:hover {
                background: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="chat-container">
            <h1>🏗️ contech1 - Construction AI Assistant</h1>
            <div id="messages" class="messages"></div>
            <div>
                <input type="text" id="userInput" placeholder="Ask me anything about construction..." />
                <button onclick="sendMessage()">Send</button>
            </div>
        </div>
        <script>
            const messagesDiv = document.getElementById('messages');
            const userInput = document.getElementById('userInput');
            
            function addMessage(role, content, tools = []) {
                const messageDiv = document.createElement('div');
                messageDiv.className = `message ${role}`;
                messageDiv.textContent = content;
                messagesDiv.appendChild(messageDiv);
                
                if (tools.length > 0) {
                    tools.forEach(tool => {
                        const toolDiv = document.createElement('div');
                        toolDiv.className = 'tool-used';
                        toolDiv.textContent = `🔧 Used tool: ${tool}`;
                        messagesDiv.appendChild(toolDiv);
                    });
                }
                
                messagesDiv.scrollTop = messagesDiv.scrollHeight;
            }
            
            async function sendMessage() {
                const message = userInput.value.trim();
                if (!message) return;
                
                addMessage('user', message);
                userInput.value = '';
                
                try {
                    const response = await fetch('/chat', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({
                            messages: [{role: 'user', content: message}]
                        })
                    });
                    
                    const data = await response.json();
                    addMessage('assistant', data.response, data.tools_used || []);
                } catch (error) {
                    addMessage('assistant', 'Error: ' + error.message);
                }
            }
            
            userInput.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') sendMessage();
            });
        </script>
    </body>
    </html>
    """

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Handle chat requests with AI and tool calling"""
    
    logger.info(f"Received chat request: {request.messages[0].content[:50] if request.messages else 'empty'}...")
    
    tools = get_construction_tools()
    tools_used = []
    
    # Convert messages to OpenAI format
    messages = [{"role": msg.role, "content": msg.content} for msg in request.messages]
    
    # Add system message - Action-based model, not just language
    messages.insert(0, {
        "role": "system",
        "content": """You are contech1, an action-based construction assistant. Your primary job is to execute tasks using tools, not just chat.

IMPORTANT:
- You are ACTION-BASED: When users ask for something, USE THE TOOLS to do it
- The language model is just a bridge to help users communicate simply
- Anyone should be able to use you - explain things in simple, straightforward language
- When users ask "what can you do" or "what tools are available", use the list_available_tools function
- Focus on DOING things, not just explaining things
- Use tools proactively - don't just describe what you could do, actually do it

Your tools can:
- Generate proposals
- Calculate material quantities and costs
- Calculate labor and equipment costs  
- Create full project estimates

When users ask questions, use the appropriate tool to give them real answers with actual calculations."""
    })
    
    # Call AI model
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Start with cheaper model, upgrade later
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )
    
    message = response.choices[0].message
    final_response = message.content or ""
    
    # Handle tool calls
    if message.tool_calls:
        for tool_call in message.tool_calls:
            tool_name = tool_call.function.name
            parameters = json.loads(tool_call.function.arguments)
            
            tools_used.append(tool_name)
            
            # Execute tool
            tool_result = execute_tool(tool_name, parameters)
            
            # Add tool result to conversation
            messages.append({
                "role": "assistant",
                "content": None,
                "tool_calls": [{
                    "id": tool_call.id,
                    "type": "function",
                    "function": {
                        "name": tool_name,
                        "arguments": tool_call.function.arguments
                    }
                }]
            })
            
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(tool_result)
            })
        
        # Get final response after tool execution
        final_response_obj = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        final_response = final_response_obj.choices[0].message.content
    
    logger.info(f"Tools used: {tools_used}")
    logger.info(f"Response length: {len(final_response)} chars")
    
    return ChatResponse(
        response=final_response,
        tools_used=tools_used
    )

# Error handler
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.error(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"response": f"An error occurred: {str(exc)}", "tools_used": []}
    )

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting contech1 backend server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)

