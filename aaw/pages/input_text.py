from .base import BasePage
import streamlit as st
from ..callbacks import submit_essay, go_input_type, go_home
from ..globals import STRINGS

__inputtextpage__ = BasePage(name='input_text')

from ..utils import image_to_text


def input_text():
    print("not here=")

    #########################
    # Set up page structure #
    #########################

    __inputtextpage__.sidebar()
    title_empty1 = st.empty()
    textarea_empty1 = st.empty()
    upload_task_empty = st.empty()

    title_empty2 = st.empty()
    textarea_empty2 = st.empty()
    upload_essay_empty = st.empty()

    col1, col2 = st.columns(2)

    with col1:
        btn_back = st.empty()
    with col2:
        btn = st.empty()

    #############################
    # Fill all empty containers #
    #############################

    title_empty1.markdown("# {}".format("Was ist die genaue Aufgabenstellung? Gibt es Zusatzmaterial?"))

    task = textarea_empty1.text_area(
        label='text_area1',
        label_visibility='collapsed',
        placeholder="Aufgabenstellung / Zusatzmaterial",
        height=100,
    )

    task_picture = upload_task_empty.file_uploader("Aufgabe hochladen",
                                                   type=['png', 'jpg', 'jpeg', 'pdf'])

    title_empty2.markdown("# {}".format("Aufsatz eingeben"))

    essay = textarea_empty2.text_area(
        label='text_area2',
        label_visibility='collapsed',
        placeholder=STRINGS["INPUT_TEXT_PLACEHOLDER"],
        height=200,
    )

    essay_picture = upload_essay_empty.file_uploader("Aufsatz hochladen",
                                                     type=['png', 'jpg', 'jpeg', 'pdf'])

    def __ocr_cache__(image_input):
        with st.spinner(STRINGS["UPLOAD_IMAGE_WAITING"]):
            text_output, error_msg = image_to_text(image_input)
        return text_output, error_msg

    if task_picture is not None:
        textt, error_msg = __ocr_cache__(task_picture)
        # text = "Test"

        if textt:
            task = textarea_empty1.text_area(label="task_area", label_visibility='collapsed', value=textt, height=250)

    if essay_picture is not None:
        texte, error_msg = __ocr_cache__(essay_picture)
        # text = "Test"

        if texte:
            essay = textarea_empty2.text_area(label="essay_area", label_visibility='collapsed', value=texte, height=300)

    print(task)
    print(essay)

    if essay:
        btn.button(STRINGS["INPUT_TEXT_BUTTON"], on_click=submit_essay, kwargs=dict(essay=essay, task=task))

    btn_back.button(label=STRINGS["BUTTON_BACK"], on_click=go_home)
