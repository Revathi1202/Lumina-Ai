import httpx

from gateway.config import MCP_SERVER_URL


class MCPProxy:

    def __init__(self):
        self.url = MCP_SERVER_URL

    async def forward_request(
        self,
        body: dict,
        headers: dict | None = None,
    ):
        async with httpx.AsyncClient(timeout=30) as client:

            response = await client.post(
                self.url,
                json=body,
                headers=headers,
            )

            return {
                "status_code": response.status_code,
                "body": response.text,
            }


proxy = MCPProxy()