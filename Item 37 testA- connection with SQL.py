import sqlite3

connection = sqlite3.connect("test_renato2.db")


c = connection.cursor()

c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")

rosterValues=(('Jean-Baptiste Zorg', 'Human', 122),
('Korben Dallas', 'Meat Popsicle', 100),
('Ak''not', 'Mangalore', -5))

c.executemany("INSERT INTO Roster VALUES(?, ?, ?)",
 rosterValues)

c.execute("SELECT Name, Species FROM Roster WHERE IQ>30")
for row in c.fetchall():
    print row

c.execute("UPDATE Roster SET Species='Human' WHERE IQ=100")

c.execute("SELECT Name, Species FROM Roster WHERE IQ>30")
for row in c.fetchall():
    print row
