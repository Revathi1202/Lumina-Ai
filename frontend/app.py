import uuid
import streamlit as st

# ==========================
# Styles
# ==========================

from styles.css import load_css

# ==========================
# Backend
# ==========================
import services.api as api



BackendAPI = api.BackendAPI

import inspect

print("BackendAPI file:", inspect.getfile(BackendAPI))
print("Methods:", [m for m in dir(BackendAPI) if not m.startswith("__")])

# ==========================
# Components
# ==========================

from components.header import render_header
from components.sidebar import render_sidebar
from components.planner_card import render_planner_card
from components.timeline import render_activity
from components.response_card import render_response_card
from components.chat_input import render_chat_input


st.set_page_config(
    page_title="Lumina AI",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

if "chat_id" not in st.session_state:
    chat = BackendAPI.create_chat()
    st.session_state.chat_id = chat["id"]
    
    


# ==========================
# Session State
# ==========================

if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_answer" not in st.session_state:
    st.session_state.last_answer = ""

if "execution_trace" not in st.session_state:
    st.session_state.execution_trace = []

if "tool_calls" not in st.session_state:
    st.session_state.tool_calls = []

if "tool_outputs" not in st.session_state:
    st.session_state.tool_outputs = []

# ==========================
# Load CSS
# ==========================

load_css()

# ==========================
# Sidebar
# ==========================

render_sidebar()

# Load selected chat

try:
    data = BackendAPI.load_chat(
        st.session_state.chat_id
    )

    st.session_state.messages = data["messages"]

except Exception:
    st.session_state.messages = []

render_header()


# or message in st.session_state.messages:

# #     if message["role"] == "user":

# #         with st.chat_message("user"):
# #             st.markdown(message["content"])


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ==========================
# Chat Input
# ==========================

prompt = render_chat_input()



if prompt:

    # Rename only when this is the first message
    if len(st.session_state.messages) == 0:

        BackendAPI.rename_chat(
            st.session_state.chat_id,
            prompt[:40]
        )

    BackendAPI.save_message(
        st.session_state.chat_id,
        "user",
        prompt
    )

# ==========================
# Backend
# ==========================

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    try:

        with st.spinner("🧠 Lumina AI is thinking..."):

            result = BackendAPI.send_message(
                query=prompt,
                thread_id=st.session_state.thread_id,
            )

        answer = result["answer"]

        st.session_state.last_answer = answer
        BackendAPI.save_message(
    st.session_state.chat_id,
    "assistant",
    answer
)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )

        st.session_state.execution_trace = result.get(
            "execution_trace",
            [],
        )

        st.session_state.tool_calls = result.get(
            "tool_calls",
            [],
        )

        st.session_state.tool_outputs = result.get(
            "tool_outputs",
            [],
        )

        st.rerun()

    except Exception as e:

        st.error(f"Backend Error\n\n{e}")

# ==========================
# Agent Activity
# ==========================

if st.session_state.execution_trace:

    render_activity(
        st.session_state.execution_trace
    )

# ==========================
# Final AI Response
# ==========================

# if st.session_state.last_answer:

#     render_response_card(
#         st.session_state.last_answer
#     )






# import os
# import sys

# PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# if PROJECT_ROOT not in sys.path:
#     sys.path.insert(0, PROJECT_ROOT)


# from backend.database.database import (
#     init_db,
#     create_chat,
#     save_message,
#     load_messages,
#     get_all_chats,
#     rename_chat

# )



# import uuid
# import streamlit as st

# # ==========================
# # Styles
# # ==========================

# from styles.css import load_css

# # ==========================
# # Backend
# # ==========================

# from services.api import BackendAPI

# # ==========================
# # Components
# # ==========================

# from components.header import render_header
# from components.sidebar import render_sidebar
# from components.planner_card import render_planner_card
# from components.timeline import render_activity
# from components.response_card import render_response_card
# from components.chat_input import render_chat_input

# # ==========================
# # Page Config
# # ==========================
# init_db()
# if "chat_id" not in st.session_state:
#     st.session_state.chat_id = create_chat()

# st.set_page_config(
#     page_title="Lumina AI",
#     page_icon="✨",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# # ==========================
# # Session State
# # ==========================

# if "thread_id" not in st.session_state:
#     st.session_state.thread_id = str(uuid.uuid4())

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# if "last_answer" not in st.session_state:
#     st.session_state.last_answer = ""

# if "execution_trace" not in st.session_state:
#     st.session_state.execution_trace = []

# if "tool_calls" not in st.session_state:
#     st.session_state.tool_calls = []

# if "tool_outputs" not in st.session_state:
#     st.session_state.tool_outputs = []

# # ==========================
# # Load CSS
# # ==========================

# load_css()

# # ==========================
# # Sidebar
# # ==========================

# render_sidebar()



# # Load selected chat
# loaded_messages = load_messages(st.session_state.chat_id)

# st.session_state.messages = [
#     {
#         "role": role,
#         "content": content,
#     }
#     for role, content in loaded_messages
# ]

# # ==========================
# # Header
# # ==========================

# render_header()

# # ==========================
# # Chat History
# # ==========================

# # for message in st.session_state.messages:

# #     if message["role"] == "user":

# #         with st.chat_message("user"):
# #             st.markdown(message["content"])


# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # ==========================
# # Chat Input
# # ==========================

# prompt = render_chat_input()



# if prompt:

#     # Rename only when this is the first message
#     if len(load_messages(st.session_state.chat_id)) == 0:
#         rename_chat(
#             st.session_state.chat_id,
#             prompt[:40]
#         )

#     save_message(
#         st.session_state.chat_id,
#         "user",
#         prompt
#     )

# # ==========================
# # Backend
# # ==========================

# if prompt:

#     st.session_state.messages.append(
#         {
#             "role": "user",
#             "content": prompt,
#         }
#     )

#     try:

#         with st.spinner("🧠 Lumina AI is thinking..."):

#             result = BackendAPI.send_message(
#                 query=prompt,
#                 thread_id=st.session_state.thread_id,
#             )

#         answer = result["answer"]

#         st.session_state.last_answer = answer
        
        
        
#         save_message(
#     st.session_state.chat_id,
#     "assistant",
#     answer
# )

#         st.session_state.messages.append(
#             {
#                 "role": "assistant",
#                 "content": answer,
#             }
#         )

#         st.session_state.execution_trace = result.get(
#             "execution_trace",
#             [],
#         )

#         st.session_state.tool_calls = result.get(
#             "tool_calls",
#             [],
#         )

#         st.session_state.tool_outputs = result.get(
#             "tool_outputs",
#             [],
#         )

#         st.rerun()

#     except Exception as e:

#         st.error(f"Backend Error\n\n{e}")

# # ==========================
# # Agent Activity
# # ==========================

# if st.session_state.execution_trace:

#     render_activity(
#         st.session_state.execution_trace
#     )

# # ==========================
# # Final AI Response
# # ==========================

# # if st.session_state.last_answer:

# #     render_response_card(
# #         st.session_state.last_answer
# #     )



