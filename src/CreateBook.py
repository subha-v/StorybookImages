from Translating import *
from ImageProcessing import *
import os
import img2pdf

def CreateBook(bookArray, firstImageFilePath):
    translatedbookarray = translate_book(bookArray)
    filename_out_final = "./images/translated-book/page"
    filename_in = firstImageFilePath
    final_pdf_list = []

    for i in range (0,len(bookArray)-1):

        if(i == 0):
            filename_in_new = "./images/book-friends/image-001.jpg"
        elif(i == 10 ):
            filename_in = "./images/book-friends/image-010.jpg"
        elif(i > 10):
            filename_in = "./images/book-friends/image-010"
            filename_in_new = filename_in.rstrip(filename_in[-1]) + f'{i % 10}.jpg'
        else: 
            filename_in_new = filename_in.rstrip(filename_in[-1]) + f'{i + 1}.jpg'

        filename_out = filename_out_final + f'{i}.jpg'
        final_pdf_list.append(filename_out)

        processTranslatedImage(filename_in_new, bookArray[i], translatedbookarray[i], filename_out)
        #img.open()
       # img.convert('RGB')
      #  pdf = img.save("./translated-book.pdf", save_all=True, append_images=final_pdf_list)

   # return pdf

if __name__ == "__main__":
    friendsBook = ["My name is Simo.", "I have four friends.", "Their names are Zizo,  \n Lele, Sisa and Ayanda.", "My friend Zizo likes to play soccer.", "My friend Lele likes to swim.", "My friend Sisa likes to play hide-and-seek", "My friend Ayanda likes to read.", "Me? I like to do the things they like to do.", "I play soccer with Zizo.", "I swim with Lele.", "I play hide-and-seek with Sisa.", "Come, friend, what do you like?", "Come, play soccer with us.", "Come, swim with us.", "Come, play hide-and-seek with us.", "Come, read with us!"]
    CreateBook(friendsBook, "./images/book-friends/image-001" )
    