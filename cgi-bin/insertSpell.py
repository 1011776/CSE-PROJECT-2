print('Content-type: text/html\n\n')

import cgi
import cgitb; cgitb.enable()
import sqlite3

mydb = 'dnd.db'
conn = sqlite3.connect(mydb)
cursor = conn.cursor()

form = cgi.FieldStorage()
name = form.getvalue('name')
level = form.getvalue('level')
description = form.getvalue('description')

values = { "name": name, "level": level, "description": description }

cursor.execute('''
        INSERT INTO Player (username, no_of_achievements, lunar_coins) 
        VALUES (:username, :achievements, :lunar)
        ''', values)
