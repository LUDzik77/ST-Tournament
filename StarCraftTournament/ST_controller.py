from ST_model import Model
from ST_view import View
from playsound import playsound
import random
import time

class Controller:
    
    def __init__(self):
        self.model = Model(self)
        self.view = View(self)
        self.play_music("sounds/start_1.mp3")
    
    def main(self):
        self.view.main()
           
    def play_music(self, file):       
        playsound(file, block = False)   

    def cannot_play(self):
        self.play_music(self.model.active_player.not_enough_sounds())
        self.model.add_to_memo("not enough minerals/gas/pop")
    
    def turn_identification_in_view(self):
        self.view.change_turn_identificator()
        
    def start_click(self):
        self.play_music("sounds/start_2.mp3")
        self.view.start_frm.destroy()
        self.view.make_panel()
                
    def load_click(self):
        self.play_music("sounds/start_2.mp3")
        self.model.initialisation_from_load()
        self.view.start_frm.destroy()
        self.view.all_initializations()
        self.debug_colors_after_load()
        self.play_music("sounds/Terran_theme_1.mp3")
    
    def panel_click(self):
        self.play_music("sounds/start_2.mp3")
        p1_name, p2_name = self.view.entry1.get(), self.view.entry2.get()
        p1_race, p2_race = self.view.p1_race.get(), self.view.p2_race.get()
        p1_color = self.model.match_color_to_name(self.view.clicked1.get())
        p2_color = self.model.match_color_to_name(self.view.clicked2.get())
        self.model.player_setup(p1_name, p1_race, p1_color, p2_name, p2_race, p2_color)
        self.view.panel_frm.destroy()
        self.model.all_initializations()
        self.view.all_initializations() 
        self.play_music("sounds/Terran_theme_1.mp3") 
        
    def find_data_for_creature_slotz(self):
        result = self.model.creatures_data()
        return (result)
    
    def find_data_for_creature_photo(self):
        result = self.model.creatures_photo()
        return (result)    
    
    def find_data_for_play_photo(self):
        result = self.model.options_photo()
        return (result) 
    
    def find_data_for_play_name(self):
        result = self.model.options_name()
        return (result)
    
    def find_data_for_play_cost(self):
        result = self.model.options_cost()
        return (result)     
    
    def find_data_for_memo_label(self):
        result = self.model.memo_archive()
        return(result)
    
    def find_data_for_player_description(self):
        result = self.model.player_description_data()
        return(result)
    
    def find_player_object(self):
        return(self.model.active_player)
    
    def find_player_color(self, player):
        result = self.model.player_color(player) 
        return(result)
    
    def find_active_player_creature_objects(self):
        data = self.model.all_board_objects()
        if self.model.active_player ==self.model.p1:
            result = [data[0],data[1],data[2]]
        else: result = [data[3],data[4],data[5]]
        return(result)
    
    def find_active_player_detector_object(self):
        result = self.model.detector_for_a_race()
        return(result)
    
    def find_placeholder_photo(self):
        result = [c.photo for l,c in self.model.p1.board.items()] + [c.photo for l,c in self.model.p2.board.items()]
        return(result)
    
    def debug_colors_after_load(self):
        self.view.set_colors_for_infobar_and_creature_slots()
    
    def verify_if_detector_play_button_needed(self):
        if self.model.avaliable_detector_play(): return(True)
        else: return(False)
    
    def verify_if_build_nuke_button_needed(self):
        if self.model.is_unit_4_active_player("Ghost"):
            if self.model.active_player.nuke == False: return(True)
        else: return(False)
    
    def verify_if_can_land_nuke(self):
        if self.model.is_unit_4_active_player("Ghost"):
            if self.model.active_player.nuke == True: return(True)
        else: return(False)
        
    def verify_if_carrier_with_no_max_interceptors_on_board(self):
        if self.model.is_unit_4_active_player("Carrier"): 
            if self.model.not_max_interceptors_for_carriers(): return(True)
        else: return(False)
        
    def verify_if_add_evolution_button(self):
        if self.model.if_upgrade_done("Advanced Evolutions"): pass
        else: return(False)
        for location, creature in self.model.active_player.board.items():
            if creature.name in ["Hydralisk", "Mutalisk"]: return(True)
        else: return(False)
        
    def verify_if_detector_can_move(self):
        if (self.model.is_unit_4_active_player("Observer")\
        or self.model.is_unit_4_active_player("Science Vessel")\
        or self.model.is_unit_4_active_player("Overlord")):
            result= self.model.is_any_empty_board_place()
            return(result)
        return(False)
  
    def verify_if_any_unit_can_move(self): 
        if self.model.if_upgrade_done("Gravic Thrusters") or self.model.if_upgrade_done("Dropships"):
            if (self.model.is_unit_4_active_player("Marine")\
            or self.model.is_unit_4_active_player("Firebat")\
            or self.model.is_unit_4_active_player("Ghost")\
            or self.model.is_unit_4_active_player("Scout")):
                result= self.model.is_any_empty_board_place()
                return(result)                
        return(False)
    
    def update_creature_descriptions(self):   
        self.view.fill_creature_slotz()
        
    def update_all_creature_pictures(self):
        result = self.model.all_board_objects()
        self.view.all_creature_picture_changer(result)  
    
    def update_memo_label(self):
        self.view.fill_memo_label()
          
    def update_infobars(self):
        self.view.fill_infobars()
        
    #works fine for seting a picture in 'play' 
    def update_picture(self, caption_placement):  
        a_photo = self.model.creature_photo_by_name(self.model.name_of_played_creature)
        a_nr = self.model.board_by_placement(caption_placement)
        self.view.creature_picture_changer(a_nr, a_photo)
       
    def _getting_back_resources(self, location): 
        if self.model.active_player.board[location].name == "Overlord":
            self.model.overlord_killed(self.model.active_player)
        else: self.model.give_back_pop(self.model.active_player, 
                                 self.model.active_player.board[location].cost[0])       
         
    def on_closing(): 
        self.view.activate_buttons()     
    
    #the loop to trigger all buttons except upgrades, evolutions and starting panel
    def on_button_click(self, caption):
        self.view.fill_creature_slotz()
        
        if caption == "play a unit":
            self.view.open_play_window()
            self.play_music(self.model.active_player.on_play_sounds())
            
        elif caption == "pass a turn":
            self.play_music("sounds/button.mp3")
            self.model.end_of_turn()
            
        elif caption == "economy  ":
            self.view.open_economy_panel()
            self.play_music(self.model.active_player.economy_sounds())
            
        elif caption == "upgrades  ":
            self.view.open_upgrades_panel(self.model.active_player.upgrades_register)
            self.play_music(self.model.active_player.upgrades_sounds())
            
        elif caption == "save game":
            self.model.save_game()
            
        elif caption == "exit game  ":             
            exit()
            
        elif caption == "get a worker\n50 minerals":
            self.play_music("sounds/button.mp3")
            self.view.add_worker_placement_panel()  
            
        elif caption == "move 10 workers":
            self.play_music("sounds/button.mp3")
            self.view.add_move_worker_panel() 
            
        elif caption in  ["+1 worker top", "+1 worker down"]:
            self._button_plus_worker_top_down(caption) 
            
        elif caption =="increase population\n100 minerals":
            self._button_increase_population()
            
        elif caption == "exit play":
            self.play_music("sounds/button.mp3")
            self.view.destroy_one_windows(self.view.play_window)
            
        elif caption == "exit economy":
            self.play_music("sounds/button.mp3")
            self.view.destroy_one_windows(self.view.economy_window)
         
        elif caption == "exit upgrades": 
            self.play_music("sounds/button.mp3")
            self.view.destroy_one_windows(self.view.upgrades_window)          
            
        elif caption in ["top --> down", "down --> top"]: 
            self._button_workers_top_down(caption)    
            
        elif caption in ["top", "center", "down"]: 
            self._button_top_center_down(caption)
        
        elif caption in ["detector-->top","detector-->center","detector-->down"]:
            self._button_detector_top_center_down(caption)
        
        elif caption == "move unit":   
            self._button_move_unit()
            
        elif caption == "move detector": 
            self._button_move_detector()
            
        elif caption in ["move from center", "move from down", "move from top"]:
            self._button_move_from_center_down_top(caption)
            
        elif caption in ["move to center", "move to down", "move to top"]:
            self._button_move_to_center_down_top(caption)          
            
        elif caption in ["Overlord","Science Vessel","Observer"]:
            self._button_detector_play(caption)
            
        elif caption == "build interceptor": 
            self._button_build_interceptor()
            
        elif caption == "build a nuke":
            self._button_build_nuke()
        
        elif caption == "land a nuke":
            self._button_land_nuke()
            
        elif caption == "exit the game":        
            exit()
            
        elif caption == "Restart a game":
            self.view.destroy()
            restart_game() 
            
        else: 
            self._button_creature_play(caption)


    def _button_land_nuke(self):
        self.play_music("sounds/nuclear_launch_detected.mp3")
        self.model.add_to_memo("Nucear launch detected!")
        self.view.destroy_one_windows(self.view.economy_window)
        time.sleep(2)
        self.model.nuke_explosion()
        self.view.fill_creature_slotz()
        self.view.fill_infobars()        
        self.play_music("sounds/explosion_sound.mp3")
        self.play_music("sounds/nuke_sound.mp3")
        self.model.end_of_turn()    
  
    def _button_build_nuke(self):        
        if  self.model.enough_resources((8,100,100)):
            self.model.take_resources_from_player((8,100,100))
            self.model.active_player.nuke = True
            self.view.fill_creature_slotz()
            self.view.fill_infobars()
            self.model.add_to_memo("Nuclear missile ready!")
            self.play_music("sounds/nuke_ready.mp3")
            self.model.end_of_turn()
            self.view.destroy_one_windows(self.view.play_window)
        else:
            self.cannot_play()    
    
    def _button_build_interceptor(self):
        if  self.model.enough_resources((0,25,0)):
            self.model.take_resources_from_player((0,25,0))
            self.model.interceptors_on_the_board()
            self.view.fill_creature_slotz()
            self.view.fill_infobars()
            self.play_music("sounds/button.mp3")
            self.model.end_of_turn()
            self.view.destroy_one_windows(self.view.play_window)
        else:
            self.cannot_play()        
    
    def _button_creature_play(self, caption):
        if self.model.enough_resources(self.model.creature_resource_cost(caption)):
            self.model.name_of_played_creature = caption
            self.play_music("sounds/button.mp3")
            self.view.add_creature_placement_panel(self.model.creature_nr_by_name(
                    self.model.name_of_played_creature))
        else:
            self.cannot_play()
            
    def _button_move_to_center_down_top(self, caption):
        location = self.model.decode_detector_instructions(self.name_of_played_creature, caption)
        self.model.boardmovement_X_to_Y(location[0], location[1])
        a_nr0 = self.model.board_by_placement(location[0])
        a_nr1 = self.model.board_by_placement(location[1])
        self.view.creature_picture_changer(a_nr0, self.model.active_player.board[location[0]].photo)
        self.view.creature_picture_changer(a_nr1, self.model.active_player.board[location[1]].photo)
        self.view.fill_creature_slotz()
        self.play_music("sounds/button.mp3")
        if self.model.if_upgrade_done("Pneumatized Carapace"): 
            self.model.add_to_memo(f"It is still your turn!")
        elif (self.model.if_upgrade_done("Gravic Thrusters")) and\
             (self.model.active_player.board[location[1]].name=="Scout"):
            self.model.add_to_memo(f"It is still your turn!")                         
        elif (self.model.if_upgrade_done("Dropships")) and\
             (self.model.active_player.board[location[1]].name in ["Marine", "Ghost", "Firebat"]):
            self.model.add_to_memo(f"It is still your turn!")         
        else: 
            self.model.end_of_turn()
        self.view.destroy_one_windows(self.view.economy_window)
    
    def _button_move_from_center_down_top(self, caption):
        self.name_of_played_creature = caption
        result = self.model.list_empty_spaces_with_descriptions()
        self.play_music("sounds/button.mp3")
        self.view.add_choose_place_to_move_for_detector_panel(result)
   
    def _button_move_unit(self):
        result = self.model.list_units_that_can_move_with_descriptions()
        self.play_music("sounds/button.mp3")
        self.view.add_choose_unit_to_move_panel(result)         
   
    def _button_move_detector(self):
        result = self.model.list_detectors_with_descriptions()
        self.play_music("sounds/button.mp3")
        self.view.add_choose_detector_to_move_panel(result)  
  
    def _button_detector_play(self, caption):          
        if caption == self.model.terran0.name:
            if self.model.enough_resources(self.model.terran0.cost):
                self.model.name_of_played_creature = caption
                self.view.add_detector_placement_panel()
            else: self.cannot_play()
        elif caption == self.model.protoss0.name:
            if self.model.enough_resources(self.model.protoss0.cost):
                self.model.name_of_played_creature = caption
                self.view.add_detector_placement_panel()
            else: self.cannot_play()
        elif caption == self.model.zerg0.name:
            self.model.name_of_played_creature = caption
            self.view.add_detector_placement_panel()
        self.play_music("sounds/button.mp3")
            
    def _button_detector_top_center_down(self, caption):
        location = self.model.caption_trim(caption)
        self._getting_back_resources(location)
        if self.model.name_of_played_creature == self.model.terran0.name:
            self.model.creature_entrance_music("Science Vessel")
            self.model.take_resources_from_player(self.model.terran0.cost)
        elif self.model.name_of_played_creature == self.model.protoss0.name:
                self.model.take_resources_from_player(self.model.protoss0.cost)
                self.play_music("sounds/button.mp3")
        else: 
            self.model.active_player.overlord -= 1
            self.play_music("sounds/button.mp3")
                
        self.model.detector_on_the_board(self.model.detector_for_a_race(), location)
        if self.model.name_of_played_creature == self.model.terran0.name:
            self.model.defensive_matrix_check_and_cast(location)
        a_nr = self.model.board_by_placement(location)
        a_detector = self.model.detector_for_a_race()
        self.view.creature_picture_changer(a_nr, a_detector.photo)
        self.view.fill_creature_slotz()
        self.view.fill_infobars()
        self.model.end_of_turn()
        self.view.destroy_one_windows(self.view.economy_window)  
        
    def _button_top_center_down(self, caption):
        if self.model.if_upgrade_done("Archon Merge") and\
           self.model.active_player.board[caption].name == "Dark Templar":
            self.model.take_resources_from_player(
                self.model.creature_resource_cost(self.model.name_of_played_creature))
            self.model.archon_on_board(caption)
            a_nr = self.model.board_by_placement(caption)
            a_photo = self.model.active_player.board[caption].photo
            self.view.creature_picture_changer(a_nr, a_photo)            
        else:   
            self._getting_back_resources(caption)
            self.model.take_resources_from_player(
                self.model.creature_resource_cost(self.model.name_of_played_creature))
            self.model.creature_on_board(self.model.name_of_played_creature, caption)
            self.update_picture(caption)
        self.view.fill_creature_slotz()
        self.view.fill_infobars()
        self.model.end_of_turn()
        self.view.destroy_one_windows(self.view.play_window)      
        
    def _button_workers_top_down(self, caption):
        self.model.moving_workers(caption)
        self.play_music("sounds/button.mp3")
        self.view.fill_infobars()
        self.view.destroy_one_windows(self.view.economy_window)         

    def _button_plus_worker_top_down(self, caption):
        if  self.model.enough_resources((1,50,0)):
            self.model.take_resources_from_player((0,50,0))
            if caption == "+1 worker top": self.model.add_1_worker("top")
            elif caption == "+1 worker down": self.model.add_1_worker("down")
            self.play_music(self.model.active_player.worker_sounds())
            self.view.fill_infobars()
            self.view.destroy_one_windows(self.view.economy_window)
        else:
            self.cannot_play()

    def _button_increase_population(self):
        if  self.model.enough_resources((0,100,0)):
            self.model.take_resources_from_player((0,100,0))
            self.model.build_house()
            self.play_music(self.model.active_player.house_sounds())
            self.view.destroy_one_windows(self.view.economy_window)
        else:
            self.cannot_play() 
    
    def on_button_move_unit(self, caption):
        self.name_of_played_creature = caption
        result = self.model.list_empty_spaces_with_descriptions()
        self.play_music("sounds/button.mp3")
        self.view.add_choose_place_to_move_for_unit_panel(result)        
            
    def on_button_upgrade_click(self, upgrade):
        if (upgrade.name=="Moebius Reactor") and\
           (self.model.is_any_empty_board_place()==False):
            self.play_music(self.model.active_player.not_enough_sounds())
            self.model.add_to_memo("You need an empty slot for a Ghost") 
        elif  self.model.enough_resources(upgrade.cost):
            self.model.add_to_memo(f"{upgrade.name} upgrade finished.")
            self.model.take_resources_from_player(upgrade.cost)
            self.model.active_player.upgrades_done.append(upgrade)
            self.model.active_player.upgrades_register.remove(upgrade)
            self.model.upgrade_instant_board_effect(upgrade)
            self.model.upgrade_player_options_effect(upgrade)
            self.model.upgrade_other_effect(upgrade)
            self.update_all_creature_pictures()  
            self.view.fill_creature_slotz()
            self.play_music(self.model.active_player.upgrade_complete_sounds())
            self.view.fill_infobars()
            self.view.destroy_one_windows(self.view.upgrades_window)
        else:
            self.cannot_play()             

    def on_button_evolution(self, evolution):
        if evolution == "Lurker": 
            creature=self.model.zerg6
            to_replace="Hydralisk"
        elif evolution == "Guardian": 
            creature=self.model.zerg7
            to_replace="Mutalisk"
        else: print("error_on_button_evolution")
        
        if  self.model.enough_resources(creature.cost):
            self.model.take_resources_from_player(creature.cost)
            all_locations = self.model.list_c_locations_on_board_for_player_by_name\
                (self.model.active_player, to_replace)
            creature_to_evolve = random.choice(all_locations)
            a_nr = self.model.board_by_placement(creature_to_evolve)
            self.model.copy_a_creature(creature_to_evolve, creature)               
            if creature == self.model.zerg6:
                self.model.active_player.board[creature_to_evolve].cost = (2,175,75)
                if self.model.if_upgrade_done("Spikes and Spines"): 
                    self.model.active_player.board[creature_to_evolve].dmg += 1                 
                self.play_music(self.model.active_player.lurker_burrow_sounds())
            elif creature == self.model.zerg7:
                self.model.active_player.board[creature_to_evolve].cost = (4,150,200)
                self.play_music(self.model.active_player.guardian_sounds())
            if self.model.if_upgrade_done("Chitinous Plating"): 
                self.model.active_player.board[creature_to_evolve].armour += 1
          
            self.view.creature_picture_changer(a_nr, creature.photo)
            self.view.fill_creature_slotz()
            self.view.fill_infobars()
            self.model.end_of_turn()
            self.view.destroy_one_windows(self.view.upgrades_window)              
        else:
            self.cannot_play()  
        
    def show_end_game(self, victor):
        self.view.open_endgame_window(victor)
        print (f"END OF THE GAME: {victor.name} is the winner!")
        
def restart_game():
    SCTournament = Controller()
    SCTournament.main()  
           
  
if __name__== '__main__':
    SCTournament = Controller()
    SCTournament.main()
    
    
