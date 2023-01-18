import streamlit as st
st.set_page_config(layout="wide")
from aaw.mysession import session
from aaw.pages import (homepage, upload_image, feedback, input_text, input_type, login, PAGES)
from aaw.utils import create_dataset

# create dataset folder
create_dataset()

# my_session setup
session.update('page_map', dict(
    home=homepage,
    upload_image=upload_image,
    feedback=feedback,
    input_text=input_text,
    input_type=input_type,
    login=login,
))

# only has effect when a new session starts, a new session starts when user refreshes the page
session.init('page_widgets', dict())
session.init('current_page', 'login')
session.init('feedback', None)
session.init('title', None)
session.init("prompt", False)
session.init('teacher', None)
session.init('debug', False)

for page in PAGES:
    page.__post_process__(session)

# render current page
debug_empty = st.empty()  # todo: remove debug
session.render()

# debugging
debug = session.get('debug')
if debug:
    debug_empty.info(session.summary())
