#!/usr/bin/python
print 'Content-type: text/html\n\n'

import cgi
import cgitb; cgitb.enable()
import sqlite3

mydb = 'videostore.db'
conn = sqlite3.connect(mydb)
cursor = conn.cursor()

print 'Drop tables if they exist<br />'
cursor.execute('''DROP TABLE IF EXISTS Movie''')

print 'create Video table<br />'
cursor.execute('''CREATE TABLE Movie
                    (movie_id INTEGER PRIMARY KEY,
                    name VARCHAR(20),
                    genre VARCHAR(10),
                    year INTEGER)''')

conn.commit()
cursor.close()

