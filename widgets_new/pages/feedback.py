from .base import BasePage
import streamlit as st

__feedbackpage__ = BasePage(name='feedback')

def feedback():
    title_empty = st.empty()
    tmp_empty = st.empty()
    widgets = [
        title_empty,
        tmp_empty
    ]
    __feedbackpage__.extend(li=widgets)

    title_empty.markdown("# Your Feedbacks")
    tmp_empty.info(st.session_state.text)
