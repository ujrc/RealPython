
#Capital_list

from capitals import capitals_dict
import random
def guess_capital(state, capital):
		while True:
			guess = raw_input("Name the capital of {}  ".format(state.upper()))
			if guess == (capital.upper()):
				print "That's correct."
				break
			elif guess =="exit":
				print "Goodbye!"
				break
State = random.choice(capitals_dict.keys())
Capital = capitals_dict[State]
guess_capital(State, Capital)


