import csv
from PIL import Image
from pdf2image import convert_from_path, convert_from_bytes
import pytesseract
import sys
import os
###
#This proof of concept assumes a adequate level of scan quality. A future iteration might include image pre-processing
#Which could involve applying gaussian blur, increased constrast, grayscale, etc.
###

#set executable location to be used when OCRing image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# get file name from user argument file name given
fileName = str("./" + sys.argv[1])

#store PILs from PDFs
pdfPages = convert_from_path(fileName, poppler_path = r'C:\Program Files\poppler-0.90.1\bin')

#store/count pages starting with 1
pageNum = 1

#iterate over each page
for page in pdfPages:
    #set up filename to be stored
    fileNameStored = "pdfPage" + str(pageNum) + ".jpg"

    #save PIL to actual jpg image
    page.save(fileNameStored, 'JPEG')

    #counter for pages incremented
    pageNum += 1

#set up file to be written to
with open('out.csv', 'w') as fileWrite:

    #use csv package to write with default comma delimiter
    writer = csv.writer(fileWrite)

    #for each image file (each page)
    for i in range(1, pageNum):

        #OCR the image (this includes newline characters used in csv writing)
        text = str(pytesseract.image_to_string(Image.open("pdfPage" + str(i) + ".jpg")))

        #set up individual lines of page
        textSplitLines = text.split("\n")

        #write to the csv file (csv writer advances to next line when encountering a \n)
        for line in textSplitLines:
            writer.writerow([line])

    #close the file after done writing
    fileWrite.close()

#print completion message to screen
print("Operation complete. Contents of your PDF can be found in the out.csv file.")


