import streamlit as st
from .base import BasePage
from ..callbacks import go_home

__loginpage__ = BasePage(name='login')



def login():
    psw_empty = st.empty()
    feedback_empty = st.empty()
    __loginpage__.append(empty=psw_empty)
    __loginpage__.append(empty=feedback_empty)

    psw = psw_empty.text_input(label='''**Please enter the passcode**''',type='password')
    if psw == 'abc':
        go_home(rerun=True)

    elif psw is not None and psw!='':
        feedback_empty.markdown('''`The passcode is wrong.`''')
