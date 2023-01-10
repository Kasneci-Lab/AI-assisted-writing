import streamlit as st
from widgets_new import *
from widgets_new.mysession import session
from widgets_new.pages import *



# my_session setup
session.update('text', '')
session.update('page_map',dict(
    home=homepage,
    upload_image = upload_image
))
session.init('page_widgets', dict())
session.init('current_page', 'home')
for page in PAGES:
    page.__post_process__(session)


# sidebar
render_sidebar()
st.sidebar.info(body=f'''Current Configuration: {st.session_state['user_args']}''')



# debugging
st.info(session.summary())



# render current page
print(session.get_current_page())
session.render()






