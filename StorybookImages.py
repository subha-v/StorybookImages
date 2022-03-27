from PIL import Image
path = "./Images/image1.png"

try: 
    img  = Image.open("./Images/image1.png") 
    img.show()
except IOError:
    pass