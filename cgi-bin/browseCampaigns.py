print('Content-type: text/html\n\n')

import cgi
import cgitb; cgitb.enable()
import sqlite3

mydb = 'dnd.db'
conn = sqlite3.connect(mydb)
cursor = conn.cursor()

print('<title>D&D Database: Search Campaigns</title>')
print('<link rel="stylesheet" href="../stylesheet.css">')

print('<h1>D&D Database</h1>')
print('<h2>Search Campaigns</h2>')

form = cgi.FieldStorage()
studentIDFK = form.getvalue('studentIDFK')
name = form.getvalue('name')

values = { "studentIDFK": studentIDFK, "name": name }

cursor.execute('''
        SELECT Campaign.CampaignID, Campaign.StudentIDFK, 
        Campaign.CampaignName, Student.FirstName, Student.LastName,
        COUNT(Character.CharacterID) AS nCharacter FROM Campaign, Student
        LEFT JOIN Character ON (Campaign.CampaignID = Character.CampaignIDFK)
        WHERE (:studentIDFK = Campaign.StudentIDFK OR :studentIDFK IS NULL)
        AND (LOWER(:name) = LOWER(Campaign.CampaignName) OR :name IS NULL)
        AND (Campaign.StudentIDFK = Student.StudentID)
        GROUP BY Campaign.CampaignID
        ''', values)

records = cursor.fetchall()

if len(records) > 0:
    print('<table>')
    print('<tr><th>Campaign Name</th><th>DM\'s Student ID</th><th>DM\'s Name</th>'
        + '<th>Characters</th><th>Edit</th><th>Delete</th><th>Add Character to</th></tr>')
    for record in records:
        print('<tr>')
        print('<td>' + str(record[2]) + '</td>')
        print('<td>' + str(record[1]) + '</td>')
        print('<td>' + str(record[3]) + ' ' + str(record[4]) + '</td>')
        print('<td>' + str(record[5]) + '</td>')
        print('''<td><form action="editCampaign.py">
                <input type="hidden" name="campaignID" value="'''
                + str(record[0]) + '''">
                <input type=submit name=empty value="">
                </form></td>''')
        print('''<td><form action="removeCampaign.py">
                <input type="hidden" name="campaignID" value="'''
                + str(record[0]) + '''">
                <input type=submit name=empty value="">
                </form></td>''')
        print('''<td><form action="addCharacterToCampaign.py">
                <input type="hidden" name="campaignID" value="'''
                + str(record[0]) + '''">
                <input type=submit name=empty value="">
                </form></td>''')
        print('</tr>')
    print('</table>')
else:
    print('No records found')

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
