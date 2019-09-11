print('Content-type: text/html\n\n')

import cgi
import cgitb; cgitb.enable()
import sqlite3

mydb = 'dnd.db'
conn = sqlite3.connect(mydb)
cursor = conn.cursor()

print('<title>D&D Database: Insert a spell</title>')
print('<link rel="stylesheet" href="../stylesheet.css">')

print('<h1>D&D Database</h1>')
print('<h2>Search Spells</h2>')

form = cgi.FieldStorage()
name = form.getvalue('name')
level = form.getvalue('level')

values = { "name": name, "level": level }

cursor.execute('''
        SELECT Name, Level FROM Spell 
        WHERE (:name = Spell(NAME) OR :name = "")
        AND (:level = OR :level = NULL)
        ''', values)

print('Insertion completed<br>')
print('<br>')
print('<a href="../insertSpell.html">Insert another spell</a><br>')
print('<a href="../index.html">Return to homepage</a><br>')

conn.commit()
cursor.close()
