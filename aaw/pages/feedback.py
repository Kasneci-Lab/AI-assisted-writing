from .base import BasePage
import streamlit as st
import openai
import time
from ..mysession import session
from ..callbacks import go_home, go_inputtext
from ..utils import store_data
from ..globals import APIs

__feedbackpage__ = BasePage(name='feedback')


def __get_feedback__(essay: str):
    openai.api_key = APIs["openai"]
    prompt = '''Beim folgenden Text handelt es sich um einen Bericht von einer Schülerin zum Thema Corona. 
    Gebe Tipps zur Ausdrucksweise wie ein Lehrer und gebe konkrete Verbessungsvorschläge. Text: """'''  # todo

    total_input = prompt + essay + '''"""'''
    error_tmp = st.empty()

    # create a completion
    while True:
        try:
            completion = openai.Completion.create(engine="text-davinci-003", prompt=total_input, max_tokens=512)
            break
        except Exception as e:
            error_tmp.error(str(e))
            time.sleep(5)
            error_tmp.empty()

    # return the completion
    return completion.choices[0].text


def feedback():
    __feedbackpage__.sidebar()

    title_empty = st.empty()
    input_empty = st.empty()
    fb_empty = st.empty()
    btn2_empty = st.empty()
    btn_empty = st.empty()

    widgets = [
        title_empty,
        input_empty,
        fb_empty,
        btn_empty,
    ]
    __feedbackpage__.extend(li=widgets)

    title_empty.markdown("# Your Feedbacks")

    essay = session.get('text')
    input_empty.info(essay)
    with st.spinner():
        feedback_text = __get_feedback__(session.get('text'))
        session.update('feedback', feedback_text)
        store_data()
    fb_empty.success(f'''{feedback_text}''')
    btn_empty.button("Reset", on_click=go_home)
    btn2_empty.button('Modify essay', on_click=go_inputtext, kwargs=dict(prompt=True))
