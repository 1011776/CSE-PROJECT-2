print('Content-type: text/html\n\n')

import cgi
import cgitb; cgitb.enable()
import sqlite3

mydb = 'dnd.db'
conn = sqlite3.connect(mydb)
cursor = conn.cursor()

print('Insert sample students<br>')
cursor.execute('''INSERT INTO Student (StudentID, FirstName, LastName, Year)
        VALUES (1011775, "Steve", "Smith", 6)''')
print('<br/>')
print('Data insertion comlete<br>')
print('<br/>')
print('<a href="../index.html">Return to homepage</a><br>')