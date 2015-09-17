import os 

Path="/home/jeanne/Desktop/Realpython/Chapter10Practicefiles/littlepics"
for current_folder,subflders, file_names in os.walk(Path):
	for file_name in file_names:
		full_path=os.path.join(current_folder, file_name)
		file_size=os.path.getsize(full_path)
		if file_size<2000 and file_name.lower().endswith(".jpg"):
			os.remove(full_path)
			print full_path
		
		
