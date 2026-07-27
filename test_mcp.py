import asyncio

from backend.mcp_manager.client import mcp_client
from backend.mcp_manager.executor import mcp_executor


async def main():

    await mcp_client.connect()

    result = await mcp_executor.execute(
        tool_name="get_random_fact",
        arguments={}
    )

    print(result)

    await mcp_client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())