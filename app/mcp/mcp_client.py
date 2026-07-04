from app.mcp.mcp_server import MCPServer


class MCPClient:

    def __init__(self):

        self.server = MCPServer()

    def discover_tools(self):

        return self.server.list_tools()

    def get_tool(self, tool):

        return self.server.get_tool(tool)