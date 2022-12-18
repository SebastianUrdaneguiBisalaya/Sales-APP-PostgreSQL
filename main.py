from appSale.modules.moduleSales import IntroduceInformationInForm
from appSale.modules.moduleRegisterUser import RegisterForm

import tkinter as tk
import util.generic as ut1
import os

from functools import partial

from tkinter import *

from util.functionsLogin import validation_username_password_database


class ShadowMenu:
    
    global introduce_name_user 
    global introduce_pasword_user

    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Sales APP")
        w,h = 900,700
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg="#fcfcfc")
        
        wtotal = self.ventana.winfo_screenwidth()
        htotal = self.ventana.winfo_screenheight()
        wventana = 900
        hventana = 700
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)
        self.ventana.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))
        
        self.ventana.resizable(width=0,height=0)
        
        absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
        absolute_image_path = os.path.join(absolute_folder_path, "C:/Users/Fabrizio/Documents/PortfolioProjects/Sales-APP/Sales-APP-PostgreSQL/appSale/assets/assetsLogin/shadowmenu.png")
        
        logo = ut1.read_image(absolute_image_path, (561,700))
        label = tk.Label(self.ventana, image=logo, bg = "#fcfcfc")
        label.place(x=0,y=0,relwidth=0.62,relheight=1)
        
        absolute_image_path_1 = os.path.join(absolute_folder_path, "C:/Users/Fabrizio/Documents/PortfolioProjects/Sales-APP/Sales-APP-PostgreSQL/appSale/assets/assetsLogin/login.png")
        logo_login = ut1.read_image(absolute_image_path_1,(233,239))
        label_login = tk.Label(self.ventana, image=logo_login, bg="#fcfcfc")
        label_login.place(x=601, y=75)
        
        absolute_image_path_2 = os.path.join(absolute_folder_path, "C:/Users/Fabrizio/Documents/PortfolioProjects/Sales-APP/Sales-APP-PostgreSQL/appSale/assets/assetsLogin/iconsmenu.png")
        icons_login = ut1.read_image(absolute_image_path_2, (224,134))
        label_icons_login = tk.Label(self.ventana, image=icons_login, bg = "#fcfcfc")
        label_icons_login.place(x=550, y = 335)
        
        #introduce_name_user = tk.StringVar()
        introduce_name_user = Entry(self.ventana, width=25, fg = "black",
                                    border=0, bg="#fcfcfc", font=("Inter", 11))
        introduce_name_user.place(x=625, y=362)
        
        #introduce_password_user = tk.StringVar()
        introduce_password_user = Entry(self.ventana, width=25, fg="black",
                                        border=0, bg="#fcfcfc", font=("Inter", 11), show="*")
        introduce_password_user.place(x=625, y=448)
        
        Frame(self.ventana, width=265,height=2.5, bg="#4FD377").place(x=570, y=390)
        Frame(self.ventana, width=265, height=2.5, bg="#4FD377").place(x=570, y=480)
            
        
        Button(self.ventana, width=22,pady=7, text = "Iniciar Sesión", bg="#8EA55A", 
               fg="white", border=0, font=("Inter", 12), relief="flat", cursor="hand2",
               command=partial(validation_username_password_database, introduce_name_user, introduce_password_user, self.ventana)).place(x=600,y=540)
        
        Button(self.ventana, text="o Regístrate si no tienes una cuenta",
                               fg="black", bg="#fcfcfc", border=0,
                               font=("Inter", 9), cursor="hand2",
                               command=RegisterForm).place(x=600,y=590)
        

        self.ventana.mainloop()




if __name__ == "__main__":
    ShadowMenu()