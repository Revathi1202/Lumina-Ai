from langgraph.graph import StateGraph, START, END

from agent.state import AgentState
from agent.nodes import planner_node, response_node
from agent.tool_node import tool_node
from agent.memory import memory

builder = StateGraph(AgentState)

# ---------------- Nodes ---------------- #

builder.add_node("planner", planner_node)
builder.add_node("tool_executor", tool_node)
builder.add_node("response", response_node)

# ---------------- Start ---------------- #

builder.add_edge(START, "planner")


# ---------------- Router ---------------- #

def planner_router(state):

    plan = state.get("plan", {})

    if plan.get("needs_tool", False):
        return "tool"

    return "response"


builder.add_conditional_edges(
    "planner",
    planner_router,
    {
        "tool": "tool_executor",
        "response": "response",
    },
)

# ---------------- Loop ---------------- #

builder.add_edge("tool_executor", "planner")

# ---------------- End ---------------- #

builder.add_edge("response", END)

graph = builder.compile(
    checkpointer=memory
)