#create a list
deserts=["ice cream","cookies"]
deserts.sort() # sort the list
print "Index of ice scream:",deserts.index("ice cream")
food =[]
food.extend(deserts)# copy deserts into food
food.extend(["broccoli","turnips"]) # add more items to food list 

print "Items in deserts list:{}\nItems in food list:{} " .format(deserts, food)

food.remove("cookies") #Remove item from the list
print food[:2]
breakfast= "cookies,cookies,cookies"
breakfast=breakfast.split(" ")# convert a string into a list
print "Items in breakfast: ", breakfast

def list_numbers(List):
	for n in List:
		if n in range(1,21):
			print n,
list_numbers([2, 4, 8, 16, 32, 64]) 


#tuple

cardinal_nums=("first","second","third")
print cardinal_nums[1]
pos1, pos2,pos3=("first","second","third")
print pos1
print pos2
print pos3

# Dictionary
birthdays={}
birthdays["Luke Skywalker"]="5/24/19"
birthdays["Obi-Wan Kenobi"]="3/11/57"
birthdays["Darth Vader"]="4/1/41"
if "Yoda" not in birthdays :
	birthdays["Yoda"]=" "
	
if "Darth Vader" not in birthdays:
	birthdays["Darth Vader"]=" "
del(birthdays["Darth Vader"])
	
print birthdays

new_birthday = dict([("Luke Skywalker","5/24/19"),("Obi-Wan Kenobi","3/11/57"),("Darth Vader","4/1/41"),("Yoda"," ")])
# for the following syntax no quotes around keys as keys are made of more than on word it's not a valid syntax
#birthday = dict(Luke Skywalker="5/24/19",Obi-Wan Kenobi="3/11/57",Darth Vader="4/1/41",Yoda =" ")

print new_birthday

