print('Content-type: text/html\n\n')

import cgi
import cgitb; cgitb.enable()
import sqlite3

mydb = 'dnd.db'
conn = sqlite3.connect(mydb)
cursor = conn.cursor()

print('<title>D&D Database: Insert a Character</title>')
print('<link rel="stylesheet" href="../stylesheet.css">')

print('<h1>D&D Database</h1>')
print('<h2>Insert a Character</h2>')

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

values = { "name":name,"studentIDFK":studentIDFK,"class":cla,"background":background,"race":race,
        "alignment":alignment,"expPoints":expPoints,"str":strength, 
        "strSave":strSave,"dex":dex,"dexSave":dexSave,"con":con,
        "conSave":conSave,"int":intellegence,"intSave":intSave,"wis":wis,
        "wisSave":wisSave,"cha":cha,"chaSave":chaSave,"inspiration":inspiration,
        "profBonus":profBonus,"gold":gold,"hitPointMax":hitPointMax,
        "pTraits":pTraits,"ideals":ideals,"bonds":bonds,"flaws":flaws,
        "otherInfo":otherInfo}

cursor.execute('''
        INSERT INTO Character (Name, StudentIDFK, Class, Background, 
        Race, Alignment, ExpPoints, Inspiration, ProfBonus, Gold, HitPointMax, 
        Ptraits, Ideals, Bonds, Flaws, OtherInfo, Strength, Dexterity, Constitution,
        Intellegence, Wisdom, Charisma, StrSave, DexSave, ConSave, IntSave, WisSave, 
        ChaSave) 
        VALUES (:name, :studentIDFK, :class, :background,
        :race, :alignment, :expPoints, :inspiration, :profBonus, :gold, :hitPointMax,
        :pTraits, :ideals, :bonds, :flaws, :otherInfo, :str, :dex, :con, :int, :wis,
        :cha, :strSave, :dexSave, :conSave, :intSave, :wisSave, :chaSave)''', values)

print('Insertion completed<br>')
print('To add your character to a campaign navigate to the campaign menu '
        + 'then search for the campaign you want to add the character to<br><br>')
print('Spells, items, proficiencies and abilities can be added later if '
    +'you navigate to their respecive menus and use the search bar<br><br>')

print('<br/>')
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
