import streamlit as st


def render_response_card(answer):

    if "messages" not in st.session_state:
        return

    if len(st.session_state.messages) == 0:
        return

    last = st.session_state.messages[-1]

    if last["role"] != "assistant":
        return

    response = last["content"]

    st.markdown("## 🤖 AI Response")

    st.markdown(
        f"""
<div class="ai-card fade">

<div style="display:flex;justify-content:space-between;align-items:center;">

<div style="display:flex;align-items:center;gap:12px;">

<div style="
width:50px;
height:50px;
border-radius:50%;
background:linear-gradient(135deg,#06B6D4,#7C3AED);
display:flex;
align-items:center;
justify-content:center;
font-size:24px;
">

🤖

</div>

<div>

<h3 style="margin:0;">
Lumina AI
</h3>

<p style="margin:0;color:#94A3B8;">
Generated Response
</p>

</div>

</div>

<div style="
padding:8px 16px;
border-radius:20px;
background:rgba(34,197,94,.15);
color:#22C55E;
font-weight:600;
">

✔ Complete

</div>

</div>

<hr>

<div style="
font-size:16px;
line-height:1.9;
padding-top:10px;
">

{response}

</div>

<hr>

<div style="
display:flex;
justify-content:space-between;
align-items:center;
margin-top:10px;
">

<div style="color:#94A3B8;">

🧠 Gemini &nbsp;&nbsp;
⚡ MCP &nbsp;&nbsp;
🚀 LangGraph

</div>

<div style="font-size:20px;">

👍 &nbsp;&nbsp; 👎 &nbsp;&nbsp; 📋

</div>

</div>

</div>
""",
        unsafe_allow_html=True,
    )