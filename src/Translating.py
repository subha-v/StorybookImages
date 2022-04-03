
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

booktext = ["My name is Simo.", "I have four friends."]


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

    # for i in range(0, 10):
    #     passedValue = bookArray[i]
    #     print("passed value:" + passedValue + "This is the i value: ", i)
    #     data = f"""
    #     {{
    #         "text": "{passedValue}",
    #         "sourceLanguage":"en",
    #         "targetLanguage": "hi"
    #     }}
    #     """
    #     time.sleep(3)
    #     resp = requests.post(url, headers=headers, data=data)

    #     response_dict = json.loads(resp.text)
    #     print("translation: " + response_dict["data"]["translated_text"])
    #     translatedbooktext.append(response_dict["data"]["translated_text"])
        
        # print(translatedbooktext)
        # translatedbooktext.append("उनके नाम ज़िज़ो, लेले, सीसा और अयंदा हैं।")

    # for i in range(10, len(bookArray)-1):
    #     passedValue = bookArray[i]
    #     print("We came to the new for loop")
    #     print("passed value:" + passedValue + "This is the i value: ", i)
    #     data = f"""
    #     {{
    #         "text": "{passedValue}",
    #         "sourceLanguage":"en",
    #         "targetLanguage": "hi"
    #     }}
    #     """
    #     resp = requests.post(url, headers=headers, data=data)
    #     response_dict = json.loads(resp.text)
    #     print("translation: " + response_dict["data"]["translated_text"])
    #     translatedbooktext.append(response_dict["data"]["translated_text"])

    # return translatedbooktext
    


if __name__ == "__main__":
    translate_book(booktext)


# data = f"""
# {{
#     "text": "{booktext[1]}",
#     "sourceLanguage":"en",
#     "targetLanguage": "hi"
# }}
# """
# resp = requests.post(url, headers=headers, data=data)
# response_dict = json.loads(resp.text)
# translatedbooktext[0] = response_dict["data"]["translated_text"]
# print(response_dict["data"]["translated_text"])