# adds image processing capabilities
from PIL import Image
# will convert the image to text string
import pytesseract
from CreateBook import *
from CreatingPaths import * 

from PIL import Image, ImageEnhance

filename = './images/friends-full-book-images/friends-asb-FKB (1)-01.jpg'

def ExtractBookText(startingFilePath, length):
    output_files, input_files = createImagePath(startingFilePath, "any", length)
    eng_booktext_array_newline = []
    eng_booktext_array_raw = []

    for i in range (0,length-1):
        # assigning an image from the source path
        img = Image.open(input_files[i])
        # adding some sharpness and contrast to the image 
        enhancer1 = ImageEnhance.Sharpness(img)
        enhancer2 = ImageEnhance.Contrast(img)
        img_edit = enhancer1.enhance(20.0)
        img_edit = enhancer2.enhance(1.5)
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

        eng_booktext_array_raw.append(result2)

    return eng_booktext_array_raw

if __name__ == "__main__":
    akb_friends_text = ExtractBookText("./images/friends-full-book-images/friends-asb-FKB (1)-", 17)
    print(akb_friends_text)

