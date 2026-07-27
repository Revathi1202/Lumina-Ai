# from .client import mcp_client


# class MCPLoader:
#     async def load_tools(self):
#         """
#         Fetch all available tools from the MCP server.
#         """

#         result = await mcp_client.session.list_tools()

#         return result.tools


# mcp_loader = MCPLoader()


from .client import mcp_client


class MCPLoader:
    async def load_tools(self):
        result = await mcp_client.session.list_tools()

        tools = []

        for tool in result.tools:
            tools.append({
                "name": tool.name,
                "description": tool.description,
                "input_schema": tool.inputSchema
            })

        return tools


mcp_loader = MCPLoader()