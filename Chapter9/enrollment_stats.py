
universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

def enrollment_stats(Universities):
	university_name=[]
	enrolled_students=[]
	tuition_fees=[]
	for university in Universities:
		university_name.append(university[0])
		enrolled_students.append(university[1])
		tuition_fees.append(university[2])
	return enrolled_students ,tuition_fees

students_tuition=enrollment_stats (universities)

Students=students_tuition[0]
tuition=students_tuition[1]

def mean (values):
# Mean of a list
	total=0
	if values=="":
		return "No value in list"
	for i in  range(len(values)):
		total+=values[i]
	return total/len(values)


def median(List):
	#median of a list
	my_list=sorted(List)
	l=len(List)
	if l%2!=0:
		return my_list[l/2]
	else:
		return (my_list[(l/2)+(l/2)-1]/2.0)
		
def Sum_All(myList):
	#sum of items in list
	Sum=0
	for n in  range(len(myList)):
		Sum+=myList[n]
	return Sum	

print "*****************************\n\
Total students:  {}".format(Sum_All(Students))
print "Total tuition:  $ {}\n\n".format(Sum_All(tuition))
print "Student mean: {} ".format(mean(Students))
print "Student median: {}\n\n".format(median(Students))
print "Tuition mean:  $ {}".format(mean(tuition))
print "Tuition mdian: $ {}\n*****************************\
".format(median(tuition))
	

