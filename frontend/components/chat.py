import requests
import streamlit as st

BACKEND_URL = "http://127.0.0.1:8000/chat"


# ---------------------------------------------------
# USER MESSAGE
# ---------------------------------------------------

def user_message(message: str):

    st.markdown(
        f"""
<div class="user-card fade">

<div style="display:flex;align-items:center;gap:12px;">

<div style="
height:46px;
width:46px;
border-radius:50%;
background:#7C3AED;
display:flex;
align-items:center;
justify-content:center;
font-size:22px;
">

👤

</div>

<div style="font-size:17px;">

{message}

</div>

</div>

</div>
""",
        unsafe_allow_html=True,
    )


# ---------------------------------------------------
# AI MESSAGE
# ---------------------------------------------------

def ai_message(message: str):

    st.markdown(
        f"""
<div class="ai-card fade">

<div style="display:flex;align-items:center;gap:12px;">

<div style="
height:46px;
width:46px;
border-radius:50%;
background:#06B6D4;
display:flex;
align-items:center;
justify-content:center;
font-size:22px;
">

🤖

</div>

<div>

<h4 style="margin-bottom:10px;">
Lumina AI
</h4>

</div>

</div>

<div style="margin-top:15px;font-size:16px;line-height:1.8;">

{message}

</div>

</div>
""",
        unsafe_allow_html=True,
    )


# ---------------------------------------------------
# CHAT WINDOW
# ---------------------------------------------------

def render_chat():

    if "messages" not in st.session_state:
        st.session_state.messages = []

    prompt = st.chat_input(
        "Ask Lumina AI anything..."
    )

    if prompt:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        st.rerun()

    for message in st.session_state.messages:

        if message["role"] == "user":
            user_message(message["content"])

        else:
            ai_message(message["content"])


# ---------------------------------------------------
# BACKEND
# ---------------------------------------------------

def process_last_message():

    if len(st.session_state.messages) == 0:
        return

    if st.session_state.messages[-1]["role"] != "user":
        return

    prompt = st.session_state.messages[-1]["content"]

    with st.spinner("🧠 Lumina AI is thinking..."):

        response = requests.post(
            BACKEND_URL,
            json={
                "query": prompt,
                "thread_id": st.session_state.thread_id
            },
            timeout=120
        )

        response.raise_for_status()

        result = response.json()

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": result["answer"]
        }
    )

    st.session_state.execution_trace = result["execution_trace"]

    st.session_state.tool_calls = result["tool_calls"]

    st.session_state.tool_outputs = result["tool_outputs"]

    st.rerun()



# import streamlit as st

# from services.api import BackendAPI


# def render_chat():

#     # No conversation selected
#     if "conversation_id" not in st.session_state:
#         st.info("Start a new conversation.")
#         return

#     try:
#         messages = BackendAPI.get_messages(
#             st.session_state.conversation_id
#         )

#     except Exception as e:
#         st.error(f"Unable to load messages.\n\n{e}")
#         return

#     if not messages:
#         st.markdown(
#             """
#             <div style="text-align:center;padding-top:120px;">
#                 <h2>✨ Lumina AI</h2>
#                 <p>How can I help you today?</p>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )
#         return

#     for message in messages:

#         with st.chat_message(message["role"]):

#             st.markdown(message["content"])