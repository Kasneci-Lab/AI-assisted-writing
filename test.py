import streamlit as st
from  PIL import Image

uploaded_file = st.file_uploader("Choose a picture", type=['png', 'jpg', 'jpeg'])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image)