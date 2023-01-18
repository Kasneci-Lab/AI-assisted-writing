import easyocr
from pathlib import Path
import json
import pandas as pd


def __read_apis__():
    API_PATH = Path('.api.json')
    with open(API_PATH, 'r', encoding='UTF-8') as f:
        load_dict = json.load(f)
    return load_dict


def __get_strings__(lang):
    df_strings = pd.read_csv("strings.csv")

    # Check if language exists, otherwise use english
    lang = lang if lang in df_strings.columns[1:] else "en"

    return pd.Series(df_strings[lang].values, index=df_strings["Variable"]).to_dict()


# ToDo: Get the language dynamically!
language = "de"

reader = easyocr.Reader([language])
STRINGS = __get_strings__(language)

INPUT_TYPES = [STRINGS["INPUT_TYPE_PICTURE"], STRINGS["INPUT_TYPE_TEXT"]]
DATAPATH = Path('dataset').joinpath('raw.csv')
APIs = __read_apis__()

