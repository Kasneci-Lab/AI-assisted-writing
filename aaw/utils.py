from pathlib import Path
PACKAGE_ROOT = str(Path(__package__).absolute())
import random
import string
import streamlit as st
from .mysession import session
import pandas as pd
from .globals import DATAPATH
from .globals import reader
import csvkit


def rmrf(path):
    path = Path(path)
    if path.exists():
        if path.is_file():
            path.unlink()
        else:
            for child in path.glob('*'):
                rmrf(child)
            path.rmdir()


def readfile(path:str) -> str:
    with open(path) as f:
        ret = f.read()
    return ret

def valid_user_arguments(kwargs:dict)->bool:
    # study-year
    studyyear = kwargs['study_year']
    if not isinstance(studyyear,int):
        return False
    return True


def error_and_stop(msg:str):
    st.sidebar.error(msg)
    # st.stop()



def get_random_string(length) -> str:
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def create_dataset():
    directory = 'dataset'
    p = Path(directory)
    p.mkdir(parents=True, exist_ok=True)

    filepath = p.joinpath('raw.csv')
    if not filepath.exists():
        df = pd.DataFrame(columns=['essay category', 'study year','title', 'essay text','teacher correction', 'feedback'])
        df.to_csv(filepath, index=False)


def store_data()->None:
    '''
    should be called after the feedback has been generated
    :return: None
    '''
    feedback = session.get('feedback')
    if feedback is not None:
        # df = pd.read_csv(DATAPATH)
        newsample={
            'essay category': session.get('user_args')['article_type'],
            'study year': session.get('user_args')['study_year'],
            'title': session.get('title'),
            'essay text': session.get('text'),
            'teacher correction': session.get('teacher'),
            'feedback': session.get('feedback')
        }
        newsample = list(newsample.values())
        csvkit.sync.sync_append(csv_filepath=DATAPATH,values=newsample)
        # df=df.append(newsample,True)
        # df.to_csv(DATAPATH,index=False)

def ocr(image)->str:
    text = reader.readtext(image=image, detail=0)
    text = ' '.join(text)
    return text