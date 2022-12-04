import tkinter as tk
import util.generic as ut1
import os

from tkinter import Frame
from tkinter import Entry
from tkinter import Button
from tkinter import Label

class IntroduceInformationInForm:
    def __init__(self):
        self.ventanasec = tk.Tk()
        self.ventanasec.title("Introduce Information In Form")
        w, h = 1000,700
        self.ventanasec.geometry("%dx%d+0+0"%(w,h))
        self.ventanasec.config(bg="#fcfcfc")
        self.ventanasec.resizable(width=0,height=0)
        
        absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
        absolute_image_path = os.path.join(absolute_folder_path, "./imageIntroduceInfo.png")
        
        background_main = ut1.read_image(absolute_image_path, (1000,700))
        label_background_main = tk.Label(self.ventanasec, image=background_main, bg="#fcfcfc")
        label_background_main.place(x=0,y=0,
                                    relheight=1, relwidth=1)
        
        self.ventanasec.mainloop()
        