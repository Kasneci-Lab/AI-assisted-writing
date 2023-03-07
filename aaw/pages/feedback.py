from .base import BasePage
import streamlit as st
from ..mysession import session
from ..callbacks import go_home, choose_input_type, go_modify_text
from ..utils import run_gpt3
from ..io_utils import store_data
from ..globals import STRINGS,NUM_PROPMTS
from ..prompt_generation import get_prompt
from ..io_utils import inc_elo_weight

__feedbackpage__ = BasePage(name='feedback')

def __option2idx__(option:str):
    idx = int(option[-1]) - 1
    return idx



def __get_feedback__(essay: str):
    prompts = get_prompt(essay,num_prompts=NUM_PROPMTS)
    fbs = []
    for p in prompts:
        text, _ = run_gpt3(p, error_tmp=st.empty())
        fbs.append(text)
    return fbs
    # return "Toll gemacht!"


def feedback():
    #########################
    # Set up page structure #
    #########################

    __feedbackpage__.sidebar()

    title_empty = st.empty()
    input_empty = st.empty()

    fb1, fb2 = st.columns(2)

    with fb1:
        fb1_title = st.empty()
        fb1_empty = st.empty()
    with fb2:
        fb2_title = st.empty()
        fb2_empty = st.empty()

    preferred_fb_idx = st.empty()

    col1, col2, col3 = st.columns(3)

    with col1:
        btn_new_essay = st.empty()
    with col2:
        btn_back = st.empty()
    with col3:
        btn_modify_essay = st.empty()

    #############################
    # Fill all empty containers #
    #############################

    title_empty.markdown("# {}".format(STRINGS["FEEDBACK_HEADER"]))

    essay = session.get('text')
    input_empty.info(essay)

    fbs = session.get("feedback")
    if session.get('new_feedback'):
        # Only regenerate the feedback, if a new text is entered
        print("generate new feedback")
        with st.spinner():
            fbs = __get_feedback__(session.get('text'))
            session.update('feedback', fbs)
            # store_data()
            session.update("new_feedback", False)

    fb1_title.markdown("### Feedback 1")
    fb2_title.markdown("### Feedback 2")
    fb1_empty.success(f'''{fbs[0]}''')
    fb2_empty.success(f'{fbs[1]}')
    idx = preferred_fb_idx.selectbox(label='Which feedback do you prefer? (Todo: replace this with string)',
                                     options=['Undefined', "Feedback 1", 'Feedback 2'],
                                     )  # todo: replace with string

    btn_new_essay.button(STRINGS["FEEDBACK_RESET"], on_click=go_home, kwargs=dict(
        require_fb = True
    ))
    btn_back.button(STRINGS["BUTTON_BACK"], on_click=choose_input_type)
    btn_modify_essay.button(STRINGS["FEEDBACK_MODIFY"], on_click=go_modify_text)

    if idx != "Undefined":
        idx = __option2idx__(idx)
        session.update('preferred_fb', idx)

        store_data()
        inc_elo_weight(idx)

