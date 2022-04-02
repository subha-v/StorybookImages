# from concurrent.futures import process
from Translating import *
from PIL import Image, ImageDraw, ImageFont
import textwrap

title_font = ImageFont.truetype('./src/fonts/ArialUnicodeMS.ttf', 60)
hindi_font = ImageFont.truetype('./src/fonts/ArialUnicodeMS.ttf', 60)


def processTranslatedImage(imagePath, engText, translatedText, savedImagePath):
    wrapper = textwrap.TextWrapper(width=50) 
    word_list = wrapper.wrap(text=translatedText) 
    translatedTextNew = ''
    for ii in word_list[:-1]:
        translatedTextNew = translatedTextNew + ii + '\n'
    translatedTextNew += word_list[-1]

    background = Image.open("./Images/backgroundimagereal.jpg")
    img = Image.open(imagePath)
    editable_background = ImageDraw.Draw(background)
    editable_background.text((1350, 200), engText, (0, 0, 0), font=title_font)
    editable_background.text((1350, 600), translatedTextNew, (0, 0, 0), font=hindi_font)
    half = 1.7
    out = img.resize([int(half * s) for s in img.size])
    background.paste(out, (60, 60))
    newimage = background.save(savedImagePath, quality=95)
    # newimage.open()

    return background.save(savedImagePath, quality=95)

if __name__ == "__main__":
    processTranslatedImage("./images/book-friends/image-007.jpg", "hallo", "मेरा नाम सिमो है। मेरा नाम सिमो है। मेरा नाम सिमो है। मेरा नाम सिमो है।", "./testing/img.png")
