print('Content-type: text/html\n\n')

import cgi
import cgitb; cgitb.enable()
import sqlite3

mydb = 'dnd.db'
conn = sqlite3.connect(mydb)
cursor = conn.cursor()

print('<title>D&D Database: Add Spell to Character</title>')
print('<link rel="stylesheet" href="../stylesheet.css">')

print('<h1>D&D Database</h1>')
print('<h2>Add Spell to Character</h2>')

form = cgi.FieldStorage()
spellID = form.getvalue('spellID')

values = { "spellID": spellID }

print('<form name="input" action="insertCharacterSpell.py">')
print('<input type="hidden" name="spellID" value="' + spellID + '"<br>')
print('Character ID:<br>')
print('<input type="number" name="characterID"><br><br>')
print('<input type="submit" value="Add to Character"><br>')
print('</form>')

print('<br>')
print('<br>')
print('<br>')
print('<form action="../spells.html">')
print('<input type=submit value="Return to Spells Menu"/>')
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
