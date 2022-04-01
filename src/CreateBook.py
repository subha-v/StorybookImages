from venv import create
from Translating import *
from ImageProcessing import *
import os
from fpdf import FPDF
from os import listdir
from CreatingPaths import *
def CreateBook(bookArray, firstImageFilePath):
    translatedbookarray = translate_book(bookArray)
    filename_out_final = "./images/translated-book/page"
    
    final_pdf_list = []
    output_file_list, input_file_list = createImagePath(firstImageFilePath, filename_out_final, 18)

    for i in range(0,len(bookArray)-1):
        processTranslatedImage(input_file_list[i], bookArray[i], translatedbookarray[i], output_file_list[i])
 

    return final_pdf_list

if __name__ == "__main__":
    friendsBook = ["My name is Simo.", "I have four friends.", "Their names are Zizo,  \n Lele, Sisa and Ayanda.", "My friend Zizo likes to play soccer.", "My friend Lele likes to swim.", "My friend Sisa likes to play hide-and-seek", "My friend Ayanda likes to read.", "Me? I like to do the things they like to do.", "I play soccer with Zizo.", "I swim with Lele.", "I play hide-and-seek with Sisa.", "Come, friend, what do you like?", "Come, play soccer with us.", "Come, swim with us.", "Come, play hide-and-seek with us.", "Come, read with us!"]
    pdf_list = CreateBook(friendsBook, "./images/book-friends/image-" )
    dirname = "./images/translated-book"
    list_images = (listdir(dirname))
    new_list = []

    for i in range (0,len(list_images)-1):
        new_list.append("./images/translated-book/" + list_images[i])


    print(pdf_list)
    pdf = FPDF()
    # imagelist is the list with all image filenames
    for image in new_list:
        pdf.add_page()
        pdf.image(image,0,0,210,297)
    pdf.output("yourfile.pdf", "F")
