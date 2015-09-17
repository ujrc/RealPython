my_file=open("poem.txt", "w") 
text="Hi there.This is a simple text file.If you can read me, congratulations! "
my_file.writelines(text)
my_file.close()
"""my_file=open ("poem.txt", "a")
lines="Read in the arw text file poem.txt fron the chapter 10 practice\
files and display each line by looping over them individually,\
the close the line; we'll discuss using file pathsin the next section\
but  now you can save your script in the same folder as the text file."

my_file.writelines(lines)
my_file.close()"""
my_in_file=open("poem.txt","r+")
lines="Read in the arw text file poem.txt fron the chapter 10 practice\
files and display each line by looping over them individually,\
the close the line; we'll discuss using file pathsin the next section\
but  now you can save your script in the same folder as the text file."
for line in my_in_file.readline():
	print line,
my_in_file.writelines(lines)

my_in_file.close()
my_in_file=open("poem.txt","r")
for line in my_in_file.readline():
	print line,
my_in_file.close()


#Exercices Chapter10

with open("poem.txt", "r") as my_in_file, open("output.txt","w") as my_output:
	for line in my_in_file.readlines():
		my_output.write(line)
		
with open("output.txt", "a") as my_output:
	letter="Write a text file output.txt thatcontains the same lines\
	as poem.txt by opening both files at the same time (in different\
	modes)and copying the original file over line-by-line;\
	do this using a loop and closing both files,	then repeat this \
	 exercise using the with keyword" 
	
	for line in letter:
		my_output.write(line)


with open("output.txt", "r") as my_output:
	for line in my_output.readlines():
		print line
		
		
	


