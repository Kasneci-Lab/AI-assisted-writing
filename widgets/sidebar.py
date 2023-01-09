import streamlit as st
import datetime
# from .utils import PACKAGE_ROOT

def render_sidebar():
    sidebar_markdown = f'''

    <center>
    <img src="https://raw.githubusercontent.com/leoxiang66/streamlit-tutorial/IDP/widgets/static/tum.png" alt="TUM" width="150"/>

    <h1>
    AI-Assisted Writting 
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
    # st.sidebar.markdown('## Choose the Paper Search Platforms')
    st.sidebar.markdown(sidebar_markdown,unsafe_allow_html=True)

    # platforms = st.sidebar.multiselect('Platforms',options=
    # [
    #     # 'Elvsier',
    #     'IEEE',
    #     # 'Google Scholar',
    #     'Arxiv',
    #     'PaperWithCode'
    # ], default=[
    #     # 'Elvsier',
    #     'IEEE',
    #     # 'Google Scholar',
    #     'Arxiv',
    #     'PaperWithCode'
    # ])
    #
    #
    #
    # st.sidebar.markdown('## Choose the max number of papers to search')
    # number_papers=st.sidebar.slider('number', 50, 200, 50, 10)
    #
    # st.sidebar.markdown('## Choose the start year of publication')
    # this_year = datetime.date.today().year
    # start_year = st.sidebar.slider('year start:', 2000, this_year, 2010, 1)
    #
    # st.sidebar.markdown('## Choose the end year of publication')
    # end_year = st.sidebar.slider('year end:', 2000, this_year, this_year, 1)
    #
    # return platforms, number_papers, start_year, end_year

    st.sidebar.markdown('## Choose the essay type')
    article_type = st.sidebar.selectbox('essay',options=['Article', 'Journal'])

    return dict(
        article_type = article_type
    )