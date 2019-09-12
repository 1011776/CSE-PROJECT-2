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
print('<h2>Edit Item</h2>')

form = cgi.FieldStorage()
itemID = form.getvalue('itemID')

values = { "itemID": itemID }

cursor.execute('''
        SELECT ItemID, Name, Description FROM Item
        WHERE ItemID = :itemID
        ''', values)

records = cursor.fetchall()

print('<form action="updateItem.py">')
print('<input type="hidden" name="itemID" value='
        + str(itemID) +'>')
print('Name:<br>')
print('<input type="text" name="name" value="' 
        + records[0][1] + '" required><br>')
print('Description:<br>')
print('<textarea rows="4", cols="50" name="description">'
        + records[0][2] + '</textarea><br><br>')
print('<input type="submit" value="Commit Changes">')
print('</form>')

print('<br>')
print('<br>')
print('<br>')
print('<form action="../items.html">')
print('<input type=submit value="Return to Items Menu"/>')
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
