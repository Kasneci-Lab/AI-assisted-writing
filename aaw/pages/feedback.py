import threading

from .base import BasePage
import streamlit as st
from ..mysession import session
from ..callbacks import go_home, go_modify_text, go_input_type
from ..utils import run_gpt
from ..io_utils import store_data
from ..globals import STRINGS, NUM_PROMPTS, PROMPTS
# from ..prompt_generation import get_prompts

__feedbackpage__ = BasePage(name='feedback')


def get_extra_info(article):
    match article:
        case 'Bericht':
            return "- Der Text enthält eine passende und ansprechende Überschrift.\n" \
                   "- Der Text ist in Einleitung, Hauptteil und Schluss gegliedert.\n" \
                   "- Die Einleitung führt knapp zum Thema hin.\n" \
                   "- Die Einleitung weckt Interesse.\n" \
                   "- Der Hauptteil enthält alle wichtigen Informationen\n" \
                   "- Die Informationen werden richtig dargestellt\n" \
                   "- Die Anordnung der Informationen ist zielführend\n" \
                   "- Der Schluss rundet den Text ab\n" \
                   "- Die gegebenen Materialien werden genutzt\n" \
                   "- Nutzt der Text Wörter gemäß ihrer Bedeutungslogik bzw. ihres üblichen Gebrauchs?\n" \
                   "- Ist der Text sachlich formuliert?\n" \
                   "- Wurden alle notwendigen Kommas gesetzt? Sind die Wörter korrekt verschriftlicht?\n" \
                   "- Nutzt der Text unterschiedliche Satzzeichen, Wörter sowie einen vielfältigen Satzbau?\n" \
                   "- Werden die Informationen aus den Materialien in eigenen Worten wiedergegeben?\n" \
                   "- Sind die einzelnen Informationen zielführend miteinander verknüpft.\n"
        case "Geschichte":
            return "- Klarere Ausdrucksweise und Strukturierung der Sätze.\n " \
                   "- Verbesserung der Beschreibungen, um die Szene lebendiger zu gestalten.\n " \
                   "- Bessere Nutzung von Adjektiven und Adverbien zur Verstärkung der Beschreibungen.\n " \
                   "- Präzisere Verwendung von Verben, um die Handlung genauer zu beschreiben.\n " \
                   "- Einheitliche und präzisere Ausdrucksweise.\n " \
                   "- Vermeidung von Wiederholungen und redundanten Phrasen.\n " \
                   "- Verbesserte Verknüpfung von Sätzen und Absätzen, um den Text flüssiger zu gestalten"
        case _:
            return ""


def get_prompts(essay: str, task: str, num_prompts=2) -> dict:
    title = session.get("title")
    user_args = session.get("user_args")
    article = user_args["article"]

    prompts = {1: ("gpt-3.5-turbo", PROMPTS[0]),
               2: ("gpt-3.5-turbo", PROMPTS[1]),
               3: ("gpt-3.5-turbo", PROMPTS[2])}
    prompts = {k: (eng, promp.format(title=title, article=article,
                                     year=user_args["year"], essay=essay, task=task,
                                     extra_info=get_extra_info(article)))
               for k, (eng, promp) in prompts.items()}
    return prompts


def __get_feedback__(essay: str, task: str) -> dict:
    prompts = get_prompts(essay, task, num_prompts=NUM_PROMPTS)
    fbs = dict()  # prompt_ids=[], feedback=[]

    def run_in_thread(current_id, current_engine, current_text):
        messages = [{"role": "user", "content": current_text}]
        text, _ = run_gpt(messages, engine=current_engine, error_tmp=st.empty())
        # text = "A"
        fbs[current_id] = text

    threads = []
    for p_id, (p_eng, p_text) in prompts.items():
        thread = threading.Thread(target=run_in_thread, args=(p_id, p_eng, p_text))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish!
    for t in threads:
        t.join()

    print("\n\n---------------------------------------------------------\n\n")
    return fbs


def feedback():
    #########################
    # Set up page structure #
    #########################
    __feedbackpage__.sidebar()

    header = st.empty()
    header.markdown("# Feedback Vorschlag")

    essay_header = st.empty()
    essay_header.markdown("## Aufsatz")

    essay_content = st.empty()

    fb1_title = st.empty()
    fb1_title.markdown("### Allgemeines Feedback")
    fb1_empty = st.empty()

    fb2_title = st.empty()
    fb2_title.markdown("### Kriterien")
    fb2_empty = st.empty()

    fb3_title = st.empty()
    fb3_title.markdown("### Verbesserungsvorschläge")
    fb3_empty = st.empty()

    divider = st.empty()
    divider.markdown("\n\n---------------------------------------------------------------------\n\n",
                     unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        btn_new_essay = st.empty()
        btn_new_essay.button(STRINGS["FEEDBACK_RESET"], on_click=go_home)
    with col2:
        btn_back = st.empty()
        btn_back.button(STRINGS["BUTTON_BACK"], on_click=go_input_type)
    with col3:
        btn_modify_essay = st.empty()
        btn_modify_essay.button(STRINGS["FEEDBACK_MODIFY"], on_click=go_modify_text)

    #############################
    # Fill all empty containers #
    #############################

    # Set Essay
    essay = session.get('text')
    essay_content.info(essay)

    fbs = session.get("feedback")

    def show_feedback():
        # print(fbs)
        fb1_empty.write(fbs[1])
        # fb1_empty.success(fbs["feedback"][0])
        fb2_empty.write(fbs[2])
        # fb2_empty.success(fbs["feedback"][1])
        fb3_empty.write(fbs[3])

    if session.get('new_feedback'):
        # Only regenerate the feedback, if a new text is entered
        with st.spinner():
            fbs = __get_feedback__(session.get('text'), session.get("task"))
            session.update('feedback', fbs)
            session.update("new_feedback", False)

            show_feedback()
            store_data()
    else:
        show_feedback()