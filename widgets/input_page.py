from io import StringIO
from  PIL import Image
import streamlit as st
from .var import reader
from .experimental import preprocess


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

    title_empty.markdown("# Upload a picture of your essay")

    uploaded_file = upload_file_empty.file_uploader("Choose a picture",type=['png','jpg','jpeg','webp'])


    if uploaded_file is not None:
        print(f'''uploaded: {uploaded_file}''')
        image = Image.open(uploaded_file)
        with st.spinner('Recognizing...'):
            text = reader.readtext(image=image, detail=0)
            text = ' '.join(text)
        md_empty.markdown('**Please correct the mistakes:**')
        text= textarea_empty.text_area('', value=text, height=600)
        btn_empty.button('Done', on_click=preprocess, kwargs=dict(
            widgets = widgets,
            text = text
        ))



def input_text():
    print('input text')


