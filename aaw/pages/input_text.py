from .base import BasePage
import streamlit as st
from ..callbacks import submit_essay
from ..mysession import session

__inputtextpage__ = BasePage(name='input_text')

def input_text():
    __inputtextpage__.sidebar()
    title_empty = st.empty()
    textarea_empty = st.empty()
    btn_empty = st.empty()

    __inputtextpage__.extend(li=[
        title_empty,
        textarea_empty,
        btn_empty
    ])


    prompt = session.get('prompt')

    if not prompt:
        title_empty.markdown("# Enter you essay here :)")
        essay = textarea_empty.text_area(
            label='',
            label_visibility='collapsed',
            placeholder="Ich liebe Schokoladen...",
            height=500,
        )
        btn_empty.button("Submit", on_click=submit_essay, kwargs=dict(
            essay=essay
        ))
    else:
        title_empty.markdown("# Modify your essay :)")
        col1,col2 = textarea_empty.columns([1,1])
        col1.markdown(f'''**Original Essay:**''')
        col1.info(session.get('text'))
        essay = col2.text_area(
            label='',
            placeholder='change your essay here',
            height=500,
        )
        expander= col1.expander('feedbacks')
        expander.success(session.get('feedback'))
        col2.button("Submit", on_click=submit_essay, kwargs=dict(
            essay=essay
        ))




