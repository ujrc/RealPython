import csv, os


#Create csv file
path="/home/jeanne/Desktop/Realpython/Chapter10Practicefiles"

with open (os.path.join(path,"score.csv"),"rU") as Files:
	high_scores={}
	for name,score in csv.reader(Files):#Read and loop through the file
		if name in high_scores:
			if(score>high_scores[name]):#Choose high score for a given name
				high_scores[name]=score
		else:
			high_scores[name]=score	
	for name in sorted(high_scores):
		print name, high_scores[name]



