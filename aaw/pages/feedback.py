from .base import BasePage
import streamlit as st
from ..mysession import session
from ..callbacks import go_home, go_inputtext, submit
from ..utils import store_data, run_gpt3
from ..globals import STRINGS

__feedbackpage__ = BasePage(name='feedback')


def __get_feedback__(essay: str):
    prompt = '''Beim folgenden Text handelt es sich um einen Bericht von einer Schülerin zum Thema Corona. 
    Gebe Tipps zur Ausdrucksweise wie ein Lehrer und gebe konkrete Verbessungsvorschläge. Text: """'''  # todo

    total_input = prompt + essay + '''"""'''

    print("Total input")
    print(total_input)

    # return the completion
    return run_gpt3(total_input, error_tmp=st.empty())


def feedback():
    __feedbackpage__.sidebar()

    title_empty = st.empty()
    input_empty = st.empty()
    fb_empty = st.empty()
    btn2_empty = st.empty()
    btn_empty = st.empty()
    # btn_back = st.empty()

    widgets = [
        title_empty,
        input_empty,
        fb_empty,
        btn_empty,
        # btn_back
    ]
    __feedbackpage__.extend(li=widgets)

    title_empty.markdown("# {}".format(STRINGS["FEEDBACK_HEADER"]))

    essay = session.get('text')
    input_empty.info(essay)

    # btn_back.button(label=STRINGS["BUTTON_BACK"], on_click=submit)

    with st.spinner():
        feedback_text = __get_feedback__(session.get('text'))
        session.update('feedback', feedback_text)
        store_data()
    fb_empty.success(f'''{feedback_text}''')
    btn_empty.button(STRINGS["FEEDBACK_RESET"], on_click=go_home)
    btn2_empty.button(STRINGS["FEEDBACK_MODIFY"], on_click=go_inputtext, kwargs=dict(prompt=True))
