import os 
from pyPdf import PdfFileReader, PdfFileWriter
path="/home/jeanne/Desktop/Realpython/Chapter12 practice files"
input1_file=PdfFileReader(file(os.path.join(path," The Emperor.pdf"),"rb"))
input2_file=PdfFileReader(file(os.path.join(path,"The Emperor cover sheet.pdf"),"rb"))

output_pdf=PdfFileWriter()


for page_num in range(0, input2_file.getNumPages()): # add the cover to the  output PdfFileWriter 
	page = input2_file.getPage(page_num)
	output_pdf.addPage(page)
	
for page_num in range(0, input1_file.getNumPages()):# Add Emperor to the output PdfFileWriter
	page = input1_file.getPage(page_num)
	output_pdf.addPage(page)
	
output_file=file(os.path.join(path, "Output/The Covered Emperor.pdf"),"wb")

output_pdf.write(output_file)



