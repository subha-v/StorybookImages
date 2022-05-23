import os
import sys
import re

# old_file_name = "./images/animalsrunaway-book/animalsrunaway-01.jpg"
# new_file_name = "./images/animalsrunaway-book/page-001.jpg"
# os.rename(old_file_name, new_file_name)
# print("Renamed files!")


# os.rename(, )


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    return [atoi(c) for c in re.split(r'(\d+)', text)]


i = 1

arrayOfFiles = os.listdir("./images/animalsrunaway-images/")
arrayOfFiles.sort(key=natural_keys)
# print("array of files: ", arrayOfFiles)

for file in os.listdir("./images/animalsrunaway-images"):
    if(i > 9):
        numbersEnd = f"0{i}"

    else:
        numbersEnd = f"00{i}"

    new_name = f"./images/animalsrunaway-book/image-{numbersEnd}.png"
    print(new_name)
    os.rename(file, new_name)

    i += 1
