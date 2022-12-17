import tkinter as tk
import util.generic as ut1
import os
import mysql.connector

from functools import partial

from tkinter import *
from tkinter import Frame
from tkinter import Entry
from tkinter import Button
from tkinter import Label
from tkinter import messagebox

from util.functionsRegisterUser import insert_username_password_database

class RegisterForm:
    
    def __init__(self):
        self.ventanaR = Toplevel()
        self.ventanaR.title("Register Sales APP")
        w, h = 450, 700
        self.ventanaR.geometry("%dx%d+0+0" % (w, h))
        self.ventanaR.config(bg="#fcfcfc")
        self.ventanaR.resizable(width=0, height=0)
        
        absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
        absolute_image_path = os.path.join(absolute_folder_path, "C:/Users/Fabrizio/Documents/PortfolioProjects/Sales-APP/Sales-APP-PostgreSQL/appSale/assets/assetsRegisterUser/RegisterForm.png")
        
        logo = ut1.read_image(absolute_image_path, (451,608))
        label = tk.Label(self.ventanaR, image = logo, bg = "#fcfcfc")
        label.place(x=0, y=0, relwidth=1, relheight=0.86)
        
        full_name = Entry(self.ventanaR, width=36, fg = "black", bg = "#fcfcfc", font = ("Inter", 11), border=0, cursor="arrow", justify="center")
        full_name.place(x=82, y = 410)
        Frame(self.ventanaR, width=309, height=2.5, bg="#EA7E7E").place(x=72, y= 435)
        
        full_name_company = Entry(self.ventanaR, width=36, fg = "black", bg = "#fcfcfc", font = ("Inter", 11), border=0, cursor="arrow", justify="center")
        full_name_company.place(x=82, y = 470)
        Frame(self.ventanaR, width=309, height=2.5, bg="#EA7E7E").place(x=72, y= 495)
        
        full_name_user = Entry(self.ventanaR, width=36, fg = "black", bg = "#fcfcfc", font = ("Inter", 11), border=0, cursor="arrow", justify="center")
        full_name_user.place(x=82, y = 534)
        Frame(self.ventanaR, width=309, height=2.5, bg="#EA7E7E").place(x=72, y= 560)
        
        full_password = Entry(self.ventanaR, width=36, fg = "black", bg = "#fcfcfc", font = ("Inter", 11), border=0, cursor="arrow", show="*", justify="center")
        full_password.place(x=82, y = 597)
        Frame(self.ventanaR, width=309, height=2.5, bg="#EA7E7E").place(x=72, y= 623)
        
        Button(self.ventanaR, width=15,pady=7, text = "Registrarse", bg="#EA7E7E", 
               fg="white", border=0, font=("Inter", 12), relief="flat", cursor="hand2",
               command=partial(insert_username_password_database, full_name, full_name_company, full_name_user, full_password)).place(x=160,y=645)
        
        self.ventanaR.mainloop()
        

# def RegisterForm(self):
#     self.ventana = Toplevel()
#     self.ventana.title("Register Sales APP")
#     w, h = 450, 700
#     self.ventana.geometry("%dx%d+0+0" % (w, h))
#     self.ventana.config(bg="#fcfcfc")
#     self.ventana.resizable(width=0, height=0)
    
#     absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
#     absolute_image_path = os.path.join(absolute_folder_path, "C:/Users/Fabrizio/Documents/PortfolioProjects/Sales-APP/Sales-APP-PostgreSQL/appSale/assets/assetsRegisterUser/RegisterForm.png")
    
#     logo = ut1.read_image(absolute_image_path, (451,608))
#     label = tk.Label(self.ventana, image = logo, bg = "#fcfcfc")
#     label.place(x=0, y=0, relwidth=1, relheight=0.86)
    
#     full_name = Entry(self.ventana, width=36, fg = "black", bg = "#fcfcfc", font = ("Inter", 11), border=0, cursor="arrow", justify="center")
#     full_name.place(x=82, y = 410)
#     Frame(self.ventana, width=309, height=2.5, bg="#EA7E7E").place(x=72, y= 435)
    
#     full_name_company = Entry(self.ventana, width=36, fg = "black", bg = "#fcfcfc", font = ("Inter", 11), border=0, cursor="arrow", justify="center")
#     full_name_company.place(x=82, y = 470)
#     Frame(self.ventana, width=309, height=2.5, bg="#EA7E7E").place(x=72, y= 495)
    
#     full_name_user = Entry(self.ventana, width=36, fg = "black", bg = "#fcfcfc", font = ("Inter", 11), border=0, cursor="arrow", justify="center")
#     full_name_user.place(x=82, y = 534)
#     Frame(self.ventana, width=309, height=2.5, bg="#EA7E7E").place(x=72, y= 560)
    
#     full_password = Entry(self.ventana, width=36, fg = "black", bg = "#fcfcfc", font = ("Inter", 11), border=0, cursor="arrow", show="*", justify="center")
#     full_password.place(x=82, y = 597)
#     Frame(self.ventana, width=309, height=2.5, bg="#EA7E7E").place(x=72, y= 623)
    
#     Button(self.ventana, width=15,pady=7, text = "Registrarse", bg="#EA7E7E", 
#             fg="white", border=0, font=("Inter", 12), relief="flat", cursor="hand2",
#             command=partial(insert_username_password_database, full_name, full_name_company, full_name_user, full_password)).place(x=160,y=645)
    
#     self.ventana.mainloop()