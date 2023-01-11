from  PIL import Image
import streamlit as st
from ..globals import reader
from .base import BasePage
from ..callbacks import submit_essay
from ..utils import get_random_string, rmrf

__uploadpage__ = BasePage(name='upload_image')

def upload_image():
    title_empty = st.empty()
    upload_file_empty = st.empty()
    md_empty = st.empty()
    textarea_empty = st.empty()
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

    uploaded_file = upload_file_empty.file_uploader("Choose a picture",type=['png','jpg','jpeg','webp'])

    if uploaded_file is not None:
        filename = uploaded_file.name
        print(f'''uploaded: {filename}''')
        image = Image.open(uploaded_file)
        if not (filename.endswith('.jpg') or filename.endswith('.jpeg')):
            random_str = get_random_string(5)
            filename = random_str+'123.jpg'
            image = image.convert('RGB')
            image.save(filename)
            image = Image.open(filename)

        with st.spinner('Recognizing...'):
            text = reader.readtext(image=image, detail=0)
            text = ' '.join(text)
            image.close()
            rmrf(filename)
        md_empty.markdown('**Please correct the mistakes:**')
        essay= textarea_empty.text_area('', value=text, height=500)
        btn_empty.button('Done', on_click=submit_essay,kwargs=dict(
            essay = essay
        ))
