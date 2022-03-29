from Translating import *
from PIL import Image, ImageDraw, ImageFont

ooktext =  {
    'page1': 'My name is Simo.',
    'page2': 'I have four friends.'
}


path = "./Images/image1.png"
title_font = ImageFont.truetype('PlayfairDisplay-Regular.ttf', 60)
hindi_font = ImageFont.truetype('ArialUnicodeMS.ttf', 60)

img1  = Image.open("./Images/image1.png") 

background = Image.open("./Images/backgroundimagereal.jpg")
width, height = background.size
editable_background = ImageDraw.Draw(background)
editable_background.text((1600,200), booktext['page1'], (0, 0, 0), font=title_font)

# Calling translation function #

# editable_background.text((1250,600), translatedbooktext[0], (0, 0, 0), font=hindi_font)

# Placeholder Text for testing #
editable_background.text((1600,600), "मेरा नाम सिमो है।", (0, 0, 0), font=hindi_font)
# img1.thumbnail((height,height))
half = 1.3
out = img1.resize( [int(half * s) for s in img1.size] )
background.paste(out, (60,60))
background.save('Images/pastedimage.jpg', quality=95)