from concurrent.futures import process
from Translating import *
from PIL import Image, ImageDraw, ImageFont

title_font = ImageFont.truetype('./src/fonts/ArialUnicodeMS.ttf', 60)
hindi_font = ImageFont.truetype('./src/fonts/ArialUnicodeMS.ttf', 60)


def processTranslatedImage(imagePath, engText, translatedText):
    background = Image.open("./Images/backgroundimagereal.jpg")
    img = Image.open(imagePath)
    width, height = background.size
    editable_background = ImageDraw.Draw(background)
    editable_background.text((1600, 200), engText, (0, 0, 0), font=title_font)
    editable_background.text((1600, 600), translatedText, (0, 0, 0), font=hindi_font)
    half = 1.7
    out = img.resize([int(half * s) for s in img.size])
    background.paste(out, (60, 60))
    newimage = background.save('Images/pastedimage.jpg', quality=95)

    return newimage

if __name__ == "__main__":
    processTranslatedImage("./images/book-friends/image-007.jpg", "hallo", "मेरा नाम सिमो है।")



# path = "./Images/image1.png"

# img1 = Image.open("./Images/image1.png")

# background = Image.open("./Images/backgroundimagereal.jpg")
# width, height = background.size
# editable_background = ImageDraw.Draw(background)
# editable_background.text(
#     (1600, 200), booktext['page1'], (0, 0, 0), font=title_font)

# # Calling translation function #

# # editable_background.text((1250,600), translatedbooktext[0], (0, 0, 0), font=hindi_font)

# # Placeholder Text for testing #
# editable_background.text(
#     (1600, 600), "मेरा नाम सिमो है।", (0, 0, 0), font=hindi_font)
# # img1.thumbnail((height,height))
# half = 1.3
# out = img1.resize([int(half * s) for s in img1.size])
# background.paste(out, (60, 60))
# background.save('Images/pastedimage.jpg', quality=95)
