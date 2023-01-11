import easyocr
from pathlib import Path

reader = easyocr.Reader(['de'])
INPUT_TYPES = ['Upload a picture', 'Input text']
DATAPATH = Path('dataset').joinpath('raw.csv')
