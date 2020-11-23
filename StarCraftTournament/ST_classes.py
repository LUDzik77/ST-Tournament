#description of this file
#The file covers all funcions of the programme;
import random
import ST_model    #to use ST_model.add_to_memo() ;/ NO IT DOES NOT WORK ;/ so i have to


class creature:
    
    def __init__(self,placement):
        self.name = "<placeholder>" 
        self.dmg = 2
        self.hp = 5
        self.cost =(0,0,0)       # population, minerals, gas
        self.placement = "None"     
        self.armour = 0             # reduction of dmg_output
        self.active = None         # active will work for haste skill as well as for paralyze etc; it is turned off after a turn;
        self.cloak = None
        self.flying = None
        self.reach = None
        self.detection = None
        self.upgraded = None
        self.photo = "images/larva.png"       # it have to match the position in view with list o photos
        self.memo = ""
        
    def attack(self,target):
        dmg_output=self.dmg-target.armour
        target.hp-=dmg_output
        if target.hp>0: 
            self.memo = (f"{self.name} deals {dmg_output} dmg to {target.name}.")
        else:        
            if isinstance(target, creature): 
                self.memo =(f"{self.name} kills {target.name}")
            else: self.memo =(f"{target.name} base was killed. you are victorious")
            
    #for now flying only!
    def can_attack_target(self, target):
        if isinstance(target, player): return(True)
        elif target.flying:
            if self.flying: return(True)
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
            for i in range (self.dmg):
                target.remove_a_worker_top() 
            if target.workers_top > 0: 
                self.memo = (f"{self.name} kills {starting_workers-target.workers_top} workers on the top!")
            else:
                target.workers_top = 0
                self.memo=(f"{self.name} kills the last worker in location!\nOpponent economy is crippled")
        
    def kill_workers_of_down(self, target):
        if target.workers_down < 1: 
            self.attack(target)
        else:
            starting_workers = target.workers_down
            for i in range (self.dmg):
                target.remove_a_worker_down() 
            if target.workers_down > 0: 
                self.memo = (f"{self.name} kills {starting_workers-target.workers_down} workers on the bottom!")
            else:
                target.workers_top = 0
                self.memo=(f"{self.name} kills the last worker in location!\nOpponent economy is crippled")
                
  
    #it will be shown under/on the Photo and maybe in options to play
    def stat_display(self):
        if self.name == "<placeholder>": return("placeholder")

        show = (f"{self.name}: {self.dmg} / {self.hp}")
        if self.armour > 0: 
            show += (f"({self.armour})")
        if self.cloak: show += (" (Inv.) ")
        if self.flying: show += (" (Fly)")
        if (self.reach==None) and (self.dmg>0) and self.flying: show += (" (AA only)")
        elif (self.reach==0.5) and (self.dmg>0) and (self.flying): show += (" (lim. AG)")
        if (self.reach==None) and (self.dmg>0) and (self.flying==None): show += (" (land only)")
        elif (self.reach==0.5) and (self.dmg>0) and (self.flying==None): show += (" (lim. AA)")
        if self.detection: show += (" (Detector)")
        
        return (show)
    
    def photo_display(self):
        return(self.photo)
    
    

#change creature SCreature later in design
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


            
class player:

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
        self.overlord = 1
        self.resources = ((self.pop_max - self.pop_in_use), 100, 100)
        self.color = color
        self.memo = ""
        self.race = self.race()

    def race(cls): return(None)
    
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
        
    
    def stat_display(self):
        show = (f"{self.name}\n{self.workers_top}    \n{self.hp}   \n{self.workers_down}   \n{self.resources[1]}   \n{self.resources[2]}   \n{self.pop_in_use}\{self.pop_max}  ")
        return (str(show))
    
    def save_data(self, text):
        ST_model.Model.add_to_memo(text)
    
    def activate_all(self):
        for board,creature in self.board.items():
            if creature != None: creature.active = True


class Zerg_player(player): 
    def race(cls):
        return("zerg")
    
class Terran_player(player): 
    def race(cls):
        return("terran")    

class Protoss_player(player): 
    def race(cls):
        return("protoss")   



class resource_patch:
    def __init__(self, resources):
        self.resource = resources
        self.depeted = None

class mineral_patch(resource_patch): pass

class gas_patch(resource_patch): pass
    
