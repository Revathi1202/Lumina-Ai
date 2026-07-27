from .loader import mcp_loader


class MCPRegistry:
    def __init__(self):
        self.tools = {}

    async def initialize(self):
        tool_list = await mcp_loader.load_tools()

        self.tools = {
            tool["name"]: tool
            for tool in tool_list
        }

    def get(self, tool_name):
        return self.tools.get(tool_name)

    def list(self):
        return list(self.tools.values())


mcp_registry = MCPRegistry()