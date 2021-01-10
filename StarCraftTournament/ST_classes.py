#The file covers all funcions of the programme;
import random

from abc import ABC, abstractmethod


class creature:
    
    def __init__(self,placement):
        self.name = "<placeholder>" 
        self.dmg = 0
        self.hp = 2
        self.cost =(0,0,0)       # population, minerals, gas
        self.placement = "None"     
        self.armour = 0            
        self.active = None        
        self.cloak = None
        self.flying = None
        self.reach = None
        self.detection = None
        self.upgraded = None
        self.photo = "images/houses_small.png"       
        self.memo = ""
       
    def dmg_output (self, AA_AG_modification):
        if self.dmg == 0: return(0)
        elif AA_AG_modification == None: return(0)
        elif AA_AG_modification == 1: 
            return(random.randint(1, self.dmg))
        else:
            mod_dmg= int(self.dmg*self.reach)
            return(random.randint(1, mod_dmg))
    
    def attack(self,target):    
        if (self.flying) and (target.flying): 
            damage = self.dmg_output(1)
        elif (self.flying) and (target.flying == None):
            damage = self.dmg_output(self.reach)
        elif (self.flying==None) and (target.flying):
            damage = self.dmg_output(self.reach)
        elif (self.flying==None) and (target.flying==None): 
            damage = self.dmg_output(1)   
        else: print ("attack function error")
        real_dmg = damage-target.armour
        if real_dmg<0: real_dmg=0
        target.hp-=real_dmg
        if target.hp>0: 
            self.memo = (f"{self.name} deals {real_dmg} dmg to {target.name}.")
        else:        
            if isinstance(target, creature): 
                self.memo = (f"{self.name} kills {target.name}")
            else: self.memo = (f"{target.name} base was killed. you are victorious")
            
    def can_attack_target(self, target, active_player):
        if isinstance(target, player): return(True)
        if target.cloak:
            if active_player.has_detection() == False:
                return(False) 
        if target.flying:
            if self.name == "Guardian": return(False) 
            elif self.flying: return(True)
            else: 
                if self.reach == None: return(False)        
        return(True)
        
    def kill_workers_of(self, target, localisation):
        if localisation == "top": self.kill_workers_of_top(target)
        elif localisation == "down": self.kill_workers_of_down(target)
        else: print ("error_of_<kill_workers_of>")

    def kill_workers_of_top(self, target):
        if target.workers_top < 1: 
            self.attack(target)
        else:
            starting_workers = target.workers_top
            if self.flying: damage=self.dmg_output(self.reach)
            else: damage=self.dmg_output(1)
            
            for i in range (damage):
                target.remove_a_worker_top() 
            if target.workers_top > 0: 
                self.memo = (f"{self.name} kills {starting_workers-target.workers_top} workers on the top!")
            else:
                target.workers_top = 0
                self.memo=(f"{self.name} kills the last worker top")
        
    def kill_workers_of_down(self, target):
        if target.workers_down < 1: 
            self.attack(target)
        else:
            starting_workers = target.workers_down
            if self.flying: damage=self.dmg_output(self.reach)
            else: damage=self.dmg_output(1)            
            
            for i in range (damage):
                target.remove_a_worker_down() 
            if target.workers_down > 0: 
                self.memo = (f"{self.name} kills {starting_workers-target.workers_down} workers on the bottom!")
            else:
                target.workers_down = 0
                self.memo=(f"{self.name} kills the last worker on the bottom!")
  
    def stat_display(self):
        if self.name == "<placeholder>": return("no unit")
        show = (f"{self.name} {self.dmg}/{self.hp}")
        if self.armour > 0: 
            show += (f"({self.armour})")
        if self.cloak: show += ("(Inv)")
        if self.flying: show += ("(Fly)")
        if (self.reach==None) and (self.dmg>0) and self.flying: show += ("(Air)")
        elif (self.reach==0.5) and (self.dmg>0) and (self.flying): show += ("(lim AG)")
        if (self.reach==None) and (self.dmg>0) and (self.flying==None): show += ("(land)")
        elif (self.reach==0.5) and (self.dmg>0) and (self.flying==None): show += ("(lim. AA)")
        if self.detection: show += ("(D)")
        return (show)
    
    def photo_display(self):
        return(self.photo)
    
    

class SCreature(creature):
        def __init__(self, name, dmg,hp, cost, armour, active, cloak, flying, reach, detection, upgraded, photo):
            self.name = name
            self.dmg = dmg
            self.hp = hp
            self.cost = cost       # population, minerals, gas
            self.placement = "None"  # "left", "center", "right" + additional (?) for cand in player.option list
            self.armour = armour            # reduction of dmg_output
            self.active = active     # active will work for haste skill as well as for paralyze etc; it is turned off after a turn; 
            self.cloak = cloak
            self.flying = flying
            self.reach = reach
            self.detection = detection
            self.upgraded = upgraded
            self.photo = photo
            self.memo = ""

            
class player(ABC):

    def __init__(self, name, hp, workers_top, workers_down, color):
        self.name = name
        self.hp = hp
        self.workers_top = workers_top
        self.workers_down = workers_down
        self.armour = 0
        self.board = {"top":None, "center":None, "down":None}
        self.options = []
        self.pop_max = 32
        self.pop_in_use = 30
        self.overlord = 0
        self.flying = None
        self.resources = ((self.pop_max - self.pop_in_use), 100, 100)
        self.color = color
        self.memo = ""
        self.race = self.race()
        self.detection = None
        self.upgrades_register = []
        self.upgrades_done = []
        self.empty_slot_photo =[]

    @abstractmethod
    def race(cls): pass
    
    @abstractmethod
    def attack_sounds(self): pass
    
    def pick_random_slot_photos(self): 
        result = random.choices(self.slot_photo_list(), k = 3)
        self.empty_slot_photo = result
    
    def get_a_worker(self, localisation):
        if localisation == "top": self.workers_top += 1
        else: self.workers_down += 1
        new_pop =  self.resources[0] - 1
        new_resources = (new_pop, self.resources[1], self.resources[2])
        self.resources = new_resources
        self.pop_in_use +=  1
            
    def remove_a_worker_top(self):
        if self.workers_top <1: pass
        else: 
            self.workers_top -= 1
            new_pop =  self.resources[0] + 1
            new_resources = (new_pop, self.resources[1], self.resources[2])
            self.resources = new_resources
            self.pop_in_use -= 1
    
    def remove_a_worker_down(self):
        if self.workers_down <1: pass
        else: 
            self.workers_down -= 1
            new_pop =  self.resources[0] + 1
            new_resources = (new_pop, self.resources[1], self.resources[2])
            self.resources = new_resources
            self.pop_in_use -= 1 
           
    def has_detection(self):
        if self.detection == True: return(True)
        else:
            for placement, creature in self.board.items():
                if creature.detection == True: return(True)
        return(False)
        
    def stat_display(self):
        space=""
        if len(self.name) <5: space += " "
        if len(self.name) <3: space += " " 
        show = (f"{space}{self.name}{space}\n<{self.workers_top}>\n{self.hp}\n<{self.workers_down}>\n{self.resources[1]}\n{self.resources[2]}\n{self.pop_in_use}\{self.pop_max}")
        return (show)   
    
    def activate_all(self):
        for board,creature in self.board.items():
            if (creature != None) and  (creature.active == None):
                if ("Siege Mode" in [ upgrade.name for upgrade in self.upgrades_done]) and (creature.name == "Siege Tank"):
                    creature.active = "Setting up"
                    creature.memo ="Siege Tank transitioning to siege mode"
                else: 
                    creature.active = True
            elif (creature != None) and  (creature.active == "Setting up"):
                if creature.name == "Siege Tank": 
                    creature.memo = "Tank in a siege mode!"
                creature.active = True

class Zerg_player(player): 
    def race(cls):
        return("zerg")
    def slot_photo_list(self):
        return(["images/zerg_slot1.png", "images/zerg_slot2.png", "images/zerg_slot3.png",\
                "images/zerg_slot4.png", "images/zerg_slot5.png", "images/zerg_slot6.png",\
                "images/zerg_slot7.png"])
    def attack_sounds(self):
        return("sounds/zergling_hit.mp3")
    def upgrades_sounds(self):
        return("sounds/z_upgrade.mp3")
    def economy_sounds(self):
        return("sounds/z_economy.mp3")
    def on_play_sounds(self):
        return("sounds/z_play.mp3")
    def upgrade_complete_sounds(self):
        return("sounds/z_upgrade_complete.mp3")
    def not_enough_sounds(self):
        return("sounds/z_not_enough_minerals.mp3") 
    def lurker_burrow_sounds(self):
        return("sounds/lurker_burrow.mp3")
    def guardian_sounds(self):
        return("sounds/guardian.mp3")    
    def worker_sounds(self):
        return("sounds/z_worker.mp3")
    def house_sounds(self):
        return("sounds/z_house.mp3")    
    
class Terran_player(player): 
    def race(cls):
        return("terran")
    def slot_photo_list(self):
        return(["images/terran_slot1.png", "images/terran_slot2.png", "images/terran_slot3.png",\
                "images/terran_slot4.png", "images/terran_slot5.png", "images/terran_slot6.png",\
                "images/terran_slot7.png"])    
    def attack_sounds(self):
        return("sounds/marine_fire.mp3")
    def upgrades_sounds(self):
        return("sounds/t_upgrade.mp3")
    def economy_sounds(self):
        return("sounds/t_economy.mp3")
    def on_play_sounds(self):
        return("sounds/t_play.mp3")
    def upgrade_complete_sounds(self):
        return("sounds/t_upgrade_complete.mp3")
    def not_enough_sounds(self):
        return("sounds/t_not_enough_minerals.mp3")  
    def siege_mode_sounds(self):
        return("sounds/siege_tank_transform.mp3")
    def worker_sounds(self):
        return("sounds/t_worker.mp3")
    def house_sounds(self):
        return("sounds/t_house.mp3")        
    
class Protoss_player(player): 
    def race(cls):
        return("protoss")
    def slot_photo_list(self):
        return(["images/protoss_slot1.png", "images/protoss_slot2.png", "images/protoss_slot3.png",\
                "images/protoss_slot4.png", "images/protoss_slot5.png", "images/protoss_slot6.png",\
                "images/protoss_slot7.png"])
    def attack_sounds(self):
        return("sounds/zealot_blade.mp3")
    def upgrades_sounds(self):
        return("sounds/p_upgrade.mp3")   
    def economy_sounds(self):
        return("sounds/p_economy.mp3")
    def on_play_sounds(self):
        return("sounds/p_play.mp3")
    def upgrade_complete_sounds(self):
        return("sounds/p_upgrade_complete.mp3")
    def not_enough_sounds(self):
        return("sounds/p_not_enough_minerals.mp3")
    def worker_sounds(self):
        return("sounds/p_worker.mp3")
    def house_sounds(self):
        return("sounds/p_house.mp3")        

class upgrade(): 
    def __init__(self, name, cost, description, photo, sound):
        self.name = name
        self.cost = cost
        self.description = description
        self.cooldown = 0
        self.photo = photo
        self.sound = sound


class resource_patch:
    def __init__(self, resources):
        self.resources = resources
        self.depeted = None

class mineral_patch(resource_patch): pass

class gas_patch(resource_patch): pass
    
