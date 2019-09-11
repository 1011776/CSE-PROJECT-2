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
        SELECT SpellID, Name, Level FROM Spell
        WHERE (:name = LOWER(Name) OR :name IS NULL)
        AND (:level = Level OR :level IS NULL)
        ''', values)

records = cursor.fetchall()

print('<table border="1px solid black">')
print('<tr><td>Spell ID<td>Name</td><td>Level</td><td>View</td></tr>')
if len(records) > 0:
	for record in records:
		print('<tr>')
		for field in record:
			print('<td>' + str(field) + '</td>')
		print('<td><form><input type="submit" value="        "></form></td></tr>')
	print('</table>')
else:
	print('No records found')

print('<a href="../insertSpell.html">Insert another spell</a><br>')
print('<a href="../index.html">Return to homepage</a><br>')

conn.commit()
cursor.close()
