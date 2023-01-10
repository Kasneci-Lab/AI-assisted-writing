import streamlit as st
from .input_page import upload_image,input_text
from .utils import clear_list
from .var import INPUT_TYPES


def clicked():
    st.session_state.submitted = True

def welcome_page():
    welcome_page = [
        st.markdown('''# 👋 Hi, I'm your AI essay tutor :)'''),
        st.markdown('''### Do you want to upload a picture of your essay or input text manually?'''),
    ]


    input_radio = st.empty()
    input_radio.radio("",INPUT_TYPES, key='input_type')
    welcome_page.append(input_radio)

    btn = st.empty()
    btn.button(label='Next', on_click=clicked)
    welcome_page.append(btn)

    st.session_state.widgets['welcome'] = welcome_page





