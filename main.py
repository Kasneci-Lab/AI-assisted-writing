import streamlit as st
from pprint import pprint
import streamlit.components.v1 as components
from widgets import *
import time



# sidebar content
user_input_dict = render_sidebar()

# # body head
# with st.form("my_form",clear_on_submit=False):
#     st.markdown('''# 👋 Hi, I'm your AI essay tutor :)''')
#     query_input = st.text_area(
#         'Enter your essay here',placeholder='''e.g. "Today I went to a park..."''',
#         # label_visibility='collapsed',
#         value=''
#     )
#
#     # Every form must have a submit button.
#     submitted = st.form_submit_button("Next")
#
#
# if submitted:
#     st.info(f'''You have entered:"\n{query_input}"\n\nWith following setting: {user_input_dict}''')



welcome_widgets,submitted,input_type = welcome_page()




if submitted:
    clear_list(welcome_widgets)
    print(input_type)






