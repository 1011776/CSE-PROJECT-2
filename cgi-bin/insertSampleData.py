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
        spells don’t nullify each other.')''')

print('<br/>')
print('Data insertion complete<br>')
print('<br/>')
print('<a href="../index.html">Return to homepage</a><br>')
