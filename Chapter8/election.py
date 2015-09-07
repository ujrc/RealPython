#Probability of winning election

from __future__ import division
from random import random

totalA=0
totalB=0

trials=10000
for trial in range(0,trials):
	winA=0
	winB=0
  # probability of both A and B in region 1  
	if(random()< .87):		
		winA+=1
	else:
		winB+=1
#probability of both A and B n region 2
	if random()< .65:
		winA+=1
	else:
		winB+=1
#probability of both A and B in region 3
	if(random()< .17):
		winA+=1
	else:
		winB+=1
#Overall outcome from election in 3 regions
	if winA>winB:
		totalA+=1
	else:
		totalB+=1		
print "probability of B wins: ",totalB/trials 
print "probability of A  wins: ",totalA/trials
# teh winner

if totalB/trials>totalA/trial:
	print "B is the winner"
else:
	print"canditate A wins the election!"
	



