from backend.mcp_manager.executor import mcp_executor


async def tool_node(state):
    plan = state["plan"]

    # If no tool is required, skip execution
    if not plan.get("needs_tool", False):
        return {
            "tool_calls": [],
            "tool_outputs": [],
            "execution_trace": []
        }

    tool_name = plan["tool"]
    arguments = plan.get("arguments", {})

    # Execute the MCP tool
    result = await mcp_executor.execute(
        tool_name=tool_name,
        arguments=arguments
    )

    return {
        "tool_calls": [
            {
                "tool": tool_name,
                "arguments": arguments
            }
        ],

        "tool_outputs": [result],

        "execution_trace": [
            {
                "type": "tool",
                "title": tool_name,
                "content": result
            }
        ]
    }