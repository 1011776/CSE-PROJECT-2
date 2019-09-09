print('Content-type: text/html\n\n')

import cgi
import cgitb; cgitb.enable()
import sqlite3

mydb = 'dnd.db'
conn = sqlite3.connect(mydb)
cursor = conn.cursor()

print('<head>')
print('<title>D&D Database: Initialise database</title>')
print('<link rel="stylesheet" href="../stylesheet.css">')
print('</head>')

print('<h1>D&D Database</h1>')
print('<h2>Insert sample data</h2>')

print('Insert sample students<br>')
cursor.execute('''INSERT INTO Student (StudentID, FirstName, LastName, Year)
        VALUES (1011775, "Steve", "Smith", 6)''')

print('Insert sample spells<br>')
cursor.execute('''INSERT INTO Spell (Name, Level, Description)
        VALUES ("Acid Arrow", 2,
        'A shimmering green arrow streaks toward a target 
        within range and bursts in a spray of acid. Make a 
        ranged spell attack against the target. On a hit, the 
        target takes 4d4 acid damage immediately and 2d4 
        acid damage at the end of its next turn. On a miss, 
        the arrow splashes the target with acid for half as 
        much of the initial damage and no damage at the end 
        of its next turn.\n
        At Higher Levels. When you cast this spell using a 
        spell slot of 3rd level or higher, the damage (both 
        initial and later) increases by ld4 for each slot level 
        above 2nd.'),
        
        ("Acid Splash", 0,
        'You hurl a bubble of acid. Choose one creature 
        within range, or choose two creatures within range 
        that are within 5 feet of each other. A target must 
        succeed on a Dexterity saving throw or take ld6 acid 
        damage.\n
        This spell’s damage increases by ld6 when you 
        reach 5th level (2d6), 11th level (3d6), and 17th 
        level (4d6).'),
        
        ("Aid ", 2,
        'Your spell bolsters your allies with toughness and 
        resolve. Choose up to three creatures within range. 
        Each target’s hit point maximum and current hit 
        points increase by 5 for the duration.\n
        At Higher Levels. When you cast this spell using a 
        spell slot of 3rd level or higher, a target’s hit points 
        increase by an additional 5 for each slot level above 
        2nd.')''')


print('<br/>')
print('Data insertion complete<br>')
print('<br/>')
print('<a href="../index.html">Return to homepage</a><br>')
