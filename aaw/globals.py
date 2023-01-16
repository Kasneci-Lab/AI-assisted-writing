import easyocr
from pathlib import Path
import json


def __read_apis__():
    API_PATH = Path('.api.json')
    with open(API_PATH, 'r', encoding='UTF-8') as f:
        load_dict = json.load(f)
    return load_dict


reader = easyocr.Reader(['de'])
INPUT_TYPES = ['Upload a picture', 'Input text']
DATAPATH = Path('dataset').joinpath('raw.csv')
APIs = __read_apis__()

