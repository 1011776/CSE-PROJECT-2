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
print('<h2>Browse Spells</h2>')

form = cgi.FieldStorage()
name = form.getvalue('name')
level = form.getvalue('level')

values = { "name": name, "level": level }

cursor.execute('''
        SELECT SpellID, Name, Level FROM Spell
        WHERE (LOWER(:name) = LOWER(Name) OR :name IS NULL)
        AND (:level = Level OR :level IS NULL)
        ''', values)

records = cursor.fetchall()

if len(records) > 0:
    print('<table>')
    print('<tr><td>Name</td><td>Level</td><td>View</td><td>Update</td><td>Delete</td></tr>')
    for record in records:
        print('<tr>')
        print('<td>' + str(record[1]) + '</td>')
        print('<td>' + str(record[2]) + '</td>')
        print('''<td><form action="viewSpell.py"viewSpell.py>
                <input type="hidden" name="spellID" value="'''
                + str(record[0]) + '''">
                <input type=submit name=empty value="">
                </form></td>''')
        print('''<td><form action="editSpell.py">
                <input type="hidden" name="spellID" value="'''
                + str(record[0]) + '''">
                <input type=submit name=empty value="">
                </form></td>''')
        print('''<td><form action="removeSpell.py">
                <input type="hidden" name="spellID" value="'''
                + str(record[0]) + '''">
                <input type=submit name=empty value="">
                </form></td>''')
        print('</tr>')
    print('</table>')
else:
    print('No records found')

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
