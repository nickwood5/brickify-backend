from openai import OpenAI
from brickify.keys import OPENAI_API_KEY

from time import time, sleep
import json

import brickify.common.utils as utils

hair_styles_map = utils.get_json("brickify/builder/styles/hair_styles.json")
hair_styles = "\n-".join(list(hair_styles_map.keys()))

class OpenAIClient:
    def __init__(self, api_key) -> None:
        self.client = OpenAI(api_key=api_key)

    def ask_model(self, model, messages):
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": messages
                    }
                ],
                max_tokens=1000,
                temperature=0,
            )
            #print(response)
            return response.choices[0].message.content
        except Exception as e:
            print(e)
            pass
        return None

    def ask_model_with_retry(self, model, messages):
        while (response := self.ask_model(model, messages)) is None:
            #print(response)
            sleep(1)
            pass
        return response


    def get_response(self, messages, model="gpt-4"):
        prompt_key = str(messages)
        if cached_response := get_from_cache(prompt_key):
            #print(f"Retrieved response from cache")

            return cached_response

        response = self.ask_model_with_retry(model, messages)

        update_cache(prompt_key, response)
        return response



    def gen(self, image_url):
        prompt = self.read_from_txt("/home/nickwood5/mysite/brickify/prompts/general")
        messages = [
            {"type": "text", "text": prompt},
            {
                "type": "image_url",
                "image_url": {
                    "url": image_url,
                    "detail": "high",
                }
            },
        ]

        return self.get_response(messages, "gpt-4-vision-preview")

    def get_closest(self, input, options):

        options_str = "\n".join([f"{i+1}: {option}" for i, option in enumerate(options)])

        prompt = f"""
    Input: {input}

    Considering above, choose the option from the following that best matches the description. If none of them match, choose the closest match
    {options_str}

    Respond with ONLY a choice by number, with no added description. You cannot respond with None of the above \
    """
        #print(prompt)
        index = self.get_response([{"type": "text", "text": prompt}])
        try:
            res = options[int(index)-1]
        except:
            res = None

        return res

    def read_from_txt(self, filename):
        with open(f"{filename}.txt", 'r') as file:
            file_contents = file.read()

        return file_contents

    def beard(self, description):
        facial_hair_styles_map = get_json("/home/nickwood5/mysite/brickify/prompt_configs/facial_hair_styles.json")
        facial_hair_styles_options_string = ", ".join(list(facial_hair_styles_map))

        prompt = self.read_from_txt("/home/nickwood5/mysite/brickify/prompts/beard").format(description, facial_hair_styles_options_string)

        messages = [
            {"type": "text", "text": prompt}
        ]
        return self.get_response(messages)

    def hair_from_image(self, image_url):
        prompt = self.read_from_txt("/home/nickwood5/mysite/brickify/prompts/hair")
        prompt = prompt.format(hair_styles)

        messages = [
            {"type": "text", "text": prompt},
            {
                "type": "image_url",
                "image_url": {
                    "url": image_url,
                    "detail": "high",
                }
            },
        ]
        return self.get_response(messages, "gpt-4-vision-preview")



def get_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

cache_path = "brickify/builder/cached_gpt4_responses.json"

def update_cache(key, value):
    cache = get_json(cache_path)

    cache[key] = value

    with open(cache_path, 'w') as f:
        json.dump(cache, f)



def get_from_cache(key):
    cache = get_json(cache_path)

    value = cache.get(key)
    return value

class Model:
    GPT_4 = "gpt-4"
    GPT_4_VISION = "gpt-4-vision-preview"

client = OpenAIClient(api_key=OPENAI_API_KEY)