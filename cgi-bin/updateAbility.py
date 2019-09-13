print('Content-type: text/html\n\n')

import cgi
import cgitb; cgitb.enable()
import sqlite3

mydb = 'dnd.db'
conn = sqlite3.connect(mydb)
cursor = conn.cursor()

print('<title>D&D Database: Edit Item</title>')
print('<link rel="stylesheet" href="../stylesheet.css">')

print('<h1>D&D Database</h1>')
print('<h2>Edit Ability</h2>')

form = cgi.FieldStorage()
abilityID = form.getvalue('abilityID')
name = form.getvalue('name')
description = form.getvalue('description')

values = { "abilityID": abilityID, "name": name, 
        "description": description }

cursor.execute('''
        UPDATE Ability
        SET Name = :name, Description = :description
        WHERE :abilityID = abilityID
        ''', values)

print('Ability successfully edited')

print('<br>')
print('<br>')
print('<br>')
print('<form action="../abilities.html">')
print('<input type=submit value="Return to Abilities Menu"/>')
print('</form>')
print('<br>')
print('<br>')
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
