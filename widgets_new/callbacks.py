import streamlit as st
from .mysession import session

def submit():
    session.clear()
    session.update('current_page', 'upload_image')