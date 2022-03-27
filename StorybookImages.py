from PIL import Image
import numpy as np

path = "./Images/image1.png"

img  = Image.open("./Images/image1.png") 
# img.show()

background = Image.open("./Images/backgroundimagereal.jpg")
background.paste(img)
background.save('Images/pastedimage.jpg', quality=95)