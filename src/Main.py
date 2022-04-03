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
                                    prompt="What's your first image filepath: ")
    number_of_pages = simpledialog.askinteger(title="Test",
                                    prompt="How many pages are in your book:  ")
    language = simpledialog.askinteger(title="Test",
                                    prompt="What language:  ")                                

    # check it out

    booktext = ExtractBookText(first_image_filepath, number_of_pages)
    CreateBook(booktext, first_image_filepath)

