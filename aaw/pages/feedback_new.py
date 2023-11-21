import threading
import ast

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


def __get_feedback__(essay: str, task: str) -> dict:
    prompts = get_prompts(essay, num_prompts=NUM_PROMPTS)
    # fbs = dict(prompt_ids=[], feedback=[])

    fbs = dict()

    # def run_in_thread(current_id, current_engine, current_text):
    #     text, _ = run_gpt(current_text, engine=current_engine, error_tmp=st.empty())
    #     fbs["prompt_ids"].append(current_id)
    #     fbs["feedback"].append(text)
    #
    # threads = []
    # for p_id, (p_eng, p_text) in prompts.items():
    #     thread = threading.Thread(target=run_in_thread, args=(p_id, p_eng, p_text))
    #     thread.start()
    #     threads.append(thread)
    #     break
    #
    # # Wait for all threads to finish!
    # for t in threads:
    #     t.join()

    # prompt = prompts[1]

    prompt = "Beurteile folgenden {text}. Es handelt sich um einen Aufsatz eines Schülers einer fünften Klasse " \
             "eines bayerischen Gymnasiums. Bestätige zunächst, dass du den Auftrag verstanden hast, den {text} " \
             "schicke ich dir im Anschluss."

    messages = [
        {"role": "system", "content": "I am a 10 year old student. "
                                      "In school, we are learning story telling at the moment."
                                      "Be very precise, stay concrete and motivating. Give me tips to improve myself."
         },
        # {"role": "system", "content": "Be very precise, stay nice and motivating. Give me tips to improve myself. "
        #                               "You only speak JSON. Do not return anything else"},
        {"role": "user", "content": "Wir haben folgende Aufgabe in der Schule: " + task},
        # {"role": "system", "content": Background infos about the essay type}
        {"role": "user", "content": "Das ist mein Text: " + essay},
        {"role": "user", "content": "Gib mir möglichst ausführliches Feedback."},
    ]

    text, _ = run_gpt(messages, engine="gpt-3.5-turbo", error_tmp=st.empty())
    print(text)

    messages.append({"role": "assistant", "content": text})

    new_cmd = "Strukturiere nun das Feedback in Inhaltliche Punkte (\"content\") und sprachliche Aspekte " \
              "(\"language\") und gibt das gleiche Feedback in einem JSON Objekt zurück. Gib nur das JSON objekt " \
              "zurück. Verwende die Überschriften als Key und die Beschreibungen als Value."

    messages.append(({"role": "user", "content": new_cmd}))

    text, _ = run_gpt(messages, engine="gpt-3.5-turbo", error_tmp=st.empty())
    print(text)

    fbs = text

    # fbs["prompt_ids"].append(0)
    # fbs["feedback"].append(text)

    # fbs["prompt_ids"].append(1)
    # fbs["feedback"].append("Nope")
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

    title_empty1 = st.empty()
    title_empty2 = st.empty()
    input_empty1 = st.empty()
    title_empty3 = st.empty()
    input_empty2 = st.empty()

    fb1, fb2 = st.columns(2)

    with fb1:
        fb1_title = st.empty()
        fb1_empty = st.empty()
        # fb1_button = st.empty()

    with fb2:
        fb2_title = st.empty()
        fb2_empty = st.empty()
        # fb2_button = st.empty()

    # thank_you_empty = st.empty()

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

    title_empty1.markdown("# {}".format(STRINGS["FEEDBACK_HEADER"]))
    title_empty2.markdown("## {}".format("Aufgabe"))
    title_empty3.markdown("## {}".format("Dein Aufsatz"))

    essay = session.get('text')
    task = session.get("task")
    input_empty1.info(task)
    input_empty2.info(essay)

    fbs = session.get("feedback")

    def show_feedback(disabled=False):
        fb1_title.markdown("### Sprache")
        fb2_title.markdown("### Inhalt")

        # fff = ast.literal_eval(fbs["feedback"][0])
        fff = ast.literal_eval(fbs)

        print(fff)

        fff_l = fff["language"]
        fff_c = fff["content"]

        fb1_empty.success(fff_l)
        fb2_empty.success(fff_c)

        # button_str = "Ich mag das hier! 👍"

        # fb1_button.button(label=button_str, key="F1", disabled=disabled, on_click=update_elo_in_background,
        #                   kwargs=dict(idx=fbs["prompt_ids"], first_is_better=True))
        # fb2_button.button(label=button_str, key="F2", disabled=disabled, on_click=update_elo_in_background,
        #                   kwargs=dict(idx=fbs["prompt_ids"], first_is_better=False))

    if session.get('new_feedback'):
        # Only regenerate the feedback, if a new text is entered
        with st.spinner():
            fbs = __get_feedback__(session.get('text'), session.get("task"))
            session.update('feedback', fbs)
            session.update("new_feedback", False)

            show_feedback(disabled=False)
            # store_data()
    else:
        show_feedback(disabled=True)
        # thank_you_empty.success("Danke, dass du dabei hilfst, PEER zu verbessern!")

    divider.markdown("\n\n---------------------------------------------------------------------\n\n",
                     unsafe_allow_html=True)

    #  "<b>Welches Feedback findest du besser?</b> Mit nur einem Klick kannst du uns helfen, PEER zu optimieren :)"

    btn_new_essay.button(STRINGS["FEEDBACK_RESET"], on_click=go_home)
    btn_back.button(STRINGS["BUTTON_BACK"], on_click=choose_input_type)
    btn_modify_essay.button(STRINGS["FEEDBACK_MODIFY"], on_click=go_modify_text)
