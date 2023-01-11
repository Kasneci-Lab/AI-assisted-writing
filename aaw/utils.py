from pathlib import Path
PACKAGE_ROOT = str(Path(__package__).absolute())
import random
import string
import streamlit as st



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
    st.error(msg)
    st.stop()



def get_random_string(length) -> str:
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str