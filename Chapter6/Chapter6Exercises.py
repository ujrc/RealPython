
from __future__ import division

#Division 
num1=4
num2=8
# Before including from __future__ import division
print num1/num2 # answer=0

#after including from __future__ import division
print num1/num2 #answer =1/2

#Functions
#1 Cube  of  a number
def cube (number):
	result=number**3
	return result
print cube(5)
print cube(78)

#2 Function to perform multplication 
def multiply(num1,num2):
	return num1*num2
Product= multiply(2,5)
print Product


#Run in circle (for loop and while loop
#1 For to display 2 thru 10

for num in range(2,11):
	print num,
	
print 
#2 While loop
n=2
while (n<=10):
	print n,
	n+=1
print 
	
#3 Function to double a given number

def doubles(num1):
	for i in range(3):
		num1*=2
		print num1,		
doubles(2)
		
	
