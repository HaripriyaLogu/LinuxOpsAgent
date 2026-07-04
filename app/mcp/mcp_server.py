from app.mcp.tool_registry import TOOLS


class MCPServer:

    def list_tools(self):

        return list(TOOLS.keys())

    def get_tool(self, tool_name):

        return TOOLS.get(tool_name)