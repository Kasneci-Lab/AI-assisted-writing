import streamlit as st
from .mysession import session
from .utils import valid_user_arguments, error_and_stop


def go_inputtext(prompt=False):
    if prompt:
        session.update("prompt",True)

    session.clear()
    session.update('current_page', 'input_text')

def resubmit_essay():
    session.update('current_page','feedback')

def go_inputtype():
    if not valid_user_arguments(session.get('user_args')):
        error_and_stop("Please enter complete arguments")
        return

    session.update('title',session.get('title_tmp'))
    title = session.get('title')
    if title is None or title == '':
        error_and_stop("Please enter the title")
        return

    session.clear()
    session.update('title',title)
    session.update('current_page','input_type')


def submit():
    session.clear()
    input_type = session.get('input_type')
    if input_type == 'Upload a picture':
        session.update('current_page', 'upload_image')
    elif input_type == "Input text":
        session.update('current_page', 'input_text')
    else:
        print(input_type)
        raise NotImplementedError() # todo


def submit_essay(essay, teacher = None):
    session.update('text',essay)
    session.clear()
    session.update('current_page','feedback')
    if teacher is not None:
        session.update('teacher',teacher)

def go_home(rerun=False):
    session.clear()
    session.update('current_page','home')
    reset_state_vars()

    if rerun:
        st.experimental_rerun()

def reset_state_vars():
    session.update('prompt',False)
    session.update('feedback', None)