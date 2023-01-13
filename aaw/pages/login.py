import streamlit as st
from .base import BasePage
from ..callbacks import go_home
import time

__loginpage__ = BasePage(name='login')



def login():
    psw_empty = st.empty()
    feedback_empty = st.empty()
    __loginpage__.append(empty=psw_empty)
    __loginpage__.append(empty=feedback_empty)

    psw = psw_empty.text_input(label='''**Please enter the passcode**''',type='password')
    if psw == 'abc':
        feedback_empty.markdown('''<font color = '#0d7f34'>The passcode is correct. You will be redirected to the app soon...</font>''',unsafe_allow_html=True)
        time.sleep(3)
        go_home(rerun=True)

    elif psw is not None and psw!='':
        feedback_empty.markdown('''<font color = 'red'>The passcode is wrong.</font>''',unsafe_allow_html=True)
