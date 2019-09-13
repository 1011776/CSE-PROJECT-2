print('Content-type: text/html\n\n')

import cgi
import cgitb; cgitb.enable()
import sqlite3

mydb = 'dnd.db'
conn = sqlite3.connect(mydb)
cursor = conn.cursor()

print('<title>D&D Database: Search Proficiencies</title>')
print('<link rel="stylesheet" href="../stylesheet.css">')

print('<h1>D&D Database</h1>')
print('<h2>Search Proficiencies</h2>')

form = cgi.FieldStorage()
name = form.getvalue('name')
attribute = form.getvalue('attribute')

values = { "name": name, "attribute": attribute }

cursor.execute('''
        SELECT proficiencyID, Name, Attribute FROM Proficiency
        WHERE (LOWER(:name) = LOWER(Name) OR :name IS NULL)
        AND (:attribute = Attribute OR :attribute IS NULL)
        ORDER BY Attribute, Name
        ''', values)

records = cursor.fetchall()

if len(records) > 0:
    print('<table>')
    print('<tr><th>Name</th><th>Attribute</th><th>Edit</th>'
            + '<th>Delete</th><th>Add to Character</th></tr>')
    for record in records:
        print('<tr>')
        print('<td>' + str(record[1]) + '</td>')
        print('<td>' + str(record[2]) + '</td>')
        print('''<td><form action="editProficiency.py">
                <input type="hidden" name="proficiencyID" value="'''
                + str(record[0]) + '''">
                <input type=submit name=empty value="">
                </form></td>''')
        print('''<td><form action="removeProficiency.py">
                <input type="hidden" name="proficiencyID" value="'''
                + str(record[0]) + '''">
                <input type=submit name=empty value="">
                </form></td>''')
        print('''<td><form action="addProficiencyToCharacter.py">
                <input type="hidden" name="proficincyID" value="'''
                + str(record[0]) + '''">
                <input type=submit name=empty value="">
                </form></td>''')
        print('</tr>')
    print('</table>')
else:
    print('No records found')

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
