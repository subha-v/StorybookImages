import cv2
import numpy as np
import os
import argparse
from glob import glob

from pathlib import Path

def extractImagesFromFile(inputFilename, outputDirectory):
    
    minWidth = 200
    minHeight = 200
    greenColor = (36, 255, 12)
    
    # Load image, grayscale, Otsu's threshold
    #inputFilename = "./images/translated-book/page2.jpg"
    #inputFilename = "./images/translated-book/page10.jpg"
    image = cv2.imread(inputFilename)
    original = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Find contours, obtain bounding box, extract and save ROI, rename images
    roi = 1
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(cnts) == 2:
        cnts = cnts[0]
    else:
         cnts[1]
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        if w >= minWidth and h >= minHeight:
            cv2.rectangle(image, (x, y), (x + w, y + h), greenColor, 2)
            ROI = original[y : y + h, x : x + w]
            if inputFilename[-6].isnumeric() :
                if inputFilename[-6] > str(0):
                    outImage = os.path.join(outputDirectory, f'image-0{inputFilename[-6:-4]}.jpg'.format(Path(inputFilename).stem, roi))
            else:
                outImage = os.path.join(outputDirectory, f'image-00{inputFilename[-5]}.jpg'.format(Path(inputFilename).stem, roi))
            cv2.imwrite(outImage, ROI)
            roi += 1

def main(files):

    outputDirectory = 'images/translated-book-images'

    # Create the output directory
    outputPath = Path.cwd() / outputDirectory
    outputPath.mkdir(exist_ok=True)

    for f in files:
        print("Prcessing {}".format(f))
        if Path(f).is_file():
            extractImagesFromFile(f, outputDirectory)
        else:
            print("Invalid file: {}".format(f))



if __name__ == "__main__":
    parser = argparse.ArgumentParser()  
    parser.add_argument("fileNames", nargs='*') 
    args = parser.parse_args()  
    fileNames = list()  
    for arg in args.fileNames:  
        fileNames += glob(arg)  
    main(fileNames)