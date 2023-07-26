import os
import glob

import random
import string
import json

import requests
import openai
from openai.error import InvalidRequestError
import time

from pdf2image import convert_from_path
from PIL import Image
from pathlib import Path

PACKAGE_ROOT = str(Path(__package__).absolute())
from aaw.globals import APIs, STRINGS


def create_dataset():
    # Create folder for raw images
    raw_dir = "raw_data"
    p_sub = Path(raw_dir)
    p_sub.mkdir(parents=True, exist_ok=True)

    # Create folder for temporary data
    tmp_dir = "tmp"
    p_tmp = Path(tmp_dir)
    p_tmp.mkdir(parents=True, exist_ok=True)


def get_random_string(length) -> str:
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def image_to_text(image):
    # Step 1: Save uploaded file
    filename = image.name
    print(f'''uploaded: {filename}''')

    image_type = filename.split(".")[-1]
    print("Image type: " + image_type)
    bytes_data = image.getvalue()

    path = "raw_data/" + filename

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

    text, error_msg = run_gpt(total_input, engine="text-davinci-003")
    text = text.strip()
    return text, error_msg


def ocr(image_name: str, num_requests=1) -> str:
    output_text = []

    # Very important that Mathpix does not save the data
    options_json = json.dumps({"metadata": {"improve_mathpix": False}})

    for i in range(num_requests):
        r = requests.post("https://api.mathpix.com/v3/text",
                          files={"file": open("tmp/" + image_name + str(i) + '.jpg', "rb")},
                          data={"options_json": options_json},
                          headers={
                              "app_id": APIs["ocr_app_id"],
                              "app_key": APIs["ocr_app_key"],
                          },
                          )
        output_text.append(r.json()["text"])

    total_output = " ".join(output_text)
    return total_output


def run_gpt(prompt: str, engine="text-davinci-003", max_tokens=1000, error_tmp=None):
    print("using engine " + engine)

    openai.api_key = APIs["openai"]

    exception = None
    # create a completion
    for i in range(10):
        try:
            if engine.startswith("text-davinci"):
                return run_gpt3(engine=engine, prompt=prompt, max_tokens=max_tokens), None
            elif engine.startswith("gpt-"):
                return run_chatgpt(engine=engine, prompt=prompt, max_tokens=max_tokens), None
            else:
                print("Unknown engine " + engine + "!")
                return "", None
        except InvalidRequestError as ire:
            # If this happens directly stop trying and return
            print("####  Invalid Request!  ####")
            print(ire)
            if error_tmp:
                error_tmp.error(STRINGS["PROCESS_ERROR"] + str(ire))
            return "", ire
        except Exception as e:
            # For all other exceptions, try multiple times
            print("#####" + str(e) + "#############")
            if error_tmp:
                error_tmp.error(str(e))
            time.sleep(5)
            if error_tmp:
                error_tmp.empty()
            exception = e

    return "", exception


def run_gpt3(prompt: str, engine="text-davinci-003", max_tokens=1000):
    completion = openai.Completion.create(engine=engine, prompt=prompt, max_tokens=max_tokens)
    # return the completion
    return completion.choices[0].text


def run_chatgpt(prompt: str, engine="gpt-3.5-turbo", max_tokens=1000):
    completion = openai.ChatCompletion.create(
        model=engine,
        messages=[
            # {"role": "system", "content": "You are a helpful teacher."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion['choices'][0]['message']['content']
