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
        self.iconbitmap(r"terran_icon.ico")
        self.configure(bg="grey")
        
        self.button_captions = ["play","pass","upgrade", 
                                "evolve", "get a worker"]
        #those can be added to alternate look of buttons#IN THE FUTURE#
        self.button_pictures = []        
        
        self.slot1_description = tk.StringVar()
        self.slot2_description = tk.StringVar()
        self.slot3_description = tk.StringVar()
        self.slot4_description = tk.StringVar()
        self.slot5_description = tk.StringVar()
        self.slot6_description = tk.StringVar()       
        
        self._make_main_frame()
        #test##############
        self._make_canvas()
        self._make_architecture()
        self.fill_creature_slotz()
        
        self.creature_list = list()
        self._hardcode_creature_images()
        
        self._create_starting_creature_labels()
        self._make_frames_inside_creature_frames()
        self._make_buttons()
        self._make_life_and_resources()

        #self._make_information_window()
        
        
    def main(self):
        self.mainloop()
        
    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)
        
    def _make_canvas(self):
        canvas_ = tk.Canvas(self.main_frm , width=600, height=600)
        canvas_.grid(row=0,column=0, rowspan=3, columnspan=3)
        self.bgg = tk.PhotoImage(file='command_center.png')
        canvas_.create_image(0, 0, image=self.bgg)
        canvas_.create_text(50, 20, text='         COOL GAME')
 
    def _make_architecture(self):
        self.creature_frame = ttk.Frame(self.main_frm)
        self.p1_frame = ttk.Frame(self.main_frm)
        self.p2_frame = ttk.Frame(self.main_frm)  # do we need it ?
        self.bottom_frame = ttk.Frame(self.main_frm)  # do we need it ?
        
        self.creature_frame.grid(row=0, column=1, columnspan=2, rowspan=3)
        self.p1_frame.grid(row=0, column=0, columnspan=1, rowspan=1)
        self.p2_frame.grid(row=0, column=3, columnspan=1, rowspan=2)
        self.bottom_frame.grid(row=3, column=1, columnspan=2, rowspan=1)
             
    def _create_starting_creature_labels(self):

        self.slot1_photo_label = tk.Label(self.creature_frame, image = self.slot1_photo, relief = SUNKEN)         
        self.slot1_photo_label.grid(row=0,column=0)
        self.slot2_photo_label = tk.Label(self.creature_frame, image = self.slot2_photo, relief = SUNKEN)         
        self.slot2_photo_label.grid(row=1,column=0)
        self.slot3_photo_label = tk.Label(self.creature_frame, image = self.slot3_photo, relief = SUNKEN)         
        self.slot3_photo_label.grid(row=2,column=0)
        self.slot4_photo_label = tk.Label(self.creature_frame, image = self.slot4_photo, relief = SUNKEN)        
        self.slot4_photo_label.grid(row=0,column=1)
        self.slot5_photo_label = tk.Label(self.creature_frame, image = self.slot5_photo, relief = SUNKEN)         
        self.slot5_photo_label.grid(row=1,column=1)
        self.slot6_photo_label = tk.Label(self.creature_frame, image = self.slot6_photo, relief = SUNKEN)         
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
        self.slot1_photo = tk.PhotoImage(file = "larva.png")
        self.slot2_photo = tk.PhotoImage(file = "larva.png")
        self.slot3_photo = tk.PhotoImage(file = "larva.png")
        self.slot4_photo = tk.PhotoImage(file = "larva.png")
        self.slot5_photo = tk.PhotoImage(file = "larva.png")
        self.slot6_photo = tk.PhotoImage(file = "larva.png")
        
        self.option1_photo = tk.PhotoImage(file = "larva.png")
        self.option2_photo = tk.PhotoImage(file = "larva.png")
        self.option3_photo = tk.PhotoImage(file = "larva.png")
        self.option4_photo = tk.PhotoImage(file = "larva.png")
        self.option5_photo = tk.PhotoImage(file = "larva.png")
        
        
    def creature_picture_changer(self, picture_slot, picture_address):

        slot = [self.slot1_photo,self.slot2_photo,self.slot3_photo,
                self.slot4_photo,self.slot5_photo, self.slot6_photo]
        slot[picture_slot-1] ["file"] = picture_address
        
    
    def _make_frames_inside_creature_frames(self):  #### ?
        
        PAD_inner = 1
        slots1 = [self.slot1_description, self.slot2_description, self.slot3_description]
        slots2 = [self.slot4_description, self.slot5_description, self.slot6_description]
        
        a_frame = ttk.Frame(self.creature_frame)
        a_frame.grid(row=0, padx=PAD_inner, pady=PAD_inner)
        
        for i in range (3):
            
            a_frame = tk.Frame(self.creature_frame)
            a_frame.grid(row=i, column=0, padx=PAD_inner, pady=PAD_inner, sticky="SE")     
            a_label = tk.Label(a_frame, textvariable = slots1[i])
            a_label.grid(row=i, column=0)
            
            a_frame = ttk.Frame(self.creature_frame)
            a_frame.grid(row=i, column=1, padx=PAD_inner, pady=PAD_inner, sticky="SE")
            a_label = ttk.Label(a_frame, textvariable = slots2[i])
            a_label.grid(row=i, column=1)
    
    #can be divaded into more functions
    def _make_life_and_resources(self):
        players_info = self.controller.find_data_for_player_description()      
        self.player_1_info = tk.Label(self.p1_frame)
        self.player_1_info["text"] = players_info[0]
        self.player_1_info.pack(side="top") 
        self.player_2_info = tk.Label(self.p1_frame,fg="green")
        self.player_2_info["text"] = players_info[1]
        self.player_2_info.pack(side="right")   
  
    #button captions can be taken for a race from a Model, later on. AND PICTURES
    #can be zipped with burtton pictures later on to alterate          
    def _make_buttons(self):
        self._photo = tk.PhotoImage(file = "population.png")
        self._photoimage = self._photo.subsample(1, 1) 
        for caption in self.button_captions:
            btn = ttk.Button(self.p1_frame, image= self._photoimage, compound = "left",text=caption, command=(
                lambda button=caption: self.controller.on_button_click(button)))
            btn.pack(side='bottom', expand=True)
    
    def _make_information_window(self):
        label_3 = tk.Label(self.p1_frame, text="*****\nHERE WILL BE\nINFORMATION WINDOW\n*****")
        label_3.pack(expand=False) 
        #we will can make it as a long string XD top down; then  line of miniatures
        #then line of player2 stats XD
          

    def open_play_window(self):
        self.play_window = tk.Toplevel()
        self.play_window.title('choose play')
        self.play_window.iconbitmap(r"terran_icon.ico")
        
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
            
        
    def add_creature_placement_panel(self,slot):
        placement_buttons = ["top","center","down"]
        a_frame = tk.Frame(self.play_window)
        a_frame.grid(row=0, column=6)
        for i in range(len(placement_buttons)):
            btn = ttk.Button(self.play_window, text=placement_buttons[i], command=(
                lambda button=placement_buttons[i]: self.controller.on_button_click(button)))
            btn.grid(row=i+2, column=slot)