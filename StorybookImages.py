from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os
import json 
import requests

booktext = ["My name is Simo.", "I have four friends."]


url = "https://platform.neuralspace.ai/api/translation/v1/translate"

headers = {}
headers["Accept"] = "application/json, text/plain, */*"
headers["authorization"] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDUxNjU3OTc0LCJkYXRhIjp7ImVtYWlsIjoic3ViaGF2ZWUyQGdtYWlsLmNvbSIsInJvbGUiOiJwcm92aWRlciIsImFwaWtleSI6ImZkOTg5YTcyLTJiZWUtNDFhNy04ZDY4LTdmYjQ0YzJlMjBiMSIsInJlZmVyZW5jZUtleSI6ImZkOTg5YTcyLTJiZWUtNDFhNy04ZDY4LTdmYjQ0YzJlMjBiMSIsInBsYW5UeXBlIjoiZGVmYXVsdCIsImNvdW50cnkiOiJVbml0ZWQgU3RhdGVzIG9mIEFtZXJpY2EgKHRoZSkifSwiaWF0IjoxNjQ1MTY1NDM3fQ.SG5vkRPNOGnka_tPrGHeyQ7aaIkBMOnM2kPzRpZYe6M"
headers["Content-Type"] = "application/json;charset=UTF-8"

data = """
{
    "text": "Hallo, how doing",
    "sourceLanguage":"en",
    "targetLanguage": "hi"}
"""


resp = requests.post(url, headers=headers, data=data)

response_dict = json.loads(resp.text)
print(response_dict["data"]["translated_text"])


path = "./Images/image1.png"
title_font = ImageFont.truetype('PlayfairDisplay-Regular.ttf', 60)

img1  = Image.open("./Images/image1.png") 


background = Image.open("./Images/backgroundimagereal.jpg")
editable_background = ImageDraw.Draw(background)
editable_background.text((1250,200), booktext[0], (0, 0, 0), font=title_font)
background.paste(img1, (100,50))
background.save('Images/pastedimage.jpg', quality=95)