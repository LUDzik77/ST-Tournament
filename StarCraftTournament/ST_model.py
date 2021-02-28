import ST_classes
import ST_SCreature
import ST_upgrades
import ST_colours
import random
import copy
import json
import jsonpickle
from datetime import datetime

class Model:
    
    def __init__(self, controller):
        self.controller = controller
        #timestamp = datetime.timestamp(datetime.now())
        
    def player_setup(self, p1_name, p1_race, p1_color, p2_name, p2_race, p2_color):
        if len(p1_name)==0: p1_name = p1_race
        elif len(p1_name) >8: p1_name = p1_name[:6]
        if len(p2_name)==0: p2_name = p2_race
        elif len(p2_name) >8: p2_name = p2_name[:6]        
        if p1_race == "Terran": self.p1 = ST_classes.Terran_player(p1_name, 50, 15, 15, p1_color)
        elif p1_race == "Zerg": self.p1 = ST_classes.Zerg_player(p1_name, 50, 15, 15, p1_color)
        elif p1_race == "Protoss": self.p1 = ST_classes.Protoss_player(p1_name, 50, 15, 15, p1_color)
        if p2_race == "Terran": self.p2 = ST_classes.Terran_player(p2_name, 50, 15, 15, p2_color)
        elif p2_race == "Zerg": self.p2 = ST_classes.Zerg_player(p2_name, 50, 15, 15, p2_color)
        elif p2_race == "Protoss": self.p2 = ST_classes.Protoss_player(p2_name, 50, 15, 15, p2_color)            
        
    def all_initializations(self):
        self._initialize_board_data()
        self._initialize_creature_prototypes()
        self._initialize_players_options()
        self._initialize_proper_placeholder_photos()
        self._initialize_resources()
        self._initialize_upgrade_prototypes()
        self._initialize_players_upgrades_register()
        self._initialize_other_data()
        
    def _initialize_other_data(self):
        self.name_of_played_creature = ""
        self.game_memo_archive = "  ***Lets begin SC Tournament***\n"
        self.active_player, self.inactive_player = self.p1, self.p2
       
    def _initialize_board_data(self):
        self.c1 = ST_classes.creature("top")
        self.c2 = ST_classes.creature("center")
        self.c3 = ST_classes.creature("down")
        self.c4 = ST_classes.creature("top")
        self.c5 = ST_classes.creature("center")
        self.c6 = ST_classes.creature("down")
        self.p1.board = {"top":self.c1, "center":self.c2, "down":self.c3}
        self.p2.board = {"top":self.c4, "center":self.c5, "down":self.c6}
        
    def _initialize_creature_prototypes(self):
        self.zerg0 = ST_classes.SCreature(*ST_SCreature.Overlord)
        self.terran0 = ST_classes.SCreature(*ST_SCreature.Science_Vessel)
        self.protoss0 = ST_classes.SCreature(*ST_SCreature.Observer)
        self.zerg1 = ST_classes.SCreature(*ST_SCreature.Zergling)
        self.zerg2 = ST_classes.SCreature(*ST_SCreature.Hydralisk)
        self.zerg3 = ST_classes.SCreature(*ST_SCreature.Mutalisk)
        self.zerg4 = ST_classes.SCreature(*ST_SCreature.Defiler)
        self.zerg5 = ST_classes.SCreature(*ST_SCreature.Ultralisk)
        self.zerg6 = ST_classes.SCreature(*ST_SCreature.Lurker)
        self.zerg7 = ST_classes.SCreature(*ST_SCreature.Guardian)  
        self.terran1 = ST_classes.SCreature(*ST_SCreature.Marine)
        self.terran2 = ST_classes.SCreature(*ST_SCreature.Firebat)
        self.terran3 = ST_classes.SCreature(*ST_SCreature.Siege_Tank)
        self.terran4 = ST_classes.SCreature(*ST_SCreature.Wright)
        self.terran5 = ST_classes.SCreature(*ST_SCreature.Battlecruiser)
        self.protoss1 = ST_classes.SCreature(*ST_SCreature.Zealot)
        self.protoss2 = ST_classes.SCreature(*ST_SCreature.Dragoon)
        self.protoss3 = ST_classes.SCreature(*ST_SCreature.Dark_Templar)
        self.protoss4 = ST_classes.SCreature(*ST_SCreature.Scout) 
        self.protoss5 = ST_classes.SCreature(*ST_SCreature.Carrier)
        self.protoss6 = ST_classes.SCreature(*ST_SCreature.Archon)
        
    def _initialize_players_options(self):
        zerg = [self.zerg1, self.zerg2, self.zerg3, self.zerg4, self.zerg5]
        protoss = [self.protoss1, self.protoss2,  self.protoss3, self.protoss4, self.protoss5]
        terran = [self.terran1, self.terran2, self.terran3, self.terran4, self.terran5]
        for player in [self.p1, self.p2]:
            if player.race == "zerg": player.options = zerg
            if player.race== "protoss": player.options = protoss
            if player.race == "terran": player.options = terran
            
    def _initialize_proper_placeholder_photos(self):
        self.p1.pick_random_slot_photos()
        self.p2.pick_random_slot_photos()        
        self.c1.photo = self.p1.empty_slot_photo[0]
        self.c2.photo = self.p1.empty_slot_photo[1]
        self.c3.photo = self.p1.empty_slot_photo[2]
        self.c4.photo = self.p2.empty_slot_photo[0]
        self.c5.photo = self.p2.empty_slot_photo[1]
        self.c6.photo = self.p2.empty_slot_photo[2]

    def _initialize_resources(self):
        self.min_top_p1 = ST_classes.mineral_patch(2000)
        self.min_down_p1 = ST_classes.mineral_patch(2000)
        self.gas_top_p1 = ST_classes.gas_patch(1100)
        self.gas_down_p1 = ST_classes.gas_patch(1100) 
        self.min_top_p2 = ST_classes.mineral_patch(2000)
        self.min_down_p2 = ST_classes.mineral_patch(2000)
        self.gas_top_p2 = ST_classes.gas_patch(1100)
        self.gas_down_p2 = ST_classes.gas_patch(1100)
        self.all_minerals_and_gas = (self.min_top_p1, self.min_down_p1, self.gas_top_p1, self.gas_down_p1,\
                                     self.min_top_p2, self.min_down_p2, self.gas_top_p2, self.gas_down_p2)
        
    def _initialize_upgrade_prototypes(self):
        # Zerg:
        self.Adrenal_Glands = ST_classes.upgrade(*ST_upgrades.Adrenal_Glands)
        self.Advanced_Evolutions = ST_classes.upgrade(*ST_upgrades.Advanced_Evolutions)
        self.Chitinous_Plating = ST_classes.upgrade(*ST_upgrades.Chitinous_Plating)
        self.Consume = ST_classes.upgrade(*ST_upgrades.Consume)
        self.Pneumatized_Carapace = ST_classes.upgrade(*ST_upgrades.Pneumatized_Carapace)
        self.Spikes_and_Spines = ST_classes.upgrade(*ST_upgrades.Spikes_and_Spines)
        
        # Terran:
        self.Siege_Mode = ST_classes.upgrade(*ST_upgrades.Siege_Mode)
        self.Cloak = ST_classes.upgrade(*ST_upgrades.Cloak)
        self.Stimpack  = ST_classes.upgrade(*ST_upgrades.Stimpack)
        self.Irradiate  = ST_classes.upgrade(*ST_upgrades.Irradiate)
        self.Dropships  = ST_classes.upgrade(*ST_upgrades.Dropships)
        # in tests/development
        self.Moebius_Reactor = ST_classes.upgrade(*ST_upgrades.Moebius_Reactor)
        
        # Protoss:
        self.Leg_Enhancements = ST_classes.upgrade(*ST_upgrades.Leg_Enhancements)
        self.Plasma_Shield = ST_classes.upgrade(*ST_upgrades.Plasma_Shield)
        self.Carrier_Capacity = ST_classes.upgrade(*ST_upgrades.Carrier_Capacity)
        self.Gravitic_Thrusters = ST_classes.upgrade(*ST_upgrades.Gravitic_Thrusters)
        self.Archon_Merge = ST_classes.upgrade(*ST_upgrades.Archon_Merge)
        # in tests/development:
        self.Psy_Storm  = ST_classes.upgrade(*ST_upgrades.Psy_Storm)         
  
    def _initialize_players_upgrades_register(self):
        zerg = [self.Adrenal_Glands, self.Advanced_Evolutions, self.Chitinous_Plating,\
                self.Consume, self.Pneumatized_Carapace,  self.Spikes_and_Spines]
        terran = [self.Stimpack, self.Siege_Mode, self.Cloak,\
                  self.Irradiate, self.Dropships, self.Moebius_Reactor]
        protoss = [self.Leg_Enhancements, self.Plasma_Shield,  self.Carrier_Capacity,\
                   self.Archon_Merge, self.Gravitic_Thrusters, self.Psy_Storm]    
        for player in [self.p1, self.p2]:
            if player.race == "zerg": player.upgrades_register = copy.deepcopy(zerg)
            if player.race == "terran": player.upgrades_register = copy.deepcopy(terran)
            if player.race== "protoss": player.upgrades_register = copy.deepcopy(protoss)
            
    def initialisation_from_load(self):
        self.player_setup("Mock", "Terran", "#cc0000", "Mock", "Terran", "#cc0000")
        self._initialize_board_data()
        self._initialize_creature_prototypes()
        self._initialize_players_options()
        self._initialize_proper_placeholder_photos()
        self._initialize_resources()
        self._initialize_upgrade_prototypes()
        self._initialize_players_upgrades_register()
        self.load_game()
    
    def match_color_to_name(self, color_name):
        for c_pair in ST_colours.SColours:
            if c_pair[1] == color_name: return(c_pair[0])
    
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
        if player == "active_player": result = self.active_player.color
        elif player == "inactive_player": result = self.inactive_player.color
        elif player == "p1": result = self.p1.color
        elif player == "p2": result = self.p2.color
        return(result)
    
    def board_by_placement(self, placement_query):
        if placement_query == "top": result=1
        elif placement_query == "center": result=2
        elif placement_query == "down": result=3
        if self.active_player == self.p2: result+=3
        return(result)
    
    def all_board_objects(self):
        result=[]
        result.append(self.p1.board["top"])
        result.append(self.p1.board["center"])
        result.append(self.p1.board["down"])
        result.append(self.p2.board["top"])
        result.append(self.p2.board["center"])
        result.append(self.p2.board["down"])    
        return(result)
    
    def creature_entrance_music(self,creature_name):
        if creature_name == "Carrier": self.controller.play_music("sounds/carrier has arrived.mp3")
        elif creature_name =="Battlecruiser": self.controller.play_music("sounds/battlecruiser operational.mp3")
        elif creature_name =="Zealot": self.controller.play_music("sounds/my life 4 aiur.mp3")
        elif creature_name =="Marine": self.controller.play_music("sounds/go go go.mp3")
        elif creature_name =="Hydralisk": self.controller.play_music("sounds/hydralisk ready.mp3")
        elif creature_name =="Siege Tank": self.controller.play_music("sounds/ready to roll out.mp3")
        elif creature_name =="Mutalisk": self.controller.play_music("sounds/mutalisk.mp3")
        elif creature_name =="Dark Templar": self.controller.play_music("sounds/dark_templar.mp3")
        elif creature_name =="Archon": self.controller.play_music("sounds/archon_merge.mp3")
        elif creature_name =="Science Vessel": self.controller.play_music("sounds/science_vessel.mp3")
        else: self.controller.play_music("sounds/button.mp3")
  
    def creature_on_board(self, creature_name, placement):
        c_index = self.creature_nr_by_name(creature_name)  
        clone = copy.deepcopy(self.active_player.options[c_index])
        self.active_player.board[placement] = clone
        self.add_to_memo(f"You have played {self.active_player.board[placement].name}({placement}).")
        self.creature_entrance_music(creature_name)
        
    def archon_on_board(self, placement):
        clone = copy.deepcopy(self.protoss6)
        self.active_player.board[placement] = clone
        if self.if_upgrade_done("Plasma Shield"): 
            self.active_player.board[placement].hp += 4
        self.add_to_memo(f"Archon was merged ({placement}).")
        self.creature_entrance_music("Archon")    
    
    def copy_a_creature(self, placement, creature_obj):
        clone = copy.deepcopy(creature_obj)
        self.active_player.board[placement] = clone
        self.add_to_memo(f"You have evolve {self.active_player.board[placement].name}({placement}).")
    
    def interceptors_on_the_board(self):
        for location, carrier in self.active_player.board.items():
            if (carrier.name == "Carrier") and (carrier.dmg < self.limit_interceptors_per_upgrade()):
                carrier.dmg += 1
                self.add_to_memo(f"Interceptor was built.({location})")            
                
    def not_max_interceptors_for_carriers(self):
        interceptors=[]
        for location, creature in self.active_player.board.items():
            if creature.name == "Carrier": interceptors.append(creature.dmg)
        result = list(filter(lambda x: x<self.limit_interceptors_per_upgrade(), interceptors))
        if len(result) != 0: return(True)
        else: return(False)
        
    def limit_interceptors_per_upgrade(self):
        limit = 4
        for  upgrade in self.active_player.upgrades_done:
            if upgrade.name == "Carrier Capacity": limit = 8
        return(limit)
        
    def list_empty_spaces_with_descriptions(self):
        result = []
        for location, creature in  self.active_player.board.items():
            if creature.name =="<placeholder>": result.append(f"move to {location}")
        return(result)
    
    def list_detectors_with_descriptions(self):
        result = []
        for location, creature in  self.active_player.board.items():
            if creature.name in ["Overlord", "Science Vessel", "Observer"]: 
                result.append(f"move from {location}")
        return(result)
    
    def list_units_that_can_move_with_descriptions(self):
        result = []
        for location, creature in  self.active_player.board.items():
            if creature.name in ["Scout", "Ghost", "Marine", "Firebat"]: 
                result.append(f"move from {location}")
        return(result)    
    
    def list_c_locations_on_board_for_player_by_name(self, player, name_query):
        result = []       
        for location,creature in player.board.items():
            if creature.name == name_query: result.append(location)
        return(result)
    
    def if_upgrade_done(self, upgrade_name_query):
        if len(self.active_player.upgrades_done) == 0: 
            return(False)
        else:
            for upgrade in self.active_player.upgrades_done:
                if upgrade.name == upgrade_name_query: 
                    return(True)
            return(False)
            
    def detector_on_the_board(self, a_detector, placement):
        self.active_player.board[placement] = a_detector
        self.add_to_memo(f"You have played {a_detector.name} ({placement}).")
        
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
        elif self.active_player.race in ["terran", "protoss"]: return(True)
        else: return (False)
    
    def is_unit_4_active_player(self, name):
        for location, unit in self.active_player.board.items():
            if unit.name == name:  return(True)
        return (False)
    
    def is_any_empty_board_place(self):
        for location, a_creature in self.active_player.board.items():
            if a_creature.name == "<placeholder>": return(True)
        return(False)

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
        res_difference = tuple(map(lambda i, j: i - j, self.active_player.resources, cost))
        if res_difference[2]<0: return(False)
        elif res_difference[1]<0: return(False)
        elif (res_difference[0]<0) and (cost[0]!=0): return(False)
        else: return(True)  

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
    
    def overlord_killed(self, player):
        player.pop_max -= 8 
        player.resources = (player.resources[0]-8,player.resources[1],player.resources[2])        
       
    def proper_minerals_patches(self):
        if self.active_player == self.p1:
            return(self.min_top_p1, self.min_down_p1, self.gas_top_p1, self.gas_down_p1)
        else: 
            return(self.min_top_p2, self.min_down_p2, self.gas_top_p2, self.gas_down_p2)                
        
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
        gas_depeated = 1   #to be implemented
        gas_gain = 0
        
        for worker in range(workers_on_gas):
            if worker <= gas_full[0]: gas_gain += gas_full[1]
            elif worker <= gas_limited[0]: gas_gain += gas_limited[1]
            elif worker <= gas_limited2[0]: gas_gain += gass_limited2[1]   
        return([minerals_gain, gas_gain])
       
    def resources_from_resource_patches(self):
        minerals_top = self.count_income(self.active_player.workers_top)[0]
        minerals_down = self.count_income(self.active_player.workers_down)[0]
        gas_top = self.count_income(self.active_player.workers_top)[1]
        gas_down = self.count_income(self.active_player.workers_down)[1]
        
        resources_patches = self.proper_minerals_patches()
        
        resources_patches[0].resources -= minerals_top
        resources_patches[1].resources -= minerals_down 
        resources_patches[2].resources -= gas_top 
        resources_patches[3].resources -= gas_down
        
        return (minerals_top+minerals_down, gas_top+gas_down)
           
    def produce_income(self):
        minerals, gas = self.resources_from_resource_patches()
        #self.add_to_memo(f"You earn {minerals} minerals and {gas} gas.")
        
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
        self.add_to_memo(f"You moved {workers_to_move} to the bottom base.")
    
    def moving_workers_from_bottom(self):
        if self.active_player.workers_down > 9:   workers_to_move = 10
        else: workers_to_move = self.active_player.workers_down
        for a_worker in range(workers_to_move):
            self.active_player.remove_a_worker_down()
            self.active_player.get_a_worker("top")
        self.add_to_memo(f"You moved {workers_to_move} to the top base.")   
    
    def add_1_worker(self, localisation):
        self.active_player.get_a_worker(localisation)
        self.add_to_memo(f"Worker was produced: {localisation}.")
        
    def build_house(self):
        self.active_player.pop_max += 8
        self.active_player.overlord += 1
        result = (self.active_player.resources[0] +8, 
                  self.active_player.resources[1], self.active_player.resources[2])
        self.active_player.resources = result
        self.controller.update_infobars()
        self.add_to_memo(f"Max population was increased.")
        
    def boardmovement_X_to_Y(self, move_from, move_to):
        self.active_player.board[move_from], self.active_player.board[move_to] =\
            self.active_player.board[move_to], self.active_player.board[move_from]
        self.add_to_memo(f"Unit was moved from {move_from} to {move_to}")
    
    def caption_trim(self, caption):
        if caption =="detector-->top": return("top")
        elif caption =="detector-->center": return("center")
        elif caption =="detector-->down": return("down")  
    
    def decode_detector_instructions(self, location_from, location_to):
        result = (location_from[10:], location_to[8:])
        return(result)
    
    def upgrade_instant_board_effect(self, upgrade):
        for location, creature in self.active_player.board.items():
            if upgrade.name == "Adrenal Glands": 
                if creature.name == "Zergling": creature.dmg += 1
            elif upgrade.name == "Chitinous Plating":
                if creature.name in ["Ultralisk", "Guardian"," Lurker"]: creature.armour += 1
            elif upgrade.name == "Spikes and Spines": 
                if creature.name in ["Hydralisk", "Lurker"]: creature.dmg += 1
            elif upgrade.name == "Consume":
                if creature.name == "Defiler": creature.active = True       
            elif upgrade.name == "Stimpack":
                if creature.name in ["Marine","Firebat"]:
                    if creature.hp > 1: creature.hp -= 1
                    creature.dmg += 1
            elif upgrade.name == "Cloak":
                if creature.name in ["Wright", "Ghost"]: 
                    creature.cloak = True
            elif upgrade.name == "Siege Mode":
                if creature.name == "Siege Tank":
                    if creature.active == True: creature.active = "Setting up"
                    creature.dmg += 4
                    creature.photo = "images/siege_tank.png"
            elif upgrade.name == "Plasma Shield":
                if creature.name == "Archon": creature.hp += 4 
                elif creature.name == "Carrier": creature.hp += 3
                elif creature.name == "Scout": creature.hp += 2
                elif creature.name == "Observer": creature.hp += 0
                else: creature.hp += 1
            elif upgrade.name == "Leg Enhancements":
                if creature.name == "Zealot": creature.active = True
    
    def upgrade_player_options_effect(self, upgrade):
        for creature in self.active_player.options:
            # ZERG:
            if (creature.name == "Zergling") and (upgrade.name == "Adrenal Glands"):
                creature.dmg += 1
            elif (creature.name == "Ultralisk") and (upgrade.name == "Chitinous Plating"):
                creature.armour += 1
            elif (creature.name == "Hydralisk") and (upgrade.name == "Spikes and Spines"):
                creature.dmg += 1  
            elif (creature.name == "Defiler") and (upgrade.name == "Consume"):
                creature.active = True                      
            # TERRAN:      
            elif (creature.name in ["Marine", "Firebat"]) and (upgrade.name == "Stimpack"):
                creature.hp -= 1
                creature.dmg += 1                  
            elif (creature.name == "Siege Tank") and (upgrade.name == "Siege Mode"):
                creature.photo = "images/siege_tank.png"
                creature.dmg += 4
            elif (creature.name in ["Wright", "Ghost"]) and (upgrade.name == "Cloak"):
                creature.cloak = True  
            # PROTOSS:
            elif upgrade.name == "Plasma Shield":    #does not serve Archons for now :) (+4)
                if creature.name == "Carrier": creature.hp += 3
                elif creature.name == "Scout": creature.hp += 2
                elif creature.name == "Observer": creature.hp += 0
                else: creature.hp += 1  
            elif (creature.name == "Zealot") and (upgrade.name == "Leg Enhancements"):
                creature.active = True
                
    def upgrade_other_effect(self, upgrade):
        if upgrade.name == "Plasma Shield": self.active_player.hp +=5

    def save_game(self):
        now = datetime.now()
        date_time = now.strftime("%Y/%m/%d %H:%M")
        self.add_to_memo(f"Game saved: {date_time}")
        player1 = jsonpickle.encode(self.p1)
        player2 = jsonpickle.encode(self.p2)
        economy = jsonpickle.encode(self.all_minerals_and_gas)
        if self.active_player == self.p1: active = 1
        elif self.active_player == self.p2: active = 2
        else: print ("error save_game()")
            
        save_ = json.dumps({"Player1": player1, 
                            "Player2": player2,
                            "Economy": economy,
                            "Active_player": active,
                            "Memo" :  self.game_memo_archive})     
        with open('save_.json', 'w') as file:
            file.write(save_)
            
    def load_game(self):
        with open('save_.json', 'r') as file:
            data = json.load(file)
            self.p1 = jsonpickle.decode(data["Player1"])
            self.p2 = jsonpickle.decode(data["Player2"])
            self.game_memo_archive = data["Memo"]
            self.all_minerals_and_gas = jsonpickle.decode(data["Economy"]) 
            self.min_top_p1 = self.all_minerals_and_gas[0]
            self.min_down_p1 = self.all_minerals_and_gas[1]
            self.gas_top_p1 = self.all_minerals_and_gas[2]
            self.gas_down_p1 = self.all_minerals_and_gas[3]
            self.min_top_p2 = self.all_minerals_and_gas[4]
            self.min_down_p2 = self.all_minerals_and_gas[5]
            self.gas_top_p2 = self.all_minerals_and_gas[6]
            self.gas_down_p2 = self.all_minerals_and_gas[7] 
            activate_player = data["Active_player"] 
            if activate_player == 1:
                self.active_player, self.inactive_player = self.p1, self.p2
            else: self.active_player, self.inactive_player = self.p2, self.p1
        
    ### SPECIAL ATTACKS // SPELLS ###
    def handle_special_attacks(self, location):
        if self.active_player.board[location].name == "Defiler":
            self.plague_spell(location)
        if self.active_player.board[location].name == "Carrier":
            if self.active_player.board[location].dmg < self.limit_interceptors_per_upgrade():
                self.active_player.board[location].dmg+=1
                self.add_to_memo(f"Interceptor was auto-built.")
        if (self.active_player.board[location].name == "Science Vessel") \
        and (self.if_upgrade_done("Irradiate")):
            if self.active_player.board[location].active:
                self.irradiate_spell(location)

    def irradiate_spell(self, location):
        if location == "center": pass
        elif self.inactive_player.board[location].name != "<placeholder>": pass
        elif location=="top" and self.inactive_player.workers_top < 1: pass
        elif location=="down" and self.inactive_player.workers_down < 1: pass        
        else:
            if location == "top":
                max_dmg = (self.inactive_player.workers_top//2.1)+2
                spell_dmg = random.randint(2, max_dmg)
                for i in range(0, spell_dmg):
                    self.inactive_player.remove_a_worker_top() 
            if location == "down":
                max_dmg = (self.inactive_player.workers_down//2.1)+2
                spell_dmg = random.randint(2, max_dmg)
                for i in range(0, spell_dmg):
                    self.inactive_player.remove_a_worker_down() 
            self.add_to_memo(f"Irradiate kills {spell_dmg} workers ({location})")  
            self.controller.play_music("sounds/irradiate.mp3")
            
    def plague_spell(self, defiler_location):
        location = random.choice(["top", "down", "center"])
        if self.inactive_player.board[location].name != "<placeholder>":
            if self.inactive_player.board[location].name != "Archon":
                self.inactive_player.board[location].hp = 1
            self.add_to_memo(f"{self.inactive_player.board[location].name} was plagued!")
            self.controller.play_music("sounds/plague.mp3")
            if self.if_upgrade_done("Consume"):
                self.active_player.board[defiler_location].hp -= 1
                #print(self.active_player.board[defiler_location].name, self.active_player.board[defiler_location].hp)  ############## to remove later
                if self.active_player.board[defiler_location].hp <1: self.add_to_memo("Defiler comitted suicide!")
                else: self.add_to_memo("Defiler deals 1 dmg to itself")
        else: 
            self.add_to_memo(f"Defiler plague ineffective") 

    def defensive_matrix_check_and_cast(self, location): 
        board = [self.active_player.board["top"],self.active_player.board["center"],\
                        self.active_player.board["down"]]
        board.remove(self.active_player.board[location])
        board = list(filter(lambda x: x.name != "<placeholder>" , board))
        if len(board) !=0:
            target_of_spell = random.choice(board)
            target_of_spell.armour += 1
            self.add_to_memo(f"Defensive Matrix on {target_of_spell.name}")
            self.controller.play_music("sounds/defensive_matrix.mp3")
        else: self.add_to_memo(f"No target for defensive matrix.")

    ### MEMO FUNCTIONS ###   
    def memo_archive(self):
        return (self.game_memo_archive)
    
    def add_to_memo(self, text):
        spacing = (7-(len(list(self.active_player.name)))) * " "
        newline = self.active_player.name + ":" + spacing + text + "\n"
        result = newline + self.game_memo_archive
        self.game_memo_archive = result
        self.trim_memo()
        self.controller.update_memo_label()
        
    def trim_memo(self):
        nr_of_lines = self.game_memo_archive.count("\n")
        if nr_of_lines >36:
            the_line = self.game_memo_archive.rfind('\n')        
            result = self.game_memo_archive[0:the_line ]
            self.game_memo_archive = result
            
    ### EOT ###
    def end_of_turn (self):
        self.eot_other_sounds()
        self.eot_archon_is_growing()
        for location in self.active_player.board:    
            if self.active_player.board[location].name == "<placeholder>":
                continue 
            
            elif self.active_player.board[location].active != True:
                self.add_to_memo(f"{self.active_player.board[location].name} inactive")
                continue
            
            elif self.inactive_player.board[location].name == "<placeholder>":
                self.handle_special_attacks(location)
                self.eot_basic_fight(location)
                    
            else:
                self.handle_special_attacks(location)
                self.eot_advanced_fight(location)
                
            self.eot_clean_up(self.active_player, location)
            self.eot_clean_up(self.inactive_player, location) 
  
        self.produce_income()
        self.eot_reset_creatures_memo() 
        self.active_player.activate_all()
        self.eot_add_activation_memos()
        self.eot_check_endgame()
        self.active_player, self.inactive_player = self.inactive_player, self.active_player
        self.controller.turn_identification_in_view()
        self.controller.update_creature_descriptions()
        self.controller.update_infobars()
        self.name_of_played_creature =""
      
    def eot_basic_fight(self, location):
        self.eot_attack_sounds()
        if location in ["top", "down"]:
            self.active_player.board[location].kill_workers_of(self.inactive_player, location)
            self.add_to_memo(self.active_player.board[location].memo)
        else:
            self.active_player.board[location].attack(self.inactive_player)
            self.add_to_memo(self.active_player.board[location].memo)
            
    def eot_advanced_fight(self, location):
        self.eot_attack_sounds()
        if self.active_player.board[location].can_attack_target(self.inactive_player.board[location], self.active_player):
            self.active_player.board[location].attack(self.inactive_player.board[location])
            self.add_to_memo(self.active_player.board[location].memo) 
        else:
            randomize = random.choice(["distracted", "not distrated"])
            if randomize == "distracted":
                self.add_to_memo(f"{self.active_player.board[location].name} didn't attack!")
                self.add_to_memo(f"{self.active_player.board[location].name} was distracted by {self.inactive_player.board[location].name}!") 
            else:
                self.add_to_memo(f"{self.active_player.board[location].name} can't reach the target!") 
                self.eot_basic_fight(location) 
      
    def eot_clean_up(self, player, location):
        if player.board[location].name  != "<placeholder>" and player.board[location].hp <1:
            if player.board[location].name == "Overlord": self.overlord_killed(player) 
            else: self.give_back_pop(player, player.board[location].cost[0])
            player.board[location] = ST_classes.creature(player.board[location])
            if location =="top": player.board[location].photo = player.empty_slot_photo[0]
            elif location =="center": player.board[location].photo = player.empty_slot_photo[1]
            elif location =="down": player.board[location].photo = player.empty_slot_photo[2]
            self.controller.update_all_creature_pictures()
            
    def eot_attack_sounds(self):
        for location, creature in self.active_player.board.items():  
            if ([upgrade.name=="Siege Mode" for upgrade in self.active_player.upgrades_done])\
            and (creature.name =="Siege Tank") and (creature.active == "Setting up"):
                file=self.active_player.siege_mode_sounds()
                self.controller.play_music(file)
            if (creature.dmg<1) or (creature.active != True): 
                continue
            elif ([upgrade.name=="Siege Mode" for upgrade in self.active_player.upgrades_done])\
            and (creature.name =="Siege Tank") and (creature.active == True):
                file=self.active_player.siege_attack_sounds()
                self.controller.play_music(file)
            elif (creature.name =="Lurker") and (creature.active == True):
                file=self.active_player.lurker_attack_sounds()
                self.controller.play_music(file)
            elif (creature.name =="Dark Templar") and (creature.active == True):
                file=self.active_player.dt_attack_sounds()
                self.controller.play_music(file)
            elif (creature.name =="Archon") and (creature.active == True):
                file=self.active_player.archon_attack_sounds()
                self.controller.play_music(file)            
            elif (creature.name =="Carrier") and (creature.active == True):
                file=self.active_player.interceptor_sounds()
                self.controller.play_music(file)            
            else:            
                file=self.active_player.attack_sounds()
                self.controller.play_music(file)
                
    def eot_other_sounds(self):
        for location, creature in self.active_player.board.items():  
            if ([upgrade.name=="Siege Mode" for upgrade in self.active_player.upgrades_done])\
            and (creature.name =="Siege Tank") and (creature.active == "Setting up"):
                file=self.active_player.siege_mode_sounds()
                self.controller.play_music(file)        
                
    def eot_add_activation_memos(self):
        for location, creature in self.active_player.board.items():
            if creature.memo != "": self.add_to_memo(creature.memo) 
        self.eot_reset_creatures_memo()
        
    def eot_reset_creatures_memo(self):
        for location, creature in self.active_player.board.items(): creature.memo = ""
    
    def eot_archon_is_growing(self):
        for location, creature in self.active_player.board.items():
            if creature.name == "Archon":
                creature.hp += 1
                self.add_to_memo("Archon reinforces his plasma shields")
                
    def eot_check_endgame(self):
        if self.inactive_player.hp <= 0: 
            self.eot_player_win(self.active_player)
        elif self.active_player.hp <= 0: 
            self.eot_player_win(self.inactive_player)        
                
    def eot_player_win(self, player):
        self.controller.play_music("sounds/you_win.mp3")
        self.add_to_memo(f"{player.name} win the game!")
        self.add_to_memo("***thanks for playing***")
        self.controller.show_end_game(player)

# TO DO LIST:
        
# end game effect (maybe reload? or just exit)
# upgrades (3 more) 
# protoss / terran additional features (Archons, ghosts, nukes)

