print('Content-type: text/html\n\n')

import cgi
import cgitb; cgitb.enable()
import sqlite3

mydb = 'dnd.db'
conn = sqlite3.connect(mydb)
cursor = conn.cursor()

form = cgi.FieldStorage()
characterID = form.getvalue('characterID')

values = { "characterID": characterID }

print('<title>D&D Database: View Ability</title>')
print('<link rel="stylesheet" href="../stylesheet.css">')

print('<h1>D&D Database</h1>')
print('<h2>View Character</h2>')

print('Page is still currently a work in progrss<br>')
print('Abilities, spells, proficiencies and items belonging to the character should be '
    + 'visible under their respective headings, as well as the rest of the character information,'
    + 'Entered into the database.<br>')

print('This page will also allow user to delete Abilities, spells, proficiencies and items '
        'using buttons placed in a table, similar to that of the previous page.<br>')

print('<h3>Ability Scores</h3>')
print('<h3>Spells</h3>')
cursor.execute('''
        SELECT Spell.SpellID, Spell.Name, Spell.Level 
        FROM Spell, CharacterSpell
        WHERE :characterID = CharacterSpell.CharacterIDFK
        AND Spell.SpellID = CharacterSpell.SpellIDFK
        ORDER BY Level, Name
        ''', values)
records = cursor.fetchall()
if len(records) > 0:
    print('<table>')
    print('<tr><th>Name</th><th>Level</th><th>View</th><th>Remove From Character</th></tr>')
    for record in records:
        print('<tr>')
        print('<td>' + str(record[1]) + '</td>')
        print('<td>' + str(record[2]) + '</td>')
        print('''<td><form action="viewSpell.py">
                <input type="hidden" name="spellID" value="'''
                + str(record[0]) + '''">
                <input type=submit name=empty value="">
                </form></td>''')
        print('''<td><form action="removeSpellFromCharacter.py">
                <input type="hidden" name="spellID" value="'''
                + str(record[0]) + '''">
                <input type=submit name=empty value="">
                </form></td>''')
        print('</tr>')
    print('</table>')
else:
    print('No records found')
print('<h3>Proficiencies</h3>')
print('<h3>Items</h3>')
print('<h3>Abilities</h3>')

print('<br/>')
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
