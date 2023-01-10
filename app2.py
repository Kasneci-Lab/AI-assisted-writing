import streamlit as st
from widgets_new import *
from widgets_new.mysession import session
from widgets_new.pages import *



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






