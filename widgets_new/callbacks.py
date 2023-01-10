import streamlit as st
from .mysession import session
from .utils import valid_user_arguments

def submit():
    session.clear()
    input_type = session.get('input_type')
    if input_type == 'Upload a picture':
        session.update('current_page', 'upload_image')
    else:
        raise NotImplementedError() # todo

def preprocess_text():
    session.clear()
    session.update('current_page','feedback')

def go_home():
    session.clear()
    session.update('current_page','home')