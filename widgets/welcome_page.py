import streamlit as st
from .input_page import upload_image,input_text
from .utils import clear_list

INPUT_TYPES = ['Upload a picture', 'Input text']


def welcome_page():
    welcome_page = [
        st.markdown('''# 👋 Hi, I'm your AI essay tutor :)'''),
        st.markdown('''### Do you want to upload a picture of your essay or input text manually?'''),
    ]

    form = st.empty()
    tmp = form.form("my_form")
    input_type=tmp.radio("",INPUT_TYPES)

    # Now add a submit button to the form:
    submitted = tmp.form_submit_button("Submit")
    welcome_page.append(form)


    return welcome_page,submitted,input_type




