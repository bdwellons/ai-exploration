## Strands with MCP Example

### Description
This example uses the Strands framework to stand up two components, an MCP server that provides calculator functionality and an agent with prompts that processes them through the MCP calculator server. The MCP provides 3 hard coded math functions and for the divide function it reaches out to a Bedrock model you define.

### Getting Started

Export your AWS credentials to your local shell environment. AWS_KEY, SECRET, etc. You will also need to find the 2 instances of "TODO" and action those.

Get your Python Virtual ENV running.

The below commands should all be run from the repository root.

Only necessary if .venv doesn't already exist
> python -m venv .venv

Start your virtual ENV
> source .venv/bin/activate # On Windows: .venv\Scripts\activate

Install dependencies from requirements.txt
> pip install -r strands-with-mcp/requirements.txt # Use pinned versions

Run the MCP Calculator Server
> python3 -u strands-with-mcp/mcp_calculator_server.py

In another terminal, run the simulated agent input
> python3 -u strands-with-mcp/strands_agent.py