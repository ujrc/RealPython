from random import choice
# lists of nouns, verbs, adjectives,prpositions and adverbs
nouns=["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
adjectives=["furry", "balding" ,"incredulous", "fragrant", "exuberant", "glistening"]
verbs=[ "kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
preposition=[ "against", "after", "into", "beneath", "upon", "for", "in", "like",
"over", "within"]
adverbs=[ "curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]
# function to make poem
def makePoem():

	noun1=choice(nouns)
	noun2=choice(nouns)
	noun3=choice(nouns)
	#Choose a distinct noun
	
	while noun1==noun2:
		noun2=choice(nouns)
	while noun1==noun3 or noun2==noun3:
		noun3=choice(nouns)
	
	adjective1=choice(adjectives)
	adjective2=choice(adjectives)
	adjective3=choice(adjectives)
	#choose a distinct adjective

	while adjective1== adjective2:
		adjective2=choice(adjectives)		
	while adjective2==adjective3 or adjective1==adjective3:
		adjective3=choice(adjectives)
	#choose a distinct verb 
	verb1=choice(verbs)
	verb2=choice(verbs)
	verb3=choice(verbs)
	while  verb1==verb2:
		verb2=choice(verbs)
	while verb2==verb3 or verb1==verb3:
		verb3=choice(verbs )
	
	preposition1=choice(preposition)
	preposition2=choice(preposition)
	#Choose a distinct preposition
	while preposition1== preposition2:
		preposition1=choice(preposition)
	adverb1=choice(adverbs)
	#choose between A/ An
	Article=""
	if  adjective1[0] in "aeiou": 
		Article+= "An"
	else:
		Article+="A"
	poem= "{} {} {}".format(Article,adjective1,noun1)
	poem+="\n"+poem+" {} {} the {} {} \n{}, the {} {}".format(verb1,preposition1,adjective2,noun2,adverb1,noun1,verb2)
	poem =poem+"\nthe {} {} {}  a {} {}".format(noun2,verb3,preposition2,adjective3, noun3)
	return poem
print makePoem()


