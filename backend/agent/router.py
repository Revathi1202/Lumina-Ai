def planner_router(state):

    if state["plan"].get("needs_tool"):
        return "tool"

    return "response"