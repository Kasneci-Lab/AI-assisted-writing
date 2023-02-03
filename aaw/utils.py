import os
import glob

import random
import string
import pandas as pd

import requests
import openai
import time

from pdf2image import convert_from_path
from PIL import Image
from pathlib import Path

PACKAGE_ROOT = str(Path(__package__).absolute())
from .mysession import session
from .globals import DATAPATH, APIs


def get_random_string(length) -> str:
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def create_dataset():
    directory = 'dataset'
    p = Path(directory)
    p.mkdir(parents=True, exist_ok=True)

    filepath = p.joinpath('raw.csv')
    if not filepath.exists():
        df = pd.DataFrame(
            columns=['essay category', 'study year', 'school type', 'state',
                     'title', 'essay text', 'feedback'])  # 'teacher correction',
        df.to_csv(filepath, index=False)


def store_data() -> None:
    """
    should be called after the feedback has been generated
    :return: None
    """
    feedback = session.get('feedback')
    if feedback is not None:
        df = pd.read_csv(DATAPATH)

        new_sample = {
            'essay category': session.get('user_args')['article'],
            'study year': session.get('user_args')['year'],
            'school type': session.get('user_args')['school'],
            'state': session.get('user_args')['state'],
            'title': session.get('title'),
            'essay text': session.get('text'),
            'feedback': session.get('feedback')
        }
        df_new = pd.DataFrame.from_records([new_sample])
        df = pd.concat([df, df_new])
        df.to_csv(DATAPATH, index=False)


def image_to_text(image) -> str:

    # Step 1: Save uploaded file
    filename = image.name
    print(f'''uploaded: {filename}''')

    image_type = filename.split(".")[-1]
    print("Image type: " + image_type)
    bytes_data = image.getvalue()

    path = "dataset/raw_data/" + filename

    # Save bytes
    with open(path, 'wb') as f:
        f.write(bytes_data)

    # Step 2: Convert file to jpg-format
    print("Convert input to JPG format...")
    # Todo: Enable to upload multiple images!
    num_requests = 1
    random_str = get_random_string(5)

    if image_type == "pdf":
        # Convert pdf to image
        images = convert_from_path(path)

        # Save images to temporary file
        for i in range(len(images)):
            images[i].save("tmp/" + str(random_str) + str(i) + '.jpg', 'JPEG')
            images[i].close()

        num_requests = len(images)
    else:
        # Save images to temporary file
        image_pillow = Image.open(path)
        image_pillow = image_pillow.convert('RGB')
        image_pillow.save("tmp/" + str(random_str) + '0.jpg', 'JPEG')
        image_pillow.close()

    # Step 3: Call OCR Software
    print("Calling OCR API...")
    ocr_text = ocr(random_str, num_requests)

    # Remove the temporary files again
    for filename in glob.glob("tmp/" + random_str + "*"):
        os.remove(filename)

    # Step 4: Use GPT-3 to improve the text
    print("Calling GPT-3....")
    prompt = "Dieser Text wurde von einer automatischen Handschrifterkennung erfasst. " \
             "Passe die Fehler an: "
    total_input = prompt + '''"""''' + ocr_text + '''"""'''

    text = run_gpt3(total_input)
    text = text.strip()
    return text


def ocr(image_name: str, num_requests=1) -> str:
    output_text = []

    for i in range(num_requests):
        r = requests.post("https://api.mathpix.com/v3/text",
                          files={"file": open("tmp/" + image_name + str(i) + '.jpg', "rb")},
                          headers={
                              "app_id": APIs["ocr_app_id"],
                              "app_key": APIs["ocr_app_key"]
                          }
                          )
        output_text.append(r.json()["text"])

    total_output = " ".join(output_text)
    return total_output


def run_gpt3(prompt: str, engine="text-davinci-003", max_tokens=1000, error_tmp=None):
    openai.api_key = APIs["openai"]

    # create a completion
    while True:
        try:
            completion = openai.Completion.create(engine=engine, prompt=prompt, max_tokens=max_tokens)
            break
        except Exception as e:
            print(str(e))
            if error_tmp:
                error_tmp.error(str(e))
            time.sleep(5)
            if error_tmp:
                error_tmp.empty()

    # return the completion
    return completion.choices[0].text
