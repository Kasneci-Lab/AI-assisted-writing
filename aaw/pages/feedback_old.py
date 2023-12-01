import threading

from .base import BasePage
import streamlit as st
from ..mysession import session
from ..callbacks import go_home, choose_input_type, go_modify_text
from ..utils import run_gpt
from ..io_utils import store_data
from ..globals import STRINGS,NUM_PROMPTS
from ..prompt_generation import get_prompts
from ..io_utils import elo_update

__feedbackpage__ = BasePage(name='feedback')


def __get_feedback__(essay: str) -> dict:
    prompts = get_prompts(essay, num_prompts=NUM_PROMPTS)
    fbs = dict(prompt_ids=[], feedback=[])

    def run_in_thread(current_id, current_engine, current_text):
        text, _ = run_gpt(current_text, engine=current_engine, error_tmp=st.empty())
        fbs["prompt_ids"].append(current_id)
        fbs["feedback"].append(text)

    threads = []
    for p_id, (p_eng, p_text) in prompts.items():
        thread = threading.Thread(target=run_in_thread, args=(p_id, p_eng, p_text))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish!
    for t in threads:
        t.join()
    return fbs


def update_elo_in_background(idx, first_is_better: bool):
    def run_in_thread():
        elo_update(idx[0], idx[1], first_is_better)

    thread = threading.Thread(target=run_in_thread)
    thread.start()


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
        fb1_button = st.empty()

    with fb2:
        fb2_title = st.empty()
        fb2_empty = st.empty()
        fb2_button = st.empty()

    thank_you_empty = st.empty()

    divider = st.empty()

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

    def show_feedback(disabled=False):
        fb1_title.markdown("### Feedback 1")
        fb2_title.markdown("### Feedback 2")
        fb1_empty.success(f'''{fbs["feedback"][0]}''')
        fb2_empty.success(f'{fbs["feedback"][1]}')

        button_str = "Ich mag das hier! 👍"

        fb1_button.button(label=button_str, key="F1", disabled=disabled, on_click=update_elo_in_background,
                          kwargs=dict(idx=fbs["prompt_ids"], first_is_better=True))
        fb2_button.button(label=button_str, key="F2", disabled=disabled, on_click=update_elo_in_background,
                          kwargs=dict(idx=fbs["prompt_ids"], first_is_better=False))

    if session.get('new_feedback'):
        # Only regenerate the feedback, if a new text is entered
        with st.spinner():
            fbs = __get_feedback__(session.get('text'))
            session.update('feedback', fbs)
            session.update("new_feedback", False)

            show_feedback(disabled=False)
            store_data()
    else:
        show_feedback(disabled=True)
        thank_you_empty.success("Danke, dass du dabei hilfst, PEER zu verbessern!")

    divider.markdown("<b>Welches Feedback findest du besser?</b>"
                     " Mit nur einem Klick kannst du uns helfen, PEER zu optimieren :)"
                     "\n\n---------------------------------------------------------------------\n\n",
                     unsafe_allow_html=True)

    btn_new_essay.button(STRINGS["FEEDBACK_RESET"], on_click=go_home)
    btn_back.button(STRINGS["BUTTON_BACK"], on_click=choose_input_type)
    btn_modify_essay.button(STRINGS["FEEDBACK_MODIFY"], on_click=go_modify_text)
