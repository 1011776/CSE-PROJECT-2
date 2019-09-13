print('Content-type: text/html\n\n')

import cgi
import cgitb; cgitb.enable()
import sqlite3

mydb = 'dnd.db'
conn = sqlite3.connect(mydb)
cursor = conn.cursor()

print('<title>D&D Database: View Ability</title>')
print('<link rel="stylesheet" href="../stylesheet.css">')

print('<h1>D&D Database</h1>')
print('<h2>View Ability</h2>')

form = cgi.FieldStorage()
abilityID = form.getvalue('abilityID')

values = { "abilityID": abilityID }

cursor.execute('''
        SELECT AbilityID, Name, Description FROM Ability
        WHERE :abilityID = AbilityID
        ''', values)

records = cursor.fetchall()

print("Name: ")
print(records[0][1])
print("<br><br>")
print("Description: ")
print(records[0][2])

print('<br/>')
print('<br/>')
print('<br/>')
print('<form action="../abilities.html">')
print('<input type=submit value="Return to Abilities Menu"/>')
print('</form>')
print('<br/>')
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
