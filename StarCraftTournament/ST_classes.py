#description of this file
#The file covers all funcions of the programme;
import random


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
        
    def attack(self,target):
        dmg_output=self.dmg-target.armour
        target.hp-=dmg_output
        if target.hp>0: 
            print(f"{self.name}  attack deals {dmg_output} dmg to {target.name}. {target.hp} hp left.")
        else:        
            if isinstance(target, creature): print(f"{self.name} kills {target.name}")
            else: print(f"{target.name} base was killed. you are victorious")
    
    def kill_workers_of(self,target):
        if target.workers<1: 
            self.attack(target)
        else:
            dmg_output=self.dmg-target.armour
            target.workers-=dmg_output
            if target.workers>0: 
                print(f"{self.name} attack kills {dmg_output} {target.name}'s workers!")
            else:        
                print(f"{self.name} kills the last worker!\nHis economy is crippled")
  
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
    
    def __init__(self, name, hp, workers):
        self.name = name
        self.hp = hp
        self.workers = workers
        self.armour = 0
        self.board = {"top":None, "center":None, "down":None}
        self.options = []
        self.race = None
        self.pop_max = 32
        self.pop_in_use = 30
        self.resources = ((self.pop_max - self.pop_in_use), 100, 100)
    
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
    
    def stat_display(self):
        show = (f"{self.name}\n{self.hp}   \n{self.workers}   \n{self.resources[1]}   \n{self.resources[2]}   \n{self.pop_in_use}\{self.pop_max}")
        return (str(show))
    
    def show_board(self):
        print([f'{x}:{y.name}' for x,y in self.board.items() if y!=None])
    
    def activate_all(self):
        for board,creature in self.board.items():
            if creature !=None: creature.active=True


      
