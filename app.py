import streamlit as st
from aaw import *
from aaw.mysession import session
from aaw.pages import *
from aaw.utils import create_dataset

# create dataset folder
create_dataset()

# my_session setup
session.update('page_map',dict(
    home=homepage,
    upload_image = upload_image,
    feedback = feedback,
    input_text = input_text,
    input_type = input_type,
))
session.init('page_widgets', dict())
session.init('current_page', 'home') # only has effect when a new session starts, a new session starts when user refreshes the page
session.update('feedback',None)
session.init('title',None)

for page in PAGES:
    page.__post_process__(session)


# sidebar
debug = render_sidebar()


# debugging
if debug:
    if debug == 'Yes':
        st.info(session.summary())



# render current page
print(session.get_current_page())
session.render()






