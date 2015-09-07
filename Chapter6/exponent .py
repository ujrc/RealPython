
#Temperature converter (Celius to Fahrenheit anf vice versa)

far= float(raw_input("Enter Degree in Fahrenheit: "))
def far_cel_converter(fahrenheit):
	Celsius=(fahrenheit-32)*5/9
	return Celsius

cel= float(raw_input("Enter Degree in Celisius: "))
def cel_far_converter(celsius):
	Farhenheit=celsius*9/5+32
	return Farhenheit
	
print "{} degrees F = {} degrees C" .format(far,far_cel_converter(far))

print "{} degrees C = {} degrees F ".format(cel,cel_far_converter(cel))


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

	
	
