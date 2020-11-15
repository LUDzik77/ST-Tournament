import ST_classes
import ST_SCreature
import random
import copy




class Model:
    
    def __init__(self, controller):

        self.controller = controller
        
        self.c1=ST_classes.creature("top")
        self.c2=ST_classes.creature("center")
        self.c3=ST_classes.creature("down")
        self.c4=ST_classes.creature("top")
        self.c5=ST_classes.creature("center")
        self.c6=ST_classes.creature("down")
        
        self.p1=ST_classes.player("Player1", 50, 30, 0)
        self.p2=ST_classes.player("Player2", 50, 15, 15)        
        
        self.t1=ST_classes.SCreature(*ST_SCreature.Zergling)
        self.t2=ST_classes.SCreature(*ST_SCreature.Hydralisk)
        self.t3=ST_classes.SCreature(*ST_SCreature.Mutalisk)
        self.t4=ST_classes.SCreature(*ST_SCreature.Ultralisk)        
        
        
        self.p1.board={"top":self.c1, "center":self.c2, "down":self.c3}
        self.p2.board={"top":self.c4, "center":self.c5, "down":self.c2}
        
        #we need to add an option to choos a race, can be in a pop up window"
        self.p1.race = "zerg"
        self.p2.race = "zerg"
        
        self.p1.options= [self.t1,self.t2,self.t3,self.t4, self.t1]
        #self.p2.pool_options(5)
        self.p2.options= [self.t1,self.t2,self.t3,self.t4, self.t1]
        
        self.active_player = self.p1
        self.inactive_player = self.p2        
        
        self.name_of_played_creature = ""
        self.game_memo_archive = "    ***Lets begin SC Tournament***\n"
   
    def creatures_data(self):
        results=(self.p1.board["top"].stat_display(), 
                self.p1.board["center"].stat_display(),
                self.p1.board["down"].stat_display(),
                self.p2.board["top"].stat_display(),
                self.p2.board["center"].stat_display(),
                self.p2.board["down"].stat_display() )
        return(results)
    
    def player_description_data(self):
        result = []
        result.append(self.p1.stat_display())
        result.append(self.p2.stat_display())
        return(result)
        
    
    def creatures_photo(self):
        results=(self.p1.board["top"].photo,
                self.p1.board["center"].photo,
                self.p1.board["down"].photo,
                self.p2.board["top"].photo,
                self.p2.board["center"].photo,
                self.p2.board["down"].photo)
        return(results)    
    
    def options_photo(self):
        results=[]
        for creature in self.active_player.options:
            results.append(creature.photo)
        return(results)     
    
    def options_name(self):
        results=[]
        for creature in self.active_player.options:
            results.append(creature.name)
        return(results)     
    
    def options_cost(self):
        results=[]
        for creature in self.active_player.options:
            results.append(creature.cost)
        return(results)         
    
    def creature_nr_by_name(self, name_query):
        for i in range(len(self.active_player.options)):
            if self.active_player.options[i].name == name_query: 
                result = (i)
        return (result)
    
    def creature_photo_by_name(self, name_query):
        for i in range(len(self.active_player.options)):
            if self.active_player.options[i].name == name_query: 
                result = (self.active_player.options[i].photo)
        return (result)
    
    
    def board_by_placement(self, placement_query):
        if placement_query =="top": result=1
        elif placement_query =="center": result=2
        elif placement_query =="down": result=3
        if self.active_player == self.p2: result+=3
        return(result)

    
    def creature_on_board(self, creature_name, placement):
        c_index = self.creature_nr_by_name(creature_name)  #-1 ?
        clone = copy.deepcopy(self.active_player.options[c_index])
        self.active_player.board[placement] = clone
        #for k,v in self.active_player.board.items(): 
        #    print (v.name)
 

    def placement_for_placeholders(self):
        result =[]
        if self.p1.board["top"] == None: result.append(1)
        if self.p1.board["center"] == None: result.append(2)
        if self.p1.board["down"] == None: result.append(3)
        if self.p2.board["top"] == None: result.append(4)
        if self.p2.board["center"] == None: result.append(5)
        if self.p2.board["down"] == None: result.append(6)
        #print(f" killed: nr {result} ")
        self.add_to_memo(f" killed: nr {result}  OMG NO!")
        return(result)           
    

    def enough_resources(self, cost):
        new_resources = tuple(map(lambda i, j: i - j, self.active_player.resources, cost))
        for i in new_resources:
            if i < 0: return(False)
        return(True)
    


    def take_resources_from_player(self, cost):
        new_resources = tuple(map(lambda i, j: i - j, self.active_player.resources, cost))
        self.active_player.resources = new_resources 
        self.active_player.pop_in_use+=cost[0]
    
    def creature_resource_cost(self, name_query):
        a_nr = self.creature_nr_by_name(name_query)
        return(self.active_player.options[a_nr].cost)
    

    def give_back_pop(self, a_player, a_creature_pop_cost):
        new_pop = a_creature_pop_cost + a_player.resources[0]
        new_resources = (new_pop, a_player.resources[1], a_player.resources[2])
        a_player.resources = new_resources
        a_player.pop_in_use -= a_creature_pop_cost
  
    def count_income(self, workers):
        #####################HERE
        workers_on_gas = (workers)//3
        
        if workers_on_gas>4: workers_on_gas=4
        
        workers_on_minerals = workers - workers_on_gas
        
        minerals_full = (8,3)
        minerals_limited = (12,2)
        minerals_limited2 = (36,1)
        minerals_gain=0
        for worker in range(workers_on_minerals):
            if worker <= minerals_full[0]: minerals_gain += minerals_full[1]
            elif worker <= minerals_limited[0]: minerals_gain += minerals_limited[1]
            elif worker <= minerals_limited2[0]: minerals_gain += minerals_limited2[1]
          
        gas_full = 4
        gas_depeted = 1   #to implement in the future
        gas_gain = workers_on_gas * gas_full 
        return([minerals_gain, gas_gain])
        
    def produce_income(self):
        minerals = self.count_income(self.active_player.workers_top)[0] + \
        self.count_income(self.active_player.workers_down)[0]
        gas = self.count_income(self.active_player.workers_top)[1] + \
            self.count_income(self.active_player.workers_down)[1]
        
        self.add_to_memo(f"You earn {minerals} minerals and {gas} gas.")
        
        updated_minerals = minerals + self.active_player.resources[1]
        updated_gas = gas + self.active_player.resources[2]
        
        player_new_resources = (self.active_player.resources[0], updated_minerals, updated_gas)
        self.active_player.resources = player_new_resources
    
    def add_1_worker(self, localisation):
        self.active_player.get_a_worker(localisation)
        self.add_to_memo(f" Worker produced for {self.active_player} in {localisation}")
        
    def memo_archive(self):
        return (self.game_memo_archive)
    
    def add_to_memo(self, text):
        newline = "    " + text + "\n"
        result = newline + self.game_memo_archive
        self.game_memo_archive = result
        self.trim_memo()
        self.controller.update_memo_label()
        
    def trim_memo(self):
        nr_of_lines = self.game_memo_archive.count("\n")
        if nr_of_lines >42:
            the_line = self.game_memo_archive.rfind('\n')        
            result = self.game_memo_archive[0:the_line ]
            self.game_memo_archive = result
    
    def end_of_turn (self):
        for SCreature in self.active_player.board:
            if self.active_player.board[SCreature].name == "<placeholder>":
                #print("No creature")
                self.add_to_memo(f" No creature in {self.active_player.name} one slot")
                continue 
            elif self.active_player.board[SCreature].active == None:
                #print(f"{self.active_player.board[SCreature].name} inactive")
                self.add_to_memo(f"{self.active_player.board[SCreature].name} inactive")
                continue
            elif self.inactive_player.board[SCreature].name == "<placeholder>":
                if SCreature in ["top", "down"]:
                    self.active_player.board[SCreature].kill_workers_of(self.inactive_player, SCreature)
                    self.add_to_memo(self.active_player.board[SCreature].memo)
                else:
                    self.active_player.board[SCreature].attack(self.inactive_player)
                    self.add_to_memo(self.active_player.board[SCreature].memo)
            else: 
                self.active_player.board[SCreature].attack(self.inactive_player.board[SCreature])
                self.add_to_memo(self.active_player.board[SCreature].memo)
                
            if self.active_player.board[SCreature].name  != "<placeholder>" and self.active_player.board[SCreature].hp <1:
                self.give_back_pop(self.active_player, self.active_player.board[SCreature].cost[0])
                self.active_player.board[SCreature] = None
                self.controller.update_placeholder_picture()
                self.active_player.board[SCreature] = ST_classes.creature(self.active_player.board[SCreature])                
    
            if self.inactive_player.board[SCreature].name  != "<placeholder>" and self.inactive_player.board[SCreature].hp <1:
                self.give_back_pop(self.inactive_player, self.inactive_player.board[SCreature].cost[0]) 
                self.inactive_player.board[SCreature] = None
                self.controller.update_placeholder_picture()
                self.inactive_player.board[SCreature] = ST_classes.creature(self.inactive_player.board[SCreature])
                
        self.produce_income()        
        self.active_player.activate_all()
        self.active_player, self.inactive_player = self.inactive_player, self.active_player      
        self.controller.update_creature_descriptions()
        self.controller.update_infobars()
        self.name_of_played_creature =""
