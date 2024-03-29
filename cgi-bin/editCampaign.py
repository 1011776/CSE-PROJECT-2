print('Content-type: text/html\n\n')

import cgi
import cgitb; cgitb.enable()
import sqlite3

mydb = 'dnd.db'
conn = sqlite3.connect(mydb)
cursor = conn.cursor()

print('<title>D&D Database: Edit Campaign</title>')
print('<link rel="stylesheet" href="../stylesheet.css">')

print('<h1>D&D Database</h1>')
print('<h2>Edit Campaign</h2>')

form = cgi.FieldStorage()
campaignID = form.getvalue('campaignID')

values = { "campaignID": campaignID }

cursor.execute('''
        SELECT CampaignID, CampaignName, StudentIDFK FROM Campaign
        WHERE CampaignID = :campaignID
        ''', values)

records = cursor.fetchall()

print('<form action="updateCampaign.py">')
print('<input type="hidden" name="campaignID" value='
        + str(campaignID) +'>')
print('Name:<br>')
print('<input type="text" name="name" value="' 
        + records[0][1] + '" required><br>')
print('DM\'s Student ID:<br>')
print('<input type="number" name="studentIDFK" '
        + 'min="1000000" max="1100000" value="'
        + str(records[0][2]) + '" required><br><br>')
print('<input type="submit" value="Commit Changes">')
print('</form>')

print('<br>')
print('<br>')
print('<br>')
print('<form action="../campaigns.html">')
print('<input type=submit value="Return to Campaigns Menu"/>')
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
