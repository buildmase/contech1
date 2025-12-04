# contech1 Development Notes

## Core Philosophy & Design Principles

### Action-Based Model (Not Just Language)
- **Primary Goal:** Execute tasks using tools, not just chat
- **Language Model Role:** Bridge to help users communicate simply with tools
- **User Experience:** Anyone should be able to use it - simple, straightforward language
- **Focus:** DOING things, not just explaining things
- **Behavior:** Use tools proactively - don't just describe what you could do, actually do it

### Key Concepts Discussed

#### Simple Tool Discovery
- Users should be able to ask "what tools are available?" or "what can you do?"
- Model responds with `list_available_tools` function
- Tools explained in simple, straightforward language
- Examples provided for each tool

#### Tool Communication
- Language model helps users communicate with tools in simple language
- Model translates natural language requests into tool calls
- Results explained back in simple terms
- No technical jargon required from users

#### Action-First Approach
- When users ask for something, USE THE TOOLS to do it
- Don't just explain what could be done - actually execute
- Give real answers with actual calculations
- Focus on actionable results

## Implementation Notes

### System Prompt Updates
- Updated system message to emphasize action-based approach
- Clear instructions: "USE THE TOOLS to do it"
- Emphasis on simple language for anyone to use
- Proactive tool usage encouraged

### Tool List Function
- Added `list_available_tools` function
- Returns tools in simple, straightforward language
- Includes descriptions and examples for each tool
- Summary provided for quick reference

### Current Tools (7 Total)
1. List Available Tools - Shows what tools are available
2. Generate Proposal - Creates construction proposal PDFs
3. Calculate Material Quantities - Figures out how much material needed
4. Calculate Material Cost - Tells material costs using real pricing
5. Calculate Labor Cost - Calculates labor costs based on hourly rates
6. Calculate Equipment Cost - Figures out equipment rental costs
7. Full Project Estimate - Creates complete project cost breakdown

## Future Ideas & Concepts

### To Be Discussed/Implemented
- [ ] Additional tool integrations
- [ ] More data sources
- [ ] UI improvements
- [ ] User feedback mechanisms

---

*Last updated: [Current Date]*
*These notes capture ideas and concepts discussed during development*

