import glob
import os 


#Display full path of files and folder within another folder
my_path="/home/jeanne/Desktop/Realpython/Chapter10Practicefiles/Images"
my_file=os.listdir(my_path)
for file_name in my_file:
	full_path=os.path.join( my_path, file_name)
	print full_path
print 

#Display full path of files with a specific extension
available_files=os.path.join(my_path,"*.png")
for files in glob.glob(available_files):
	print files,
print 
			

#Rename files

for currentfolder, subfolders,file_names in os.walk(my_path):
	for file_name in file_names:
		
		full_path=os.path.join(currentfolder,file_name)
		new_file_name=full_path[0:len(full_path)-4]+".jpg"
		os.rename(full_path,new_file_name)
		new_file =full_path
		print (new_file_name)
		print os.path.exists(new_file_name)
	
		
		
		




	
