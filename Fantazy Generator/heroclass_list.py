import random

def get_race_class(race):
    if race == "human":
        race_class = HUMAN_STARTING_CLASSES
    elif race == "elf":
        race_class = ELF_STARTING_CLASSES
    elif race == "dwarf":
        race_class = DWARF_STARTING_CLASSES
    elif race == "hobbit":
        race_class = HOBBIT_STARTING_CLASSES    
    return(race_class)


def find_heroclass_object(hero_class):
    if hero_class == "Warrior": return(WarriorHeroClass())
    if hero_class == "Ranger":  return(RangerHeroClass()) 
    if hero_class == "Rogue":   return(RogueHeroClass())
    if hero_class == "Acolyte": return(AcolyteHeroClass())


class HeroClass():
    def __str__(self):
        print(self.name)
    
    def get_1_skill(self):
        sum_to_randomize = sum([x for x in self.skilltree.values()])
        random_number = random.randint(1, sum_to_randomize)        
        for skill, chance in self.skilltree.items():
            random_number -= chance
            if random_number <= 0:
                return(skill)
        
class WarriorHeroClass(HeroClass):
    def __init__(self):
        self.name = "Warrior"
        self.skilltree = SKILLS_WARRIOR
        #mainskill = skill with double grow?
        #to_advance = skill which need to grow?

class RangerHeroClass(HeroClass):
    def __init__(self):
        self.name = "Ranger"
        self.skilltree = SKILLS_RANGER

class RogueHeroClass(HeroClass):
    def __init__(self):
        self.name = "Rogue"
        self.skilltree = SKILLS_ROGUE

class AcolyteHeroClass(HeroClass):
    def __init__(self):
        self.name = "Acolyte"
        self.skilltree = SKILLS_ACOLYTE


HUMAN_STARTING_CLASSES = {
    "Warrior": 4,
    "Ranger" : 2,
    "Rogue"  : 2,
    "Acolyte": 2   
}

ELF_STARTING_CLASSES = {
    "Warrior": 2,
    "Ranger" : 4,
    "Rogue"  : 2,
    "Acolyte": 2   
}

DWARF_STARTING_CLASSES = {
    "Warrior": 4,
    "Ranger" : 1,
    "Rogue"  : 2,
    "Acolyte": 1   
}

HOBBIT_STARTING_CLASSES = {
    "Warrior": 2,
    "Ranger" : 1,
    "Rogue"  : 4,
    "Acolyte": 2   
}




#growth per level for heroclass 
SKILLS_WARRIOR = {
"RES_GEN"     : 20,
"RES_CRIT"    : 10,
"RES_MELEE"   : 20,
"RES_PIERCING": 20,
"RES_MAGIC"   : 0,
"W_POLEARMS"  : 30,
"W_CLASSIC"   : 30,
"W_SMALL"     : 20,
"W_UNARMED"   : 20,
"W_BOW"       : 15,
"W_SPECIAL"   : 5,
"B_STRENGH "  : 5,
"B_DEXTERITY" : 5,
"B_INITIATIVE": 5,
"B_AIMING"    : 5,
"DUELIST"     : 1,
"LUCK"        : 0,
"LEADERSHIP"  : 0,
"FAMOUS"      : 1,
"M_MAGIC"     : 0,     
"M_WISDOM"    : 0
    }

SKILLS_RANGER = {
"RES_GEN"     : 10,
"RES_CRIT"    : 1,
"RES_MELEE"   : 10,
"RES_PIERCING": 10,
"RES_MAGIC"   : 0,
"W_POLEARMS"  : 0,
"W_CLASSIC"   : 10,
"W_SMALL"     : 15,
"W_UNARMED"   : 5,
"W_BOW"       : 30,
"W_SPECIAL"   : 15,
"B_STRENGH "  : 1,
"B_DEXTERITY" : 2,
"B_INITIATIVE": 6,
"B_AIMING"    : 6,
"DUELIST"     : 1,
"LUCK"        : 1,
"LEADERSHIP"  : 0,
"FAMOUS"      : 1,
"M_MAGIC"     : 0,     
"M_WISDOM"    : 0
    }

SKILLS_ROGUE = {
"RES_GEN"     : 0,
"RES_CRIT"    : 10,
"RES_MELEE"   : 1,
"RES_PIERCING": 20,
"RES_MAGIC"   : 0,
"W_POLEARMS"  : 0,
"W_CLASSIC"   : 10,
"W_SMALL"     : 30,
"W_UNARMED"   : 5,
"W_BOW"       : 5,
"W_SPECIAL"   : 15,
"B_STRENGH "  : 1,
"B_DEXTERITY" : 5,
"B_INITIATIVE": 3,
"B_AIMING"    : 3,
"DUELIST"     : 1,
"LUCK"        : 10,
"LEADERSHIP"  : 0,
"FAMOUS"      : 0,
"M_MAGIC"     : 0,     
"M_WISDOM"    : 0
    }

SKILLS_ACOLYTE = {
"RES_GEN"     : 1,
"RES_CRIT"    : 1,
"RES_MELEE"   : 1,
"RES_PIERCING": 1,
"RES_MAGIC"   : 5,
"W_POLEARMS"  : 0,
"W_CLASSIC"   : 1,
"W_SMALL"     : 5,
"W_UNARMED"   : 1,
"W_BOW"       : 0,
"W_SPECIAL"   : 5,
"B_STRENGH "  : 1,
"B_DEXTERITY" : 1,
"B_INITIATIVE": 2,
"B_AIMING"    : 1,
"DUELIST"     : 0,
"LUCK"        : 1,
"LEADERSHIP"  : 1,
"FAMOUS"      : 1,
"M_MAGIC"     : 10,     
"M_WISDOM"    : 10
    }

SKILLS_BARBARIAN = {
"RES_GEN"     : 25,
"RES_CRIT"    : 5,
"RES_MELEE"   : 5,
"RES_PIERCING": 5,
"RES_MAGIC"   : 5,
"W_POLEARMS"  : 30,
"W_CLASSIC"   : 10,
"W_SMALL"     : 1,
"W_UNARMED"   : 20,
"W_BOW"       : 1,
"W_SPECIAL"   : 0,
"B_STRENGH "  : 5,
"B_DEXTERITY" : 2,
"B_INITIATIVE": 0,
"B_AIMING"    : 0,
"DUELIST"     : 1,
"LUCK"        : 1,
"LEADERSHIP"  : 0,
"CRAFTY"      : 1,
"FAMOUS"      : 1,
"M_MAGIC"     : 0,     
"M_WISDOM"    : 0
    }

SKILLS_SORCERER = {
"RES_GEN"     : 1,
"RES_CRIT"    : 1,
"RES_MELEE"   : 1,
"RES_PIERCING": 1,
"RES_MAGIC"   : 5,
"W_POLEARMS"  : 0,
"W_CLASSIC"   : 1,
"W_SMALL"     : 2,
"W_UNARMED"   : 2,
"W_BOW"       : 0,
"W_SPECIAL"   : 1,
"B_STRENGH "  : 0,
"B_DEXTERITY" : 1,
"B_INITIATIVE": 3,
"B_AIMING"    : 1,
"DUELIST"     : 0,
"LUCK"        : 1,
"LEADERSHIP"  : 3,
"FAMOUS"      : 2,
"M_MAGIC"     : 15,     
"M_WISDOM"    : 5
    }

