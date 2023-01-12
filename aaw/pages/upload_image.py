from  PIL import Image
import streamlit as st
from .base import BasePage
from ..callbacks import submit_essay
from ..utils import get_random_string, rmrf, ocr

__uploadpage__ = BasePage(name='upload_image')


def upload_image():
    __uploadpage__.sidebar()

    title_empty = st.empty()
    upload_file_empty = st.empty()
    upload_teacher_empty = st.empty()
    md_empty = st.empty()
    textarea_empty = st.empty()
    teacher_empty = st.empty()
    btn_empty = st.empty()
    widgets = [
        title_empty,
        upload_file_empty,
        md_empty,
        textarea_empty,
        btn_empty
    ]
    __uploadpage__.extend(li=widgets)

    title_empty.markdown("# Upload a picture of your essay")

    essay_picture = upload_file_empty.file_uploader("**Upload a picture of your essay**",type=['png','jpg','jpeg','webp'])
    teacher_picture = upload_teacher_empty.file_uploader("**(optional) Upload a picture of teacher's correction**",
                                                    type=['png', 'jpg', 'jpeg', 'webp'])

    essay_text = None
    teahcer_text = None

    @st.cache
    def __ocr_cache__(image):
        with st.spinner('Recognizing...'):
            text = ocr(image)
            image.close()
            rmrf(filename)
        return text

    if essay_picture is not None:
        filename = essay_picture.name
        print(f'''uploaded: {filename}''')
        image = Image.open(essay_picture)
        if not (filename.endswith('.jpg') or filename.endswith('.jpeg')):
            random_str = get_random_string(5)
            filename = random_str + '123.jpg'
            image = image.convert('RGB')
            image.save(filename)
            image = Image.open(filename)

        text = __ocr_cache__(image)
        md_empty.markdown('### Please correct the OCR mistakes:')
        essay_text = textarea_empty.text_area('**Essay**', value=text, height=500)


    if teacher_picture is not None:
        filename = teacher_picture.name
        print(f'''uploaded: {filename}''')
        image = Image.open(teacher_picture)
        if not (filename.endswith('.jpg') or filename.endswith('.jpeg')):
            random_str = get_random_string(5)
            filename = random_str + '123.jpg'
            image = image.convert('RGB')
            image.save(filename)
            image = Image.open(filename)

        text = __ocr_cache__(image)
        teahcer_text = teacher_empty.text_area('**Teacher correction**', value=text, height=200)

    if essay_picture is not None:
        btn_empty.button("Done",on_click=submit_essay,kwargs=dict(
            essay = essay_text,
            teacher = teahcer_text
        ))


