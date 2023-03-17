import streamlit as st
st.set_page_config(layout="wide")
from aaw.mysession import session
from aaw.pages import (homepage, upload_image, feedback, input_text, input_type, modify_text, PAGES)
from aaw.utils import create_dataset

# Create dataset folder
create_dataset()

# Set up session variables for page navigation and data storage
session.update('page_map', dict(
    home=homepage,
    upload_image=upload_image,
    feedback=feedback,
    input_text=input_text,
    input_type=input_type,
    modify_text=modify_text,
))

# Initialize session variables with default values
# These variables will only be initialized when a new session starts (e.g., when the user refreshes the page)
session.init('page_widgets', dict())
session.init('current_page', "home")  # 'login'
session.init('feedback', None)
session.init('title', None)
session.init("user_args", dict())
session.init("input_type", None)
session.init("new_feedback", True)

<<<<<<< Updated upstream

=======
# Perform post-processing for each page in PAGES
>>>>>>> Stashed changes
for page in PAGES:
    page.__post_process__(session)

# Render the current page
session.render()
