from mcp.client.streamable_http import streamablehttp_client
from strands import Agent
from strands.tools.mcp.mcp_client import MCPClient

def create_streamable_http_transport():
   return streamablehttp_client("http://localhost:8000/mcp/")

streamable_http_mcp_client = MCPClient(create_streamable_http_transport)

# Use the MCP server in a context manager
with streamable_http_mcp_client:
    # Get the tools from the MCP server
    tools = streamable_http_mcp_client.list_tools_sync()

    # Create an agent with the MCP tools
    agent = Agent(tools=tools)

    # Direct imethod access with MCP Tool selection
    result = streamable_http_mcp_client.call_tool_sync(
        tool_use_id="tool-123",
        name="add",
        arguments={"x": 125, "y": 375}
    )

    print(f"Calculation result: {result['content'][0]['text']}")

    # Explicit tool call
    result = agent.tool.add(x=145, y=325)
    print(f"Calculation result: {result['content'][0]['text']}")

    result = agent.tool.divide(x=100, y=201)
    print(f"Calculation result: {result['content'][0]['text']}")