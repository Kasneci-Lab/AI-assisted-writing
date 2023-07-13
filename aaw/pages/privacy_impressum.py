from pathlib import Path

import streamlit as st
from .base import BasePage

__privacy_page__ = BasePage(name='privacy')
__imprint_page__ = BasePage(name='imprint')


def privacy():
    __privacy_page__.sidebar()

    markdown = read_markdown_file("privacy.md")
    st.markdown(markdown, unsafe_allow_html=True)


def imprint():
    __imprint_page__.sidebar()

    markdown = read_markdown_file("imprint.md")
    st.markdown(markdown, unsafe_allow_html=True)


def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()
