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
    "ocr_app_id": st.secrets["ocr_secrets"]["ocr_app_id"],
    "ocr_app_key": st.secrets["ocr_secrets"]["ocr_app_key"],
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
