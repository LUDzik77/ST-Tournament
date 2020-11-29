import ST_classes

# zerg when you hit "evolve" automaticaly creature posses button evolve

#Test_creature  = ("mutalisk", 4, 12, (2,100,100), 0, None, None, "mutalisk.png",["cloak", "flying", "reach", "detection",])
Mutalisk = ("Mutalisk", 3, 10, (2,100,100), 0, True, None, True, 1, None, None, "images/mutalisk.png" )

Zergling = ("Zergling", 2, 4, (1,25,0), 0, True, None, None, None, None, None, "images/zergling.png" )
Crackling = ("crackling", 6, 5, (0,25,0), 0, True, None, None, None, None, True )  

Marine = ("Marine", 3, 5, (1,50,0), 0, None, None, None, 1, None, None, "images/marine.png" )
Marine_stimpack = ("Marine (stimpack)", 4, 6, (1,50,0), 0, True, None, None, 1, None, True )

Firebat = ("Firebat", 3, 5, (1,50,25), 1, None, None, None, None, None, None, "images/firebat.png" )

Hydralisk = ("Hydralisk", 4, 7, (1,75,25), 0, None, None, None, 1, None, None, "images/hydralisk.png" )
Lurker = ("Lurker", 6, 12, (1,50,100), 1, None, True, None, None, None, True ) #active= cloak? or burrowed/siege = 1 turn

Zealot = ("Zealot", 3, 9, (2,100,0),  1, None, None, None, None, None, None, "images/zealot.png" )
Chargelot = ("Chargelot", 3, 10, (2,100,0),  1, True, None, None, None, None, True )

Dragoon = ("Dragoon", 5, 12, (2,125,50), 0, None, None, None, 1, None, None, "images/dragoon.png" )
Stalker = ("Stalker", 4, 10, (2,100,50), 0, True, None, None, 1, None, None, "images/dragoon.png" )  # or Active with blink?
Immortal = ("Immortal", 6, 24, (4,275,100), 0, None, None, None, None, None, None, "images/dragoon.png" )   #shield - max dmd dlt =3 ?

Hellion = ("Hellion", 5, 8, (2,100,0), 0, None, None, None, None, None, None )
Hellbat = ("Hellbat", 5, 10, (2,100,0), 1, None, None, None, None, None, None )

Wright = ("Wright", 4, 10, (2,150,100), 0, True, None, True, 0.5, None, None, "images/wright.png" ) 
Cloaked_Wright = ("Cloaked Wright", 6, 12, (2,150,100), 0, True, True, True, 0.5, None, True )

Dark_Templar = ("Dark Templar", 7, 7, (3,150,125),  0, None, True, None, None, None, None, "images/dark templar.png")

Overlord = ("Overlord", 0, 15, (0,100,0), 0, True, None, True, None, True, True, "images/overlord.png" ) 

Observer = ("Observer", 0, 5, (1,25,75), 0, True, True, True, None, True, True, "images/observer.png" )

Science_Vessel = ("Science Vessel", 0, 20, (3,100,200), 1, True, None, True, None, True, True, "images/science vessel.png" ) #?

Ultralisk = ("Ultralisk", 8, 15, (6,300,200), 2, None, None, None, None, None, None, "images/ultralisk.png" )

Carrier = ("Carrier", 7, 30, (6,350,200), 0, None, None, True, 1, None, None, "images/carrier.png" )

Scout = ("Scout", 6, 20, (3,275,125), 0, None, None, True, 0.5, None, None, "images/scout.png" ) #Maybe  reach= "0.5" - reduced dmg to non-fly

Battlecruiser = ("Battlecruiser", 10, 50, (8, 400, 300), 0, None, None, True, 1, None, None, "images/Battlecruiser.png" )

Siege_Tank = ("Siege Tank", 7, 12, (3,150,100), 0, None, None, None, None, None, None, "images/tank.png" )