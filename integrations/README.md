# Swift Tool Integrations

This directory contains wrappers/adapters for your existing Swift tools.

## Tools to Integrate

1. **Proposal Generator** (`proposal_generator.py`)
   - Generate construction proposals
   - Input: Project details, materials, costs
   - Output: PDF proposal

2. **Swift Stakes** (`swift_stakes.py`)
   - Staking and measurement tools
   - Input: Coordinates, measurements
   - Output: Staking data

3. **Simple Takeoff** (`simple_takeoff.py`)
   - Material takeoff calculations
   - Input: Drawings, measurements
   - Output: Material quantities

4. **Schedule Generator** (`schedule_generator.py`)
   - Project scheduling
   - Input: Tasks, dependencies
   - Output: Project schedule

5. **Tempest Construction** (`tempest.py`)
   - Job management
   - Input: Job data
   - Output: Job status, reports

## Integration Methods

### Option 1: HTTP API (Recommended)
- Wrap Swift app in HTTP server
- Call via REST API
- Most flexible

### Option 2: Command Line
- Swift app accepts CLI args
- Call via subprocess
- Simpler but less flexible

### Option 3: Python Bridge
- Use PyObjC to call Swift directly
- Most integrated but complex

