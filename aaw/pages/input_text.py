from .base import BasePage
import streamlit as st
from ..callbacks import submit_essay

__inputtextpage__ = BasePage(name='input_text')

def input_text():
    global __inputtextpage__
    title_empty = st.empty()
    textarea_empty = st.empty()
    btn_empty = st.empty()

    __inputtextpage__.extend(li=[
        title_empty,
        textarea_empty,
        btn_empty
    ])

    title_empty.markdown("# Enter you essay here :)")
    essay = textarea_empty.text_area(label='', placeholder="Ich liebe Schokoladen...", height=600)
    btn_empty.button("Submit", on_click=submit_essay,kwargs=dict(
        essay = essay
    ))
