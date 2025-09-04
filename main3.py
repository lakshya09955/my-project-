# This script merges multiple PDF files into a single PDF file using PyPDF2.
from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs=[]
n=int(input("How many PDFs do you want to merge?\n"))

for i in range(0,n):
    name=input(f"Enter the name of PDF {i+1}:\n")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()