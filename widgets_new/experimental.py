import streamlit as st





def pipeline():
    text = st.session_state.text
    if text !='':
        st.info(text)
