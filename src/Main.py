from TextExtraction import *
from CreateBook import *
from CreatingPaths import *
from Translating import *
import tkinter as tk
from tkinter import simpledialog

if __name__ == "__main__":
    ROOT = tk.Tk()

    ROOT.withdraw()
    
    # the input dialog
    first_image_filepath = simpledialog.askstring(title="Test",
                                    prompt="What is the first image of your book's filepath?: ")
    first_image_filepath2 = simpledialog.askstring(title="Test",
                                    prompt="What is the first image of your images flepath?: ")
    number_of_pages = simpledialog.askinteger(title="Test",
                                    prompt="How many pages are in your book?:  ")
    language = simpledialog.askstring(title="Test",
                                    prompt="What language code is there for your book?:  ")                                

    # check it out
    print(first_image_filepath)
    booktext = ExtractBookText(first_image_filepath, number_of_pages)
    pdf_list = CreateBook(booktext, first_image_filepath2, language)

    dirname = "./images/translated-book"
    list_images = (listdir(dirname))

    new_list = []

    for i in range (0,len(list_images)-1):
        new_list.append("./images/translated-book/" + list_images[i])

    print(new_list)

    # this makes it in letterformat so it's horizontal not vertical
    pdf = FPDF('L', 'mm', 'A4')
    # imagelist is the list with all image filenames
    for image in pdf_list:
        pdf.add_page()
        #the 300 and 250 is the size for the iamge to be blown up to
        pdf.image(image,0,0,300,225)
    pdf.output("yourfile3.pdf", "F")

