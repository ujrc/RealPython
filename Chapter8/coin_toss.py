from __future__ import division
from random import randint
	
trials=10000
flips=0
for trial in range(trials):
	initial_flip = randint(0, 1)
	flips += 1
	while randint(0,1)==initial_flip:
		flips+=1
	else:
		flips+=1
print flips/trials
		

	



