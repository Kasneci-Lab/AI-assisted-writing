from .mysession import session
from .globals import APIs, COLUMNS, ELO_COLUMNS
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


#########################
#                       #
#   Store essay data    #
#                       #
#########################

def get_whole_dataset():
    cursor = login_to_google()
    query = f'SELECT * FROM "{APIs["essay_gsheets_url"]}"'
    dataset = cursor.execute(query)
    return dataset


def add_row_to_dataset(new_values):
    cursor = login_to_google()
    columns_str = ", ".join(COLUMNS)
    new_values_str = ", ".join([f"\'{str(x)}\'" for x in new_values.values()])

    query2 = f'INSERT INTO "{APIs["essay_gsheets_url"]}" ({columns_str}) VALUES ({new_values_str})'
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
            'feedback1': session.get('feedback')["feedback"][0],
            'feedback2': session.get('feedback')["feedback"][1],
            'time_stamp': datetime.today().strftime('%Y-%m-%d')
        }
        try:
            add_row_to_dataset(new_sample)
        except ProgrammingError as err:
            print("#####  There was an error storing the new instance!  ########")
            print(err)


#########################
#                       #
#   Store elo ranking   #
#                       #
#########################

def __elo_column_to_idx__(column):
    try:
        return ELO_COLUMNS.index(column)
    except ValueError as e:
        print("Column " + column + " not in dataset!")
        return 0


def get_whole_elo(to_prob=True) -> dict:
    """
    :return: a dict object with keys: "prompts", "weights"
    """
    cursor = login_to_google()
    query = f'SELECT * FROM "{APIs["elo_gsheets_url"]}"'
    dataset = cursor.execute(query)

    elo_dict = dict(ids=[], names=[], prompts=[], weights=[], engines=[])

    ids_idx = __elo_column_to_idx__("id")
    names_idx = __elo_column_to_idx__("name")
    prompt_idx = __elo_column_to_idx__("prompt")
    weight_idx = __elo_column_to_idx__("weight")
    engine_idx = __elo_column_to_idx__("engine")

    for i in dataset:
        elo_dict["ids"].append(i[ids_idx])
        elo_dict["names"].append(i[names_idx])
        elo_dict["prompts"].append(i[prompt_idx])
        elo_dict["weights"].append(i[weight_idx])
        elo_dict["engines"].append(i[engine_idx])

    elo_dict["weights"] = np.array(elo_dict["weights"], dtype=float)

    if to_prob:
        elo_dict["weights"] /= np.sum(elo_dict["weights"])

    return elo_dict


def update_elo_weights(prompt_id, new_elo):
    cursor = login_to_google()
    query = f'''UPDATE "{APIs['elo_gsheets_url']}" SET Weight = {new_elo} WHERE id = {prompt_id}'''
    cursor.execute(query)


def elo_update(idx_prompt_a:int, idx_prompt_b:int, outcome_a_won:bool):
    # Quick explanation of the ELO Ranking System
    # https://www.youtube.com/watch?v=AsYfbmp0To0
    current_elo = get_whole_elo(to_prob=False)['weights']
    new_elo_a, new_elo_b = compute_updated_elo(current_elo[idx_prompt_a], current_elo[idx_prompt_b], outcome_a_won)
    
    # write the changes to the Google sheet
    update_elo_weights(idx_prompt_a, new_elo_a)
    update_elo_weights(idx_prompt_b, new_elo_b)


def compute_updated_elo(elo_a, elo_b, outcome_a_won):
    # Step 1: calculate expected winning probability of Prompt A
    probability = 1 / (1 + 10 ** ((elo_b - elo_a) / 400))

    # Step 2: update rankings based on outcome
    if outcome_a_won:
        elo_a += 32 * (1 - probability)
        elo_b -= 32 * (1 - probability)
    else:
        elo_a += 32 * (0 - probability)
        elo_b -= 32 * (0 - probability)

    return elo_a, elo_b
