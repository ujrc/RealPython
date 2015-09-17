import os 
import csv

#Read and skip header
my_path="/home/jeanne/Desktop/Realpython/Chapter10Practicefiles"
with open(os.path.join(my_path,"pastimes.csv"), "rU") as output_file:
	file_reader=csv.reader(output_file)
	next(file_reader)
	for row in file_reader:
		
		print row
	
# display row as  a list of string 
my_path="/home/jeanne/Desktop/Realpython/Chapter10Practicefiles"# path for location of csv file
input_file_path=os.path.join(my_path,"pastimes.csv")
out_file_path=os.path.join(my_path,"categorized pastimes.csv")

with open(input_file_path,"rU") as input_file, open(out_file_path,"wb") as output_file:
	file_reader=csv.reader(input_file)#read csv file
	file_writer=csv.writer(output_file)# wrrite csv file
	next(file_reader) # skip header row
	file_writer.writerow(["Name", "Favorite Pastime", "Type of pastime"])# add new header row
	for row in file_reader:
		
		if row[1].lower().find("fighting")!=-1: # find word fighting in 'Favorite Pastime'
			row.append("Combat")
		else:
			row.append("Other")
		file_writer.writerow(row) # add new row to output
		print ",".join(row)
		
			
	
	
		
	
		
		
  
		
