import streamlit as st
from ..callbacks import go_home
from ..mysession import session
from ..globals import STRINGS


def render_sidebar():
    sidebar_markdown = '''

    <center>
    <img src="https://raw.githubusercontent.com/leoxiang66/streamlit-tutorial/IDP/widgets/static/tum.png" alt="TUM" 
    width="150"/>

    <h1>
    {header}
    </h1>


    <code>
    v0.2.1
    </code>


    </center>


    <center>
    <a href="https://github.com/leoxiang66/ai-assisted-writing">
    <img src = "https://cdn-icons-png.flaticon.com/512/733/733609.png" width="23"></img></a>
    
    <a href="mailto:xiang.tao@outlook.de">
    <img src="https://cdn-icons-png.flaticon.com/512/646/646094.png" alt="email" width = "27" ></a>
    </center>

    ---

    '''.format(header=STRINGS["SIDEBAR_HEADER"])
    st.sidebar.markdown(sidebar_markdown, unsafe_allow_html=True)

    st.sidebar.markdown('## {}'.format(STRINGS["SIDEBAR_CATEGORY"]))
    article_type = st.sidebar.selectbox('Category', on_change=go_home, label_visibility='collapsed', options=[
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

    st.sidebar.markdown('## {}'.format(STRINGS["SIDEBAR_SCHOOL"]))
    school_type = st.sidebar.selectbox('School Type', on_change=go_home, label_visibility='collapsed', options=[
        'Grundschule',
        'Hauptschule',
        'Realschule',
        'Gymnasium',
    ])

    st.sidebar.markdown('## {}'.format(STRINGS["SIDEBAR_YEAR"]))
    study_year = st.sidebar.selectbox('Study year', on_change=go_home, label_visibility='collapsed',
                                      options=list(range(1, 14)))

    st.sidebar.markdown('## {}'.format(STRINGS["SIDEBAR_STATE"]))
    state = st.sidebar.selectbox('State', on_change=go_home, label_visibility='collapsed', options=[
        'Bayern',
        'Baden-Württemberg',
        'Berlin',
        'Brandenburg',
        'Bremen',
        'Hamburg',
        'Hessen',
        'Mecklenburg-Vorpommern',
        'Niedersachsen',
        'Nordrhein-Westfalen',
        'Rheinland-Pfalz',
        'Saarland',
        'Sachsen',
        'Schleswig-Holstein',
        'Thüringen'
    ])

    st.session_state.user_args = dict(
        article_type=article_type,
        study_year=study_year,
        school_type=school_type,
        state=state
    )

    # if st.sidebar.selectbox('Debug', options=['No', 'Yes']) == 'Yes':
    #     session.update('debug', True)
    # else:
    session.update('debug', False)
