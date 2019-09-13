print('Content-type: text/html\n\n')

import cgi
import cgitb; cgitb.enable()
import sqlite3

mydb = 'dnd.db'
conn = sqlite3.connect(mydb)
cursor = conn.cursor()

print('<title>D&D Database: Edit Proficiency</title>')
print('<link rel="stylesheet" href="../stylesheet.css">')

print('<h1>D&D Database</h1>')
print('<h2>Edit Proficiency</h2>')

form = cgi.FieldStorage()
proficiencyID = form.getvalue('proficiencyID')

values = { "proficiencyID": proficiencyID }

cursor.execute('''
        SELECT ProficiencyID, Name, Attribute FROM Proficiency
        WHERE ProficiencyID = :proficiencyID
        ''', values)

records = cursor.fetchall()

print('<form action="updateProficiency.py">')
print('<input type="hidden" name="itemID" value='
        + str(proficiencyID) +'>')
print('Name: ')
print('<input type="text" name="name" value="'
        + str(records[0][1]) +'"><br><br>') 
print('Attribute: ')
print('<select name="attribute">')
print('<option disabled selected value> -- select an option -- </option>')
print('<option value="Str">Strength</option>')
print('<option value="Dex">Dexterity</option>')
print('<option value="Con">Constitution</option>')
print('<option value="Int">Intellegence</option>')
print('<option value="Wis">Wisdom</option>')
print('<option value="Cha">Charisma</option>')
print('</select>') 
print('<br><br>') 
print('<input type="submit" value="Commit Changes">')
print('</form>')

print('<br>')
print('<br>')
print('<br>')
print('<form action="../proficiencies.html">')
print('<input type=submit value="Return to Proficiencies Menu"/>')
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
