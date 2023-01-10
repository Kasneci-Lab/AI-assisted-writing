from .base import BasePage
from ..globals import INPUT_TYPES
from ..callbacks import submit
import streamlit as st

__homepage__ = BasePage(name='home')

def homepage():
    global __homepage__

    __homepage__.extend(li=[
        st.markdown('''# 👋 Hi, I'm your AI essay tutor :)'''),
        st.markdown('''### Do you want to upload a picture of your essay or input text manually?'''),
    ]
    )

    input_radio = st.empty()
    btn = st.empty()
    __homepage__.extend(li=[input_radio, btn])

    input_radio.radio("", INPUT_TYPES,key='input_type')
    btn.button(label='Next', on_click=submit)