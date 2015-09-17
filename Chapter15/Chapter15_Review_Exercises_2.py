from numpy import array, arange,vstack,dot,random
from matplotlib import pyplot as plt
from numpy import array, arange,vstack,dot,random
from matplotlib import pyplot as plt
import os
import csv

plt.plot([1,3,5,7,9,11],[0,2,4,6,8,10])
plt.show()

plt.plot([1,2,3,4,5,6,7],[80,81,77,70,68,66,76], "y-*")
plt.plot([80,81,77,70,68,66,76], "c-*")

plt.title("Weekly temp")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.axis([0,10,0,82])
plt.show()

plt.plot(arange(1,100,5))
plt.show()

plt.plot([1,2,3,4,5,6,7,8],[2,4,6,8,10,12,14,16])

plt.plot([2,4,6,8,10,12,14,16], "y-*")
plt.show()

plt.plot(arange(3,60,3), "g*")
plt.show()

hours=arange(1,16)
temperature=arange(1,16)
plt.plot(hours, temperature**2, "r.", hours, temperature, "g-x")
plt.axis([0,20,0,400])
plt.title("Doube plots")
plt.xlabel("hours")
plt.ylabel("raise of Temp per hour")
plt.legend(("hours","temperature"), loc=2)
plt.show()

days=arange(1,14)
learners=arange(15,28)
plt.plot(days,learners**2, "c", days,learners)
plt.axis([0,18,0,850])
plt.title("index of Learning programming")
plt.xlabel("Days")
plt.ylabel("Learners")
plt.show()
plt.bar(arange(1,12), arange(1,23,2), width=.75)
plt.show()


plt.bar(arange(1,12)*2, arange(1,23,2), color="green")
plt.bar(arange(1,12)*2+1, arange(1,43,4),color="yellow")
plt.xticks(arange(1,12)*2+1, arange(1,13))
plt.show()


plt.hist(random.randn(20000),10)
plt.annotate('Expected Mean', xy=(0,0),xytext=(0,200),ha="center",
arrowprops=dict(facecolor='yellow'),fontsize=30)
plt.show()
#plt.annotate(r"$\hat \mu= 0$",xy=(0,0),xytext=(0,100),ha="center",
#arrowprops=dict(facecolor="white"), fontsize=25)
plt.hist(random.randn(10000),25)
plt.annotate(r"$\hat \mu= 0$",xy=(0,0),xytext=(0,200),ha="center",arrowprops=dict(facecolor="red"), fontsize=20)
path="/home/jeanne/Desktop/Realpython/Chapter12 practice files/Output/" 
plt.savefig(path+"histogram.png")
plt.savefig(path+"histogram.pdf")
plt.savefig(path+"histogram.jpg")
plt.show()


x1=[]
x2=[]
y=[]
path="/home/jeanne/Desktop/Realpython/Chapter15practice files/"
with open("/home/jeanne/Desktop/Realpython/Chapter15practice files /pirates.csv","rU")as file_name:
	csv_file=csv.reader(file_name)
	next(file_name)

	for year,temp, pirate in csv_file:	
		x1.append(year)
		x2.append(temp)
		y.append(pirate)
	
	plt.plot(x2,y, "r-*")
	plt.title("Relationship between temperture and pirates ")
	plt.xlabel("Temperature")
	plt.ylabel("Pirates")
	
	for year in range(len(x1)):
		plt.annotate(x1[year], xy=(x2[year],y[year]))
	
	plt.savefig("/home/jeanne/Desktop/Realpython/Chapter15practice files /"+"TempVsPirates.png")
	plt.show()
	
