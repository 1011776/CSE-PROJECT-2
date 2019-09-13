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
firstName = form.getvalue('firstName')
lastName = form.getvalue('lastName')
year = form.getvalue('year')

values = { "firstName": firstName, "lastName": lastName, "year": year }

cursor.execute('''
        SELECT Student.StudentID, Student.FirstName, Student.LastName, 
        Student.Year, COUNT(Campaign.CampaignID) AS nCampaign,
        COUNT(Character.CharacterID) AS nCharacter FROM Student
        LEFT JOIN Campaign ON (Student.StudentID = Campaign.StudentIDFK)
        LEFT JOIN Character ON (Student.StudentID = Character.StudentIDFK)
        WHERE (LOWER(:lastName) = LOWER(Student.lastName) OR :lastName IS NULL)
        AND (:year = Student.year OR :year IS NULL)
        GROUP BY Student.StudentID
        ''', values)

records = cursor.fetchall()

if len(records) > 0:
    print('<table>')
    print('<tr><th>Student ID</th><th>First Name</th><th>Last Name</th>'
    +'<th>Year</th><th>Campaigns</th><th>Characters</th>'
    + '<th>Edit</th><th>Remove</th></tr>')
    for record in records:
        print('<tr>')
        print('<td>' + str(record[0]) + '</td>')
        print('<td>' + str(record[1]) + '</td>')
        print('<td>' + str(record[2]) + '</td>')
        print('<td>' + str(record[3]) + '</td>')
        print('<td>' + str(record[4]) + '</td>')
        print('<td>' + str(record[5]) + '</td>')
        print('''<td><form action="editStudent.py">
                <input type="hidden" name="studentID" value="'''
                + str(record[0]) + '''">
                <input type=submit name=empty value="">
                </form></td>''')
        print('''<td><form action="removeStudent.py">
                <input type="hidden" name="studentID" value="'''
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
print('<form action="../students.html">')
print('<input type=submit value="Return to Students Menu"/>')
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
