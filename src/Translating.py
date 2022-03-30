

from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os
import json 
import requests

booktext =  {
    'page1': 'My name is Simo.',
    'page2': 'I have four friends.'
}
# booktext = ["My name is Simo.", "I have four friends."]
translatedbooktext = [""]

url = "https://platform.neuralspace.ai/api/translation/v1/translate"

headers = {}
headers["Accept"] = "application/json, text/plain, */*"
headers["authorization"] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDg1OTIyOTk2LCJkYXRhIjp7ImVtYWlsIjoiaW5mb0BsaW5ndWlzdGljc2p1c3RpY2VsZWFndWUub3JnIiwicm9sZSI6InByb3ZpZGVyIiwiYXBpa2V5IjoiNzI5Njk2MTQtMWRlYS00YjhjLTljYjctYjFlYmQwYzQzMDI1IiwicmVmZXJlbmNlS2V5IjoiNzI5Njk2MTQtMWRlYS00YjhjLTljYjctYjFlYmQwYzQzMDI1IiwicGxhblR5cGUiOiJkZWZhdWx0IiwiY291bnRyeSI6IlVuaXRlZCBTdGF0ZXMifSwiaWF0IjoxNjQ4NTkxOTM5fQ.ATPJJTfIRcrFn8OrTiTYTcdrXm1bpx8OLY4jVKzBg_8"
headers["Content-Type"] = "application/json;charset=UTF-8"

data = f"""
{{
    "text": "{booktext['page1']}",
    "sourceLanguage":"en",
    "targetLanguage": "hi"
}}
"""
# print(data)
 
resp = requests.post(url, headers=headers, data=data)
print(resp.text)
# response_dict = json.loads(resp.text)
# translatedbooktext[0] = response_dict["data"]["translated_text"]
# print(translatedbooktext)
# print(response_dict["data"]["translated_text"])