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
        self.photo = "larva.png"       # it have to match the position in view with list o photos
        self.memo = ""
        
    def attack(self,target):
        dmg_output=self.dmg-target.armour
        target.hp-=dmg_output
        if target.hp>0: 
            self.memo = (f"{self.name} deals {dmg_output} dmg to {target.name} base. {target.hp} hp left.")
        else:        
            if isinstance(target, creature): self.memo(f"{self.name} kills {target.name}")
            else: self.memo =(f"{target.name} base was killed. you are victorious")
    
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
                self.memo = (f"{self.name} kills {starting_workers-target.workers_top} {target.name}'s workers on the top!")
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
                self.memo = (f"{self.name} kills {starting_workers-target.workers_down} {target.name}'s workers on the bottom!")
            else:
                target.workers_top = 0
                self.memo=(f"{self.name} kills the last worker in location!\nOpponent economy is crippled")
                
  
    #it will be shown under/on the Photo and maybe in options to play
    def stat_display(self):
        if self.name == "<placeholder>":
            show = ("placeholder")
        else:
            show = (f"{self.name}: {self.dmg} / {self.hp}({self.armour})")
        return (str(show))
    
    def photo_display(self):
        return(self.photo)
    
    

    
#change creature SCreature later in design
class SCreature(creature):
        def __init__(self, placement, name, dmg,hp, cost, armour, active, cloak, flying, reach, detection, upgraded, photo):
            self.name = name
            self.dmg = dmg
            self.hp = hp
            self.cost = cost       # population, minerals, gas
            self.placement = placement    # "left", "center", "right" + additional (?) for cand in player.option list
            self.armour = armour            # reduction of dmg_output
            self.active = active     # active will work for haste skill as well as for paralyze etc; it is turned off after a turn; 
            self.cloak = cloak
            self.flying = flying
            self.reach = reach
            self.detection = detection
            self.upgraded = upgraded
            self.photo = photo

#It groups all actions of players
class player:
    
    def __init__(self, name, hp, workers_top, workers_down):
        self.name = name
        self.hp = hp
        self.workers_top = workers_top
        self.workers_down = workers_down
        self.armour = 0
        self.board = {"top":None, "center":None, "down":None}
        self.options = []
        self.race = None
        self.pop_max = 32
        self.pop_in_use = 30
        self.resources = ((self.pop_max - self.pop_in_use), 100, 100)
        self.memo = ""
    
    #displays the play options FOR USER
    def display_play(self):
        basic_show_play = enumerate([x for x in self.options], start=1)
        for count,item in basic_show_play:
            print(count, item.name)
    
    #early customisation, play options are pooled once the race is chosen
    # to used like that:  player.race=choose_race()
    def choose_race(self):
        command=""
        print(f"{self.name} please choose the race (zerg, terran, protoss): ")
        while command not in ["zerg", "terran", "protoss"]:
            command = input()
            if command =='zerg': return ("zerg")
            if command =='terran': return ("terran")
            if command =='protoss': return ("protoss")
    
    #hardcoded all creatures option for races;  we can move it  somehow later on ex. json        
    def creaturelist(self):
        if self.race ==  "zerg" : return ([creature(None), creature(None), creature(None),creature(None),creature(None),creature(None)])
        if self.race ==  "terran": return ([creature(None), creature(None), creature(None),creature(None),creature(None),creature(None)])
        if self.race ==  "protoss" : return ([creature(None), creature(None), creature(None),creature(None),creature(None),creature(None)])
        
    def pool_options(self, nr_creatures):
        pool=random.sample(self.creaturelist(), nr_creatures)
        self.options.extend(pool)
    
    def play(self):   
        self.play_creature()
    
    def play_creature(self):
        command="StarCraft_LoL"
        play_decision = []
        len(self.options)
        while command not in ["1","2","3","4","5","6","7","8","9"]\
              or int(command)>len(self.options):
            command= input(f'{self.name} choose a play: ')
            if command =='pass': 
                return(None)
        play_decision.append(self.options[int(command)-1])
        print("Choose a place on the board: ")
        while command not in ["top", "down", "center", "pass"]:           
            command= input()
            if command =='pass': 
                return(None)
        play_decision.append(command)
        print(f' You played {play_decision[0].name} on the {play_decision[1]}.')
        self.board[play_decision[1]] = play_decision[0]
        
    
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
    
    def show_board(self):
        print([f'{x}:{y.name}' for x,y in self.board.items() if y!=None])
    
    def activate_all(self):
        for board,creature in self.board.items():
            if creature !=None: creature.active=True


