from ST_model import Model
from ST_view import View
from playsound import playsound



class Controller:
    
    def __init__(self):
        self.model = Model(self)
        self.view = View(self)
        #self.play_music("sounds/Terran_theme_1.mp3")
        
    def main(self):
        self.view.main()
           
    def play_music(self, file):
        playsound(file, block=False)
        
    def cannot_play(self):
        self.play_music("sounds/not_enough_minerals.mp3")
        self.model.add_to_memo("not_enough_minerals! XD")    
    
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
    
    def find_player_color(self, player):
        result = self.model.player_color(player) 
        return(result)
    
    def find_active_player_detector_object(self):
        result = self.model.detector_for_a_race()
        return(result)
    
    def verify_if_detector_play_button_needed(self):
        if self.model.avaliable_detector_play(): return(True)
        else: return(False)
        
    def verify_if_carrier_with_no_max_interceptors_on_board(self):
        if self.model.is_unit_4_active_player("Carrier"): 
            if self.model.not_max_interceptors_for_carriers(): return(True)
        else: return(False)        
    
    def verify_if_detector_can_move(self):
        if (self.model.is_unit_4_active_player("Observer")\
        or self.model.is_unit_4_active_player("Science Vessel")\
        or self.model.is_unit_4_active_player("Overlord")):
            result= self.model.is_empty_board_place()
            return(result)
        return(False)
  
    def update_creature_descriptions(self):   
        self.view.fill_creature_slotz()
        
    def update_memo_label(self):
        self.view.fill_memo_label()
          
    def update_infobars(self):
        self.view.fill_infobars()
        
    #works fine for seting a picture in 'play' 
    def update_picture(self, caption_placement):  
        a_photo = self.model.creature_photo_by_name(self.model.name_of_played_creature)
        a_nr = self.model.board_by_placement(caption_placement)
        self.view.creature_picture_changer(a_nr, a_photo)
    
    def update_placeholder_picture(self):
        a_photo= "images/larva.png"
        placement = self.model.placement_for_placeholders()
        for a_nr in placement:
            self.view.creature_picture_changer(a_nr, a_photo)
            
    def _getting_back_resources(self, location): 
        if self.model.active_player.board[location].name == "Overlord": 
            self.model.active_player.pop_max -= 8 
        else: self.model.give_back_pop(self.model.active_player, 
                                 self.model.active_player.board[location].cost[0])       
         
    def on_closing(): 
        self.view.activate_buttons()     
    
    def on_button_click(self, caption):
        self.view.fill_creature_slotz()
        
        if caption == "play a unit":
            self.view.open_play_window()
            
        elif caption == "pass a turn":
            self.model.end_of_turn()
            
        elif caption == ' economy':
            self.view.open_economy_panel()
            
        elif caption == '  upgrades':
            pass 
        
        elif caption == "get a worker\n50 minerals":
            self.view.add_worker_placement_panel()  
            
        elif caption == "move 10 workers":
            self.view.add_move_worker_panel() 
            
        elif caption in  ["+1 worker top", "+1 worker down"]:
            self._button_plus_worker_top_down(caption) 
            
        elif caption =="increase population\n100 minerals":
            self._button_increase_population()
            
        elif caption == "exit play": 
            self.view.destroy_one_windows(self.view.play_window)  
            
        elif caption == "exit economy": 
            self.view.destroy_one_windows(self.view.economy_window)     
            
        elif caption in ["top --> down", "down --> top"]: 
            self._button_workers_top_down(caption)    
            
        elif caption in ["top", "center", "down"]: 
            self._button_top_center_down(caption)
        
        elif caption in ["detector-->top","detector-->center","detector-->down"]:
            self._button_detector_top_center_down(caption)
            
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
          
        else: 
            self._button_creature_play(caption)

    def _button_build_interceptor(self):
        if  self.model.enough_resources((0,25,0)):
            self.model.take_resources_from_player((0,25,0))
            self.model.interceptors_on_the_board()
            self.view.fill_creature_slotz()
            self.view.fill_infobars()
            self.model.end_of_turn()
            self.view.destroy_one_windows(self.view.play_window)
        else:
            self.cannot_play()        
    
    def _button_creature_play(self, caption):
        if self.model.enough_resources(self.model.creature_resource_cost(caption)):
            self.model.name_of_played_creature = caption
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
        self.view.destroy_one_windows(self.view.economy_window)
    
    def _button_move_from_center_down_top(self, caption):
        self.name_of_played_creature = caption
        result = self.model.list_empty_spaces_with_descriptions()
        self.view.add_choose_place_to_move_for_detector_panel(result)
   
    def _button_move_detector(self):
        result = self.model.list_detectors_with_descriptions()
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
            
    def _button_detector_top_center_down(self, caption):
        location = self.model.caption_trim(caption)
        self._getting_back_resources(location)
        if self.model.name_of_played_creature == self.model.terran0.name:
            self.model.take_resources_from_player(self.model.terran0.cost)
        elif self.model.name_of_played_creature == self.model.protoss0.name:
                self.model.take_resources_from_player(self.model.protoss0.cost)
        else:         self.model.active_player.overlord -= 1
                
        self.model.detector_on_the_board(self.model.detector_for_a_race(), location)

        a_nr = self.model.board_by_placement(location)
        a_detector = self.model.detector_for_a_race()
        self.view.creature_picture_changer(a_nr, a_detector.photo)
        self.view.fill_creature_slotz()
        self.view.fill_infobars()
        self.model.end_of_turn()
        self.view.destroy_one_windows(self.view.economy_window)  
        
    def _button_top_center_down(self, caption):
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
        self.view.fill_infobars()
        self.view.destroy_one_windows(self.view.economy_window)         

    def _button_plus_worker_top_down(self, caption):
        if  self.model.enough_resources((1,50,0)):
            self.model.take_resources_from_player((0,50,0))
            if caption == "+1 worker top": self.model.add_1_worker("top")
            elif caption == "+1 worker down": self.model.add_1_worker("down")
            self.view.fill_infobars()
            self.view.destroy_one_windows(self.view.economy_window)
        else:
            self.cannot_play()

    def _button_increase_population(self):
        if  self.model.enough_resources((0,100,0)):
            self.model.take_resources_from_player((0,100,0))
            self.model.build_house()
            self.view.destroy_one_windows(self.view.economy_window)
        else:
            self.cannot_play()        
            



if __name__== '__main__':
    SCTournament = Controller()
    SCTournament.main()
    
    
