from random import randint
#chapter 8 if /elif statements
string= raw_input(" Enter a string: ")
if (len(string)>5):
	print "{} is greater than 5".format(len(string))
elif(len(string)==5):
	print "{} is equal to  5".format(len(string))
	
else:
	print " {} is les s than 5".format(len(string))
	
#Break and continue

#1 while and break
user_input=raw_input("Enter q or Q:  ")
while (True):
	if (user_input in "qQ"):
			user_input=raw_input("Enter q or Q:  ")
	else:
		break
	
#2 for and continue

for num in range(1,51):
	if(num%3==0):
		continue
	else:
		print num,
		
		
#Exception handling
while  True:
	try:
		numbers=int(raw_input("Enter an integer: "))
	 	print numbers 
		break

	except ValueError:
		print "Try again"
		continue 
 
 # 1 return random die 
random_number =randint(1,6)		
print random_number 

#2
trials=10000
flips=0
for i in range(0,10000):
	flips+=randint(1,6)
	average=flips/trials
print "The average of {} throws is {}".format(trials, average)





	
	
