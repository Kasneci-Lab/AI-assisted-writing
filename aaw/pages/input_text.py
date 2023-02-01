from .base import BasePage
import streamlit as st
from ..callbacks import submit_essay, go_inputtype
from ..mysession import session
from ..globals import STRINGS

__inputtextpage__ = BasePage(name='input_text')


def input_text():
    __inputtextpage__.sidebar()
    title_empty = st.empty()
    textarea_empty = st.empty()
    btn_empty = st.empty()
    btn_back = st.empty()

    __inputtextpage__.extend(li=[
        title_empty,
        textarea_empty,
        btn_empty,
        btn_back
    ])

    prompt = session.get('prompt')

    btn_back.button(label=STRINGS["BUTTON_BACK"], on_click=go_inputtype)

    if not prompt:
        title_empty.markdown("# {}".format(STRINGS["INPUT_TEXT_HEADER"]))
        essay = textarea_empty.text_area(
            label='',
            label_visibility='collapsed',
            placeholder=STRINGS["INPUT_TEXT_PLACEHOLDER"],
            height=500,
        )
        btn_empty.button(STRINGS["INPUT_TEXT_BUTTON"], on_click=submit_essay, kwargs=dict(
            essay=essay
        ))
    else:
        title_empty.markdown("# {}".format(STRINGS["INPUT_TEXT_MODIFY"]))
        col1, col2 = textarea_empty.columns([1, 1])
        col1.markdown('''**{}:**'''.format(STRINGS["INPUT_TEXT_ORIGINAL"]))
        col1.info(session.get('text'))
        essay = col2.text_area(
            label='',
            placeholder=STRINGS["INPUT_TEXT_PLACEHOLDER_MODIFY"],
            height=500,
        )
        expander = col1.expander('feedbacks')
        expander.success(session.get('feedback'))
        col2.button(STRINGS["INPUT_TEXT_BUTTON"], on_click=submit_essay, kwargs=dict(
            essay=essay
        ))




