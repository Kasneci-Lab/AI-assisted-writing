from .base import BasePage
import streamlit as st
from ..callbacks import submit_essay, go_input_type
from ..globals import STRINGS

__inputtextpage__ = BasePage(name='input_text')


def input_text():
    #########################
    # Set up page structure #
    #########################

    __inputtextpage__.sidebar()
    title_empty = st.empty()
    textarea_empty = st.empty()

    col1, col2 = st.columns(2)

    with col1:
        btn_back = st.empty()
    with col2:
        btn = st.empty()

    #############################
    # Fill all empty containers #
    #############################

    title_empty.markdown("# {}".format(STRINGS["INPUT_TEXT_HEADER"]))

    essay = textarea_empty.text_area(
        label='text_area',
        label_visibility='collapsed',
        placeholder=STRINGS["INPUT_TEXT_PLACEHOLDER"],
        height=500,
    )

    btn.button(STRINGS["INPUT_TEXT_BUTTON"], on_click=submit_essay, kwargs=dict(essay=essay))
    btn_back.button(label=STRINGS["BUTTON_BACK"], on_click=go_input_type)
