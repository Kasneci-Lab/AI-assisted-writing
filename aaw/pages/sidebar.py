import streamlit as st
from ..callbacks import go_home
from ..mysession import session





def render_sidebar():
    sidebar_markdown = f'''

    <center>
    <img src="https://raw.githubusercontent.com/leoxiang66/streamlit-tutorial/IDP/widgets/static/tum.png" alt="TUM" width="150"/>

    <h1>
    AI-Assisted Writing 
    </h1>


    <code>
    v0.1.0
    </code>


    </center>


    <center>
    <a href="https://github.com/leoxiang66/ai-assisted-writing"><img src = "https://cdn-icons-png.flaticon.com/512/733/733609.png" width="23"></img></a>  <a href="mailto:xiang.tao@outlook.de"><img src="https://cdn-icons-png.flaticon.com/512/646/646094.png" alt="email" width = "27" ></a>
    </center>

    ---

    '''
    st.sidebar.markdown(sidebar_markdown,unsafe_allow_html=True)



    st.sidebar.markdown('## Choose the essay category')
    article_type = st.sidebar.selectbox('Category',on_change=go_home,label_visibility='collapsed',options=[
        'Bericht',
        'Erörterung',
        'Essay',
        'Gedichtsanalyse',
        'Inhaltsangabe',
        'Kurzgeschichte',
        'Rezension',
        'Sachtextanalyse',
        'Szenenanalyse',
    ])

    st.sidebar.markdown('## Choose your study year')
    study_year = st.sidebar.selectbox('Study year',label_visibility='collapsed',options=['-']+list(range(1,14)),on_change=go_home)
    st.session_state.user_args = dict(
        article_type = article_type,
        study_year = study_year
    )

    if st.sidebar.selectbox('Debug', options=['No', 'Yes']) == 'Yes':
        session.update('debug',True)
    else:
        session.update('debug', False)


