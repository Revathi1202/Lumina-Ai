import asyncio

from mcp_manager.executor import mcp_executor

from agent.tool_metadata import get_tool_metadata
from agent.result_formatter import format_result


# ----------------------------------------
# Execute a single MCP tool
# ----------------------------------------

async def execute_tool(tool):

    tool_name = tool["tool"]
    arguments = tool.get("arguments", {})

    # Execute MCP Tool
    raw_result = await mcp_executor.execute(
        tool_name=tool_name,
        arguments=arguments
    )

    # UI Metadata
    metadata = get_tool_metadata(tool_name)

    # Format output for UI
    formatted_result = format_result(
        tool_name,
        raw_result
    )

    return {

        # Used internally by planner
        "tool_call": {
            "tool": tool_name,
            "arguments": arguments
        },

        # Used by planner in next iteration
        "tool_output": raw_result,

        # Used ONLY by UI
        "trace": {

            "type": "tool",

            "title": metadata["title"],

            "content": {

                "icon": metadata["icon"],

                "description": metadata["description"],

                "status": "Completed",

                "tool_name": tool_name,

                "arguments": arguments,

                "result": formatted_result

            }

        }

    }


# ----------------------------------------
# Tool Node
# ----------------------------------------

async def tool_node(state):

    plan = state["plan"]

    if not plan.get("needs_tool", False):

        return {

            "tool_calls": [],

            "tool_outputs": [],

            "execution_trace": []

        }

    results = await asyncio.gather(

        *(execute_tool(tool)
          for tool in plan.get("tools", []))

    )

    return {

        "tool_calls": [
            item["tool_call"]
            for item in results
        ],

        "tool_outputs": [
            item["tool_output"]
            for item in results
        ],

        "execution_trace": [
            item["trace"]
            for item in results
        ]

    }