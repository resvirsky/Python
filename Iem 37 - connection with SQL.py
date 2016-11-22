Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import sqlite3
>>> connection = sqlite3.connect(':memory:')
>>> c = connection.cursor()
>>> c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")
<sqlite3.Cursor object at 0x0340CF60>
>>> c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)
