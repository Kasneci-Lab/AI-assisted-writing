from .base import BasePage
import streamlit as st
from ..callbacks import submit_essay
from ..globals import STRINGS
from ..mysession import session

__modifytextpage__ = BasePage(name='modify_text')


def modify_text():
    #########################
    # Set up page structure #
    #########################

    __modifytextpage__.sidebar()
    title_empty = st.empty()
    feedback_empty = st.empty()
    textarea_empty = st.empty()

    col1, col2 = st.columns(2)

    with col1:
        btn_back = st.empty()
    with col2:
        btn = st.empty()

    #############################
    # Fill all empty containers #
    #############################

    title_empty.markdown("# {}".format(STRINGS["INPUT_TEXT_MODIFY"]))

    feedback = session.get("feedback")

    feedback_empty.info(feedback)

    old_essay = session.get('text')

    print(old_essay)

    essay = textarea_empty.text_area(
        value=old_essay,
        label='text_area',
        label_visibility='collapsed',
        height=500,
    )

    btn.button(STRINGS["MODIFY_TEXT_BUTTON"], on_click=submit_essay, kwargs=dict(essay=essay))
    btn_back.button(label=STRINGS["BUTTON_BACK"], on_click=submit_essay)
