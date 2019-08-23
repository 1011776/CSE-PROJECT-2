print 'Content-type: text/html\n\n'

import cgi
import cgitb; cgitb.enable()
import sqlite3

mydb = 'dnd.db'
conn = sqlite3.connect(mydb)
cursor = conn.cursor()

print 'Drop tables if they exist<br />'
cursor.execute('''DROP TABLE IF EXISTS Movie''')

print 'create Player table<br />'
cursor.execute('''CREATE TABLE Player
                    (StudentID INTEGER PRIMARY KEY,
                    Year INT`,
                    FirstName VARCHAR(20),
                    LastName VARCHAR(20))''')

conn.commit()
cursor.close()

