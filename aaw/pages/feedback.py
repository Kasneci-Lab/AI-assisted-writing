from .base import BasePage
import streamlit as st
import openai
import time
from ..mysession import session
from ..callbacks import go_home


__feedbackpage__ = BasePage(name='feedback')

def __getfeedback__(essay:str):
    openai.api_key = "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" # todo: api
    prompt = '''Beim folgenden Text handelt es sich um einen Bericht von einer Schülerin zum Thema Corona. Gebe Tipps zur Ausdrucksweise wie ein Lehrer und gebe konkrete Verbessungsvorschläge. Text: """''' # todo

    input = prompt + essay + '''"""'''
    error_tmp = st.empty()

    # create a completion
    while True:
        try:
            completion = openai.Completion.create(engine="text-davinci-003", prompt=input, max_tokens=512)
            break
        except Exception as e:
            error_tmp.error(str(e))
            time.sleep(5)
            error_tmp.empty()

    # return the completion
    return completion.choices[0].text



def feedback():
    title_empty = st.empty()
    input_empty = st.empty()
    fb_empty = st.empty()
    btn_empty = st.empty()
    widgets = [
        title_empty,
        input_empty,
        fb_empty,
        btn_empty
    ]
    __feedbackpage__.extend(li=widgets)

    title_empty.markdown("# Your Feedbacks")
    input_empty.markdown(session.get('text'))
    with st.spinner():
        feedback_text = __getfeedback__(session.get('text'))
    fb_empty.info(f'''{feedback_text}''')
    btn_empty.button("Reset", on_click=go_home)

