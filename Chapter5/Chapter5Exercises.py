
# data types
#exercise 1
mystring="123"
result=int (mystring)*3
print  " integer times 3 is :",result

#exercice #
my_str="12.34"
result=float(my_str)*4
print "float times 5 is: ",result
 
#exercise 3

my_int=12
my_float=45.6
print ("Integer and flaot side by side :",str(my_int)+str(my_float))

# Exercises on Streamline your print statements

#1
weight =0.2
animal="newt"
print weight," kg is the weight of the ", animal
print  str(weight)+" kg is the weight of the "+ animal

#2

print "{} kg is the weight of the {}".format(weight, animal)

#3
print "{0} kg is the weight of the ".format(weight, animal)

#4
print "{weight} kg is the weight of the {animal}".format(weight=0.2, animal="newt")

#exercise on Find a string in a string

#1 Find "a" in "AAA"
print "AAA".find("a")

#2 Find "2.0"

num=2.0
print ("version"+str(num)).find("2.0")

#3 FInd the name of a city in 
phrase =raw_input("Enter 5 cities names:")
print phrase.find("Miami")
