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
print('<h2>Insert sample data</h2>')

# Tabs have been removed so that they don't appear in data

print('Insert sample students<br>')
cursor.execute('''
INSERT INTO Student (StudentID, FirstName, LastName, Year) VALUES 
(1038387,   "Caleb",    "Miles",    5),
(1028983,   "Daquan",   "Lopez",    6),
(1088611,   "Caldwell", "Santos",   12),
(1031582,   "Burke",    "Luna",     6),
(1082808,   "Plato",    "Simpson",  5),
(1082129,   "Julian",   "Butler",   9),
(1000607,   "Lawrence", "Warner",   11),
(1005740,   "Lev",      "Morin",    9),
(1075728,   "Reece",    "Puckett",  5),
(1043641,   "Garrison", "Steele",   7)
''')

print('Insert sample campaigns<br>')
cursor.execute('''
INSERT INTO Campaign (StudentIDFK, CampaignName) VALUES
("Lost Mine of Phandelver",     1028983),
("Hoard of the Dragon Queen",   1088611)
''')

print('Insert sample characters<br>')
cursor.execute('''
INSERT INTO Character (Name, StudentIDFK, CampaignIDFK, Class, Background, 
Race, Alignment, ExpPoints, Inspiration, ProfBonus, Gold, HitPointMax, 
Ptraits, Ideals, Bonds, Flaws, OtherInfo, Strength, Dexterity, Constitution,
Intellegence, Wisdom, Charisma, StrSave, DexSave, ConSave, IntSave, WisSave, 
ChaSave) VALUES 
("Angelica Ashley", 1038387, 1, "Warlock", "Beast Hunter", "Human", 
"Lawful Neutral", 185223, 0, 3, 147, 197, "imperdiet dictum magna. Ut 
tincidunt orci quis lectus. Nullam suscipit, est ac", "Nulla tempor augue ac 
ipsum. Phasellus vitae mauris sit amet lorem semper auctor. Mauris vel 
turpis.", "eleifend. Cras sed leo. Cras vehicula aliquet libero. Integer in 
magna. Phasellus dolor elit, pellentesque a, facilisis non, bibendum sed,", 
"vitae velit egestas lacinia. Sed congue, elit sed consequat auctor, nunc 
nulla vulputate", "dictum mi, ac mattis velit justo nec ante. Maecenas mi 
felis, adipiscing fringilla, porttitor vulputate, posuere vulputate, lacus.", 
8, 15, 13, 17, 16, 9, 1, 0, 1, 1, 0, 1),

("Chloe Macias", 1028983, 2, "Barbarian", "Slave", "Half-Orc", "Chaotic Good", 
332133, 1, 5, 788, 150, "vel pede blandit congue. In scelerisque scelerisque 
dui. Suspendisse ac metus vitae velit egestas lacinia. Sed congue, elit sed", 
"adipiscing elit. Aliquam auctor, velit eget laoreet posuere, enim nisl 
elementum", "tortor. Nunc commodo auctor velit. Aliquam nisl. Nulla eu neque 
pellentesque massa lobortis ultrices. Vivamus rhoncus. Donec est. Nunc", 
"vitae, posuere at, velit. Cras lorem lorem, luctus ut, pellentesque eget, 
dictum placerat,", "magna et ipsum cursus vestibulum. Mauris magna. Duis 
dignissim tempor arcu. Vestibulum ut eros non enim commodo hendrerit. Donec 
porttitor", 10, 18, 14, 14, 20, 15, 1, 0, 1, 0, 1, 0),

("Sonia Wheeler", 1031582, 1, "Sorcerer", "Adventurer", "Human", "Lawful Good", 
72424, 0, 5, 234, 71, "mauris blandit mattis. Cras eget nisi dictum augue 
malesuada malesuada. Integer id magna et ipsum cursus vestibulum. Mauris 
magna.", "tristique pellentesque, tellus sem mollis dui, in sodales elit erat 
vitae", "Duis risus odio, auctor vitae, aliquet nec, imperdiet nec, leo. 
Morbi neque tellus,", "lectus ante dictum mi, ac mattis velit justo nec ante. 
Maecenas mi felis, adipiscing fringilla, porttitor vulputate, posuere", 
"Mauris vestibulum, neque sed dictum eleifend, nunc risus varius orci, in 
consequat enim", 17, 18, 10, 9, 18, 14, 1, 0, 0, 1, 1, 0),

("Hanna Chapman", 1082808, 1, "Wizard", "Apothecary", "Half-Elf", "Chaotic Good", 
92553, 1, 3, 742, 161, "mi pede, nonummy ut, molestie in, tempus eu, ligula. 
Aenean euismod mauris eu elit. Nulla facilisi. Sed", "in, dolor. Fusce 
feugiat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aliquam 
auctor,", "per conubia nostra, per inceptos hymenaeos. Mauris ut quam vel 
sapien imperdiet", "sit amet nulla. Donec non justo. Proin non massa non ante 
bibendum ullamcorper. Duis cursus, diam at pretium aliquet,", "Duis ac arcu. 
Nunc mauris. Morbi non sapien molestie orci tincidunt adipiscing. Mauris 
molestie", 9, 11, 14, 9, 12, 15, 0, 0, 0, 1, 0, 1),

("Sawyer Arnold", 1082129, 1, "Druid", "Alchemist", "Tiefling", "Lawful Neutral", 
63642, 0, 4, 221, 44, "magna, malesuada vel, convallis in, cursus et, eros. 
Proin ultrices. Duis volutpat nunc sit amet metus. Aliquam", "vitae, posuere 
at, velit. Cras lorem lorem, luctus ut, pellentesque eget, dictum", "euismod 
enim. Etiam gravida molestie arcu. Sed eu nibh vulputate", "Quisque fringilla 
euismod enim. Etiam gravida molestie arcu. Sed eu nibh vulputate", "mauris 
sit amet lorem semper auctor. Mauris vel turpis. Aliquam adipiscing lobortis 
risus.", 14, 19, 13, 10, 18, 15, 1, 0, 1, 1, 1, 1),

("Mark Meadows", 1000607, 2, "Cleric", "Bounty Hunter", "Gnome", "Neutral Good", 
58358, 0, 4, 330, 40, "aliquet lobortis, nisi nibh lacinia orci, consectetuer 
euismod est arcu", "tellus justo sit amet nulla. Donec non justo. Proin non", 
"Fusce mollis. Duis sit amet diam eu dolor egestas rhoncus. Proin nisl sem, 
consequat nec, mollis", "Vivamus nibh dolor, nonummy ac, feugiat non, 
lobortis quis, pede. Suspendisse dui. Fusce", "facilisis vitae, orci. 
Phasellus dapibus quam quis diam. Pellentesque habitant morbi tristique", 15, 
9, 11, 14, 14, 10, 0, 0, 1, 0, 0, 0),

("Ila Burnett", 1005740, 2, "Monk", "Alchemist", "Dwarf", "Lawful Good", 27966, 1, 
2, 585, 169, "nulla. Cras eu tellus eu augue porttitor interdum. Sed auctor 
odio a purus. Duis elementum, dui quis accumsan convallis,", "eget mollis 
lectus pede et risus. Quisque libero lacus, varius et, euismod et,", "sed 
dictum eleifend, nunc risus varius orci, in consequat enim diam vel arcu. 
Curabitur ut", "in lobortis tellus justo sit amet nulla. Donec non justo. 
Proin non massa non ante bibendum", "Nunc laoreet lectus quis massa. Mauris 
vestibulum, neque sed dictum", 11, 18, 14, 16, 10, 8, 1, 1, 0, 1, 1, 0),

("Molly Bailey", 1075728, 1, "Wizard", "Amnesiac", "Elf", "Neutral Good", 123387, 
0, 2, 701, 2, "vitae odio sagittis semper. Nam tempor diam dictum sapien. 
Aenean massa.", "eu enim. Etiam imperdiet dictum magna. Ut tincidunt orci 
quis lectus. Nullam", "molestie dapibus ligula. Aliquam erat volutpat. Nulla 
dignissim. Maecenas ornare egestas ligula. Nullam feugiat placerat velit. 
Quisque varius. Nam porttitor", "fringilla mi lacinia mattis. Integer eu 
lacus. Quisque imperdiet, erat nonummy ultricies ornare,", "Maecenas ornare 
egestas ligula. Nullam feugiat placerat velit. Quisque varius. Nam porttitor 
scelerisque neque. Nullam nisl. Maecenas malesuada fringilla est.", 11, 15, 
10, 18, 17, 15, 1, 0, 1, 0, 0, 0),

("Sebastian Jacobs", 1043641, 1, "Druid", "Bounty Hunter", "Dwarf", "Lawful 
Neutral", 85025, 0, 5, 874, 102, "Proin dolor. Nulla semper tellus id nunc 
interdum feugiat. Sed", "massa. Suspendisse eleifend. Cras sed leo. Cras 
vehicula aliquet libero. Integer in", "vitae semper egestas, urna justo 
faucibus lectus, a sollicitudin orci sem eget massa. Suspendisse eleifend. 
Cras sed leo. Cras vehicula", "justo. Proin non massa non ante bibendum 
ullamcorper. Duis cursus,", "magna. Praesent interdum ligula eu enim. Etiam 
imperdiet dictum magna. Ut tincidunt orci quis lectus. Nullam suscipit, est 
ac", 20, 11, 11, 11, 11, 13, 1, 1, 0, 0, 0, 0),

("Samson Booth", 1043641, 2, "Fighter", "Doctor", "Human", "Neutral Good", 64938, 
1, 6, 293, 164, "Morbi non sapien molestie orci tincidunt adipiscing. Mauris 
molestie pharetra", "risus odio, auctor vitae, aliquet nec, imperdiet nec, 
leo. Morbi neque tellus, imperdiet non, vestibulum nec, euismod in,", 
"imperdiet non, vestibulum nec, euismod in, dolor. Fusce feugiat. Lorem ipsum 
dolor sit amet, consectetuer adipiscing", "penatibus et magnis dis parturient 
montes, nascetur ridiculus mus. Proin vel arcu eu odio tristique pharetra.", 
"nisi. Mauris nulla. Integer urna. Vivamus molestie dapibus ligula. Aliquam", 
8, 12, 12, 20, 17, 20, 0, 1, 1, 0, 1, 0)
''')

print('Insert sample spells<br>')
cursor.execute('''
INSERT INTO Spell (Name, Level, Description) VALUES 
("Acid Arrow", 2,
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
2nd.'),

("Alarm", 1,
'You set an alarm against unwanted intrusion.\n
Choose a door, a window, or an area within range 
that is no larger than a 20-foot cube. Until the spell 
ends, an alarm alerts you whenever a Tiny or larger 
creature touches or enters the warded area. When 
you cast the spell, you can designate creatures that 
won’t set off the alarm. You also choose whether the 
alarm is mental or audible.\n
A mental alarm alerts you with a ping in your 
mind if you are within 1 mile of the warded area.\n 
This ping awakens you if you are sleeping.\n
An audible alarm produces the sound of a hand 
bell for 10 seconds within 60 feet.'),

("Alter Self ", 2,
'You assume a different form. When you cast the spell, 
choose one of the following options, the effects of 
which last for the duration of the spell. While the 
spell lasts, you can end one option as an action to 
gain the benefits of a different one.\n
Aquatic Adaptation. You adapt your body to an 
aquatic environment, sprouting gills and growing 
webbing between your fingers. You can breathe 
underwater and gain a swimming speed equal to 
your walking speed.\n
Change Appearance. You transform your 
appearance. You decide what you look like, including 
your height, weight, facial features, sound of your 
voice, hair length, coloration, and distinguishing 
characteristics, if any. You can make yourself appear 
as a member of another race, though none of your 
statistics change. You also can’t appear as a creature 
of a different size than you, and your basic shape 
stays the same; if you’re bipedal, you can’t use this 
spell to become quadrupedal, for instance. At any time 
for the duration of the spell, you can use your action 
to change your appearance in this way again.\n 
Natural Weapons. You grow claws, fangs, spines, 
horns, or a different natural weapon of your choice. 
Your unarmed strikes deal ld6 bludgeoning, 
piercing, or slashing damage, as appropriate to the 
natural weapon you chose, and you are proficient 
with your unarmed strikes. Finally, the natural 
weapon is magic and you have a +1 bonus to the 
attack and damage rolls you make using it.'),

("Animal Messenger", 2,
'By means of this spell, you use an animal to deliver a 
message. Choose a Tiny beast you can see within 
range, such as a squirrel, a blue jay, or a bat. You 
specify a location, which you must have visited, and 
a recipient who matches a general description, such 
as "a man or woman dressed in the uniform of the 
town guard” or "a red-haired dwarf wearing a 
pointed hat." You also speak a message of up to 
twenty-five words. The target beast travels for the 
duration of the spell toward the specified location, 
covering about 50 miles per 24 hours for a flying 
messenger, or 25 miles for other animals.\n
When the messenger arrives, it delivers your 
message to the creature that you described, 
replicating the sound of your voice. The messenger 
speaks only to a creature matching the description 
you gave. If the messenger doesn’t reach its 
destination before the spell ends, the message is lost, 
and the beast makes its way back to where you cast 
this spell.\n
At Higher Levels. If you cast this spell using a spell 
slot of 3nd level or higher, the duration of the spell 
increases by 48 hours for each slot level above 2nd.'),

("Animal Shapes", 8,
'Your magic turns others into beasts. Choose any 
number of willing creatures that you can see within 
range. You transform each target into the form of a 
Large or smaller beast with a challenge rating of 4 or 
lower. On subsequent turns, you can use your action 
to transform affected creatures into new forms.\n
The transformation lasts for the duration for each 
target, or until the target drops to 0 hit points or dies. 
You can choose a different form for each target. A 
target’s game statistics are replaced by the statistics 
of the chosen beast, though the target retains its 
alignment and Intelligence, Wisdom, and Charisma 
scores. The target assumes the hit points of its new 
form, and when it reverts to its normal form, it 
returns to the number of hit points it had before it 
transformed. If it reverts as a result of dropping to 0 
hit points, any excess damage carries over to its 
normal form. As long as the excess damage doesn’t 
reduce the creature’s normal form to 0 hit points, it 
isn’t knocked unconscious. The creature is limited in 
the actions it can perform by the nature of its new 
form, and it can’t speak or cast spells.\n
The target’s gear melds into the new form. The 
target can’t activate, wield, or otherwise benefit 
from any of its equipment.'),

("Animate Dead", 3,
'This spell creates an undead servant. Choose a pile 
of bones or a corpse of a Medium or Small humanoid 
within range. Your spell imbues the target with a 
foul mimicry of life, raising it as an undead creature. 
The target becomes a skeleton if you chose bones or 
a zombie if you chose a corpse (the GM has the 
creature’s game statistics).\n
On each of your turns, you can use a bonus action 
to mentally command any creature you made with 
this spell if the creature is within 60 feet of you (if 
you control multiple creatures, you can command 
any or all of them at the same time, issuing the same 
command to each one). You decide what action the 
creature will take and where it will move during its 
next turn, or you can issue a general command, such 
as to guard a particular chamber or corridor. If you 
issue no commands, the creature only defends itself 
against hostile creatures. Once given an order, the 
creature continues to follow it until its task is 
complete.\n
The creature is under your control for 24 hours, 
after which it stops obeying any command you’ve 
given it. To maintain control of the creature for 
another 24 hours, you must cast this spell on the 
creature again before the current 24-hour period 
ends. This use of the spell reasserts your control 
over up to four creatures you have animated with 
this spell, rather than animating a new one.\n
At Higher Levels. When you cast this spell using a 
spell slot of 4th level or higher, you animate or 
reassert control over two additional undead 
creatures for each slot level above 3rd. Each of the 
creatures must come from a different corpse or pile 
of bones.'),

("Antilife Shell", 5,
'A shimmering barrier extends out from you in a 10- 
foot radius and moves with you, remaining centered 
on you and hedging out creatures other than undead 
and constructs. The barrier lasts for the duration.\n
The barrier prevents an affected creature from 
passing or reaching through. An affected creature 
can cast spells or make attacks with ranged or reach 
weapons through the barrier.\n
If you move so that an affected creature is forced 
to pass through the barrier, the spell ends.'),

("Antimagic Field", 8,
'A 10-foot-radius invisible sphere of antimagic 
surrounds you. This area is divorced from the 
magical energy that suffuses the multiverse. Within 
the sphere, spells can’t be cast, summoned creatures 
disappear, and even magic items become mundane. 
Until the spell ends, the sphere moves with you, 
centered on you.
Spells and other magical effects, except those 
created by an artifact or a deity, are suppressed in 
the sphere and can’t protrude into it. A slot 
expended to cast a suppressed spell is consumed. 
While an effect is suppressed, it doesn’t function, but 
the time it spends suppressed counts against its 
duration.\n
Targeted Effects. Spells and other magical effects, 
such as magic missile and charm person, that target a 
creature or an object in the sphere have no effect on 
that target.\n
Areas of Magic. The area of another spell or 
magical effect, such as fireball, can’t extend into the 
sphere. If the sphere overlaps an area of magic, the 
part of the area that is covered by the sphere is 
suppressed. For example, the flames created by a 
wall of fire are suppressed within the sphere, 
creating a gap in the wall if the overlap is large 
enough.\n
Spells. Any active spell or other magical effect on a 
creature or an object in the sphere is suppressed 
while the creature or object is in it.\n
Magic Items. The properties and powers of magic 
items are suppressed in the sphere. For example, a 
+1 longsword in the sphere functions as a 
nonmagical longsword.\n
A magic weapon’s properties and powers are 
suppressed if it is used against a target in the sphere 
or wielded by an attacker in the sphere. If a magic 
weapon or a piece of magic ammunition fully leaves 
the sphere (for example, if you fire a magic arrow or 
throw a magic spear at a target outside the sphere), 
the magic of the item ceases to be suppressed as 
soon as it exits.\n
Magical Travel. Teleportation and planar travel 
fail to work in the sphere, whether the sphere is the 
destination or the departure point for such magical 
travel. A portal to another location, world, or plane 
of existence, as well as an opening to an 
extradimensional space such as that created by the 
rope trick spell, temporarily closes while in the 
sphere.\n
Creatures and Objects. A creature or object 
summoned or created by magic temporarily winks 
out of existence in the sphere. Such a creature 
instantly reappears once the space the creature 
occupied is no longer within the sphere.\n
Dispel Magic. Spells and magical effects such as 
dispel magic have no effect on the sphere. Likewise, 
the spheres created by different antimagic field 
spells don’t nullify each other.')
''')

print('Insert sample proficiencies<br>')
cursor.execute('''INSERT INTO Proficiency (Name, Attribute) VALUES
("Acrobatics",      "Dex"),
("Animal Handling", "Wis"),
("Arcana",          "Int"),
("Athletics",       "Str"),
("Deception",       "Cha"),
("History",         "Int"),
("Insight",         "Wis"),
("Intimidation",    "Cha"),
("Investigation",   "Int"),
("Medicine",        "Wis"),
("Nature",          "Int"),
("Perception",      "Wis"),
("Performance",     "Cha"),
("Persuasion",      "Cha"),
("Religion",        "Int"),
("Sleight of Hand", "Dex"),
("Stealth",         "Dex"),
("Survival",        "Wis")
''')

print('Insert sample items<br>')
cursor.execute('''INSERT INTO Item (Name, Description) VALUES
("Acid",
'As an action, you can splash the contents of 
this vial onto a creature within 5 feet of you or throw 
the vial up to 20 feet, shattering it on impact. In 
either case, make a ranged attack against a creature 
or object, treating the acid as an improvised weapon. 
On a hit, the target takes 2d6 acid damage.'),

("Alchemist’s Fire",
'This sticky, adhesive fluid ignites 
when exposed to air. As an action, you can throw this 
flask up to 20 feet, shattering it on impact. Make a 
ranged attack against a creature or object, treating 
the alchemist’s fire as an improvised weapon. On a 
hit, the target takes ld4 fire damage at the start of 
each of its turns. A creature can end this damage by 
using its action to make a DC 10 Dexterity check to 
extinguish the flames.'),

("Antitoxin",
'A creature that drinks this vial of liquid 
gains advantage on saving throws against poison for 
1 hour. It confers no benefit to undead or constructs.'),

("Arcane Focus",
'An arcane focus is a special item — 
an orb, a crystal, a rod, a specially constructed staff, a 
wand-like length of wood, or some similar item — 
designed to channel the power of arcane spells. A
sorcerer, warlock, or wizard can use such an item as 
a spellcasting focus.'),

("Ball Bearings",
'As an action, you can spill these 
tiny metal balls from their pouch to cover a level, 
square area that is 10 feet on a side. A creature 
moving across the covered area must succeed on a 
DC 10 Dexterity saving throw or fall prone. A 
creature moving through the area at half speed 
doesn’t need to make the save.'),

("Block and Tackle",
'A set of pulleys with a cable 
threaded through them and a hook to attach to 
objects, a block and tackle allows you to hoist up to 
four times the weight you can normally lift.'),

("Book",
'A book might contain poetry, historical 
accounts, information pertaining to a particular field 
of lore, diagrams and notes on gnomish contraptions, 
or just about anything else that can be represented 
using text or pictures. A book of spells is a spellbook.'),

("Caltrops",
'As an action, you can spread a bag of 
caltrops to cover a square area that is 5 feet on a side. 
Any creature that enters the area must succeed on a 
DC 15 Dexterity saving throw or stop moving this 
turn and take 1 piercing damage. Taking this damage 
reduces the creature’s walking speed by 10 feet until 
the creature regains at least 1 hit point. A creature 
moving through the area at half speed doesn’t need 
to make the save.'),

("Candle",
'For 1 hour, a candle sheds bright light in a 
5-foot radius and dim light for an additional 5 feet.'),

("Case, Crossbow Bolt",
'This wooden case can hold 
up to twenty crossbow bolts.')''')

print('Insert sample abilities<br>')
cursor.execute('''INSERT INTO Ability (Name, Description) VALUES
("Grappler",
'You’ve developed the skills necessary to hold your 
own in close-quarters grappling. You gain the 
following benefits:\n
• You have advantage on attack rolls against a 
creature you are grappling.\n
• You can use your action to try to pin a creature 
grappled by you. To do so, make another grapple 
check. If you succeed, you and the creature are 
both restrained until the grapple ends.'),

("Darkvision",
'You can see in dim light within 60 feet of you as if it 
were bright light, and in darkness as if it were dim
light. You can’t discern color in darkness, only shades 
of gray.'),

("Dwarven Resilience",
'You have advantage on 
saving throws against poison, and you have 
resistance against poison damage.'),

("Stonecunning",
'Whenever you make an 
Intelligence (History) check related to the origin of 
stonework, you are considered proficient in the 
History skill and add double your proficiency bonus 
to the check, instead of your normal proficiency 
bonus.'),

("Dwarven Toughness",
'Your hit point maximum 
increases by 1, and it increases by 1 every time you 
gain a level.'),

("Fey Ancestry",
'You have advantage on saving 
throws against being charmed, and magic can’t put 
you to sleep.'),

("Lucky",
'When you roll a 1 on the d20 for an attack 
roll, ability check, or saving throw, you can reroll the 
die and must use the new roll.'),

("Halfling Nimbleness",
'You can move through the 
space of any creature that is of a size larger than 
yours.'),

("Naturally Stealthy",
'You can attempt to hide even 
when you are obscured only by a creature that is at 
least one size larger than you.'),

("Tinker",
'You have proficiency with artisan’s tools 
(tinker’s tools). Using those tools, you can spend 1 
hour and 10 gp worth of materials to construct a 
Tiny clockwork device (AC 5, 1 hp). The device 
ceases to function after 24 hours (unless you spend 
1 hour repairing it to keep the device functioning), 
or when you use your action to dismantle it; at that 
time, you can reclaim the materials used to create it. 
You can have up to three such devices active at a 
time.\n
When you create a device, choose one of the 
following options:\n
Clockwork Toy. This toy is a clockwork animal, 
monster, or person, such as a frog, mouse, bird, 
dragon, or soldier. When placed on the ground, the 
toy moves 5 feet across the ground on each of your 
turns in a random direction. It makes noises as 
appropriate to the creature it represents.\n
Fire Starter. The device produces a miniature flame, 
which you can use to light a candle, torch, or 
campfire. Using the device requires your action. 
Music Box. When opened, this music box plays a 
single song at a moderate volume. The box stops 
playing when it reaches the song’s end or when it 
is closed.')
''')


print('<br/>')
print('Data insertion complete<br>')
print('<br/>')
print('<a href="../index.html">Return to homepage</a><br>')

conn.commit()
cursor.close()
