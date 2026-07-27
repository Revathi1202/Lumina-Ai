# from gateway.config import MCP_SERVER_URL


# class MCPClient:
#     def __init__(self):
#         self.server_url = MCP_SERVER_URL
#         self.session = None

#     async def connect(self):
#         """
#         Connect to the remote MCP server.
#         """
#         print(f"Connecting to: {self.server_url}")

#     async def disconnect(self):
#         """
#         Close MCP connection.
#         """
#         print("Disconnected")


# mcp_client = MCPClient()


from contextlib import AsyncExitStack

import httpx
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

from gateway.config import MCP_SERVER_URL, MCP_GATEWAY_TOKEN


class MCPClient:
    def __init__(self):
        self.session = None
        self.exit_stack = AsyncExitStack()

    async def connect(self):
        """
        Connect to the remote MCP server.
        """

        http_client = httpx.AsyncClient(
            headers={
                "Authorization": f"Bearer {MCP_GATEWAY_TOKEN}"
            },
            timeout=30.0,
        )


        read_stream, write_stream, _ = await self.exit_stack.enter_async_context(
            streamable_http_client(
                MCP_SERVER_URL,
                http_client=http_client,
            )
        )

        self.session = await self.exit_stack.enter_async_context(
            ClientSession(
                read_stream,
                write_stream,
            )
        )

        await self.session.initialize()

        print("✅ Connected to MCP Server")

        return self.session

    async def disconnect(self):
        await self.exit_stack.aclose()
        print("Disconnected")


mcp_client = MCPClient()