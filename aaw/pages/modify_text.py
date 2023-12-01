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

    f1, f2, f3 = st.columns(3)
    with f1:
        f1_empty = st.empty()
    with f2:
        f2_empty = st.empty()
    with f3:
        f3_empty = st.empty()

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

    f1_empty.write(session.get("feedback")[1])
    f2_empty.write(session.get("feedback")[2])
    f3_empty.write(session.get("feedback")[3])

    old_essay = session.get('text')

    essay = textarea_empty.text_area(
        value=old_essay,
        label='text_area',
        label_visibility='collapsed',
        height=500,
    )

    btn.button(STRINGS["MODIFY_TEXT_BUTTON"], on_click=submit_essay, kwargs=dict(essay=essay))
    btn_back.button(label=STRINGS["BUTTON_BACK"], on_click=submit_essay)
