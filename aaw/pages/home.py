import streamlit as st
from .base import BasePage
from ..callbacks import go_inputtype
from ..globals import STRINGS

__homepage__ = BasePage(name='home')


def homepage():
    __homepage__.sidebar()
    __homepage__.append(empty=st.markdown('''# {}'''.format(STRINGS["HOME_HEADER"])))

    titleheader_empty = st.empty()
    title_empty = st.empty()
    btn_empty = st.empty()

    titleheader_empty.markdown('''#### {}'''.format(STRINGS["HOME_TITLE_HEADER"]))
    title_empty.text_input('title', label_visibility='collapsed', placeholder=STRINGS["HOME_TITLE_PLACEHOLDER"],
                           key='title_tmp')
    btn_empty.button(STRINGS["HOME_TITLE_BUTTON"], on_click=go_inputtype)

    __homepage__.extend(li=[
        titleheader_empty,
        title_empty,
        btn_empty
    ])
