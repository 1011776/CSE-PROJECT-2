print('Content-type: text/html\n\n')

import cgi
import cgitb; cgitb.enable()
import sqlite3

mydb = 'dnd.db'
conn = sqlite3.connect(mydb)
cursor = conn.cursor()

print('<head><title>D&D Database: Insert a spell</title></head>')

print('<h2>D&D Database</h2>')
print('<h3>Insert a spell</h3>')

print('Insert spell<br>')
form = cgi.FieldStorage()
name = form.getvalue('name')
level = form.getvalue('level')
description = form.getvalue('description')

values = { "name": name, "level": level, "description": description }

cursor.execute('''
        INSERT INTO Spell (Name, Level, Description) 
        VALUES (:name, :level, :description)
        ''', values)

print('<br>')
print('Insertion completed<br>')
print('<br>')
print('<a href="../index.html">Return to homepage</a><br>')
