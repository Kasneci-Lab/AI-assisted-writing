from .base import BasePage
from ..globals import INPUT_TYPES, STRINGS
from ..callbacks import submit, go_home
import streamlit as st


__inputtypepage__ = BasePage(name='input_type')


def input_type():
    __inputtypepage__.sidebar()

    __inputtypepage__.extend(li=[
        st.markdown('''# {}'''.format(STRINGS["INPUT_TYPE_HEADER"])),
    ])

    input_radio = st.empty()
    btn = st.empty()
    btn_back = st.empty()
    __inputtypepage__.extend(li=[
        input_radio,
        btn,
        btn_back])

    input_radio.radio("", INPUT_TYPES, key='input_type')
    btn.button(label=STRINGS["INPUT_TYPE_BUTTON"], on_click=submit)
    btn_back.button(label=STRINGS["BUTTON_BACK"], on_click=go_home)



