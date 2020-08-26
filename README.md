# PyPDFOCR
This project uses PyPDF2Image and Tesseract to read PDFs, convert to images, and write text content to a CSV file.

## Installation disclaimer
This program uses machine-specific paths and installations.
You would need to install pillow, pypdf2image, pytesseract, tesseract-ocr, and poppler locally and change the paths on lines 9 and 15 to use this project locally.

## Usage
run the command `python main.py <pdf file path>`
The program will generate the converted JPEG files as well as a CSV with the context arranged line by line approximating the original PDF.
