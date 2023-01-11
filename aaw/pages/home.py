import streamlit as st
from .base import BasePage
from ..callbacks import go_inputtype

__homepage__ = BasePage(name='home')

def homepage():
    __homepage__.append(empty=st.markdown('''# 👋 Hi, I'm your AI essay tutor :)'''))

    titleheader_empty = st.empty()
    title_empty = st.empty()
    btn_empty = st.empty()

    titleheader_empty.markdown('''#### Please enter the title of your essay''')
    title_empty.text_input('', placeholder='My Cool Title',key='title_tmp')
    btn_empty.button('Next',on_click=go_inputtype)

    __homepage__.extend(li=[
        titleheader_empty,
        title_empty,
        btn_empty
    ])
