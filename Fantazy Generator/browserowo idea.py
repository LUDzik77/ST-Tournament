from abc import ABCMeta, abstractclassmethod
from collections import Counter
import random
import skill_list, character_list, heroclass_list, name_list

#https://refactoring.guru/design-patterns/builder

class IHero ():
    
    def get_stats(self):
        return(self.name, self.heroclass.name, self.character, self.skills) 
    
    def randomize_starting_stats(self):
        race_skill = skill_list.get_race_skill(self.race)              
        full_list = []
        for i in range (0,5):
            sum_to_randomize = sum([x for x in race_skill.values()])
            random_number = random.randint(1, sum_to_randomize)
            for skill, chance in race_skill.items():
                random_number -= chance
                if random_number <= 0: 
                    full_list.append(skill)
                    break
        self.skills = (dict(Counter(full_list)))
        
    def randomize_starting_class(self): 
        race_class = heroclass_list.get_race_class(self.race)
        sum_to_randomize = sum([x for x in race_class.values()])
        random_number = random.randint(1, sum_to_randomize)
        hero_class = "to be updated"
        for heroclass_, chance in race_class.items():
            random_number -= chance
            if random_number <= 0:
                hero_class = heroclass_
                break
        hero_class_object = heroclass_list.find_heroclass_object(hero_class)
        return(hero_class_object)

        
    def randomize_character(self):
        race_character = character_list.get_race_character(self.race)
        full_list = []
        for trait, chance_ in race_character.items():
            random_number = random.randint(1,70)
            if chance_ >= random_number:
                full_list.append(trait)
        full_list = character_list.trim_traits(full_list)
        return(full_list)
        
    def add_skill(self, skill, *args, **kwargs):
        random_nr = random.randint(4,13)
        if "Force" in args:
            self.skills[skill] = 1
        elif skill in self.skills.keys():
            self.skills[skill] += 1
        elif random_nr < len(self.skills.keys()):          
            self.add_level_to_skill()
        else:         
            self.skills[skill] = 1
    
    def add_class_skill(self, *args, **kwargs):
        skill = self.heroclass.get_1_skill()
        self.add_skill(skill)
    
    def add_race_skill(self, *args, **kwargs):
        race_skill = skill_list.get_race_skill(self.race)              
        sum_to_randomize = sum([x for x in race_skill.values()])
        random_number = random.randint(1, sum_to_randomize)   
        for skill, chance in race_skill.items():
            random_number -= chance
            if random_number <= 0:
                self.add_skill(skill)
                break
    
    def add_level_to_skill(self):
        print("adding_level to s kill")
        skill = random.sample(self.skills.keys(), 1)
        print("adding:", skill)
        self.add_skill(*skill)
        
        

class Human (IHero):
    
    def __init__(self, *args):
        self.nickname = False
        self.race = "human"
        self.heroclass = self.randomize_starting_class()
        self.character = self.randomize_character()
        self.skills = {}
        self.active_abilities = []
        self.name = name_list.make_name(self.race)
        self.randomize_starting_stats()
        self.add_class_skill()

class Elf (IHero):
    
    def __init__(self, *args):
        self.name = "Unknown elf"
        self.nickname = False
        self.race = "elf"
        self.heroclass = self.randomize_starting_class()
        self.character = self.randomize_character()
        self.skills = {}
        self.active_abilities = []
        self.name = name_list.make_name(self.race)
        self.randomize_starting_stats()
        self.add_class_skill()
        
class Dwarf (IHero):
    
    def __init__(self, *args):
        self.name = "Unknown dwarf"
        self.nickname = False
        self.race = "dwarf"
        self.heroclass = self.randomize_starting_class()
        self.character = self.randomize_character()
        self.skills = {}
        self.active_abilities = []
        self.name = name_list.make_name(self.race)
        self.randomize_starting_stats()
        self.add_class_skill()
        
class Hobbit (IHero):
    
    def __init__(self, *args):
        self.name = "Unknown hobbit"
        self.nickname = False
        self.race = "hobbit"
        self.heroclass = self.randomize_starting_class()
        self.character = self.randomize_character()
        self.skills = {}
        self.active_abilities = []
        self.name = name_list.make_name(self.race)
        self.randomize_starting_stats()
        self.add_class_skill()
        
class HeroFactory():
    
    @staticmethod
    def get_hero(race, *args, **kwargs):
        try:
            if race == "human":
                return (Human(*args, **kwargs))
            elif race == "elf":
                return (Elf(*args, **kwargs))
            elif race == "dwarf":
                return (Dwarf(*args, **kwargs)) 
            elif race == "hobbit":
                return (Hobbit(*args, **kwargs))             
            raise AssertionError("race or args not found")
        except AssertionError as _error:
            print(_error)
    
            
if __name__ == "__main__":    
    HERO1 = HeroFactory.get_hero("human", 5)
    HERO2 = HeroFactory.get_hero("elf", 5)
    HERO3 = HeroFactory.get_hero("dwarf", 5)
    HERO4 = HeroFactory.get_hero("hobbit", 5)
    print(HERO1.get_stats())
    print(HERO2.get_stats())
    print(HERO3.get_stats())
    print(HERO4.get_stats())
    
    
    