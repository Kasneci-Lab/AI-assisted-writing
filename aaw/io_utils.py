from .mysession import session
import numpy as np

import pandas as pd

from datetime import datetime

ESSAY_FILE = "essay_data.xlsx"
ELO_FILE = "elo_ranking.xlsx"


#########################
#                       #
#   Store essay data    #
#                       #
#########################


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
            # Add row to data set
            df = pd.read_excel(ESSAY_FILE)
            df.loc[len(df)] = new_sample
            # df = pd.concat([df, pd.DataFrame([new_values])], ignore_index=True)
            df.to_excel(ESSAY_FILE, index=False)

        except Exception as err:
            print("#####  There was an error storing the new instance!  ########")
            print(err)


#########################
#                       #
#   Store elo ranking   #
#                       #
#########################


def get_elo_weights(df, to_prob=True) -> dict:
    weights = np.array(df["weight"].values, dtype=float)

    if to_prob:
        weights /= np.sum(weights)

    return weights


def elo_update(idx_prompt_a: int, idx_prompt_b: int, outcome_a_won: bool):
    # Quick explanation of the ELO Ranking System
    # https://www.youtube.com/watch?v=AsYfbmp0To0

    df = pd.read_excel(ELO_FILE)

    current_elo = get_elo_weights(df, to_prob=False)
    new_elo_a, new_elo_b = compute_updated_elo(current_elo[idx_prompt_a], current_elo[idx_prompt_b], outcome_a_won)

    df.loc[df["id"] == idx_prompt_a, "weight"] = new_elo_a
    df.loc[df["id"] == idx_prompt_b, "weight"] = new_elo_b

    try:
        # Save new weights
        df.to_excel(ELO_FILE, index=False)
    except Exception as err:
        print("#####  There was an error storing the new weights!  ########")
        print(err)


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


#########################
#                       #
#   Sample prompts      #
#                       #
#########################

def sample_prompts(num_prompts=2) -> dict:
    elo_dataset = pd.read_excel(ELO_FILE)

    # Choose two prompts based on the elo ranking they have ("better" prompts are sampled more often)
    weights = get_elo_weights(elo_dataset, to_prob=True)
    sampled_idx = np.random.choice(len(weights), p=weights, size=num_prompts, replace=False)

    print("Comparing the prompts " + elo_dataset["name"][sampled_idx[0]] +
          " and " + elo_dataset["name"][sampled_idx[1]])

    return {elo_dataset['id'][i]: (elo_dataset['engine'][i], elo_dataset['prompt'][i]) for i in sampled_idx}
