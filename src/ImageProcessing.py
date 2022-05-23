# from concurrent.futures import process
from Translating import *
from PIL import Image, ImageDraw, ImageFont
from PIL import features
import textwrap
import pyvips

title_font = ImageFont.truetype('./src/fonts/ArialUnicodeMS.ttf', 60)
hindi_font = ImageFont.truetype('./src/fonts/BalooTammudu2-VariableFont_wght.ttf', 60, layout_engine=ImageFont.LAYOUT_RAQM)

def processTranslatedImage(imagePath, engText, translatedText, savedImagePath):
    wrapper = textwrap.TextWrapper(width=25)
    word_list = wrapper.wrap(text=translatedText)
    translatedTextNew = ''
    for ii in word_list[:-1]:
        translatedTextNew = translatedTextNew + ii + '\n'
    translatedTextNew += word_list[-1]

    wrapper = textwrap.TextWrapper(width=25)
    word_list2 = wrapper.wrap(text=engText)
    engTextNew = ''
    for ii in word_list2[:-1]:
        engTextNew = engTextNew + ii + '\n'
    engTextNew += word_list2[-1]

    background = Image.open("./Images/backgroundimagereal.jpg")
    img = Image.open(imagePath)
    editable_background = ImageDraw.Draw(background)
    editable_background.text((1350, 200), engTextNew,
                             (0, 0, 0), font=title_font)
    editable_background.text(
        (1350, 800), translatedTextNew, (0, 0, 0), font=hindi_font)
    half = 1.7
    out = img.resize([int(half * s) for s in img.size])
    background.paste(out, (60, 60))
    newimage = background.save(savedImagePath, quality=95)
    # newimage.open()

    return background.save(savedImagePath, quality=95)


if __name__ == "__main__":
    # processTranslatedImage("./images/decision-book-images/image-001.jpg", "hallo",
    #                        "ఒక గ్రామంలో వివిధ వృత్తుల వారి మధ్య విభేదాలు వచ్చాయి.", "./testing/img.png")
    # print(features.check("raqm"))
    text = "ఒక గ్రామంలో వివిధ వృత్తుల వారి మధ్య విభేదాలు వచ్చాయి."
    output_file = "./Images/backgroundimagereal.jpg"
    image = pyvips.Image.text(text, width=800, height=500, font='Arial Unicode MS', dpi=96)
    image.write_to_file(output_file)
