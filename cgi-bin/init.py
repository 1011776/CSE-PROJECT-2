print('Content-type: text/html\n\n')

import cgi
import cgitb; cgitb.enable()
import sqlite3

mydb = 'dnd.db'
conn = sqlite3.connect(mydb)
cursor = conn.cursor()

print('<title>D&D Database: Initialise database</title>')
print('<link rel="stylesheet" href="../stylesheet.css">')

print('<h1>D&D Database</h1>')
print('<h2>Initialise database</h2>')

print('Enable foreign keys<br>')
cursor.execute('PRAGMA foreign_keys = ON')

print('Drop tables if they exist<br>')
cursor.execute('''DROP TABLE IF EXISTS CharacterAbility''')
cursor.execute('''DROP TABLE IF EXISTS CharacterItem''')
cursor.execute('''DROP TABLE IF EXISTS CharacterProficiency''')
cursor.execute('''DROP TABLE IF EXISTS CharacterSpell''')
cursor.execute('''DROP TABLE IF EXISTS Character''')
cursor.execute('''DROP TABLE IF EXISTS Campaign''')
cursor.execute('''DROP TABLE IF EXISTS Student''')
cursor.execute('''DROP TABLE IF EXISTS Spell''')
cursor.execute('''DROP TABLE IF EXISTS Proficiency''')
cursor.execute('''DROP TABLE IF EXISTS Item''')
cursor.execute('''DROP TABLE IF EXISTS Ability''')

print('Create Student table<br>')
cursor.execute('''
        CREATE TABLE Student (
        StudentID       INTEGER PRIMARY KEY AUTOINCREMENT,
        Year            INTEGER,
        FirstName       VARCHAR(100),
        LastName        VARCHAR(100)
        )''')

print('Create Campaign table<br>')
cursor.execute('''
        CREATE TABLE Campaign (
        CampaignID      INTEGER PRIMARY KEY AUTOINCREMENT,
        StudentIDFK     INTEGER,
        CampaignName    VARCHAR(100),
        FOREIGN KEY (StudentIDFK) REFERENCES Student(StudentID)
        )''')

print('Create Character table<br>')
cursor.execute('''
        CREATE TABLE Character (
        CharacterID     INTEGER PRIMARY KEY,
        Name            VARCHAR(100),
        StudentIDFK     INTEGER,
        CampaignIDFK    INTEGER,
        Class           VARCHAR(100),
        Background      VARCHAR(100),
        Race            VARCHAR(100),
        Alignment       VARCHAR(100),
        ExpPoints       INTEGER,
        Inspiration     INTEGER,
        ProfBonus       INTEGER,
        Gold            INTEGER,
        HitPointMax     INTEGER,
        PTraits         VARCHAR(1000),
        Ideals          VARCHAR(1000),
        Bonds           VARCHAR(1000),
        Flaws           VARCHAR(1000),
        OtherInfo       VARCHAR(1000),
        Strength        INTEGER,
        Dexterity       INTEGER,
        Constitution    INTEGER,
        Intellegence    INTEGER,
        Wisdom          INTEGER,
        Charisma        INTEGER,
        StrSave         INTEGER,
        DexSave         INTEGER,
        ConSave         INTEGER,
        IntSave         INTEGER,
        WisSave         INTEGER,
        ChaSave         INTEGER,
        FOREIGN KEY (StudentIDFK) REFERENCES Student(StudentID),
        FOREIGN KEY (CampaignIDFK) REFERENCES Campaign(CampaignID)
        )''')

print('Create CharacterSpell table<br>')
cursor.execute('''
        CREATE TABLE CharacterSpell (
        CharacterIDFK   INTEGER,
        SpellIDFK       INTEGER,
        FOREIGN KEY (CharacterIDFK) REFERENCES Character(CharacterID),
        FOREIGN KEY (SpellIDFK) REFERENCES Spell(SpellID)
        )''')

print('Create Spell table<br>')
cursor.execute('''
        CREATE TABLE Spell (
        SpellID         INTEGER PRIMARY KEY AUTOINCREMENT,
        Name            VARCHAR(100),
        Level           INTEGER,
        Description     VARCHAR(10000)
        )''')

print('Create CharacterProficiency table<br>')
cursor.execute('''
        CREATE TABLE CharacterProficiency (
        CharacterIDFK   INTEGER,
        ProficiencyIDFK INTEGER,
        FOREIGN KEY (CharacterIDFK) REFERENCES Character(CharacterID),
        FOREIGN KEY (ProficiencyIDFK) REFERENCES Character(ProficiencyID)
        )''')

print('Create Proficiency table<br>')
cursor.execute('''
        CREATE TABLE Proficiency (
        ProficiencyID   INTEGER PRIMARY KEY AUTOINCREMENT,
        Name            VARCHAR(100),
        Attribute       VARCHAR(3)
        )''')

print('Create CharacterItem table<br>')
cursor.execute('''
        CREATE TABLE CharacterItem (
        CharacterIDFK   INTEGER,
        ItemIDFK        INTEGER,
        Quantity        INTEGER,
        FOREIGN KEY (CharacterIDFK) REFERENCES Character(CharacterID),
        FOREIGN KEY (ItemIDFK) REFERENCES Item(ItemID)
        )''')

print('Create Item table<br>')
cursor.execute('''
        CREATE TABLE Item (
        ItemID          INTEGER PRIMARY KEY AUTOINCREMENT,
        Name            VARCHAR(100),
        Description     VARCHAR(10000)
        )''')

print('Create CharacterAbility table<br>')
cursor.execute('''
        CREATE TABLE CharacterAbility (
        CharacterIDFK   INTEGER,
        AbilityIDFK     INTEGER,
        FOREIGN KEY (CharacterIDFK) REFERENCES Character(CharacterID),
        FOREIGN KEY (AbilityIDFK) REFERENCES Character(AbilityID)
        )''')

print('Create Ability table<br>')
cursor.execute('''
        CREATE TABLE Ability (
        AbilityID       INTEGER PRIMARY KEY AUTOINCREMENT,
        Name            VARCHAR(100),
        Description     VARCHAR(10000)
        )''')

print('<br/>')
print('Table creation complete<br>')
print('<br/>')
print('<form action="insertSampleData.py">')
print('<input type=submit value="Insert Sample Data"/>')
print('</form><br><br>')
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
