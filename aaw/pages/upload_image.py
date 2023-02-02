import streamlit as st
from .base import BasePage
from ..callbacks import submit_essay, go_input_type
from ..utils import image_to_text
from ..globals import STRINGS

__uploadpage__ = BasePage(name='upload_image')


def upload_image():
    #########################
    # Set up page structure #
    #########################

    __uploadpage__.sidebar()

    title_empty = st.empty()
    upload_file_empty = st.empty()
    md_empty = st.empty()
    textarea_empty = st.empty()

    col1, col2 = st.columns(2)

    with col1:
        btn_back = st.empty()
    with col2:
        btn = st.empty()

    #############################
    # Fill all empty containers #
    #############################

    title_empty.markdown("# {}".format(STRINGS["UPLOAD_IMAGE_HEADER"]))

    essay_picture = upload_file_empty.file_uploader("**{}**".format(STRINGS["UPLOAD_IMAGE_ESSAY"]),
                                                    type=['png', 'jpg', 'jpeg', 'pdf'])

    btn_back.button(label=STRINGS["BUTTON_BACK"], on_click=go_input_type)

    essay_text = None

    @st.cache(show_spinner=False)
    def __ocr_cache__(image_input):
        with st.spinner(STRINGS["UPLOAD_IMAGE_WAITING"]):
            text_output = image_to_text(image_input)
        return text_output

    if essay_picture is not None:
        text = __ocr_cache__(essay_picture)
        # text = "Test"
        md_empty.markdown('### {}:'.format(STRINGS["UPLOAD_IMAGE_CORRECT_MISTAKES"]))
        essay_text = textarea_empty.text_area('**{}**'.format(STRINGS["UPLOAD_IMAGE_ESSAY"]),
                                              value=text, height=500)

    if essay_text:
        btn.button(STRINGS["UPLOAD_IMAGE_BUTTON"], on_click=submit_essay, kwargs=dict(essay=essay_text))
