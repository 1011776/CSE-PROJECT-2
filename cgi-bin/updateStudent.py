print('Content-type: text/html\n\n')

import cgi
import cgitb; cgitb.enable()
import sqlite3

mydb = 'dnd.db'
conn = sqlite3.connect(mydb)
cursor = conn.cursor()

print('<title>D&D Database: Edit Student</title>')
print('<link rel="stylesheet" href="../stylesheet.css">')

print('<h1>D&D Database</h1>')
print('<h2>Edit Student</h2>')

form = cgi.FieldStorage()
studentID = form.getvalue('studentID')
firstName = form.getvalue('firstName')
lastName = form.getvalue('lastName')
year = form.getvalue('year')

values = { "studentID": studentID, "firstName": firstName, 
        "lastName": lastName, "year": year }

cursor.execute('''
        UPDATE Student
        SET FirstName = :firstName, LastName = :lastName, Year = :year
        WHERE :studentID = StudentID
        ''', values)

print('Student details updated')

print('<br>')
print('<br>')
print('<br>')
print('<form action="../students.html">')
print('<input type=submit value="Return to Students Menu"/>')
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
