from .base import BasePage
from ..globals import INPUT_TYPES
from ..callbacks import submit
import streamlit as st


__inputtypepage__ = BasePage(name='input_type')

def input_type():
    global __inputtypepage__

    __inputtypepage__.extend(li=[
        st.markdown('''# Do you want to upload a picture of your essay or input text manually?'''),
    ]
    )

    input_radio = st.empty()
    btn = st.empty()
    __inputtypepage__.extend(li=[
        input_radio,
        btn])

    input_radio.radio("", INPUT_TYPES,key='input_type')
    btn.button(label='Next', on_click=submit)



