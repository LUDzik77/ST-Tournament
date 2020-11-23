
from ST_model import Model
from ST_view import View
from playsound import playsound



class Controller:
    
    def __init__(self):
        self.model = Model(self)
        self.view = View(self)
        #playsound("sounds/Terran_theme_1.mp3", block=False)
        
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
    
    ###### NEW  #####
    def find_active_player_detector_object(self):
        result = self.model.detector_for_a_race()
        return(result)
    
    def verify_if_detector_play_button_needed(self):
        if self.model.avaliable_detector_play():
            print("passed")
            return(True)
        else: 
            print("not passed verify")
            return(False)
        
    def update_creature_descriptions(self):   
        self.view.fill_creature_slotz()
        
    def update_memo_label(self):
        self.view.fill_memo_label()
          
    def update_infobars(self):
        self.view.fill_infobars()
        
    #works fine for seting a picture in 'play' 
    def update_picture(self, caption_placement):  
        a_photo = self.model.creature_photo_by_name(
            self.model.name_of_played_creature)
        a_nr = self.model.board_by_placement(caption_placement)
        self.view.creature_picture_changer(a_nr, a_photo)
    
    def update_placeholder_picture(self):
        a_photo= "images/larva.png"
        placement = self.model.placement_for_placeholders()
        for a_nr in placement:
            self.view.creature_picture_changer(a_nr, a_photo) 
         
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
            """
            if self.model.active_player.overlord>0:
                self.view.add_move_overlord()           
            if self.model.active_player.race == == "terran":
                self.view.add_move_overlord()
            elif self.model.active_player.race == "protoss":
                    self.view.add_move_overlord()
            """
            
        elif caption == '  upgrades':
            pass
        
        elif caption == 'evolutions':
            pass    
        
        elif caption == "get a worker (50 minerals)":
            self.view.add_worker_placement_panel()  
            
        elif caption == "move 10 workers":
            self.view.add_move_worker_panel() 
            
        elif caption in  ["+1 worker top", "+1 worker down"]:
            self._button_plus_worker_top_down(caption) 
            
        elif caption =="increase population (100 min.)":
            self._button_increase_population()
            
        elif caption == "exit play": 
            self.view.destroy_one_windows(self.view.play_window)  
            
        elif caption == "exit economy": 
            self.view.destroy_one_windows(self.view.economy_window)     
            
        elif caption in ["top --> down", "down --> top"]: 
            self._button_workers_top_down(caption)    
            
        elif caption in ["top", "center", "down"]: 
            self._button_top_center_down(caption)
            
        elif caption in ["Overlord","Science Vessel","Observer"]:
            self._button_detector_play(caption)
            
        else: 
            self._button_creature_play(caption)


    def _button_creature_play(self, caption):
        if self.model.enough_resources(self.model.creature_resource_cost(caption)):
            self.model.name_of_played_creature = caption
            self.view.add_creature_placement_panel(self.model.creature_nr_by_name(
                    self.model.name_of_played_creature))
        else:
            self.cannot_play()
    
    #hardcoded ;(
    def _button_detector_play(self, caption):          
        if caption == "Science Vessel":
            if self.model.enough_resources((3,100,225)):
                self.model.name_of_played_creature = caption
                self.view.add_detector_placement_panel()
            else: self.cannot_play()
        elif caption == "Observer":
            if self.model.enough_resources((1,25,75)):
                self.model.name_of_played_creature = caption
                self.view.add_detector_placement_panel()
            else: self.cannot_play()
        elif caption == "Observer":
            self.model.name_of_played_creature = caption
            self.view.add_detecter_placement_panel() 

                   
    def _button_top_center_down(self, caption):
        self.model.give_back_pop(self.model.active_player, 
                                 self.model.active_player.board[caption].cost[0])
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
            self.model.take_resources_from_player((1,50,0))
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
    
    
