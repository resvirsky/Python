import sqlite3

with sqlite3.connect("test_renato.db") as connection:
    c = connection.cursor()
    c.execute("SELECT Name, Species FROM Roster WHERE IQ>30")
    for row in c.fetchall():
        print row
