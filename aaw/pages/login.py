import streamlit as st
from .base import BasePage
from ..callbacks import go_home
from ..globals import STRINGS, APIs
import time

__loginpage__ = BasePage(name='login')


def login():
    psw_empty = st.empty()
    feedback_empty = st.empty()
    __loginpage__.append(empty=psw_empty)
    __loginpage__.append(empty=feedback_empty)

    psw = psw_empty.text_input(label='''**{}**'''.format(STRINGS["LOGIN_HEADER"]), type='password')
    if psw == APIs["login_pwd"]:
        feedback_empty.markdown('''<font color = '#0d7f34'>{}</font>'''.format(STRINGS["LOGIN_SUCCESS"]),
                                unsafe_allow_html=True)
        # time.sleep(3)
        go_home(rerun=True)

    elif psw is not None and psw != '':
        feedback_empty.markdown('''<font color = 'red'>{}</font>'''.format(STRINGS["LOGIN_FAILURE"]),
                                unsafe_allow_html=True)
