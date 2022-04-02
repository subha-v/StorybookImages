
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os
import json 
import requests

# # # DO NOT CHANGE # # #
url = "https://platform.neuralspace.ai/api/translation/v1/translate"

headers = {}
headers["Accept"] = "application/json, text/plain, */*"
headers["authorization"] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDg1OTIyOTk2LCJkYXRhIjp7ImVtYWlsIjoiaW5mb0BsaW5ndWlzdGljc2p1c3RpY2VsZWFndWUub3JnIiwicm9sZSI6InByb3ZpZGVyIiwiYXBpa2V5IjoiNzI5Njk2MTQtMWRlYS00YjhjLTljYjctYjFlYmQwYzQzMDI1IiwicmVmZXJlbmNlS2V5IjoiNzI5Njk2MTQtMWRlYS00YjhjLTljYjctYjFlYmQwYzQzMDI1IiwicGxhblR5cGUiOiJkZWZhdWx0IiwiY291bnRyeSI6IlVuaXRlZCBTdGF0ZXMifSwiaWF0IjoxNjQ4NTkxOTM5fQ.ATPJJTfIRcrFn8OrTiTYTcdrXm1bpx8OLY4jVKzBg_8"
headers["Content-Type"] = "application/json;charset=UTF-8"

# # # DO NOT CHANGE # # #

booktext = ["My name is Simo.", "I have four friends."]


def translate_book(bookArray): 
    translatedbooktext = []
    for i in range(len(bookArray)-1):
        passedValue = bookArray[i]
        print("passed value:" + passedValue)
        data = f"""
        {{
            "text": "{passedValue}",
            "sourceLanguage":"en",
            "targetLanguage": "hi"
        }}
        """
        # resp = requests.post(url, headers=headers, data=data)
        # response_dict = json.loads(resp.text)
        # print("translation: " + response_dict["data"]["translated_text"])
        # translatedbooktext.append(response_dict["data"]["translated_text"])
        translatedbooktext.append("उनके नाम ज़िज़ो, लेले, सीसा और अयंदा हैं।")
        # print(translatedbooktext)

    return translatedbooktext

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