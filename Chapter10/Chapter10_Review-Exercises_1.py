
# 1.read in poem.txt
my_file=open("poem.txt","rb")
for line in my_file.readlines():
	print line
my_file.close()
	 
	 
#2.Read files using with keyword
with open("poem.txt","rb") as my_files:
	for line in my_files.readlines():
		print line
	
# copy contents of poem.txt into output.txt
input_files=open("poem.txt","rb")
output_files=open("output.txt","wb")
for line in input_files.readline():
	output_files.write(line)
	print line,
output_files.close()
input_files.close()

with open("poem.txt","rb") as input_files, open("output.txt","wb") as output_files:
	for line in input_files.readline():
		output_files.write(line)
		

#4 Append text to output.txt	
with open ("output.txt","a+") as output_file:
	new_line="This is text will added to whatever is in output.txt file"
	output_file.write(new_line)
	for line in output_file:
		print line,
	
