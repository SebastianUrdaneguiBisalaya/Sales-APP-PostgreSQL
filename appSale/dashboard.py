import tkinter as tk
import util.generic as ut1
import os
import mysql.connector

from tkinter import Frame
from tkinter import Entry
from tkinter import Button
from tkinter import Label
from tkinter import messagebox

class Dashboard:
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Dashboard Sales APP")
        w, h = 1300, 700
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg="#fcfcfc")
        self.ventana.resizable(width=0,height=0)
        
        absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
        absolute_image_path = os.path.join(absolute_folder_path, "./Dashboard.png")
        
        main_screen = ut1.read_image(absolute_image_path, (1300,700))
        label = tk.Label(self.ventana, image = main_screen, bg = "#fcfcfc")
        label.place(x=0, y=0, relwidth=1, relheight=1)
        
        
        self.ventana.mainloop()