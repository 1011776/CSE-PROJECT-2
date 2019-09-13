print('Content-type: text/html\n\n')

import cgi
import cgitb; cgitb.enable()
import sqlite3

mydb = 'dnd.db'
conn = sqlite3.connect(mydb)
cursor = conn.cursor()

print('<title>D&D Database: Search Students</title>')
print('<link rel="stylesheet" href="../stylesheet.css">')

print('<h1>D&D Database</h1>')
print('<h2>Search Students</h2>')


form = cgi.FieldStorage()
name = form.getvalue('name')
studentIDFK = form.getvalue('studentIDFK')
cla = form.getvalue('class')
background = form.getvalue('background')
race = form.getvalue('race')
alignment = form.getvalue('alignment')
expPoints = form.getvalue('expPoints')
strength = form.getvalue('str')
strSave = form.getvalue('strSave')
dex = form.getvalue('dex')
dexSave = form.getvalue('dexSave')
con = form.getvalue('con')
conSave = form.getvalue('conSave')
intellegence = form.getvalue('int')
intSave = form.getvalue('intSave')
wis = form.getvalue('wis')
wisSave = form.getvalue('wisSave')
cha = form.getvalue('cha')
chaSave = form.getvalue('chaSave')
profBonus = form.getvalue('profBonus')
inspiration = form.getvalue('inspiration')
gold = form.getvalue('gold')
hitPointMax = form.getvalue('hitPointMax')
pTraits = form.getvalue('pTraits')
ideals = form.getvalue('ideals')
bonds = form.getvalue('bonds')
flaws = form.getvalue('flaws')
otherInfo = form.getvalue('otherInfo')
campaignName = form.getvalue('campaignName')

values = { "name":name,"studentIDFK":studentIDFK,"class":cla,"background":background,"race":race,
        "alignment":alignment,"expPoints":expPoints,"str":strength, 
        "strSave":strSave,"dex":dex,"dexSave":dexSave,"con":con,
        "conSave":conSave,"int":intellegence,"intSave":intSave,"wis":wis,
        "wisSave":wisSave,"cha":cha,"chaSave":chaSave,"inspiration":inspiration,
        "profBonus":profBonus,"gold":gold,"hitPointMax":hitPointMax,
        "pTraits":pTraits,"ideals":ideals,"bonds":bonds,"flaws":flaws,
        "otherInfo":otherInfo, "campaignName":campaignName
}


cursor.execute('''
        SELECT Character.CharacterID, Character.name, Character.class,
        Student.StudentID, Student.FirstName, Student.LastName, Campaign.CampaignName
        FROM Character, Campaign, Student
        WHERE (:studentIDFK = Student.StudentID OR :studentIDFK IS NULL)
        AND (LOWER(:campaignName) = LOWER(Campaign.CampaignName) OR :campaignName IS NULL)
        AND (LOWER(:name) = LOWER(Character.name) OR :name IS NULL)
        AND (LOWER(:class) = LOWER(Character.class) OR :class IS NULL)
        AND (Character.StudentIDFK = Student.StudentID)
        AND (Character.CampaignIDFK = Campaign.CampaignID)
        GROUP BY Student.StudentID
        ORDER BY Student.LastName
        ''', values)

records = cursor.fetchall()

if len(records) > 0:
    print('<table>')
    print('<tr><th>Character ID</th><th>Character Name</th><th>Class</th>'
    +'<th>Student ID</th><th>Student Name</th><th>Campaign Name</th>'
    + '<th>View</th><th>Edit</th><th>Remove</th></tr>')
    for record in records:
        print('<tr>')
        print('<td>' + str(record[0]) + '</td>')
        print('<td>' + str(record[1]) + '</td>')
        print('<td>' + str(record[2]) + '</td>')
        print('<td>' + str(record[3]) + '</td>')
        print('<td>' + str(record[4]) + ' ' + str(record[5]) + '</td>')
        print('<td>' + str(record[6]) + '</td>')
        print('''<td><form action="viewCharacter.py">
                <input type="hidden" name="characterID" value="'''
                + str(record[0]) + '''">
                <input type=submit name=empty value="">
                </form></td>''')
        print('''<td><form action="../WIP.html">
                <input type="hidden" name="characterID" value="'''
                + str(record[0]) + '''">
                <input type=submit name=empty value="">
                </form></td>''')
        print('''<td><form action="removeCharacter.py">
                <input type="hidden" name="characterID" value="'''
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
print('<form action="../searchCharacters.html">')
print('<input type=submit value="Return to Character Search"/>')
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
