from .base import BasePage
from ..globals import INPUT_TYPES, STRINGS
from ..callbacks import submit
import streamlit as st


__inputtypepage__ = BasePage(name='input_type')


def input_type():
    __inputtypepage__.sidebar()

    __inputtypepage__.extend(li=[
        st.markdown('''# {}'''.format(STRINGS["INPUT_TYPE_HEADER"])),
    ])

    input_radio = st.empty()
    btn = st.empty()
    __inputtypepage__.extend(li=[
        input_radio,
        btn])

    input_radio.radio("", INPUT_TYPES, key='input_type')
    btn.button(label=STRINGS["INPUT_TYPE_BUTTON"], on_click=submit)



