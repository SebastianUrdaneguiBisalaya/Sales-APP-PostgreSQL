# import os

# import tkinter
# from tkinter import *

# from tkinter import Tk, PhotoImage, Label

# window = tkinter.Tk()
# window.title("Sales APP")

# frame = tkinter.Frame(window)
# frame.pack()

# window.geometry("900x700")
# window.config(bg="white")

# # # Saving User Information
# # user_info_frame = tkinter.LabelFrame(frame, text = "User Information")
# # user_info_frame.grid(row=0, column=0)

# # first_name_label = tkinter.Label(user_info_frame, text = "First Name")
# # first_name_label.grid(row=0, column=0)

# absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
# absolute_image_path = os.path.join(absolute_folder_path, "./shadowmenu.png")

# image_central = PhotoImage(file=absolute_image_path)
# background = Label(window, image=image_central)
# background.pack()
# background.place(width=700,height=900, bordermode=OUTSIDE,
#                  relx=0.001,rely=0.01) 
# background.config(bg = "white")

# # This function allows keep the app running
# window.mainloop()

import tkinter as tk
from tkinter.font import BOLD
import util.generic as ut1
import os

from tkinter import Frame
from tkinter import messagebox
from tkinter import Entry

class ShadowMenu:
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Sales APP")
        # w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        w,h = 900,700
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg="#fcfcfc")
        self.ventana.resizable(width=0,height=0)
        
        absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
        absolute_image_path = os.path.join(absolute_folder_path, "./shadowmenu.png")
        
        logo = ut1.read_image(absolute_image_path, (561,700))
        label = tk.Label(self.ventana, image=logo, bg = "#fcfcfc")
        label.place(x=0,y=0,relwidth=0.62,relheight=1)
        
        absolute_image_path_1 = os.path.join(absolute_folder_path, "./login.png")
        logo_login = ut1.read_image(absolute_image_path_1,(233,239))
        label_login = tk.Label(self.ventana, image=logo_login, bg="#fcfcfc")
        label_login.place(x=601, y=75)
        
        absolute_image_path_2 = os.path.join(absolute_folder_path, "./iconsmenu.png")
        icons_login = ut1.read_image(absolute_image_path_2, (224,134))
        label_icons_login = tk.Label(self.ventana, image=icons_login, bg = "#fcfcfc")
        label_icons_login.place(x=550, y = 335)
        
        # frame = Frame(self.ventana, width=233, height=180, bg = "red")
        # frame.place(x=601, y = 340)
        
        # introduce_name_user = Entry(self.ventana, width=22, fg = "black",
        #                             border=2, bg="white", font=("Inter", 11))
        # introduce_name_user.place(x=645, y=365)
        # introduce_name_user.insert(0, "Username")
        
        self.ventana.mainloop()