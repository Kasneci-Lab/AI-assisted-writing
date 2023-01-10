import streamlit as st
from pprint import pprint
import streamlit.components.v1 as components
from widgets import *
from widgets.var import INPUT_TYPES
import time
from PIL import Image

# sidebar content
user_input_dict = render_sidebar()
st.sidebar.info(body=f'''Current Configuration: {user_input_dict}''')


if 'submitted' not in st.session_state:
    st.session_state.submitted = False

if 'texted' not in st.session_state:
    st.session_state.texted = False

if 'text' not in st.session_state:
    st.session_state.text = ''

if 'ing' not in st.session_state:
    st.session_state.ing = False

if 'input_type' not in st.session_state:
    st.session_state.input_type = None

if 'widgets' not in st.session_state:
    st.session_state.widgets = dict(
        welcome = None
    )





if not st.session_state.ing:
    welcome_widgets, input_type = welcome_page()




if st.session_state.texted:
    pipeline()
    print(1)
    st.stop()

elif st.session_state.submitted:
    print(2)
    st.session_state.ing = True
    valid_arguments(user_input_dict)
    clear_list(welcome_widgets)
    # upload an image
    if input_type == INPUT_TYPES[0]:
        ret = upload_image()

    elif input_type == INPUT_TYPES[1]:
        input_text()
    st.stop()







