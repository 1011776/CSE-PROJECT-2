print('Content-type: text/html\n\n')

import cgi
import cgitb; cgitb.enable()
import sqlite3

mydb = 'dnd.db'
conn = sqlite3.connect(mydb)
cursor = conn.cursor()

print('<title>D&D Database: Edit Spell</title>')
print('<link rel="stylesheet" href="../stylesheet.css">')

print('<h1>D&D Database</h1>')
print('<h2>Edit Spell</h2>')

form = cgi.FieldStorage()
spellID = form.getvalue('spellID')
name = form.getvalue('name')
level = form.getvalue('level')
description = form.getvalue('description')

values = { "spellID": spellID, "name": name, "level": level, 
        "description": description }

cursor.execute('''
        UPDATE Spell
        SET Name = :name, Level = :level, Description = :description
        WHERE :spellID = spellID
        ''', values)

print('Insertion completed<br>')

print('<br/>')
print('<form action="../index.html">')
print('<input type=submit value="Return to Homepage"/>')
print('</form>')

print('<div class="footer">')
print('D&D Database is unofficial Fan Content permitted under')
print('the Fan Content Policy. Not approved/endorsed by')
print('Wizards. Portions of the materials used are property')
print('of Wizards of the Coast. &#169;Wizards of the Coast LLC')
print('</div>')

conn.commit()
cursor.close()
