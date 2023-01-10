import streamlit as st

if 'submitted' not in st.session_state:
    st.session_state.submitted = False

if 'texted' not in st.session_state:
    st.session_state.texted = False

if 'text' not in st.session_state:
    st.session_state.text = ''

if 'ing' not in st.session_state:
    st.session_state.ing = False

if 'input_type' not in st.session_state:
    st.session_state.input_type = None

if 'widgets' not in st.session_state:
    st.session_state.widgets = dict(
        welcome = None
    )