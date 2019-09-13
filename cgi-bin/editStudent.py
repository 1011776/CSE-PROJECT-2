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

values = { "studentID": studentID }

cursor.execute('''
        SELECT StudentID, FirstName, LastName, Year FROM Student
        WHERE StudentID = :studentID
        ''', values)

records = cursor.fetchall()

print('<form action="updateStudent.py">')
print('<input type="hidden" name="studentID" value='
        + str(studentID) +'>')
print('First Name: ')
print('<input type="text" name="firstName" value="' 
        + records[0][1] + '" required><br>')
print('Last Name: ')
print('<input type="text" name="lastName" value="' 
        + records[0][2] + '" required><br>')
print('Year: ')
print('<input type="number" name="year" min="5" max="12" value=' 
        + str(records[0][3]) +' required><br>')
print('<input type="submit" value="Commit Changes">')
print('</form>')

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
