"""
Example: How to integrate your Swift tools with an AI model

This shows the REALISTIC approach - you don't need to rewrite your Swift apps,
just expose them so the AI can call them.
"""

from openai import OpenAI
import json

# Initialize OpenAI client (or use Claude, etc.)
client = OpenAI()

def define_your_tools():
    """
    Define your Swift tools as functions the AI model can use
    
    The model will see these descriptions and know when to use them
    """
    tools = [
        {
            "type": "function",
            "function": {
                "name": "generate_proposal",
                "description": "Generates a construction proposal PDF using the Proposal Generator tool. Use this when user asks to create, generate, or build a proposal.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_name": {
                            "type": "string",
                            "description": "Name of the construction project"
                        },
                        "client_name": {
                            "type": "string",
                            "description": "Name of the client"
                        },
                        "materials": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of materials needed"
                        },
                        "labor_hours": {
                            "type": "number",
                            "description": "Total labor hours estimated"
                        },
                        "total_cost": {
                            "type": "number",
                            "description": "Total project cost"
                        }
                    },
                    "required": ["project_name", "client_name", "total_cost"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "calculate_takeoff",
                "description": "Calculates material quantities from construction drawings using Simple Takeoff. Use this when user asks about quantities, takeoffs, or measurements from drawings.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "drawing_path": {
                            "type": "string",
                            "description": "Path to the construction drawing file"
                        },
                        "material_type": {
                            "type": "string",
                            "description": "Type of material to calculate (pipe, wire, conduit, etc.)"
                        },
                        "scale": {
                            "type": "number",
                            "description": "Drawing scale if known"
                        }
                    },
                    "required": ["drawing_path", "material_type"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "calculate_stakes",
                "description": "Calculates staking points and measurements using Swift Stakes. Use this for surveying, staking, or measurement calculations.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "coordinates": {
                            "type": "array",
                            "items": {"type": "number"},
                            "description": "List of coordinate points"
                        },
                        "measurement_type": {
                            "type": "string",
                            "description": "Type of measurement (distance, elevation, angle)"
                        }
                    },
                    "required": ["coordinates"]
                }
            }
        }
    ]
    return tools

def call_swift_tool(tool_name: str, parameters: dict):
    """
    This is where you'd call your actual Swift tool
    
    Options:
    1. HTTP API - If Swift app is running as web server
    2. CLI - If Swift app accepts command line args
    3. Python bridge - Direct Swift call via PyObjC
    """
    
    if tool_name == "generate_proposal":
        # Option 1: Call HTTP API
        # import requests
        # response = requests.post("http://localhost:8080/generate-proposal", json=parameters)
        # return response.json()
        
        # Option 2: Call CLI
        # import subprocess
        # result = subprocess.run(["swift", "ProposalGenerator", "--project", parameters["project_name"]], capture_output=True)
        # return {"status": "success", "pdf_path": "..."}
        
        # For now, return mock
        return {
            "status": "success",
            "pdf_path": f"/proposals/{parameters['project_name']}.pdf",
            "message": "Proposal generated successfully"
        }
    
    elif tool_name == "calculate_takeoff":
        # Call Simple Takeoff tool
        return {
            "status": "success",
            "quantities": {
                "material": parameters["material_type"],
                "total_length": 1000,
                "unit": "feet"
            }
        }
    
    elif tool_name == "calculate_stakes":
        # Call Swift Stakes tool
        return {
            "status": "success",
            "stakes": [
                {"point": 1, "x": 100, "y": 200},
                {"point": 2, "x": 150, "y": 250}
            ]
        }

def ask_ai(user_query: str):
    """
    Ask the AI model a question - it will automatically use your tools!
    """
    
    # Define available tools
    tools = define_your_tools()
    
    # Send to AI model with tools
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or "gpt-4", "claude-3-opus", etc.
        messages=[
            {
                "role": "system",
                "content": "You are a construction AI assistant. You have access to tools for generating proposals, calculating takeoffs, and staking. Use these tools when appropriate."
            },
            {
                "role": "user",
                "content": user_query
            }
        ],
        tools=tools,
        tool_choice="auto"  # Let model decide when to use tools
    )
    
    message = response.choices[0].message
    
    # Check if model wants to use a tool
    if message.tool_calls:
        tool_calls = message.tool_calls
        
        # Execute each tool call
        for tool_call in tool_calls:
            tool_name = tool_call.function.name
            parameters = json.loads(tool_call.function.arguments)
            
            # Call your Swift tool!
            result = call_swift_tool(tool_name, parameters)
            
            # Send result back to model
            # (In real implementation, you'd continue the conversation)
            print(f"Tool {tool_name} called with: {parameters}")
            print(f"Result: {result}")
    
    return message.content

# Example usage
if __name__ == "__main__":
    # The AI will automatically use your Proposal Generator!
    result = ask_ai("Generate a proposal for a 1000ft waterline project for Wasatch Mobile Homes, total cost $50,000")
    print(result)
    
    # The AI will automatically use Simple Takeoff!
    result = ask_ai("Calculate the pipe quantity needed from drawing at /path/to/drawing.pdf")
    print(result)

