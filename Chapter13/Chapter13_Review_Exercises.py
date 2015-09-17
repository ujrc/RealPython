import sqlite3
connection =sqlite3.connect(':memory:')# Create a temporary database
c=connection.cursor() 
c.execute("create table Roster(Name Text, Species Text,IQ int)")
my_data=(("Jean-Baptiste Zorg","Human",122),
("Korben Dallas", "Meat Popsicle",100),
("Ak'not","Mangalore",-5))
c.executemany("insert into Roster Values(?,?,?)",my_data)
connection.commit()
c.execute ("update Roster set Species= ?  where Name=?  and Iq=?", ("Human","Korben Dallas",100))
c.execute("select Name, IQ from Roster where Species='Human'")
for row in c.fetchall():
	print row


my_data=(("Jean-Baptiste Zorg","Human",122),
("Koren Dallas","Meat Popsicle",100),
("Ak'not","Manglore",-5))
with sqlite3.connect(":memory:") as connection:
	c=connection.cursor()
	c.execute("create table Roster(Name Text,Species text, IQ int )")
	c.executemany("insert into Roster values(?,?,?)",my_data)
	c.execute("select Name, Species, IQ from Roster")
	for row in c.fetchall():
		print row
	c.execute("UPDATE Roster SET Species=? where Name=? AND IQ=?", ('Human','Koren Dallas',100))
	
	c.execute("select Name, Species, IQ from Roster where Species='Human'")
	for row in c.fetchall():
		print row


