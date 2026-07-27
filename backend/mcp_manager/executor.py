from .client import mcp_client


class MCPExecutor:
    async def execute(self, tool_name: str, arguments: dict):
        """
        Execute an MCP tool.
        """

        result = await mcp_client.session.call_tool(
            tool_name,
            arguments,
        )
        
        
        if result.isError:
            return {
        "success": False,
        "error": result.content
    }
        return {
    "success": True,
    "data": result.structuredContent,
    "text": result.content[0].text if result.content else ""
}



mcp_executor = MCPExecutor()