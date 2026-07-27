# import streamlit as st


# def render_activity(trace):

#     if not trace:
#         return

#     st.markdown("## 🕒 Agent Activity")

#     shown_analysis = False

#     for step in trace:

#         step_type = step.get("type")

#         # Show analysis only once
#         if step_type == "planner":

#             if not shown_analysis:
#                 st.success("✓ Analysed your request")
#                 shown_analysis = True

#             continue

#         if step_type != "tool":
#             continue

#         title = step.get("title", "")

#         if title == "Location Lookup":
#             st.success("✓ Located requested location")

#         elif title == "Weather Lookup":
#             st.success("✓ Retrieved live weather")

#         elif title == "Diagram Generator":
#             st.success("✓ Generated diagram")

#         elif title == "Document Search":
#             st.success("✓ Searched uploaded document")

#         elif title == "Web Search":
#             st.success("✓ Searched web")

#         elif title == "Database Lookup":
#             st.success("✓ Retrieved database information")

#         else:
#             st.success(f"✓ {title}")

#     st.success("✓ Generated response")



import streamlit as st


def render_activity(trace):

    if not trace:
        return

    st.markdown("## 🕒 Agent Activity")

    planner_shown = False

    for step in trace:

        step_type = step.get("type", "")

        # ------------------------------------
        # Planner
        # ------------------------------------
        if step_type == "planner":

            if planner_shown:
                continue

            planner_shown = True

            content = step.get("content", {})

            summary = content.get("summary", "")
            next_step = content.get("next_step", "")

            with st.expander("🧠 Planner", expanded=True):

                st.success("✓ Analysed your request")

                if summary:
                    st.markdown(f"**Intent**")
                    st.info(summary)

                if next_step:
                    st.markdown("**🔧 Selected Tool**")
                    st.code(next_step)

            continue

        # ------------------------------------
        # Tool Execution
        # ------------------------------------
        if step_type == "tool":

            content = step.get("content", {})

            tool_name = content.get("tool_name", "Unknown Tool")
            description = content.get("description", "")
            arguments = content.get("arguments", {})
            result = content.get("result", "")

            with st.expander(f"⚡ Executing: {tool_name}", expanded=False):

                st.success("✓ Tool Execution")

                if description:
                    st.markdown(f"**Description**")
                    st.info(description)

                if arguments:
                    st.markdown("**Arguments**")
                    st.json(arguments)

                if result:
                    st.markdown("**📄 Tool Result**")
                    st.write(result)

    # ------------------------------------
    # Response
    # ------------------------------------

    with st.expander("🤖 Response Generation", expanded=True):

        st.success("✓ Generated final response")