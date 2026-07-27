import time
import streamlit as st


# ----------------------------------------------------
# Typing Animation
# ----------------------------------------------------

def typing_animation():

    placeholder = st.empty()

    text = ""

    for word in [
        "🧠 Planning...",
        "⚡ Calling MCP Tools...",
        "📚 Collecting Knowledge...",
        "🤖 Generating Response..."
    ]:

        text += word + "\n"

        placeholder.markdown(
            f"""
<div style="
background:rgba(255,255,255,.05);
padding:18px;
border-radius:15px;
border-left:5px solid #06B6D4;
font-size:17px;
line-height:2;
">
{text}
</div>
""",
            unsafe_allow_html=True,
        )

        time.sleep(0.5)

    placeholder.empty()


# ----------------------------------------------------
# Online Badge
# ----------------------------------------------------

def online_badge():

    st.markdown(
        """
<div style="
display:flex;
align-items:center;
gap:10px;
">

<div style="
height:14px;
width:14px;
background:#22C55E;
border-radius:50%;
animation:pulse 1.5s infinite;
"></div>

<span style="
font-size:15px;
font-weight:600;
color:#E2E8F0;
">
System Online
</span>

</div>

<style>

@keyframes pulse{

0%{
transform:scale(1);
opacity:1;
}

50%{
transform:scale(1.5);
opacity:.4;
}

100%{
transform:scale(1);
opacity:1;
}

}

</style>
""",
        unsafe_allow_html=True,
    )


# ----------------------------------------------------
# Shimmer Loader
# ----------------------------------------------------

def shimmer():

    st.markdown(
        """
<style>

.shimmer{

height:110px;

border-radius:18px;

background:
linear-gradient(
90deg,
rgba(255,255,255,.04),
rgba(255,255,255,.10),
rgba(255,255,255,.04)
);

background-size:400% 100%;

animation:loading 1.4s infinite;

margin-top:15px;

}

@keyframes loading{

0%{
background-position:100% 0;
}

100%{
background-position:-100% 0;
}

}

</style>

<div class="shimmer"></div>
""",
        unsafe_allow_html=True,
    )


# ----------------------------------------------------
# Progress Animation
# ----------------------------------------------------

def progress_bar():

    bar = st.progress(0)

    for i in range(101):

        time.sleep(0.01)

        bar.progress(i)

    bar.empty()


# ----------------------------------------------------
# Success Animation
# ----------------------------------------------------

def success():

    st.balloons()

    st.success("✅ Task Completed Successfully")


# ----------------------------------------------------
# Thinking Card
# ----------------------------------------------------

def thinking():

    st.markdown(
        """
<div style="
padding:20px;
border-radius:18px;
background:rgba(124,58,237,.15);
border-left:5px solid #7C3AED;
font-size:18px;
font-weight:600;
">

🧠 Lumina AI is thinking...

</div>
""",
        unsafe_allow_html=True,
    )