print('Content-type: text/html\n\n')

import cgi
import cgitb; cgitb.enable()
import sqlite3

mydb = 'dnd.db'
conn = sqlite3.connect(mydb)
cursor = conn.cursor()

print('<title>D&D Database: Update a spell</title>')
print('<link rel="stylesheet" href="../stylesheet.css">')

print('<h1>D&D Database</h1>')
print('<h2>Edit spell</h2>')

form = cgi.FieldStorage()
name = form.getvalue('spellID')

values = { "spellID": spellID }

cursor.execute('''
        SELECT SpellID, Name, Level, Description FROM Spell
        WHERE SpellID == :spellID
        ''', values)

records = cursor.fetchall()

print('form action="cgi-bin/insertSpell.py">')
print('Name:<br>')
print('<input type="text" name="name" value="' 
        + records[0][1] + ' required><br>')
print('Level:<br>')
print('<input type="number" name="level" min="0" max="9" value="' 
        + records[0][2] +'" required><br>')
print('Description:<br>')
print('<textarea rows="4", cols="50" name="description" value="'
        + record[0][3] + '"required>')
print('</textarea><br><br>')
print('<input type="submit" value="Submit"><br>')
print('</form><br>')

print('Insertion completed<br>')
print('<br>')

print('Spell data successfully updated')
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
