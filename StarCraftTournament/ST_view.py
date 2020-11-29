import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import GROOVE, RIDGE, RAISED, SUNKEN


class View(tk.Tk):

    PAD = 5
    
    def __init__(self, controller):

        super().__init__()
        
        self.controller = controller
        
        self.title("StarCraft Tournament")
        self.iconbitmap(r"images/terran_icon.ico")
        self.configure(bg="navyblue")
        
        self.button_captions = ["play a unit","pass a turn","  upgrades", 
                                "evolutions", " economy"]
        
        self.button_pictures = []        
        
        self.slot1_description = tk.StringVar()
        self.slot2_description = tk.StringVar()
        self.slot3_description = tk.StringVar()
        self.slot4_description = tk.StringVar()
        self.slot5_description = tk.StringVar()
        self.slot6_description = tk.StringVar()       
        
        self.creature_list = list()
        
        self.button_box = []
        
        self._make_main_frame()
        self._make_architecture()
        self.fill_creature_slotz()
        self._hardcode_creature_images()
        #test####AHTUNG --- CANVAS ARE SICK SHIT ------#####
        #self._make_canvas()         
        self._create_starting_creature_labels()
        self._make_frames_inside_creature_frames()
        self._make_memo_window()
        self._make_main_buttons()
        self._make_infobars()
        self.fill_infobars()
        
        
    def main(self):
        self.mainloop()
        
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

        self.slot1_photo_label = tk.Label(self.creature_frame, image = self.slot1_photo, bg= "blue", relief = SUNKEN)         
        self.slot1_photo_label.grid(row=0,column=0)
        self.slot2_photo_label = tk.Label(self.creature_frame, image = self.slot2_photo, bg= "blue", relief = SUNKEN)         
        self.slot2_photo_label.grid(row=1,column=0)
        self.slot3_photo_label = tk.Label(self.creature_frame, image = self.slot3_photo, bg= "blue", relief = SUNKEN)         
        self.slot3_photo_label.grid(row=2,column=0)
        self.slot4_photo_label = tk.Label(self.creature_frame, image = self.slot4_photo, bg= "red", relief = SUNKEN)        
        self.slot4_photo_label.grid(row=0,column=1)
        self.slot5_photo_label = tk.Label(self.creature_frame, image = self.slot5_photo, bg= "red", relief = SUNKEN)         
        self.slot5_photo_label.grid(row=1,column=1)
        self.slot6_photo_label = tk.Label(self.creature_frame, image = self.slot6_photo, bg= "red", relief = SUNKEN)         
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
        #tkinter technology need refereances saved
        #otherwise they go to python garbage collection.
        self.slot1_photo = tk.PhotoImage(file = "images/larva.png")
        self.slot2_photo = tk.PhotoImage(file = "images/larva.png")
        self.slot3_photo = tk.PhotoImage(file = "images/larva.png")
        self.slot4_photo = tk.PhotoImage(file = "images/larva.png")
        self.slot5_photo = tk.PhotoImage(file = "images/larva.png")
        self.slot6_photo = tk.PhotoImage(file = "images/larva.png")
        
        self.option1_photo = tk.PhotoImage(file = "images/larva.png")
        self.option2_photo = tk.PhotoImage(file = "images/larva.png")
        self.option3_photo = tk.PhotoImage(file = "images/larva.png")
        self.option4_photo = tk.PhotoImage(file = "images/larva.png")
        self.option5_photo = tk.PhotoImage(file = "images/larva.png")
        
        self.economy_window1 = tk.PhotoImage(file = "images/SCV.png")
        self.economy_window2 = tk.PhotoImage(file = "images/SCV_run_away.png")
        
        self.exit_photo = tk.PhotoImage(file = "images/exit.png")
        self.houses_photo = tk.PhotoImage(file = "images/houses.png")
        self.detector_photo = tk.PhotoImage(file = "images/observer.png")
        
    def creature_picture_changer(self, picture_slot, picture_address):

        slot = [self.slot1_photo,self.slot2_photo,self.slot3_photo,
                self.slot4_photo,self.slot5_photo, self.slot6_photo]
        slot[picture_slot-1] ["file"] = picture_address
        
    
    def _make_frames_inside_creature_frames(self):  
        PAD_inner = 1
        slots1 = [self.slot1_description, self.slot2_description, self.slot3_description]
        slots2 = [self.slot4_description, self.slot5_description, self.slot6_description]
        
        a_frame = ttk.Frame(self.creature_frame)
        a_frame.grid(row=0, padx=PAD_inner, pady=PAD_inner)
        
        for i in range (3):
            
            a_frame = tk.Frame(self.creature_frame)
            a_frame.grid(row=i, column=0, padx=PAD_inner, pady=PAD_inner, sticky="SE")     
            a_label = tk.Label(a_frame, textvariable = slots1[i])
            a_label.grid(row=i, column=0 )
            
            a_frame = ttk.Frame(self.creature_frame)
            a_frame.grid(row=i, column=1, padx=PAD_inner, pady=PAD_inner, sticky="SE")
            a_label = ttk.Label(a_frame, textvariable = slots2[i])
            a_label.grid(row=i, column=1 )
    

    def _make_infobars(self):        
        players_info = self.controller.find_data_for_player_description()  
        
        self.infobar_frame = tk.Frame(self.work_frame)
        self.infobar_frame.grid(row=0, column=0)
        
        self.player_1_infobar = tk.Label(self.infobar_frame, bg=self.controller.find_player_color("active_player"),
                                         fg="grey", font=("Arial", 12, 'bold'), anchor="n")
        self.player_1_infobar.grid(row=0, column=0)
        
        self.infobar_photo = tk.PhotoImage(file = "images/infobar_.png")
        self.infobar_= tk.Label(self.infobar_frame, image=self.infobar_photo, anchor="n")
        self.infobar_.grid(row=0, column=1)
        
        self.player_2_infobar = tk.Label(self.infobar_frame, bg = self.controller.find_player_color("inactive_player"),
                                         fg="navyblue", font=("Arial", 12, 'bold'), anchor="n")
        self.player_2_infobar.grid(row=0, column=2) 
       
        
    def fill_infobars(self):
        players_info = self.controller.find_data_for_player_description()      
        self.player_1_infobar["text"] = players_info[0]
        self.player_2_infobar["text"] = players_info[1]
  
    #button captions can be taken for a race from a Model, ????. AND PICTURES
    #can be zipped with button pictures later on to alterate          
    def _make_main_buttons(self):
        self._photo = tk.PhotoImage(file = "images/population.png")
        self._photoimage = self._photo.subsample(1, 1) 
        index=0
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
        
        self.memo_label = tk.Label(self.memo_frame, fg="navyblue", font=("Arial", 8, 'bold'), justify="left")
        self.memo_label.grid(sticky="w")
        
        self.fill_memo_label()        

        
    def fill_memo_label(self):
        self.memo_label["text"] = self.controller.find_data_for_memo_label()

    def _make_exit_button(self, parent, text, column):
        
        btn = ttk.Button(parent, text=text, image=self.exit_photo, command=
                         (lambda button=text: self.controller.on_button_click(button)))
        btn.grid(row=0,column=column)
       
    def make_detector_play_button(self):
        if self.controller.verify_if_detector_play_button_needed():
            detector = self.controller.find_active_player_detector_object()
            self.detector_photo["file"] = detector.photo
            btn = ttk.Button(self.economy_window, text=detector.name, image=self.detector_photo, 
                             command=(lambda button=detector.name: self.controller.on_button_click(button)))
            btn.grid(row=0,column=4)
            label_cost = tk.Label(self.economy_window)             
            if detector.name =="Overlord": 
                cost_description = "move overlord to the board"
            else: 
                cost_description = (f" {str(detector.cost[1])} min\
            {str(detector.cost[2])} gas \
            {str(detector.cost[0])} pop")  
            label_cost["text"] = "Get detector!\n" + cost_description
            label_cost.grid(row=1,column=4)
    
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
        
        picture_slot =[self.option1_photo, self.option2_photo, self.option3_photo,
                              self.option4_photo, self.option5_photo] 
        
        for i in range (len(picture_slot)):
            picture_slot[i] ["file"] = picture_names[i]
            cost_description = (f" {str(picture_costs[i][1])} min\
            {str(picture_costs[i][2])} gas \
            {str(picture_costs[i][0])} pop")  
            label_cost = tk.Label(self.play_window)
            label_cost["text"] = cost_description
            label_cost.grid(row=1,column=i) 
            
            btn = ttk.Button(self.play_window, text=picture_data[i], image=picture_slot[i], 
                             command=
                             (lambda button=picture_data[i]: self.controller.on_button_click(button)))
            btn.grid(row=0,column=i)        
            
        self._make_exit_button(self.play_window, "exit play", 7)
        
        
    def add_creature_placement_panel(self,slot):
        placement_buttons = ["top","center","down"]
        for i in range(len(placement_buttons)):
            btn = ttk.Button(self.play_window, text=placement_buttons[i], command=(
                lambda button=placement_buttons[i]: self.controller.on_button_click(button)))
            btn.grid(row=i+2, column=slot)         

    
    def open_economy_panel(self):
        self.economy_window = tk.Toplevel(bg = self.controller.find_player_color("active_player"))
        self.economy_window.title('your economy commander!')
        self.economy_window.iconbitmap(r"images/terran_icon.ico")
        self.disable_buttons()
        self.economy_window.protocol( 'WM_DELETE_WINDOW', self.__CancelCommand)  
    
        
        descriptions_economy = ["get a worker (50 minerals)", "move 10 workers", "increase population (100 min.)"]
        photos_economy = [self.economy_window1, self.economy_window2, self.houses_photo]
        data = zip(descriptions_economy, photos_economy)
        
        for i in range (len(photos_economy)):
            btn = ttk.Button(self.economy_window, text=descriptions_economy[i], 
                             image=photos_economy[i], command=
                                 (lambda button=descriptions_economy[i]: self.controller.on_button_click(button)))
            btn.grid(row=0,column=i)                 
        for i in range (len(photos_economy)):
            a_label = tk.Label(self.economy_window)
            a_label["text"] = descriptions_economy[i]
            a_label.grid(row=1, column=i) 
        self.make_detector_play_button()
        self._make_exit_button(self.economy_window, "exit economy", 5)
        
            
    
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
           
    def destroy_one_windows(self, given_window):
        given_window.destroy()
        self.activate_buttons()
          
    def disable_buttons(self):  
        for a_button in self.button_box:  a_button["state"] = "disabled"
    
    def activate_buttons(self):     
        for a_button in self.button_box:  a_button["state"] = "normal" 
        
    #this is to update method on exit button, so you cannot do it manually
    def __CancelCommand(event=None): pass       
        
       
        
        ## we can make with state color for windows
        #destroy all windwos  on the end of turn
        
        #We need to remove "x" from toplevel
        #or
        #make on_click even when it is called  (to activate buttons)