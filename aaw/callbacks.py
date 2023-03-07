import streamlit as st
from .mysession import session
from .globals import STRINGS


def go_home(keep_state=False,require_fb = False):
    if require_fb:
        if session.get('preferred_fb') is None:
            st.error('Please select your preferred feedback.')
            return

    session.clear()
    session.update('current_page', 'home')

    if not keep_state:
        session.update('feedback', None)
        session.update('title', None)
        session.update("user_args", dict())
        session.update("input_type", None)
        session.update('preferred_fb',None)



def go_input_type():
    # Check if there is a new title entered
    title_tmp = session.get('title_tmp')

    # If so, update title
    if title_tmp:
        session.update('title', title_tmp)

    # Verify there is a title set
    title = session.get('title')
    if title is None or title == '':
        st.error(STRINGS["ERROR_TITLE_MISSING"])
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


def choose_input_type():
    tmp_input_type = session.get("tmp_input_type")
    if tmp_input_type:
        session.update('input_type', tmp_input_type)

    input_type = session.get("input_type")

    # Save all new values
    session.clear()
    session.update('input_type', input_type)
    if input_type == STRINGS["INPUT_TYPE_PICTURE"]:
        session.update('current_page', 'upload_image')
    elif input_type == STRINGS["INPUT_TYPE_TEXT"]:
        session.update('current_page', 'input_text')
    else:
        print(input_type)
        raise NotImplementedError()


def submit_essay(essay=None):
    if essay:
        session.update('text', essay)
        session.update('preferred_fb', None)
        session.update("new_feedback", True)

    else:
        session.update("new_feedback", False)


    session.clear()
    session.update('current_page', 'feedback')


def go_modify_text():
    if session.get('preferred_fb') is None:
        st.error('Please select your preferred feedback.')
        return
    else:
        session.clear()
        session.update('current_page', 'modify_text')
