
from PIL import Image
# will convert the image to text string
import pytesseract
from CreateBook import *
from CreatingPaths import * 
from PIL import Image, ImageEnhance

      # assigning an image from the source path
img = Image.open("./images/decision-book/page-007.jpg")
# adding some sharpness and contrast to the image 
enhancer1 = ImageEnhance.Sharpness(img)
enhancer2 = ImageEnhance.Contrast(img)
img_edit = enhancer1.enhance(20.0)
# img_edit = enhancer2.enhance(1.5)
# save the new image
img_edit.save("edited_image.png")
# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img_edit)

l = ['0','1','2','3','4','5','6','7','8','9', '/']

st_res=""
for ch in result:
    if ch not in l:
        st_res+=ch

result2 = st_res.replace("\n", " ")
result2 = result2 + "()"
print("BEfore: " + result2)
result2 = result2.replace("   ()", " ()", 1)
print("After: " + result2)
