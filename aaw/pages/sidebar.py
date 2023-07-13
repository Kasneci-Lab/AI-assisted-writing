import streamlit as st
from ..globals import STRINGS
from ..mysession import session

logo_url = "https://raw.githubusercontent.com/Kasneci-Lab/AI-assisted-writing/ui/img/Peer_logo.png"
dalle_url = "https://raw.githubusercontent.com/Kasneci-Lab/AI-assisted-writing/ui/img/DALLE-PEER.png"


def render_sidebar():
    sidebar_markdown = '''

    <center>
    <a href=/>
        <img src={logo_url} alt="PEER Logo" width="250" />
    </a>
    
    &nbsp;
    
    <code> v0.2.1 </code>
    </center>

    <center>
    <a href="https://github.com/Kasneci-Lab/AI-assisted-writing">
    <img src = "https://cdn-icons-png.flaticon.com/512/733/733609.png" width="23"></img></a>
    
    <a href="mailto:kathrin.sessler@tum.de">
    <img src="https://cdn-icons-png.flaticon.com/512/646/646094.png" alt="email" width = "27" ></a>
    </center>
    
    ---
    
    
    &nbsp;
    
    <center>
    <img src={dalle_url} alt="DALLE-PEER" width="250">
    </center>
    
    &nbsp;
    
    &nbsp;
    
    ---

    '''.format(header=STRINGS["SIDEBAR_HEADER"], logo_url=logo_url, dalle_url=dalle_url)

    st.sidebar.markdown(sidebar_markdown, unsafe_allow_html=True)

    st.sidebar.button("Datenschutzerklärung", on_click=to_legal_page, args=("privacy",), type="primary")
    st.sidebar.button("Impressum", on_click=to_legal_page, args=("imprint",), type="primary")

    st.markdown(
        """
        <style>
        button[kind="primary"] {
            background: none!important;
            padding: 0 !important;
            color: #444444 !important;
            text-decoration: none;
            cursor: pointer;
            border: none !important;
            text-align: center;
            width: inherit;
        }
        button[kind="primary"]:hover {
            text-decoration: none;
            color: black !important;
        }
        button[kind="primary"]:focus {
            outline: none !important;
            box-shadow: none !important;
            color: black !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def to_legal_page(name):
    session.clear()
    session.update('current_page', name)

    # Reset all things
    session.update('feedback', None)
    session.update('title', None)
    session.update("user_args", dict())
    session.update("input_type", None)
