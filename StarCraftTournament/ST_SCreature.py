#this one  should be changed to FACTORY design pattern
# TBD after more important  things a re working

import ST_classes


#"real" one  - placement, name, dmg, hp, cost, armour, active, cloak, flying, reach, detection, upgraded, photo):

# zerg when you hit "evolve" automaticaly creature posses button evolve


Mutalisk = ("None", "mutalisk", 4, 12, (2,100,100), 0, None, None, True, 1, None, None, "mutalisk.png" )

Zergling = ("None", "zergling", 2, 5, (0,25,0), 0, True, None, None, None, None, None, "zergling.png" )
Crackling = ("None", "crackling", 6, 5, (0,25,0), 0, True, None, None, None, None, True )  #suicide option --> add

Marine = ("None", "Marine", 3, 6, (1,50,0), 0, None, None, None, True, None, None )
Marine_stimpack = ("None", "Marine (stimpack)", 4, 6, (1,50,0), 0, True, None, None, True, None, True )

Hydralisk = ("None", "hydralisk", 4, 10, (1,75,25), 0, None, None, None, True, None, None, "hydralisk.png" )
Lurker = ("None", "Lurker", 6, 15, (1,50,100), 0, None, True, None, None, None, True ) #active= cloak? or burrowed/siege = 1 turn

Zealot = ("None", "Zealot", 4, 15, (2,100,0),  1, None, None, None, None, None, None )
Chargelot = ("None", "Chargelot", 4, 15, (2,100,0),  1, True, None, None, None, None, True )

Hellion = ("None", "Hellion", 5, 10, (2,100, 0), 0, None, None, None, None, None, None )
Hellbat = ("None", "Hellbat", 5, 12, (2,100, 0), 1, None, None, None, None, None, None )

Wright = ("None", "Wright", 6, 12, (2,150, 100), 0, True, None, True, 0.5, None, None ) #Maybe  reach= "0.5" - reduced dmg to non-fly
Cloaked_Wright = ("None", "Cloaked Wright", 6, 12, (2,150, 100), 0, True, True, True, 0.5, None, True )

Dark_Templar = ("None", "Dark Templar", 10, 8, (3,150,125),  0, None, True, None, None, None, None )
Dark_Templar_blink = ("None", "Dark_Templar (blink)", 10, 8, (3,200,150),  0, True, True, None, None, None, True )

Overlord = ("None", "Overlord", 0, 25, (0,100, 0), 0, True, None, True, None, True, True ) #gives +1 pop ?

Observer = ("None", "Observer", 0, 5, (0, 25, 75), 0, True, True, True, None, True, True )

Science_Vessel = ("None", "Science_Vessel", 0, 20, (4, 100, 225), 1, True, None, True, None, True, True ) #?

Ultralisk = ("None", "ultralisk", 8, 50, (6,300,200), 2, None, None, None, None, None, None, "ultralisk.png" )