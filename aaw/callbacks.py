import streamlit as st
from .mysession import session
from .utils import valid_user_arguments, error_and_stop
from .globals import STRINGS


def go_inputtext(prompt=False):
    # if prompt:
    #    session.update("prompt", True)

    session.clear()
    session.update('current_page', 'input_text')


def resubmit_essay():
    session.update('current_page', 'feedback')


def go_inputtype():
    # Check if there is a new title entered
    title_tmp = session.get('title_tmp')

    # If so, update title
    if title_tmp:
        session.update('title', title_tmp)

    # Verify there is a title set
    title = session.get('title')
    if title is None or title == '':
        error_and_stop("Please enter the title")
        return

    # Set all further variables
    user_args = dict(
        article=session.get('article'),
        school=session.get('school'),
        year=session.get('year'),
        state=session.get('state')
    )

    # Save all new values
    session.clear()
    session.update('title', title)
    session.update("user_args", user_args)
    session.update('current_page', 'input_type')


def submit():
    tmp_input_type = session.get("tmp_input_type")
    if tmp_input_type:
        session.update('input_type', tmp_input_type)

    input_type = session.get("input_type")

    session.clear()
    session.update('input_type', input_type)
    if input_type == STRINGS["INPUT_TYPE_PICTURE"]:
        session.update('current_page', 'upload_image')
    elif input_type == STRINGS["INPUT_TYPE_TEXT"]:
        session.update('current_page', 'input_text')
    else:
        print(input_type)
        raise NotImplementedError()  # todo


def submit_essay(essay, teacher=None):
    session.update('text', essay)
    session.clear()
    session.update('current_page', 'feedback')
    if teacher is not None:
        session.update('teacher', teacher)


def go_home(rerun=False):
    # session.clear()
    session.update('current_page', 'home')
    reset_state_vars()

    if rerun:
        st.experimental_rerun()


def reset_state_vars():
    session.update('prompt', False)
    session.update('feedback', None)
