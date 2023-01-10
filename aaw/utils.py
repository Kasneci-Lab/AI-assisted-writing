from pathlib import Path
import os
PACKAGE_ROOT = str(Path(__package__).absolute())

import streamlit as st


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
