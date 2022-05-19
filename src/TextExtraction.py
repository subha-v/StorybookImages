# adds image processing capabilities
from PIL import Image
# will convert the image to text string
import pytesseract
from CreateBook import *
from CreatingPaths import * 
from string import punctuation

from PIL import Image, ImageEnhance

filename = './images/friends-full-book-images/friends-asb-FKB (1)-01.jpg'

def ExtractBookText(startingFilePath, length):
    output_files, input_files = createImagePath(startingFilePath, "any", length)
    eng_booktext_array_raw = []

    for i in range (0,length-1):
        # assigning an image from the source path
        img = Image.open(input_files[i])
        # adding some sharpness and contrast to the image 
        enhancer1 = ImageEnhance.Sharpness(img)
        enhancer2 = ImageEnhance.Contrast(img)
        img_edit = enhancer1.enhance(20.0)
        #img_edit = enhancer2.enhance(1.5)
        # save the new image
        img_edit.save("edited_image.png")
        # converts the image to result and saves it into result variable
        result = pytesseract.image_to_string(img)

        l = ['0','1','2','3','4','5','6','7','8','9', '/', '“', '”', '@', '|', '\\', ')', '_']
        # punctuationStuff = set(punctuation)
        print("Before punctuation and other stuff Removal: ", result)
        st_res=""
        for ch in result:
            if ch not in l:
                st_res+=ch

        random_string = '''I

ms
  
i j ;
'''
        st_res.replace(random_string, '')


        print("After punctuation and other stuff removal: ", st_res)

        result2 = st_res.replace("\n", " ")
        result2 = result2 + "()"
        print("Before: " + result2)
        result2 = result2.replace("   ()", " ()", 1)
        print("After: " + result2)
        eng_booktext_array_raw.append(result2)

    delimiter = ' '
        # Convert list of items to a string value
    final_str = delimiter.join(map(str, eng_booktext_array_raw))

    return final_str

if __name__ == "__main__":
    array, list = ExtractBookText("./images/disagreement-book/page-", 8)
    print(array)

