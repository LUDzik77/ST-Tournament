import tkinter as tk
import ST_colours
from tkinter import ttk
from tkinter import GROOVE, RIDGE, RAISED, SUNKEN


class View(tk.Tk):

    PAD = 5
    
    def __init__(self, controller):
        super().__init__()   
        self.controller = controller
        self.title("StarCraft Tournament")
        self.iconbitmap(r"images/terran_icon.ico")
        self.configure(bg="navyblue")
        self._fonts_for_GUI()
        self._make_panel()
        
    def main(self):
        self.mainloop()
    
    def _fonts_for_GUI(self):
        self.small_font = ("Courier", 8, "bold")
        self.medium_font = ("Courier", 9, "bold")
        self.big_font = ("Courier", 12, "bold")       

    def _make_panel(self):
        self.panel_frm = ttk.Frame(self)
        self.panel_frm.pack(padx=self.PAD, pady=self.PAD)
        self._make_labels_for_panel()
        self._make_entry_races_and_photos_for_panel()
        self.make_colors_and_button_for_panel()
        
    def _make_labels_for_panel(self):       
        description_label_names1 =("Player 1\nname:", "race:")
        description_label_names2 =("Player 2\nname:", "race:")
        for i in range(len(description_label_names1)):
            a_label1=tk.Label(self.panel_frm, text=description_label_names1[i], font=self.medium_font)
            a_label1.grid(row=i, column=0)
            a_label2=tk.Label(self.panel_frm, text=description_label_names2[i], font=self.medium_font)
            a_label2.grid(row=i, column=3)
            
        #description_colors = ("colour:", "colour:")
        c_label1=tk.Label(self.panel_frm, text="colour:", font=self.medium_font)
        c_label1.grid(row=5, column=0)
        c_label2=tk.Label(self.panel_frm, text=" colour:", font=self.medium_font)
        c_label2.grid(row=5, column=3)   
            
    def _make_entry_races_and_photos_for_panel(self):    
        self.entry1 = tk.Entry(self.panel_frm, width=9) 
        self.entry2 = tk.Entry(self.panel_frm, width=9) 
        self.entry1.grid(row=0, column=2)
        self.entry2.grid(row=0, column=4)
        self.p1_race = tk.StringVar()   
        self.p2_race = tk.StringVar()   
        self.p1_race.set("Terran")
        self.p2_race.set("Terran")
        self.Terran_img = tk.PhotoImage(file="images/Ticon.png") 
        self.Zerg_img = tk.PhotoImage(file="images/Zicon.png")        
        self.Protoss_img = tk.PhotoImage(file="images/Picon.png")         
        images = (self.Terran_img, self.Zerg_img, self.Protoss_img)     
        
        races=("Terran ","Zerg    ", "Protoss")
        for i in range(len(races)):
            r1 = tk.Radiobutton(self.panel_frm, image=images[i], text=races[i], variable=self.p1_race, value=races[i].strip())
            r2 = tk.Radiobutton(self.panel_frm, image=images[i], text=races[i], variable=self.p2_race, value=races[i].strip())
            r1.grid(row=i+1, column=2)
            r2.grid(row=i+1, column=4)
            
    def make_colors_and_button_for_panel(self): 
        colors_ = [x[1] for x in ST_colours.SColours]
        self.clicked1,self.clicked2 = tk.StringVar(), tk.StringVar()  
        self.clicked1.set(colors_[1])
        self.clicked2.set(colors_[10])
        color_list1 = tk.OptionMenu(self.panel_frm, self.clicked1, *colors_)
        color_list2 = tk.OptionMenu(self.panel_frm, self.clicked2, *colors_)
        color_list1.grid(row=5, column=2)
        color_list2.grid(row=5, column=4)
      
        self.small_man_photo = tk.PhotoImage(file = "images/population.png")
        self.small_man_photo = self.small_man_photo.subsample(1, 1)         
        start_game_button = ttk.Button(self.panel_frm, text="START THE GAME", \
                                       image=self.small_man_photo, compound="left",\
                                       command = lambda : self.controller.panel_click())
        start_game_button.grid(row=6, columnspan=18, ipadx=40)

    
    def all_initializations(self):
        self.button_captions = ["play a unit", "pass a turn",
                                " economy","  upgrades"]
        self.button_pictures = []        
        self.creature_list = list()
        self.button_box = []
        
        self._make_slot_desciptionsVar()
        self._make_main_frame()
        self._make_architecture()
        self.fill_creature_slotz()
        self._hardcode_creature_images()
        #test####AHTUNG --- CANVAS ARE SICK SHIT ------#####
        #self._make_canvas()         
        self._create_starting_creature_labels()
        self._make_frames_inside_creature_frames()
        self._make_memo_window()
        self._make_turn_indicator()
        self.change_turn_identificator()
        self._make_main_buttons()
        self._make_infobars()
        self.fill_infobars() 
       
    def _make_slot_desciptionsVar(self):
        self.slot1_description = tk.StringVar()
        self.slot2_description = tk.StringVar()
        self.slot3_description = tk.StringVar()
        self.slot4_description = tk.StringVar()
        self.slot5_description = tk.StringVar()
        self.slot6_description = tk.StringVar()          
        
    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)
        
    def _make_canvas(self):
        canvas_ = tk.Canvas(self.work_frame)
        canvas_.grid(row=0,column=0, rowspan=1, columnspan=1, sticky="n")
        self.bgg = tk.PhotoImage(file='images/command_center.png')
        canvas_.create_image(500, 0, image=self.bgg)
        canvas_.create_text(50, 20, text='         COOL GAME')
 
    def _make_architecture(self):
        self.creature_frame = ttk.Frame(self.main_frm)
        self.work_frame = ttk.Frame(self.main_frm)
        self.memo_frame = ttk.Frame(self.main_frm)  

        self.creature_frame.grid(row=0, column=1, columnspan=2, rowspan=3)
        self.work_frame.grid(row=0, column=0, columnspan=1, rowspan=3)
        self.memo_frame.grid(row=0, column=3, columnspan=1, rowspan=3)
             
    def _create_starting_creature_labels(self):
        bg1= self.controller.find_player_color("active_player"), 
        bg2= self.controller.find_player_color("inactive_player"), 
        self.slot1_photo_label = tk.Label(self.creature_frame, image = self.slot1_photo, bg= bg1, relief = SUNKEN)        
        self.slot1_photo_label.grid(row=0,column=0)
        self.slot2_photo_label = tk.Label(self.creature_frame, image = self.slot2_photo, bg= bg1, relief = SUNKEN)         
        self.slot2_photo_label.grid(row=1,column=0)
        self.slot3_photo_label = tk.Label(self.creature_frame, image = self.slot3_photo, bg= bg1, relief = SUNKEN)         
        self.slot3_photo_label.grid(row=2,column=0)
        self.slot4_photo_label = tk.Label(self.creature_frame, image = self.slot4_photo, bg= bg2, relief = SUNKEN)        
        self.slot4_photo_label.grid(row=0,column=1)
        self.slot5_photo_label = tk.Label(self.creature_frame, image = self.slot5_photo, bg= bg2, relief = SUNKEN)          
        self.slot5_photo_label.grid(row=1,column=1)
        self.slot6_photo_label = tk.Label(self.creature_frame, image = self.slot6_photo, bg= bg2, relief = SUNKEN)          
        self.slot6_photo_label.grid(row=2,column=1)        

    def fill_creature_slotz(self):
        result = self.controller.find_data_for_creature_slotz()
        self.slot1_description.set(result[0])
        self.slot2_description.set(result[1])
        self.slot3_description.set(result[2])
        self.slot4_description.set(result[3])
        self.slot5_description.set(result[4])
        self.slot6_description.set(result[5])      
    
    def _hardcode_creature_images(self):
        #tkinter technology need photo references saved
        #otherwise they go to python garbage collection and do not show up. 

        placeholder_photos = self.controller.find_placeholder_photo()
        
        self.slot1_photo = tk.PhotoImage(file = placeholder_photos[0])
        self.slot2_photo = tk.PhotoImage(file = placeholder_photos[1])
        self.slot3_photo = tk.PhotoImage(file = placeholder_photos[2])
        self.slot4_photo = tk.PhotoImage(file = placeholder_photos[3])
        self.slot5_photo = tk.PhotoImage(file = placeholder_photos[4])
        self.slot6_photo = tk.PhotoImage(file = placeholder_photos[5])
        
        self.option1_photo = tk.PhotoImage(file = "images/houses_small.png")
        self.option2_photo = tk.PhotoImage(file = "images/houses_small.png")
        self.option3_photo = tk.PhotoImage(file = "images/houses_small.png")
        self.option4_photo = tk.PhotoImage(file = "images/houses_small.png")
        self.option5_photo = tk.PhotoImage(file = "images/houses_small.png")
        
        self.economy_window1 = tk.PhotoImage(file = "images/SCV.png")
        self.economy_window2 = tk.PhotoImage(file = "images/SCV_run_away.png")
        
        self.exit_photo = tk.PhotoImage(file = "images/exit.png")
        self.houses_photo = tk.PhotoImage(file = "images/houses.png")
        self.detector_photo = tk.PhotoImage(file = "images/observer.png")
        self.move_detector = tk.PhotoImage(file = "images/move_detector.png")
        self.interceptor_photo = tk.PhotoImage(file = "images/interceptor.png")
        self.turn_indicator_photo = tk.PhotoImage(file = "images/tank.png")
        
        self.upgrade_slot1 = tk.PhotoImage(file = "images/houses_small.png")
        self.upgrade_slot2 = tk.PhotoImage(file = "images/houses_small.png")
        self.upgrade_slot3 = tk.PhotoImage(file = "images/houses_small.png")
        
        self.evolution_Lurker= tk.PhotoImage(file = "images/Lurker.png")
        self.evolution_Guardian = tk.PhotoImage(file = "images/Guardian.png")

    def creature_picture_changer(self, picture_slot, picture_address):
        slot = [self.slot1_photo, self.slot2_photo, self.slot3_photo,
                self.slot4_photo, self.slot5_photo, self.slot6_photo]
        slot[picture_slot-1] ["file"] = picture_address
     
    def all_creature_picture_changer(self, p1_p2_board):
        slot = [self.slot1_photo,self.slot2_photo,self.slot3_photo,
                self.slot4_photo,self.slot5_photo, self.slot6_photo]        
        for i in range(len(p1_p2_board)):
            slot[i]["file"] = p1_p2_board[i].photo
    
    def _make_frames_inside_creature_frames(self):  
        PAD_inner = 1
        slots1 = [self.slot1_description, self.slot2_description, self.slot3_description]
        slots2 = [self.slot4_description, self.slot5_description, self.slot6_description]
        
        a_frame = ttk.Frame(self.creature_frame)
        a_frame.grid(row=0, padx=PAD_inner, pady=PAD_inner)
        
        for i in range (3):
            
            a_frame = tk.Frame(self.creature_frame)
            a_frame.grid(row=i, column=0, padx=PAD_inner, pady=PAD_inner, sticky="SE")     
            a_label = tk.Label(a_frame, textvariable = slots1[i], font=self.medium_font)
            a_label.grid(row=i, column=0 )
            
            a_frame = ttk.Frame(self.creature_frame)
            a_frame.grid(row=i, column=1, padx=PAD_inner, pady=PAD_inner, sticky="SE")
            a_label = ttk.Label(a_frame, textvariable = slots2[i], font=self.medium_font)
            a_label.grid(row=i, column=1)
            
    def _make_turn_indicator(self):
        a_player = self.controller.find_player_object()
        self.turn_indicator_frame = tk.Frame(self.work_frame)
        self.turn_indicator_frame.grid(row=0, column=0)
        
        self.turn_indicator_photo_label = tk.Label(self.turn_indicator_frame, image=self.turn_indicator_photo, 
                                    bg = self.controller.find_player_color("active_player"),
                                         fg="navyblue", font=self.big_font, anchor="n") 
        self.turn_indicator_photo_label.grid(row=0, column=0)
        
        self.turn_indicator_text_label = tk.Label(self.turn_indicator_frame, \
                                                  font=self.big_font, fg=a_player.color, bg ="black")
        self.turn_indicator_text_label["text"] = (f"{a_player.name}'s turn")
        self.turn_indicator_text_label.grid(row=1, column=0)
        
    def change_turn_identificator(self):
        a_player = self.controller.find_player_object()
        self.turn_indicator_photo_label["bg"] = a_player.color
        self.turn_indicator_text_label["text"] = (f"{a_player.name}'s turn")
        self.turn_indicator_text_label["fg"] = a_player.color
        if a_player.race == "terran": self.turn_indicator_photo["file"]="images/siege_tank.png"
        elif a_player.race == "zerg": self.turn_indicator_photo["file"]="images/mutalisk.png"
        elif a_player.race == "protoss": self.turn_indicator_photo["file"]="images/zealot.png"
        
    def _make_infobars(self):        
        players_info = self.controller.find_data_for_player_description()  
        
        self.infobar_frame = tk.Frame(self.work_frame)
        self.infobar_frame.grid(row=1, column=0)
        
        self.player_1_infobar = tk.Label(self.infobar_frame, bg=self.controller.find_player_color("active_player"),
                                         fg="black", font=self.big_font, anchor="n")
        self.player_1_infobar.grid(row=0, column=0)
        
        self.infobar_photo = tk.PhotoImage(file = "images/infobar.png")
        self.infobar_= tk.Label(self.infobar_frame, image=self.infobar_photo, anchor="n")
        self.infobar_.grid(row=0, column=1)
        
        self.player_2_infobar = tk.Label(self.infobar_frame, bg = self.controller.find_player_color("inactive_player"),
                                         fg="black", font=self.big_font, anchor="n")
        self.player_2_infobar.grid(row=0, column=2) 
         
    def fill_infobars(self):
        players_info = self.controller.find_data_for_player_description()      
        self.player_1_infobar["text"] = players_info[0]
        self.player_2_infobar["text"] = players_info[1]
  
        
    def _make_main_buttons(self):
        self._photo = tk.PhotoImage(file = "images/population.png")
        self._photoimage = self._photo.subsample(1, 1) 
        index=1
        for caption in self.button_captions:
            index+=1
            btn = ttk.Button(self.work_frame, image=self._photoimage, compound="left", 
                             text=caption, cursor="cross", command=(
                                 lambda button=caption: self.controller.on_button_click(button)))
            self.button_box.append(btn)
            btn.grid(row=index, column=0, sticky="WE")

    
    def _make_memo_window(self):
        scroll_frame = tk.Frame(self.memo_frame)
        scroll_frame.grid()
        
        self.memo_label = tk.Label(self.memo_frame, fg="navyblue", font=self.small_font, justify="left")
        self.memo_label.grid(sticky="w")
        
        self.fill_memo_label()        

    def fill_memo_label(self):
        self.memo_label["text"] = self.controller.find_data_for_memo_label()

    def _make_exit_button(self, parent, text, row, column):
        btn = ttk.Button(parent, text=text, image=self.exit_photo, command=
                         (lambda button=text: self.controller.on_button_click(button)))
        btn.grid(row=row,column=column)
       
    def make_detector_play_button(self):
        if self.controller.verify_if_detector_play_button_needed():
            detector = self.controller.find_active_player_detector_object()
            self.detector_photo["file"] = detector.photo
            btn = ttk.Button(self.economy_window, text=detector.name, image=self.detector_photo, 
                             command=(lambda button=detector.name: self.controller.on_button_click(button)))
            btn.grid(row=0,column=4)
            label_cost = tk.Label(self.economy_window, font=self.medium_font)             
            if detector.name =="Overlord": 
                cost_description = "move overlord to the board"
            else: 
                cost_description = (f"{str(detector.cost[1])} minerals\
            \n{str(detector.cost[2])} gas     \
            \n{str(detector.cost[0])} population")                   
            label_cost["text"] = "Get detector!\n" + cost_description
            label_cost.grid(row=1,column=4)
    
    def make_move_detector_button(self):
        btn = ttk.Button(self.economy_window, text="move detector", image=self.move_detector, 
                         command=(lambda button="move detector": self.controller.on_button_click(button)))
        btn.grid(row=0,column=5)      
        label = tk.Label(self.economy_window, text="move detector", font=self.medium_font)
        label.grid(row=1,column=5)
        
    def add_choose_detector_to_move_panel(self, detectors):  
        for  i in range(len(detectors)):
            btn = ttk.Button(self.economy_window, text=detectors[i], command=(
                lambda button=detectors[i]: self.controller.on_button_click(button)))
            btn.grid(row=i+2, column=5)
   
    def add_choose_place_to_move_for_detector_panel(self, places):
        for  i in range(len(places)):
            btn = ttk.Button(self.economy_window, text=places[i], command=(
                lambda button=places[i]: self.controller.on_button_click(button)))
            btn.grid(row=i+4, column=5)        

    def add_detector_placement_panel(self):
        placement_buttons = ["detector-->top","detector-->center","detector-->down"]
        for i in range(len(placement_buttons)):
            btn = ttk.Button(self.economy_window, text=placement_buttons[i], command=(
                lambda button=placement_buttons[i]: self.controller.on_button_click(button)))
            btn.grid(row=i+2, column=4) 
    
    def open_play_window(self):
        self.play_window = tk.Toplevel(bg = self.controller.find_player_color("active_player"))
        self.play_window.title('choose play')
        self.play_window.iconbitmap(r"images/terran_icon.ico")
        self.disable_buttons()
        self.play_window.protocol( 'WM_DELETE_WINDOW', self.__CancelCommand) 
        
        picture_data = self.controller.find_data_for_play_name()
        picture_names = self.controller.find_data_for_play_photo()
        picture_costs = self.controller.find_data_for_play_cost()     
        picture_slot = [self.option1_photo, self.option2_photo, self.option3_photo,
                              self.option4_photo, self.option5_photo] 
        
        for i in range (len(picture_slot)):
            picture_slot[i] ["file"] = picture_names[i]

            cost_description = (f"{str(picture_costs[i][1])} minerals\
            \n{str(picture_costs[i][2])} gas     \
            \n{str(picture_costs[i][0])} population")              
            
            label_cost = tk.Label(self.play_window, font=self.medium_font)
            label_cost["text"] = cost_description
            label_cost.grid(row=1,column=i) 
            
            btn = ttk.Button(self.play_window, text=picture_data[i], image=picture_slot[i], 
                             command=
                             (lambda button=picture_data[i]: self.controller.on_button_click(button)))
            btn.grid(row=0,column=i)        
        if self.controller.verify_if_carrier_with_no_max_interceptors_on_board(): self.add_interceptor_panel()
        self._make_exit_button(self.play_window, "exit play", 0, 7)
         
        
    def add_creature_placement_panel(self,slot):
        placement_buttons = ["top","center","down"]
        for i in range(len(placement_buttons)):
            btn = ttk.Button(self.play_window, text=placement_buttons[i], command=(
                lambda button=placement_buttons[i]: self.controller.on_button_click(button)))
            btn.grid(row=i+2, column=slot)
            
    def add_interceptor_panel(self):
        btn = ttk.Button(self.play_window, text="build interceptor", image=self.interceptor_photo, command=
                         (lambda button="build interceptor": self.controller.on_button_click(button)))
        btn.grid(row=0,column=6)
        cost_description = ("25 minerals      \n0 gas            \n0 population")                      
        label_cost = tk.Label(self.play_window, text=cost_description, font=self.medium_font)
        label_cost.grid(row=1,column=6)      
    
    def open_economy_panel(self):
        self.economy_window = tk.Toplevel(bg = self.controller.find_player_color("active_player"))
        self.economy_window.title('your economy commander!')
        self.economy_window.iconbitmap(r"images/terran_icon.ico")
        self.disable_buttons()
        self.economy_window.protocol( 'WM_DELETE_WINDOW', self.__CancelCommand)  
    
        
        descriptions_economy = ["get a worker\n50 minerals", "move 10 workers", "increase population\n100 minerals"]
        photos_economy = [self.economy_window1, self.economy_window2, self.houses_photo]
        data = zip(descriptions_economy, photos_economy)
        
        for i in range (len(photos_economy)):
            btn = ttk.Button(self.economy_window, text=descriptions_economy[i], 
                             image=photos_economy[i], command=
                                 (lambda button=descriptions_economy[i]: self.controller.on_button_click(button)))
            btn.grid(row=0,column=i)                 
            a_label = tk.Label(self.economy_window, font=self.medium_font)
            a_label["text"] = descriptions_economy[i]
            a_label.grid(row=1, column=i) 
            
        self.make_detector_play_button()
        if self.controller.verify_if_detector_can_move(): self.make_move_detector_button()
        self._make_exit_button(self.economy_window, "exit economy", 0, 7)   
    
    def add_worker_placement_panel(self):
        placing_buttons = ["+1 worker top","+1 worker down"]
        for i in range(len(placing_buttons)):
            btn = ttk.Button(self.economy_window, text=placing_buttons [i], command=(
                lambda button=placing_buttons [i]: self.controller.on_button_click(button)))
            btn.grid(row=i+2, column=0)
            
    def add_move_worker_panel(self):
        to_move_buttons = ["top --> down","down --> top"]      
        for i in range(len(to_move_buttons)):
            btn = ttk.Button(self.economy_window, text=to_move_buttons[i], command=(
                lambda button=to_move_buttons[i]: self.controller.on_button_click(button)))
            btn.grid(row=i+2, column=1)
            
    def open_upgrades_panel(self, upgrades):
        player = self.controller.find_player_object()
        if (len(upgrades) > 0) or (player.race == "zerg"):
            self.upgrades_window = tk.Toplevel(bg = self.controller.find_player_color("active_player"))
            self.upgrades_window.title('choose upgrade')
            self.upgrades_window.iconbitmap(r"images/terran_icon.ico")            
            self.disable_buttons()
            self.upgrades_window.protocol( 'WM_DELETE_WINDOW', self.__CancelCommand)              
            self._make_exit_button(self.upgrades_window, "exit upgrades", 4, 4) 
            
            picture_slot = [self.upgrade_slot1 , self.upgrade_slot2 , self.upgrade_slot3]
            
            for i in range(len(upgrades)): 
                btn = ttk.Button(self.upgrades_window, text="test", 
                         image=picture_slot[i], command=
                         (lambda an_object=upgrades[i]: self.controller.on_button_upgrade_click(an_object)))    
                picture_slot[i]["file"] = upgrades[i].photo
                btn.grid(row=i,column=0)
                a_frame =  ttk.Frame(self.upgrades_window)
                a_frame.grid(row=i,column=1)
                a_title = tk.Label(a_frame, font=self.big_font)
                a_title["text"] = upgrades[i].name
                a_title.grid(row=0)
                a_title = tk.Label(a_frame, font=self.medium_font)
                a_title["text"] = (f"{upgrades[i].cost[1]} minerals {upgrades[i].cost[2]} gas")
                a_title.grid(row=1)
                a_title = tk.Label(a_frame, font=self.small_font)
                a_title["text"] = upgrades[i].description
                a_title.grid(row=2)
            self._add_evolution_button()
        else: print("no upgrades")
            
    def _add_evolution_button(self):
        if self.controller.verify_if_add_evolution_button(): 
            _creatures = self.controller.find_active_player_creature_objects()
            buttons, labels, labels2 =[],[],[]
            
            if "Hydralisk" in [c.name for c in _creatures]:
                btn1 = ttk.Button(self.upgrades_window, text="Lurker", 
                                     image=self.evolution_Lurker, command=
                                     (lambda button="Lurker": self.controller.on_button_evolution(button)))
                buttons.append(btn1)
                a_label1 = tk.Label(self.upgrades_window, font=self.medium_font)
                a_label1["text"] = "Evolves random hydralisk\ninto a lurker."
                labels.append(a_label1)
                a_label11 = tk.Label(self.upgrades_window, font=self.small_font)
                a_label11["text"] = "1 pop 100 min. 50 gas"
                labels2.append(a_label11)                
                
            if "Mutalisk" in [c.name for c in _creatures]:
                btn2 = ttk.Button(self.upgrades_window, text="Guardian", 
                                     image=self.evolution_Guardian, command=
                                     (lambda button="Guardian": self.controller.on_button_evolution(button)))
                buttons.append(btn2)
                a_label2 = tk.Label(self.upgrades_window, font=self.medium_font)
                a_label2["text"] = "Evolves random mutalisk\ninto a guardian."
                labels.append(a_label2)
                a_label22 = tk.Label(self.upgrades_window, font=self.small_font)
                a_label22["text"] = "2 pop 50 min. 100 gas"
                labels2.append(a_label22)               
                
            for i in range(len(buttons)):
                buttons[i].grid(row=4,column=i+1)
                labels[i].grid(row=5,column=i+1)
                labels2[i].grid(row=6,column=i+1)
            
           
    def destroy_one_windows(self, given_window):
        given_window.destroy()
        self.activate_buttons()
          
    def disable_buttons(self):  
        for a_button in self.button_box:  a_button["state"] = "disabled"
    
    def activate_buttons(self):     
        for a_button in self.button_box:  a_button["state"] = "normal" 
        
    #this is to update method on exit button, so you cannot do it manually
    def __CancelCommand(event=None): pass       