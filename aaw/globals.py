from pathlib import Path
import pandas as pd
import streamlit as st


def __get_strings__(lang):
    df_strings = pd.read_csv("strings.csv")

    # Check if language exists, otherwise use english
    lang = lang if lang in df_strings.columns[1:] else "en"

    return pd.Series(df_strings[lang].values, index=df_strings["Variable"]).to_dict()


# ToDo: Get the language dynamically!
language = "de"

STRINGS = __get_strings__(language)

INPUT_TYPES = [STRINGS["INPUT_TYPE_PICTURE"], STRINGS["INPUT_TYPE_TEXT"]]
DATAPATH = Path('dataset').joinpath('raw.csv')
NUM_PROMPTS = 2

APIs = {
    "openai": st.secrets["openai_secrets"]["openai_key"],
    "login_pwd": st.secrets["login_password"],
    "ocr_app_id": st.secrets["ocr_secrets"]["ocr_app_id"],
    "ocr_app_key": st.secrets["ocr_secrets"]["ocr_app_key"],
    "g_service_account": st.secrets["gcp_service_account"],
    "gsheets_url":  st.secrets["gsheets"]["private_gsheets_url"],
    "elo_gsheets_url": st.secrets["gsheets"]["elo_gsheets_url"],
    "essay_gsheets_url": st.secrets["gsheets"]["essay_gsheets_url"]
}

COLUMNS = ["essay_category",
           "study_year",
           "school_type",
           "state",
           "title",
           "essay_text",
           "feedback1",
           "feedback2",
           "time_stamp"]

ELO_COLUMNS = ["id", "name", "prompt", "weight", "engine"]
