from app.mcp.mcp_client import MCPClient

client = MCPClient()

print("\nAvailable Tools:\n")

for tool in client.discover_tools():

    print(tool)

print("\nFilesystem Tool:\n")

print(client.get_tool("filesystem"))