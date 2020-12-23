from tkinter import *

import tkinter

top = Tk()

mb=  Menubutton ( top, text="P1 race:", relief=RAISED )
mb.grid()
mb.menu =  Menu(mb, tearoff = 100)
mb["menu"] = mb.menu

mayoVar = StringVar()
ketchVar = StringVar()

mb.menu.add_checkbutton (label="Z", variable=mayoVar)
mb.menu.add_checkbutton (label="T", variable=ketchVar)

mb.pack()
top.mainloop()