import streamlit as st
from aaw import *
from aaw.mysession import session
from aaw.pages import *



# my_session setup
session.update('page_map',dict(
    home=homepage,
    upload_image = upload_image,
    feedback = feedback
))
session.init('page_widgets', dict())
session.init('current_page', 'home')
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






