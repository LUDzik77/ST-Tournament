#this one  should be changed to FACTORY design pattern
# TBD after more important  things a re working

import ST_classes


#"real" one  -  name, dmg, hp, cost, armour, active, cloak, flying, reach, detection, upgraded, photo):

# zerg when you hit "evolve" automaticaly creature posses button evolve

#Test_creature  = ("mutalisk", 4, 12, (2,100,100), 0, None, None, "mutalisk.png",["cloak", "flying", "reach", "detection",])
Mutalisk = ("Mutalisk", 4, 12, (2,100,100), 0, None, None, True, 1, None, None, "images/mutalisk.png" )

Zergling = ("Zergling", 2, 5, (1,25,0), 0, True, None, None, None, None, None, "images/zergling.png" )
Crackling = ("crackling", 6, 5, (0,25,0), 0, True, None, None, None, None, True )  

Marine = ("Marine", 3, 6, (1,50,0), 0, None, None, None, 1, None, None, "images/marine.png" )
Marine_stimpack = ("Marine (stimpack)", 4, 6, (1,50,0), 0, True, None, None, 1, None, True )

Hydralisk = ("hydralisk", 4, 10, (1,75,25), 0, None, None, None, 1, None, None, "images/hydralisk.png" )
Lurker = ("Lurker", 6, 15, (1,50,100), 0, None, True, None, None, None, True ) #active= cloak? or burrowed/siege = 1 turn

Zealot = ("Zealot", 3, 10, (2,100,0),  1, None, None, None, None, None, None, "images/zealot.gif" )
Chargelot = ("Chargelot", 3, 10, (2,100,0),  1, True, None, None, None, None, True )

Hellion = ("Hellion", 5, 10, (2,100,0), 0, None, None, None, None, None, None )
Hellbat = ("Hellbat", 5, 12, (2,100,0), 1, None, None, None, None, None, None )

Wright = ("Wright", 4, 13, (2,150,100), 0, True, None, True, 0.5, None, None, "images/wright.png" ) #Maybe  reach= "0.5" - reduced dmg to non-fly
Cloaked_Wright = ("Cloaked Wright", 6, 12, (2,150,100), 0, True, True, True, 0.5, None, True )

Dark_Templar = ("Dark Templar", 10, 8, (3,150,125),  0, None, True, None, None, None, None )
Dark_Templar_blink = ("Dark Templar (blink)", 10, 8, (3,200,150),  0, True, True, None, None, None, True )

Overlord = ("Overlord", 0, 25, (0,100,0), 0, True, None, True, None, True, True, "images/overlord.png" ) #gives +1 pop ?

Observer = ("Observer", 0, 5, (1,25,75), 0, True, True, True, None, True, True, "images/observer.png" )

Science_Vessel = ("Science Vessel", 0, 20, (3,100,225), 1, True, None, True, None, True, True, "images/science vessel.png" ) #?

Ultralisk = ("Ultralisk", 7, 30, (6,300,200), 2, None, None, None, None, None, None, "images/ultralisk.png" )

Carrier = ("Carrier", 6, 30, (6,350,200), 0, None, None, True, 1, None, None, "images/carrier.png" )

Scout = ("Scout", 6, 20, (3,275,125), 0, None, None, True, 0.5, None, None, "images/scout.png" ) #Maybe  reach= "0.5" - reduced dmg to non-fly

Battlecruiser = ("Battlecruiser", 5, 50, (8, 400, 300), 1, None, None, True, 1, None, None, "images/Battlecruiser.png" )

Siege_Tank = ("Siege Tank", 6, 15, (3,150,100), 0, None, None, None, None, None, None, "images/tank.png" )