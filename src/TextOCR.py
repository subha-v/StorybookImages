# adds image processing capabilities
from PIL import Image
# will convert the image to text string
import pytesseract

filename = './images/friends-full-book-images/friends-asb-FKB (1)-01.jpg'

# adds more image processing capabilities
from PIL import Image, ImageEnhance
# assigning an image from the source path
img = Image.open(filename)
# adding some sharpness and contrast to the image 
enhancer1 = ImageEnhance.Sharpness(img)
enhancer2 = ImageEnhance.Contrast(img)
img_edit = enhancer1.enhance(20.0)
img_edit = enhancer2.enhance(1.5)
# save the new image
img_edit.save("edited_image.png")
# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img_edit)
print("Result: " + result)