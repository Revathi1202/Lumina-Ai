import json

from agent.llm import llm
from agent.prompts import PLANNER_PROMPT
from agent.models import PlannerOutput

from mcp_manager.registry import mcp_registry


async def planner_node(state):

    # -----------------------------
    # Available MCP Tools
    # -----------------------------
    tools = mcp_registry.list()

    tool_description = ""

    for tool in tools:

        tool_description += f"""
Tool Name: {tool['name']}
Description: {tool['description']}
Input Schema:
{json.dumps(tool['input_schema'], indent=2)}

"""

    # -----------------------------
    # Previous Tool Executions
    # -----------------------------
    previous_tool_results = ""

    tool_calls = state.get("tool_calls", [])
    tool_outputs = state.get("tool_outputs", [])

    if tool_calls and tool_outputs:

        for index, (call, output) in enumerate(
            zip(tool_calls, tool_outputs), start=1
        ):

            previous_tool_results += f"""

Execution {index}

Tool:
{call["tool"]}

Arguments:
{json.dumps(call["arguments"], indent=2)}

Output:
{str(output)}

"""

    else:

        previous_tool_results = "No tools have been executed yet."

    # -----------------------------
    # Build Prompt
    # -----------------------------
    prompt = PLANNER_PROMPT.format(
        tool_list=tool_description,
        user_query=state["user_query"],
        previous_tool_results=previous_tool_results
    )

    planner_llm = llm.with_structured_output(PlannerOutput)

    try:

        plan = planner_llm.invoke(prompt)

    except Exception as e:

        print("Planner Error:", e)

        plan = PlannerOutput(
            needs_tool=False,
            tools=[],
            reason="Planner failed."
        )

    # -----------------------------
    # Planner Trace
    # -----------------------------
    
    
    planner_trace = {
    "type": "planner",
    "title": "Planner",
    "content": {
        "summary": plan.reason,
        "next_step": ", ".join(
            [tool.tool for tool in plan.tools]
        ) if plan.needs_tool else "No external tool required"
    }
}
#     planner_trace = {
#     "type": "planner",
#     "title": "Understanding your request",
#     "content": {
#         "summary": "...",
#         "next_step": "..."
#     }
# }



    return {

        "plan": plan.model_dump(),

        "selected_tools": [
            tool.tool
            for tool in plan.tools
        ] if plan.needs_tool else [],

        "execution_trace": [
            planner_trace
        ]
    }
# ---------------- Response ---------------- #
import json

from agent.llm import llm


async def response_node(state):

    # -----------------------------
    # Convert tool outputs to text
    # -----------------------------
    readable_outputs = []

    for output in state.get("tool_outputs", []):

        try:

            # List of TextContent objects
            if isinstance(output, list):

                texts = []

                for item in output:

                    if hasattr(item, "text"):
                        texts.append(item.text)
                    else:
                        texts.append(str(item))

                readable_outputs.append("\n".join(texts))

            # Single TextContent object
            elif hasattr(output, "text"):

                readable_outputs.append(output.text)

            # Dictionary
            elif isinstance(output, dict):

                readable_outputs.append(
                    json.dumps(output, indent=2)
                )

            # Everything else
            else:

                readable_outputs.append(str(output))

        except Exception:

            readable_outputs.append(str(output))

    tool_results = "\n\n".join(readable_outputs)

    # -----------------------------
    # Final Response Prompt
    # -----------------------------
    prompt = f"""
You are Lumina AI, an intelligent AI assistant.

Answer the user's question naturally and professionally.

User Question:
{state["user_query"]}

Tool Results:
{tool_results}

Instructions:

- Tool results are the source of truth.
- Use all available tool results to generate one complete answer.
- Never mention planner output.
- Never mention tool names.
- Never mention MCP.
- Never mention JSON.
- Never expose internal reasoning.
- Never say "According to the tool..."
- Never say "The planner selected..."
- Do not include raw API responses.
- If multiple tool results are available, combine them into one coherent answer.
- If no tool results are available, answer using your own knowledge.
- If the available information is incomplete, politely mention what is missing instead of inventing facts.

Return only the final answer.
"""

    response = llm.invoke(prompt)

    return {
        "final_answer": response.content,
        "execution_trace": [
            {
                "type": "response",
                "title": "Final Response",
                "content": response.content,
            }
        ],
    }