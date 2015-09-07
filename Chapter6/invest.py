#Track investments
#amount=float(raw_input("Princial amount: "))
#rate=float(raw_input( "annual rate of return: "))
#time=int(raw_input("Time: "))
def invest(amount ,rate,time):
	print "principal amount: {}".format(amount)
	print "annual rate retun: {}".format(rate)
	Amount=0
	for i in range(1,time+1):
		Amount=amount*(1+rate)**i
		print "Yearr {} : {}".format(i,Amount)
invest( 100, 0.05,8)
invest(2000,0.025,5)

	
	
