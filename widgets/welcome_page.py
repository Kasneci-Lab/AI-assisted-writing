import streamlit as st
from .input_page import upload_image,input_text
from .utils import clear_list
from .var import INPUT_TYPES


def clicked():
    st.session_state.submitted = True

def welcome_page():
    welcome_page = [
        st.markdown('''# 👋 Hi, I'm your AI essay tutor :)'''),
        st.markdown('''### Do you want to upload a picture of your essay or input text manually?'''),
    ]

    # form = st.empty()
    # tmp = form.form("my_form")
    # input_type=tmp.radio("",INPUT_TYPES)
    #
    # # Now add a submit button to the form:
    # submitted = tmp.form_submit_button("Submit")
    input_radio = st.empty()
    input_type = input_radio.radio("",INPUT_TYPES)
    welcome_page.append(input_radio)

    btn = st.empty()
    btn.button(label='Next', on_click=clicked)
    welcome_page.append(btn)

    st.session_state.widgets['welcome'] = welcome_page

    return input_type




