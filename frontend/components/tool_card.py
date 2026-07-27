# import json
# import streamlit as st


# def render_tool_cards(tool_calls, tool_outputs):

#     if not tool_calls:
#         return

#     st.subheader("⚡ MCP Tool Execution")

#     for index, tool in enumerate(tool_calls):

#         with st.container(border=True):

#             col1, col2 = st.columns([4, 1])

#             with col1:

#                 st.markdown(
#                     f"### 🔧 {tool.get('tool','Unknown Tool')}"
#                 )

#             with col2:

#                 st.success("Done")

#             # ----------------------------
#             # Arguments
#             # ----------------------------

#             arguments = tool.get("arguments", {})

#             if arguments:

#                 with st.expander("📥 Input Arguments"):

#                     st.json(arguments)

#             # ----------------------------
#             # Output
#             # ----------------------------

#             if index < len(tool_outputs):

#                 output = tool_outputs[index]

#                 with st.expander(
#                     "📤 Tool Output",
#                     expanded=True
#                 ):

#                     if isinstance(output, dict):

#                         st.json(output)

#                     elif isinstance(output, list):

#                         st.json(output)

#                     else:

#                         st.code(
#                             str(output),
#                             language="text"
#                         )