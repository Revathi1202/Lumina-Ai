import streamlit as st


def render_header():

    st.markdown(
        """
<div style="
background:#111827;
border:1px solid rgba(255,255,255,.06);
border-radius:20px;
padding:18px 24px;
margin-top:-10px;
margin-bottom:18px;
">

<div style="
display:flex;
justify-content:space-between;
align-items:center;
">

<div>

<h1 class="main-title" style="margin:0;">
✨ Lumina AI
</h1>

<p style="
margin-top:6px;
margin-bottom:0;
font-size:15px;
color:#CBD5E1;
">
Agentic AI Platform with MCP Integration
</p>

</div>

<div>

<span style="
background:#16A34A;
padding:8px 18px;
border-radius:20px;
font-weight:600;
color:white;
font-size:14px;
">
🟢 Agent Ready
</span>

</div>

</div>

<div style="height:18px;"></div>

<div style="
display:grid;
grid-template-columns:repeat(4,1fr);
gap:12px;
">

<div style="
background:#1E293B;
border-radius:14px;
padding:16px;
border:1px solid rgba(255,255,255,.05);
">

<div style="font-size:24px;">🤖</div>

<div style="
margin-top:10px;
font-size:15px;
font-weight:600;
color:white;
">
AI Model
</div>

<div style="
margin-top:4px;
font-size:14px;
color:#22C55E;
">
Gemini 2.5 Flash
</div>

</div>

<div style="
background:#1E293B;
border-radius:14px;
padding:16px;
border:1px solid rgba(255,255,255,.05);
">

<div style="font-size:24px;">🧠</div>

<div style="
margin-top:10px;
font-size:15px;
font-weight:600;
color:white;
">
Agent
</div>

<div style="
margin-top:4px;
font-size:14px;
color:#38BDF8;
">
LangGraph
</div>

</div>

<div style="
background:#1E293B;
border-radius:14px;
padding:16px;
border:1px solid rgba(255,255,255,.05);
">

<div style="font-size:24px;">🔌</div>

<div style="
margin-top:10px;
font-size:15px;
font-weight:600;
color:white;
">
MCP Gateway
</div>

<div style="
margin-top:4px;
font-size:14px;
color:#22C55E;
">
Connected
</div>

</div>

<div style="
background:#1E293B;
border-radius:14px;
padding:16px;
border:1px solid rgba(255,255,255,.05);
">

<div style="font-size:24px;">⚙</div>

<div style="
margin-top:10px;
font-size:15px;
font-weight:600;
color:white;
">
Tools
</div>

<div style="
margin-top:4px;
font-size:14px;
color:#FACC15;
">
12 Available
</div>

</div>

</div>

</div>
""",
        unsafe_allow_html=True,
    )