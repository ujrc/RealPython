from pyPdf import PdfFileReader, PdfFileWriter
import os

#1. Extract info from pdf file

path="/home/jeanne/Desktop/Realpython/Chapter12 practice files"
input_file=PdfFileReader(file(os.path.join(path,"The whistling gypsy.pdf"), "rb"))
title=input_file.getDocumentInfo().title
author=input_file.getDocumentInfo().author
pages=input_file.getNumPages()
print "{}\n{}\n{}\n".format(title,author,pages)


# 
path="/home/jeanne/Desktop/Realpython/Chapter12 practice files"
file_name=PdfFileReader(file(os.path.join(path,"The whistling gypsy.pdf"),"rb"))
output_file_name=os.path.join(path,"Output/The whistling gypsy.txt")

output_file=open(output_file_name,"wb")
for page_num in range(1,file_name.getNumPages()):
	text=file_name.getPage(page_num).extractText()
	text=text.replace(" ","\n")
	text=text.encode("utf-12")
	output_file.write(text)
output_file.close()

#
path="/home/jeanne/Desktop/Realpython/Chapter12 practice files"
input_file=PdfFileReader(file(os.path.join(path,"The whistling gypsy.pdf"),"rb"))
output_file_pdf=PdfFileWriter()

for page_num in range(0,input_file.getNumPages()):
	output_file_pdf.addPage(input_file.getPage(page_num))
	
output_file=file(os.path.join(path,"Output/The Whistling Gypsy.pdf"),"wb")
output_file_pdf.write(output_file)
output_file.close()





##
