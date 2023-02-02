import streamlit as st
from ..globals import STRINGS

# <img src="https://raw.githubusercontent.com/leoxiang66/streamlit-tutorial/IDP/widgets/static/tum.png"
# alt="TUM" width="200"/>

logo_url = "https://raw.githubusercontent.com/Kasneci-Lab/AI-assisted-writing/ui/img/Peer_logo.png?" \
           "token=GHSAT0AAAAAAB5LLOQ6SNTKYWBWMEEJVQ4SY62WHRQ"
dalle_url = "https://raw.githubusercontent.com/Kasneci-Lab/AI-assisted-writing/ui/img/DALLE-PEER.png?" \
            "token=GHSAT0AAAAAAB5LLOQ6GMWJVVBUI2DADYJ4Y62WG6A"


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
    
    &nbsp;
    
    <center>
    <img src={dalle_url} alt="DALLE-PEER" width="250">
    </center>
    
    <!--
    ---
    
    <p>P.E.E.R ist ein Projekt des Lehrstuhls für Human-Centered Technologies for Learning an der TUM.
    Ziel des Projektes ist es Schüler von der Grundschule bis zur Universität beim Erstellen von
    Aufsätzen aller Art zu unterstützen. Die Texte werden mit Unterstützung von KI untersucht und
    es wird ein möglichst konstruktives Feedback erzeugt. Alle Aufsatzdaten werden anonymisiert
    erfasst, um P.E.E.R stetig zu verbessern.</p> 
    
    -->


    '''.format(header=STRINGS["SIDEBAR_HEADER"], logo_url=logo_url, dalle_url=dalle_url)

    st.sidebar.markdown(sidebar_markdown, unsafe_allow_html=True)
