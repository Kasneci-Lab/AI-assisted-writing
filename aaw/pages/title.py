import streamlit as st
from .base import BasePage

titleheader_empty = st.empty()
title_empty = st.empty()
titleheader_empty.markdown('''#### Please enter the title of your essay''')
title_empty.text_input('', placeholder='My Cool Title')
