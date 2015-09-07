user_input=int(raw_input("Enter a positive integer: "))
for i in range(1,user_input+1):
	if user_input%i==0:
		print "{} is a divisor of {}".format(i,user_input)
	
