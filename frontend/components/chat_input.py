import streamlit as st


def render_chat_input():

    col1, col2 = st.columns([12, 1])

    with col1:
        prompt = st.text_input(
            "",
            placeholder="Ask Lumina AI anything...",
            label_visibility="collapsed",
            key="chat_input"
        )

    with col2:
        send = st.button("➤", use_container_width=True)

    if send and prompt.strip():
        return prompt

    return None