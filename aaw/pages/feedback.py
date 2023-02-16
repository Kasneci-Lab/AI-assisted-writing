from .base import BasePage
import streamlit as st
from ..mysession import session
from ..callbacks import go_home, choose_input_type, go_modify_text
from ..utils import store_data, run_gpt3
from ..globals import STRINGS
from ..prompt_generation import get_prompt

__feedbackpage__ = BasePage(name='feedback')


def __get_feedback__(essay: str):
    prompt = get_prompt(essay)
    text, _ = run_gpt3(prompt, error_tmp=st.empty())
    return text
    # return "Toll gemacht!"


def feedback():
    #########################
    # Set up page structure #
    #########################

    __feedbackpage__.sidebar()

    title_empty = st.empty()
    input_empty = st.empty()
    fb_empty = st.empty()

    col1, col2, col3 = st.columns(3)

    with col1:
        btn_new_essay = st.empty()
    with col2:
        btn_back = st.empty()
    with col3:
        btn_modify_essay = st.empty()

    #############################
    # Fill all empty containers #
    #############################

    title_empty.markdown("# {}".format(STRINGS["FEEDBACK_HEADER"]))

    essay = session.get('text')
    input_empty.info(essay)

    feedback_text = session.get("feedback")

    if session.get("new_feedback"):
        # Only regenerate the feedback, if a new text is entered
        with st.spinner():
            feedback_text = __get_feedback__(session.get('text'))
            session.update('feedback', feedback_text)
            fb_empty.success(f'''{feedback_text}''')
            store_data()

    fb_empty.success(f'''{feedback_text}''')

    btn_new_essay.button(STRINGS["FEEDBACK_RESET"], on_click=go_home)
    btn_back.button(STRINGS["BUTTON_BACK"], on_click=choose_input_type)
    btn_modify_essay.button(STRINGS["FEEDBACK_MODIFY"], on_click=go_modify_text)
