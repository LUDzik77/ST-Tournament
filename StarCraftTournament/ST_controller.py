
from ST_model import Model
from ST_view import View
from playsound import playsound



class Controller:
    
    def __init__(self):
        self.model = Model(self)
        self.view = View(self)
        #playsound("Terran_theme_1.mp3", block=False)
        
    def main(self):
        self.view.main()
        
    
    def play_music(self, file):
        playsound(file, block=False)
        #self.play_music("not_enough_minerals.mp3")
    
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
    
    def update_creature_descriptions(self):   
        self.view.fill_creature_slotz()
        
    def find_data_for_player_description(self):
        result = self.model.player_description_data()
        return(result)
    
    #works fine for seting a picture in 'play' 
    def update_picture(self, caption_placement):  
        a_photo = self.model.creature_photo_by_name(
            self.model.name_of_played_creature)
        a_nr = self.model.board_by_placement(caption_placement)
        self.view.creature_picture_changer(a_nr, a_photo)
    
    def update_placeholder_picture(self):
        a_photo= "larva.png"
        placement = self.model.placement_for_placeholders()
        for a_nr in placement:
            self.view.creature_picture_changer(a_nr, a_photo) 


    def on_button_click(self, caption):
        self.view.fill_creature_slotz()
        if caption == "play":
            self.view.open_play_window()        
        elif caption == "pass":
            self.model.end_of_turn()
        elif caption in ["top","center","down"]:
            self.model.take_resources_from_player(
                self.model.creature_resource_cost(self.model.name_of_played_creature))
            self.model.creature_on_board(self.model.name_of_played_creature, caption)
            self.update_picture(caption)
            self.view.fill_creature_slotz()
            self.model.end_of_turn()
            self.view.play_window.destroy()
        #here all other buttons captions:  "upgrade", "evolve", "get a worker"
        
        #else = clicking a >SCreature< from option panel
        else :
            print(self.model.active_player.resources)
            if self.model.enough_resources(self.model.creature_resource_cost(caption)):
                self.model.name_of_played_creature = caption
                self.view.add_creature_placement_panel(
                    self.model.creature_nr_by_name(
                        self.model.name_of_played_creature))
            else:
                self.play_music("not_enough_minerals.mp3")

    
        
           


if __name__== '__main__':
    SCTournament = Controller()
    SCTournament.main()