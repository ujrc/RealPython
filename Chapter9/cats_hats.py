
cats_has_hats=[]
rounds=100
cats=100
for Round in range(1,rounds+1):
	for cat in range(cats):
           # Only look at cats that are divisible by the round
		if cat% Round == 0:
			if cat not  in cats_has_hats:
				cats_has_hats.append(cat)
			else:
				cats_has_hats.remove(cat)

print cats_has_hats


