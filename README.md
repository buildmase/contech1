# contech1 - Construction AI Assistant

An action-based construction AI assistant that executes tasks using integrated tools, not just chat. Uses your existing Swift tools (Proposal Generator, Swift Stakes, Simple Takeoff) plus custom Python libraries.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Set up API key
echo "OPENAI_API_KEY=your-key-here" > .env

# Run server
./start.sh
# Or: cd backend && python app.py
```

Visit: http://localhost:8000

See [QUICK_START.md](QUICK_START.md) for detailed setup.

## Architecture

```
User Query → AI Model → Tool Selection → Execute Tool → Return Results → AI Response
```

**Action-Based Model:**
- Executes tasks using tools, not just chat
- Language model bridges user communication with tools
- Simple language for anyone to use

## Project Structure

```
contech1/
├── backend/          # FastAPI server
│   ├── app.py       # Main API with tool calling
│   └── vercel.json  # Deployment config
├── tools/            # Custom Python tools
│   └── estimating_tools.py
├── integrations/     # Swift tool wrappers (to be added)
├── src/              # Example code
├── docs/             # Detailed documentation
│   ├── HOW_IT_WORKS.md
│   ├── INTEGRATION.md
│   ├── TOOLS_AND_RESOURCES.md
│   └── DEPLOYMENT.md
├── README.md         # This file
├── QUICK_START.md    # Setup guide
├── NOTES.md          # Development notes
└── requirements.txt  # Python dependencies
```

## Current Tools (7 Available)

1. **List Available Tools** - Shows what tools are available
2. **Generate Proposal** - Creates construction proposal PDFs
3. **Calculate Material Quantities** - Figures out how much material needed
4. **Calculate Material Cost** - Tells material costs using real pricing
5. **Calculate Labor Cost** - Calculates labor costs based on hourly rates
6. **Calculate Equipment Cost** - Figures out equipment rental costs
7. **Full Project Estimate** - Creates complete project cost breakdown

See [docs/TOOLS_AND_RESOURCES.md](docs/TOOLS_AND_RESOURCES.md) for details.

## Documentation

- **[QUICK_START.md](QUICK_START.md)** - Get running in 10 minutes
- **[docs/HOW_IT_WORKS.md](docs/HOW_IT_WORKS.md)** - Technical architecture
- **[docs/INTEGRATION.md](docs/INTEGRATION.md)** - Integration guide and checklist
- **[docs/TOOLS_AND_RESOURCES.md](docs/TOOLS_AND_RESOURCES.md)** - Available tools and resources
- **[docs/DEPLOYMENT.md](docs/DEPLOYMENT.md)** - Deploy to production
- **[NOTES.md](NOTES.md)** - Development notes and ideas

## Next Steps

1. Deploy backend (see [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md))
2. Integrate Swift tools (see [docs/INTEGRATION.md](docs/INTEGRATION.md))
3. Load real pricing data (see [docs/TOOLS_AND_RESOURCES.md](docs/TOOLS_AND_RESOURCES.md))

## Live Website

- **contech1**: https://masonearl.com/pages/contech1.html
- **Tools Page**: https://masonearl.com/pages/tools.html

