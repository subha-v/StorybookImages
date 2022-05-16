
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os
import json 
import requests
import time
import re
from SensitiveInfo import *

# # # DO NOT CHANGE # # #
url = "https://platform.neuralspace.ai/api/translation/v1/translate"

headers = {}
headers["Accept"] = "application/json, text/plain, */*"
headers["authorization"] = auth_token
headers["Content-Type"] = "application/json;charset=UTF-8"

# # # DO NOT CHANGE # # #

booktext = "My village had many problems. We made a long line to fetch water from one tap.  () We locked our houses early because of thieves.    ()"


def translate_book(bookArray, languageToken): 
    translatedbooktext = ""
    passedValue = bookArray
    data = f"""
    {{
        "text": "{passedValue}",
        "sourceLanguage":"en",
        "targetLanguage": "{languageToken}"
    }}
    """
    time.sleep(3)
    resp = requests.post(url, headers=headers, data=data)

    response_dict = json.loads(resp.text)
    print("translation: " + response_dict["data"]["translated_text"])
    translatedbooktext = response_dict["data"]["translated_text"]
    sentences = []
    
    sentences = translatedbooktext.split("()")
    print(sentences)

    sentences2 = bookArray.split("()")
    
    return sentences, sentences2

if __name__ == "__main__":
    translate_book(booktext, "ps")

