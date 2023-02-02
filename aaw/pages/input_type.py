from .base import BasePage
from ..globals import INPUT_TYPES, STRINGS
from ..callbacks import choose_input_type, go_home
import streamlit as st


__inputtypepage__ = BasePage(name='input_type')


def input_type():
    #########################
    # Set up page structure #
    #########################

    __inputtypepage__.sidebar()

    __inputtypepage__.extend(li=[
        st.markdown('''# {}'''.format(STRINGS["INPUT_TYPE_HEADER"])),
    ])

    input_radio = st.empty()

    col1, col2 = st.columns(2)

    with col1:
        btn_back = st.empty()
    with col2:
        btn = st.empty()

    #############################
    # Fill all empty containers #
    #############################

    input_radio.radio("input_type", INPUT_TYPES, key='tmp_input_type', label_visibility="collapsed")

    btn.button(label=STRINGS["INPUT_TYPE_BUTTON"], on_click=choose_input_type)
    btn_back.button(label=STRINGS["BUTTON_BACK"], on_click=go_home)



