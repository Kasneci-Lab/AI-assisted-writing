import streamlit as st
from .utils import clear_list


def preprocess(widgets, text):
    st.session_state.texted = True
    clear_list(widgets)
    st.session_state.text = text
    if text !='':
        st.info(text)

def pipeline():
    text = st.session_state.text
    if text !='':
        st.info(text)
