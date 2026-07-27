import uuid
import streamlit as st

from backend.database.database import (
    get_all_chats,
    create_chat,
)


def render_sidebar():

    with st.sidebar:

        # =====================================
        # Logo
        # =====================================

        st.markdown("# ✨ Lumina AI")
        st.caption("Agentic AI Learning Assistant")

        st.divider()

        # =====================================
        # New Chat
        # =====================================

        if st.button("➕ New Chat", use_container_width=True):

            st.session_state.chat_id = create_chat()

            st.session_state.messages = []
            st.session_state.last_answer = ""
            st.session_state.execution_trace = []
            st.session_state.tool_calls = []
            st.session_state.tool_outputs = []

            st.session_state.thread_id = str(uuid.uuid4())

            st.rerun()

        st.divider()

        # =====================================
        # Chat History
        # =====================================

        st.markdown("### 💬 Chats")

        chats = get_all_chats()

        if chats:

            for chat_id, title in chats:

                if st.button(
                    title,
                    key=f"chat_{chat_id}",
                    use_container_width=True,
                ):
                    st.session_state.chat_id = chat_id
                    st.session_state.last_answer = ""
                    st.rerun()

        else:

            st.caption("No chats yet.")

        st.divider()

        # =====================================
        # Agent Status
        # =====================================

        st.markdown("## 🤖 Agent Status")

        st.info(
            f"""
**Active Session**

`{st.session_state.thread_id[:8]}`
"""
        )

        # =====================================
        # Components
        # =====================================

        st.markdown("### 🧩 Components")

        col1, col2 = st.columns(2)

        with col1:

            st.success("🤖 AI Model")
            st.caption("Gemini 2.5 Flash")

            st.success("🧠 Agent")
            st.caption("LangGraph")

        with col2:

            st.success("🔌 MCP")
            st.caption("Connected")

            st.success("⚙️ Tools")
            st.caption("12 Available")

        st.divider()

        # =====================================
        # Session Overview
        # =====================================

        st.markdown("## 📊 Session Overview")

        st.metric(
            "Conversation Turns",
            len(st.session_state.messages),
        )

        st.metric(
            "Tool Calls",
            len(st.session_state.tool_calls),
        )

        st.metric(
            "Execution Steps",
            len(st.session_state.execution_trace),
        )

        st.divider()

        # =====================================
        # Architecture
        # =====================================

        st.markdown("## 🏗️ Architecture")

        st.markdown(
            """
- 🤖 Gemini 2.5 Flash
- 🧠 LangGraph
- 🔌 MCP Gateway
- ⚡ FastAPI
"""
        )

# import uuid
# import streamlit as st


# from backend.database import get_all_chats


# def render_sidebar():

#     with st.sidebar:

#         # =====================================
#         # Logo
#         # =====================================

#         st.markdown("# Lumina AI")
#         st.caption("Agentic AI Platform")

#         st.divider()

#         # =====================================
#         # New Chat
#         # =====================================

#         if st.button("➕ New Chat", use_container_width=True):

#             st.session_state.messages = []
#             st.session_state.execution_trace = []
#             st.session_state.tool_calls = []
#             st.session_state.tool_outputs = []

#             st.session_state.thread_id = str(uuid.uuid4())

#             st.rerun()

#         st.divider()

#         # =====================================
#         # Agent Status
#         # =====================================

#         st.markdown("## 🤖 Agent Status")

#         st.info(
#             f"""
# **Active Session**

# `{st.session_state.thread_id[:8]}`
# """
#         )
        
        
#         chats = get_all_chats()
#         st.subheader("Chats")
#         for chat_id, title in chats:
#             if st.button(
#         title,
#         key=f"chat_{chat_id}",
#         use_container_width=True,
#     ):
#                 st.session_state.chat_id = chat_id
#                 st.rerun()

#         st.markdown("### 🧩 Components")

#         col1, col2 = st.columns(2)

#         with col1:

#             st.success("🤖 AI Model")
#             st.caption("Gemini 2.5 Flash")

#             st.success("🧠 Agent")
#             st.caption("LangGraph")

#         with col2:

#             st.success("🔌 MCP")
#             st.caption("Connected")

#             st.success("⚙ Tools")
#             st.caption("12 Available")

#         st.divider()

#         # =====================================
#         # Session Overview
#         # =====================================

#         st.markdown("## 📊 Session Overview")

#         st.metric(
#             "Conversation Turns",
#             len(st.session_state.messages),
#         )

#         st.metric(
#             "Tool Calls",
#             len(st.session_state.tool_calls),
#         )

#         st.metric(
#             "Execution Steps",
#             len(st.session_state.execution_trace),
#         )

#         st.divider()

#         # =====================================
#         # Architecture
#         # =====================================

#         st.markdown("## 🏗 Architecture")

#         st.markdown(
#             """
# - 🤖 Gemini 2.5 Flash
# - 🧠 LangGraph Agent
# - 🔌 MCP Gateway
# - ⚡ FastAPI Backend
# """
#         )


# import streamlit as st
# from services.api import BackendAPI


# def render_sidebar():

#     with st.sidebar:

#         st.title("✨ Lumina AI")
#         st.caption("Agentic AI Platform")

#         st.divider()

#         # ==========================================
#         # New Chat
#         # ==========================================

#         if st.button(
#             "➕ New Chat",
#             use_container_width=True,
#         ):

#             conversation = BackendAPI.create_conversation()

#             st.session_state.conversation_id = conversation["id"]
#             st.session_state.thread_id = conversation["id"]

#             st.session_state.execution_trace = []
#             st.session_state.tool_calls = []
#             st.session_state.tool_outputs = []

#             st.rerun()

#         st.divider()

#         st.subheader("💬 Chats")

#         try:

#             conversations = BackendAPI.get_conversations()

#         except Exception:

#             st.error("Cannot connect to backend.")
#             return

#         if len(conversations) == 0:

#             st.caption("No conversations yet.")

#             return

#         # ==========================================
#         # Conversation List
#         # ==========================================

#         for conversation in conversations:

#             col1, col2 = st.columns([5, 1])

#             # -----------------------
#             # Open Conversation
#             # -----------------------

#             with col1:

#                 selected = (
#                     st.session_state.get("conversation_id")
#                     == conversation["id"]
#                 )

#                 label = conversation["title"]

#                 if selected:
#                     label = "🟢 " + label

#                 if st.button(
#                     label,
#                     key=f"chat_{conversation['id']}",
#                     use_container_width=True,
#                 ):

#                     st.session_state.conversation_id = conversation["id"]
#                     st.session_state.thread_id = conversation["id"]

#                     st.session_state.execution_trace = []
#                     st.session_state.tool_calls = []
#                     st.session_state.tool_outputs = []

#                     st.rerun()

#             # -----------------------
#             # Delete Conversation
#             # -----------------------

#             with col2:

#                 if st.button(
#                     "🗑️",
#                     key=f"delete_{conversation['id']}",
#                 ):

#                     BackendAPI.delete_conversation(
#                         conversation["id"]
#                     )

#                     # if deleted active chat,
#                     # create a new one

#                     if (
#                         st.session_state.get("conversation_id")
#                         == conversation["id"]
#                     ):

#                         new_chat = BackendAPI.create_conversation()

#                         st.session_state.conversation_id = new_chat["id"]
#                         st.session_state.thread_id = new_chat["id"]

#                     st.rerun()