import ST_classes
import ST_SCreature
import random
import copy



class Model:
    
    def __init__(self, controller):

        self.controller = controller
        
        self.c1 = ST_classes.creature("top")
        self.c2 = ST_classes.creature("center")
        self.c3 = ST_classes.creature("down")
        self.c4 = ST_classes.creature("top")
        self.c5 = ST_classes.creature("center")
        self.c6 = ST_classes.creature("down")
        
        ####################  NEW #######################
        self.p1 = ST_classes.Protoss_player("Player1", 50, 30, 0, "blue")
        self.p2 = ST_classes.Terran_player("Player2", 50, 15, 15, "red")        
        print(f" race p1 {self.p1.race}")
        print(f" race p2 {self.p2.race}")
        self.zerg0 = ST_classes.SCreature(*ST_SCreature.Overlord)
        self.zerg1 = ST_classes.SCreature(*ST_SCreature.Zergling)
        self.zerg2 = ST_classes.SCreature(*ST_SCreature.Hydralisk)
        self.zerg3 = ST_classes.SCreature(*ST_SCreature.Mutalisk)
        self.zerg4 = ST_classes.SCreature(*ST_SCreature.Ultralisk)   
        
        self.terran0 = ST_classes.SCreature(*ST_SCreature.Science_Vessel)
        self.terran1 = ST_classes.SCreature(*ST_SCreature.Marine)
        self.terran3 = ST_classes.SCreature(*ST_SCreature.Wright)
        self.terran4 = ST_classes.SCreature(*ST_SCreature.Siege_Tank)
        self.terran5 = ST_classes.SCreature(*ST_SCreature.Battlecruiser)
        
        self.protoss0 = ST_classes.SCreature(*ST_SCreature.Observer)
        self.protoss1 = ST_classes.SCreature(*ST_SCreature.Zealot)
        self.protoss3 = ST_classes.SCreature(*ST_SCreature.Scout) 
        self.protoss5 = ST_classes.SCreature(*ST_SCreature.Carrier) 
        
        self.p1.board = {"top":self.c1, "center":self.c2, "down":self.c3}
        self.p2.board = {"top":self.c4, "center":self.c5, "down":self.c2}
        
        self.p1.options= [self.zerg1, self.zerg2, self.zerg3, self.zerg4, self.protoss5]
        #self.p2.pool_options(5)
        self.p2.options= [self.protoss1 , self.protoss3 , self.terran4, self.terran3, self.terran5 ]
        
        self.active_player = self.p1
        self.inactive_player = self.p2        
        
        ############################  USE THIS CRAP :D  ###############
        self.min_top_p1 = ST_classes.mineral_patch(3000)
        self.min_down_p1 = ST_classes.mineral_patch(3000)
        self.gas_top_p1 = ST_classes.gas_patch(1500)
        self.gas_down_p1 = ST_classes.gas_patch(1500) 
        self.min_top_p2 = ST_classes.mineral_patch(3000)
        self.min_down_p2 = ST_classes.mineral_patch(3000)
        self.gas_top_p2 = ST_classes.gas_patch(1500)
        self.gas_down_p2 = ST_classes.gas_patch(1500)         
        ###############################################################        
        
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
    
    def player_color(self, player):
        if player =="active_player": result = self.active_player.color
        elif player =="inactive_player": result = self.inactive_player.color
        else: print("player_color()  error")
        return(result)
 
    
    def board_by_placement(self, placement_query):
        if placement_query =="top": result=1
        elif placement_query =="center": result=2
        elif placement_query =="down": result=3
        if self.active_player == self.p2: result+=3
        return(result)

    
    def creature_on_board(self, creature_name, placement):
        c_index = self.creature_nr_by_name(creature_name)  
        clone = copy.deepcopy(self.active_player.options[c_index])
        self.active_player.board[placement] = clone
        self.add_to_memo(f"You have played {self.active_player.board[placement].name} ({placement}).")
        #for k,v in self.active_player.board.items(): 
        #    print (v.name)
 
#######################  READY  ###############################
    def detector_on_the_board(self, a_detector, placement):
        self.active_player.board[placement] = a_detector
        self.add_to_memo(f"You have played {self.active_player.board[placement].name} ({placement}).")
        
    def detector_for_a_race(self): 
        if self.active_player.race == "zerg":
            clone = copy.deepcopy(self.zerg0)
        elif self.active_player.race == "terran":
            clone = copy.deepcopy(self.terran0)
        elif self.active_player.race == "protoss":
            clone = copy.deepcopy(self.protoss0)        
        return(clone)
    
    def avaliable_detector_play(self): 
        if (self.active_player.race == "zerg") and (self.active_player.overlord > 0):
            return(True)
        elif self.active_player.race in ["terran", "protoss"]:
            return(True)
        else: return (False)     

    def placement_for_placeholders(self):
        result =[]
        if self.p1.board["top"] == None: result.append(1)
        if self.p1.board["center"] == None: result.append(2)
        if self.p1.board["down"] == None: result.append(3)
        if self.p2.board["top"] == None: result.append(4)
        if self.p2.board["center"] == None: result.append(5)
        if self.p2.board["down"] == None: result.append(6)
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
          
        gas_full = (2,5)
        gas_limited = (3,4)
        gas_limited2 = (4,3)          
        gas_depeted = 1   # to be implemented
        gas_gain = 0
        
        for worker in range(workers_on_gas):
            if worker <= gas_full[0]: gas_gain += gas_full[1]
            elif worker <= gas_limited[0]: gas_gain += gas_limited[1]
            elif worker <= gas_limited2[0]: gas_gain += gass_limited2[1]   
            
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
    
    def moving_workers(self, caption): 
        if caption == "top --> down": self.moving_workers_from_top()
        elif caption == "down --> top": self.moving_workers_from_bottom()
        else: print("moving_workers() entry error")
        
    def moving_workers_from_top(self):
        if self.active_player.workers_top > 9:   workers_to_move = 10
        else: workers_to_move = self.active_player.workers_top
        for a_worker in range(workers_to_move):
            self.active_player.remove_a_worker_top()
            self.active_player.get_a_worker("down")
        self.add_to_memo(f"You moved {workers_to_move} to the bottom base")
    
    def moving_workers_from_bottom(self):
        if self.active_player.workers_down > 9:   workers_to_move = 10
        else: workers_to_move = self.active_player.workers_down
        for a_worker in range(workers_to_move):
            self.active_player.remove_a_worker_down()
            self.active_player.get_a_worker("top")
        self.add_to_memo(f"You moved {workers_to_move} to the top base")   
    
    def add_1_worker(self, localisation):
        self.active_player.get_a_worker(localisation)
        self.add_to_memo(f" Worker was produced- {localisation}")
        
    def build_house(self):
        self.active_player.pop_max += 8
        result = (self.active_player.resources[0] +8, 
                  self.active_player.resources[1], self.active_player.resources[2])
        self.active_player.resources = result
        self.controller.update_infobars()
        self.add_to_memo(f" Your max population was increased")        
    
        
    def memo_archive(self):
        return (self.game_memo_archive)
    
    def add_to_memo(self, text):
        newline = self.active_player.name + ":" + "  " + text + "\n"
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
        for location in self.active_player.board:
            
            if self.active_player.board[location].name == "<placeholder>":
                #self.add_to_memo(f" No creature in a slot")
                continue 
            
            elif self.active_player.board[location].active == None:
                self.add_to_memo(f"{self.active_player.board[location].name} inactive")
                continue
            
            elif self.inactive_player.board[location].name == "<placeholder>":
                self.eot_basic_fight(location)
                    
            else: 
                self.eot_advanced_fight(location)
               
            self.eot_clean_up(self.active_player, location)
            self.eot_clean_up(self.inactive_player, location) 
  
        self.produce_income()        
        self.active_player.activate_all()
        self.active_player, self.inactive_player = self.inactive_player, self.active_player      
        self.controller.update_creature_descriptions()
        self.controller.update_infobars()
        self.name_of_played_creature =""
      
    def eot_basic_fight(self, location): 
        if location in ["top", "down"]:
            self.active_player.board[location].kill_workers_of(self.inactive_player, location)
            self.add_to_memo(self.active_player.board[location].memo)
        else:
            self.active_player.board[location].attack(self.inactive_player)
            self.add_to_memo(self.active_player.board[location].memo)
            
    def eot_advanced_fight(self, location): 
        if self.active_player.board[location].can_attack_target(self.inactive_player.board[location]):
            self.active_player.board[location].attack(self.inactive_player.board[location])
            self.add_to_memo(self.active_player.board[location].memo) 
        else:
            self.add_to_memo(f"{self.active_player.board[location].name} cannot reach the target!")
            self.eot_basic_fight(location) 
      
    def eot_clean_up(self, player, location):
        if player.board[location].name  != "<placeholder>" and player.board[location].hp <1:
            self.give_back_pop(player, player.board[location].cost[0])
            player.board[location] = None
            self.controller.update_placeholder_picture()
            player.board[location] = ST_classes.creature(player.board[location]) 
    
    
    
    
    
    
   