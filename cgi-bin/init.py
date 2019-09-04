print('Content-type: text/html\n\n')

import cgi
import cgitb; cgitb.enable()
import sqlite3

mydb = 'dnd.db'
conn = sqlite3.connect(mydb)
cursor = conn.cursor()

print('Drop tables if they exist<br />')
cursor.execute('''DROP TABLE IF EXISTS Student''')
cursor.execute('''DROP TABLE IF EXISTS Campaign''')
cursor.execute('''DROP TABLE IF EXISTS Character''')
cursor.execute('''DROP TABLE IF EXISTS CharacterProficiency''')
cursor.execute('''DROP TABLE IF EXISTS Proficiency''')
cursor.execute('''DROP TABLE IF EXISTS CharacterItem''')
cursor.execute('''DROP TABLE IF EXISTS Item''')
cursor.execute('''DROP TABLE IF EXISTS CharacterAbility''')
cursor.execute('''DROP TABLE IF EXISTS Ability''')

print('create Student table<br />')
cursor.execute('''CREATE TABLE Student (
        StudentID       INTEGER PRIMARY KEY,
        Year            INT,
        FirstName       VARCHAR(100),
        LastName        VARCHAR(100)
        )''')

print('create Campaign table<br />')
cursor.execute('''CREATE TABLE Campaign (
        CampaignID      INTEGER PRIMARY KEY,
        StudentIDFK     FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
        FirstName       VARCHAR(100),
        LastName        VARCHAR(100)
        )''')

print('create Character table<br />')
cursor.execute('''CREATE TABLE Character (
        CharacterID     INTEGER PRIMARY KEY,
        Name            VARCHAR(100),
        StudentIDFK     FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
        CampaignIDFK    FOREIGN KEY (CampaignID) REFERENCES Campaign(CampaignID),
        Class           VARCHAR(100),
        Background      VARCHAR(100),
        Race            VARCHAR(100),
        Alignment       VARCHAR(100),
        ExpPoints       INTEGER,
        Inspiration     INTEGER
        ProfBonus       INTEGER,
        Gold            INTEGER,
        HitPointMax     INTEGER,
        TotalHitDice    INTEGER,
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
        WisSave         INTEGER,
        ChaSave         INTEGER
        )''')

print('create CharacterSpell table')
cursor.execute('''CREATE TABLE CharacterSpell (
        CharacterID     FOREIGN KEY (CharacterID) REFERENCES Character(CharacterID),
        SpellID         FOREIGN KEY (SpellID) REFERENCES Character(SpellID)
        )''')

print('create Spell table<br />')
cursor.execute('''CREATE TABLE Spell (
        SpellID         INTEGER PRIMARY KEY,
        Name            VARCHAR(100),
        Level           INTEGER,
        Description     VARCHAR(1000)
        )''')

print('create CharacterProficiency table<br />')
cursor.execute('''CREATE TABLE CharacterProficiency
        CharacterID     FOREIGN KEY (CharacterID) REFERENCES Character(CharacterID),
        ProficiencyID   FOREIGN KEY (ProficiencyID) REFERENCES Character(ProficiencyID)
        )''')

print('create Proficiency table<br />')
cursor.execute('''CREATE TABLE Proficiency
        ProficiencyID   INTEGER PRIMARY KEY,
        Name            VARCHAR(100),
        Attribute       VARCHAR(3)
        )''')

print('create CharacterItem table<br />')
cursor.execute('''CREATE TABLE Item
        CharacterID     FOREIGN KEY (CharacterID) REFERENCES Character(CharacterID),
        ItemID          FOREIGN KEY (ItemID) REFERENCES Character(ItemID),
        Quantity        INTEGER
        )''')

print('create Item table<br />')
cursor.execute('''CREATE TABLE Proficiency
        ItemID          INTEGER PRIMARY KEY,
        Name            VARCHAR(100),
        Description     VARCHAR(1000)
        )''')

print('create CharacterAbility table<br />')
cursor.execute('''CREATE TABLE Ability
        CharacterID     FOREIGN KEY (CharacterID) REFERENCES Character(CharacterID),
        AbilityID       FOREIGN KEY (AbilityID) REFERENCES Character(AbilityID)
        )''')

print('create Ability table<br />')
cursor.execute('''CREATE TABLE Proficiency
        AbilityID       INTEGER PRIMARY KEY,
        Name            VARCHAR(100),
        Description     VARCHAR(1000)
        )''')

conn.commit()
cursor.close()
