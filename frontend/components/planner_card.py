import streamlit as st


def render_planner_card(execution_trace):

    if not execution_trace:
        return

    planner = None

    for step in execution_trace:

        if step.get("type") == "plan":
            planner = step
            break

    if planner is None:
        return

    content = planner.get("content", {})

    if not isinstance(content, dict):
        return

    st.subheader("🧠 Planner")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Needs Tool",
            "Yes" if content.get("needs_tool") else "No"
        )

    with col2:
        st.metric(
            "Tools Selected",
            len(content.get("tools", []))
        )

    reason = content.get("reason", "")

    if reason:
        st.info(reason)

    tools = content.get("tools", [])

    if tools:

        st.write("### Selected Tools")

        for tool in tools:

            st.success(f"🔧 {tool['tool']}")

            if tool.get("arguments"):
                st.json(tool["arguments"])