from fnmatch import translate
from src.Translating import *

def CreateBook(bookArray, firstImageFilePath):
    translatedbookarray = translate_book(bookArray)
    
    return 