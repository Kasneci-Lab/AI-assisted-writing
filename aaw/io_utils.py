from .mysession import session
from .globals import APIs, COLUMNS
import numpy as np

from shillelagh.exceptions import ProgrammingError
from shillelagh.backends.apsw.db import connect

from datetime import datetime


def login_to_google():
    print("\n\n##########################\n\n")
    print("Login to Google API")

    connect_args = {"path": ":memory:",
                   "adapters": "gsheetsapi",
                   "adapter_kwargs": {
                       "gsheetsapi": {
                           "service_account_info": {
                               **APIs["g_service_account"]
                           }
                       }
                   }
    }

    conn = connect(**connect_args)
    cursor = conn.cursor()
    print("Login done.")
    return cursor


def get_whole_dataset():
    cursor = login_to_google()
    query = f'SELECT * FROM "{APIs["gsheets_url"]}"'
    dataset = cursor.execute(query)
    return dataset


def add_row_to_dataset(new_values):
    cursor = login_to_google()
    columns_str = ", ".join(COLUMNS)
    new_values_str = ", ".join([f"\'{str(x)}\'" for x in new_values.values()])

    query2 = f'INSERT INTO "{APIs["gsheets_url"]}" ({columns_str}) VALUES ({new_values_str})'
    print(query2)
    cursor.execute(query2)


def store_data() -> None:
    """
    should be called after the feedback has been generated
    :return: None
    """
    feedback = session.get('feedback')
    if feedback is not None:
        new_sample = {
            'essay_category': session.get('user_args')['article'],
            'study_year': session.get('user_args')['year'],
            'school_type': session.get('user_args')['school'],
            'state': session.get('user_args')['state'],
            'title': session.get('title'),
            'essay_text': session.get('text'),
            'feedback': session.get('feedback')[session.get('preferred_fb')],
            'time_stamp': datetime.today().strftime('%Y-%m-%d')
        }

        try:
            add_row_to_dataset(new_sample)
        except ProgrammingError as err:
            print("#####  There was an error storing the new instance!  ########")
            print(err)


def get_whole_elo(to_prob=True) -> dict:
    '''

    :return: a dict object with keys: "prompts", "weights"
    '''
    cursor = login_to_google()
    query = f'SELECT * FROM "{APIs["elo_gsheets_url"]}"'
    dataset = cursor.execute(query)
    prompts = []
    weights = []

    for i in dataset:
        prompts.append(i[1])
        weights.append(i[2])

    weights = np.array(weights, dtype=float)
    if to_prob:
        weights /= np.sum(weights)

    return dict(
        prompts = prompts,
        weights = weights
    )

def inc_elo_weight(idx:int):
    tmp = get_whole_elo(to_prob=False)['weights']
    new_weight = tmp[idx] + 0.5  #todo: linear or exp?

    cursor = login_to_google()
    query = f'''UPDATE "{APIs['elo_gsheets_url']}" SET Weight = {new_weight} WHERE id = {idx}'''
    cursor.execute(query)
    print(f'{idx}th prompt has inc weight.')