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
headers["authorization"] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDUxNjU3OTc0LCJkYXRhIjp7ImVtYWlsIjoic3ViaGF2ZWUyQGdtYWlsLmNvbSIsInJvbGUiOiJwcm92aWRlciIsImFwaWtleSI6ImZkOTg5YTcyLTJiZWUtNDFhNy04ZDY4LTdmYjQ0YzJlMjBiMSIsInJlZmVyZW5jZUtleSI6ImZkOTg5YTcyLTJiZWUtNDFhNy04ZDY4LTdmYjQ0YzJlMjBiMSIsInBsYW5UeXBlIjoiZGVmYXVsdCIsImNvdW50cnkiOiJVbml0ZWQgU3RhdGVzIG9mIEFtZXJpY2EgKHRoZSkifSwiaWF0IjoxNjQ1MTY1NDM3fQ.SG5vkRPNOGnka_tPrGHeyQ7aaIkBMOnM2kPzRpZYe6M"
headers["Content-Type"] = "application/json;charset=UTF-8"


data = """
{
    "text": "My name is Simo.",
    "sourceLanguage":"en",
    "targetLanguage": "hi"
}
"""

 
# resp = requests.post(url, headers=headers, data=data)

# response_dict = json.loads(resp.text)
# translatedbooktext[0] = response_dict["data"]["translated_text"]
# print(translatedbooktext)
# print(response_dict["data"]["translated_text"])
