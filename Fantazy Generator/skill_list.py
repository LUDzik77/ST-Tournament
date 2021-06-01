#FILE WITH SKILLLIST AND STARTLING SKILLS FOR RACE

def get_race_skill(race):
    if race == "human":
        race_skill = SKILLS_HUMAN
    elif race == "elf":
        race_skill = SKILLS_ELF
    elif race == "dwarf":
        race_skill = SKILLS_DWARF
    elif race == "hobbit":
        race_skill = SKILLS_HOBBIT     
    return(race_skill)

def get_skillname(skilllist):
    #map(lambda x skillist.ite)
    #dict(zip(ini_list, list(ini_dict.values())))
    pass


#All skills (technical name: game name)
ALL_SKILLS = {
#small resistance for all dmg
"RES_GEN"     : "Toughness",
#reduces critical strikes and nearly death situation
"RES_CRIT"    : "Fighting heart",
#specialized resistances
"RES_MELEE"   : "Stone skin",
"RES_PIERCING": "Arrowproof",
"RES_MAGIC"   : "Magic immune",
#melee weapons dmg/
"W_POLEARMS"  : "Big weapons",
"W_CLASSIC"   : "Normal weapons",
"W_SMALL"     : "Small weapons",
"W_UNARMED"   : "Unarmed combat",
#other weapons dmg
"W_BOW"      : "Archery",
#crossbow, gunpowder, sling
"W_SPECIAL"   : "Special weapons",

#dmg and durability
"B_STRENGH "  : "Strength",
#additional moves
"B_DEXTERITY" : "Dexterity",
#who move first
"B_INITIATIVE" : "Initiative",
#for all ranged weapons+magic
"B_AIMING"    : "Aiming",
#
#B_REGENERATION = 0
"DUELIST"      : "Duelist",
#critical strikes and gettting items
"LUCK"         : "Luck",
#more quests
#ADVENTURER = 0
"LEADERSHIP"   : "Leadership",
#workshop skill :)
"CRAFTY"   : "Crafty",
#CRAFTY = 0
##just an idea for dwarfs
#RUNES = 0
"FAMOUS"   : "Recognition",
##power of spells
"M_MAGIC"      : "Magic power",
##mana reg=number of spells per fight        
"M_WISDOM"     : "Wisdom"
#M_CURSES = 0
#M_BLESSINGS = 0
#SUMMONS = 0
}


SKILLS_HUMAN = {
"RES_GEN"     : 10,
"RES_CRIT"    : 10,
"RES_MELEE"   : 10,
"RES_PIERCING": 5,
"RES_MAGIC"   : 5,
"W_POLEARMS"  : 15,
"W_CLASSIC"   : 15,
"W_SMALL"     : 5,
"W_UNARMED"   : 10,
"W_BOW"       : 10,
"W_SPECIAL"   : 5,
"B_STRENGH "  : 5,
"B_DEXTERITY" : 5,
"B_INITIATIVE": 5,
"B_AIMING"    : 5,
"DUELIST"     : 10,
"LUCK"        : 10,
"LEADERSHIP"  : 15,
"CRAFTY"      : 5,
"FAMOUS"      : 5,
"M_MAGIC"     : 5,     
"M_WISDOM"    : 10
    }

SKILLS_ELF = {
"RES_GEN"     : 1,
"RES_CRIT"    : 5,
"RES_MELEE"   : 5,
"RES_PIERCING": 1,
"RES_MAGIC"   : 10,
"W_POLEARMS"  : 5,
"W_CLASSIC"   : 10,
"W_SMALL"     : 10,
"W_UNARMED"   : 1,
"W_BOW"       : 20,
"W_SPECIAL"   : 3,
"B_STRENGH "  : 2,
"B_DEXTERITY" : 15,
"B_INITIATIVE": 10,
"B_AIMING"    : 15,
"DUELIST"     : 15,
"LUCK"        : 10,
"LEADERSHIP"  : 5,
"CRAFTY"      : 1,
"FAMOUS"      : 5,
"M_MAGIC"     : 10,     
"M_WISDOM"    : 5
    }

SKILLS_DWARF = {
"RES_GEN"     : 15,
"RES_CRIT"    : 10,
"RES_MELEE"   : 15,
"RES_PIERCING": 15,
"RES_MAGIC"   : 10,
"W_POLEARMS"  : 5,
"W_CLASSIC"   : 15,
"W_SMALL"     : 10,
"W_UNARMED"   : 10,
"W_BOW"       : 1,
"W_SPECIAL"   : 15,
"B_STRENGH "  : 10,
"B_DEXTERITY" : 2,
"B_INITIATIVE": 1,
"B_AIMING"    : 5,
"DUELIST"     : 5,
"LUCK"        : 1,
"LEADERSHIP"  : 10,
"CRAFTY"      : 10,
"FAMOUS"      : 5,
"M_MAGIC"     : 5,     
"M_WISDOM"    : 1
    }

SKILLS_HOBBIT = {
"RES_GEN"     : 1,
"RES_CRIT"    : 5,
"RES_MELEE"   : 1,
"RES_PIERCING": 20,
"RES_MAGIC"   : 10,
"W_POLEARMS"  : 0,
"W_CLASSIC"   : 5,
"W_SMALL"     : 20,
"W_UNARMED"   : 5,
"W_BOW"       : 5,
"W_SPECIAL"   : 15,
"B_STRENGH "  : 2,
"B_DEXTERITY" : 10,
"B_INITIATIVE": 15,
"B_AIMING"    : 5,
"DUELIST"     : 3,
"LUCK"        : 20,
"LEADERSHIP"  : 1,
"CRAFTY"      : 3,
"FAMOUS"      : 5,
"M_MAGIC"     : 5,     
"M_WISDOM"    : 5
    }

