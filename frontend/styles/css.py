import streamlit as st


def load_css():

    st.markdown(
        """
<style>

/* ===========================
   GOOGLE FONT
=========================== */

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family:'Poppins',sans-serif;
}


/* ===========================
   MAIN APP
=========================== */

.stApp{

background:linear-gradient(
135deg,
#020617 0%,
#0F172A 40%,
#111827 75%,
#1E293B 100%
);

color:#F8FAFC;

}


/* ===========================
   HIDE STREAMLIT
=========================== */

#MainMenu,
header,
footer{

visibility:hidden;

}


/* ===========================
   SIDEBAR
=========================== */

section[data-testid="stSidebar"]{

background:#0F172A;

border-right:1px solid rgba(255,255,255,.06);

padding-top:10px;

}

section[data-testid="stSidebar"] *{

color:white !important;

}


/* ===========================
   HEADINGS
=========================== */

h1,h2,h3,h4,h5,h6{

color:white;

}

p,span,label{

color:#E2E8F0;

}


/* ===========================
   TITLE
=========================== */

.main-title{

font-size:46px;

font-weight:700;

background:linear-gradient(
90deg,
#8B5CF6,
#06B6D4
);

-webkit-background-clip:text;

-webkit-text-fill-color:transparent;

margin-bottom:5px;

}

.subtitle{

font-size:18px;

font-weight:500;

color:#CBD5E1;

}


/* ===========================
   BUTTONS
=========================== */

.stButton>button{

width:100%;

height:46px;

border:none;

border-radius:14px;

font-weight:600;

background:linear-gradient(
90deg,
#7C3AED,
#06B6D4
);

color:white;

transition:.3s;

}

.stButton>button:hover{

transform:translateY(-2px);

box-shadow:0 10px 25px rgba(124,58,237,.35);

}


/* ==========================
   CUSTOM CHAT INPUT
========================== */

.stTextInput input{

background:#111827 !important;

color:white !important;

border:1px solid rgba(255,255,255,.08) !important;

border-radius:16px !important;

padding:14px !important;

font-size:16px !important;

}

.stTextInput input::placeholder{

color:#94A3B8 !important;

}

.stTextInput input:focus{

border:1px solid #7C3AED !important;

box-shadow:none !important;

}

/* ===========================
   CODE BLOCK
=========================== */

pre{

background:#1E293B !important;

border-radius:12px;

border:1px solid rgba(255,255,255,.08);

}

code{

color:#38BDF8 !important;

}


/* ===========================
   METRICS
=========================== */

[data-testid="stMetric"]{

background:#1E293B;

padding:15px;

border-radius:16px;

border:1px solid rgba(255,255,255,.05);

}

[data-testid="stMetricLabel"]{

color:#CBD5E1 !important;

}

[data-testid="stMetricValue"]{

color:white !important;

}


/* ===========================
   DIVIDER
=========================== */

hr{

border-color:rgba(255,255,255,.08);

}


/* ===========================
   SCROLLBAR
=========================== */

::-webkit-scrollbar{

width:8px;

}

::-webkit-scrollbar-track{

background:#0F172A;

}

::-webkit-scrollbar-thumb{

background:#6366F1;

border-radius:30px;

}

</style>
""",
        unsafe_allow_html=True,
    )