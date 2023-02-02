import streamlit as st
from .base import BasePage
from ..callbacks import go_inputtype
from ..globals import STRINGS

__homepage__ = BasePage(name='home')


def homepage():
    #########################
    # Set up page structure #
    #########################

    __homepage__.sidebar()
    __homepage__.append(empty=st.markdown('''# {}'''.format(STRINGS["HOME_HEADER"])))

    # Add some space
    st.empty().markdown("&nbsp;")

    st.empty().markdown('''#### {}'''.format(STRINGS["HOME_HEADER_DESCRIPTION"]))

    # Add some space
    st.empty().markdown("&nbsp;")

    title_header_empty = st.empty()
    title_choice_empty = st.empty()

    # Add some space
    st.empty().markdown("&nbsp;")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        article_header_empty = st.empty()
        article_choice_empty = st.empty()

    with col2:
        school_header_empty = st.empty()
        school_choice_empty = st.empty()

    with col3:
        year_header_empty = st.empty()
        year_choice_empty = st.empty()

    with col4:
        state_header_empty = st.empty()
        state_choice_empty = st.empty()

    # Add some space
    st.empty().markdown("&nbsp;")

    btn_empty = st.empty()

    # Add some space
    st.empty().markdown("&nbsp;")

    st.empty().markdown(STRINGS["PROJECT_DESCRIPTION"])

    #############################
    # Fill all empty containers #
    #############################

    title_header_empty.markdown('''#### {}'''.format(STRINGS["HOME_TITLE"]))
    title_choice_empty.text_input('title',
                                  label_visibility='collapsed',
                                  placeholder=STRINGS["HOME_TITLE_PLACEHOLDER"],
                                  key='title_tmp')

    article_header_empty.markdown('''##### {}'''.format(STRINGS["SIDEBAR_CATEGORY"]))
    article_choice_empty.selectbox("article", label_visibility="collapsed",
                                   options=['Bericht',
                                            'Erörterung',
                                            'Essay',
                                            'Gedichtsanalyse',
                                            'Inhaltsangabe',
                                            'Kurzgeschichte',
                                            'Rezension',
                                            'Sachtextanalyse',
                                            'Szenenanalyse', ], key='article')

    school_header_empty.markdown('''##### {}'''.format(STRINGS["SIDEBAR_SCHOOL"]))
    school_choice_empty.selectbox("school", label_visibility="collapsed",
                                  options=['Grundschule',
                                           'Hauptschule',
                                           'Realschule',
                                           'Gymnasium', ], key='school')

    year_header_empty.markdown('''##### {}'''.format(STRINGS["SIDEBAR_YEAR"]))
    year_choice_empty.selectbox("year", label_visibility="collapsed",
                                options=list(range(1, 14)), key='year')

    state_header_empty.markdown('''##### {}'''.format(STRINGS["SIDEBAR_STATE"]))
    state_choice_empty.selectbox("state", label_visibility="collapsed",
                                 options=[
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
                                 ], key='state')

    btn_empty.button(STRINGS["HOME_TITLE_BUTTON"], on_click=go_inputtype)
