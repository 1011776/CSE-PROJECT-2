print('Content-type: text/html\n\n')

import cgi
import cgitb; cgitb.enable()
import sqlite3

mydb = 'dnd.db'
conn = sqlite3.connect(mydb)
cursor = conn.cursor()

print('<title>D&D Database: Remove Proficiency</title>')
print('<link rel="stylesheet" href="../stylesheet.css">')

print('<h1>D&D Database</h1>')
print('<h2>Remove Proficiency</h2>')

form = cgi.FieldStorage()
proficiencyID = form.getvalue('proficiencyID')

values = { "proficiencyID": proficiencyID }

cursor.execute('''
        DELETE FROM CharacterProficiency
        WHERE :proficiencyID = ProficiencyIDFK
        ''', values)

cursor.execute('''
        DELETE FROM Proficiency
        WHERE :proficiencyID = ProficiencyID
        ''', values)

records = cursor.fetchall()

print('Proficiency successfully removed from database')
print('<br/>')
print('<br/>')
print('<br/>')
print('<form action="../proficiencies.html">')
print('<input type=submit value="Return to Proficiencies Menu"/>')
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
