print('Content-type: text/html\n\n')

import cgi
import cgitb; cgitb.enable()
import sqlite3

mydb = 'dnd.db'
conn = sqlite3.connect(mydb)
cursor = conn.cursor()

print('<title>D&D Database: Add Character to Campaign</title>')
print('<link rel="stylesheet" href="../stylesheet.css">')

print('<h1>D&D Database</h1>')
print('<h2>Add Character to Campaign</h2>')

form = cgi.FieldStorage()
campaignID = form.getvalue('campaignID')
characterID = form.getvalue('characterID')

values = { "campaignID": campaignID, "characterID": characterID }

cursor.execute('''
        UPDATE Character
        SET CampaignIDFK = :campaignID
        WHERE CharacterID = :characterID
        ''', values)

print('Character added to campaign')

print('<br>')
print('<br>')
print('<br>')
print('<form action="../campaigns.html">')
print('<input type=submit value="Return to Campaign Menu"/>')
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
