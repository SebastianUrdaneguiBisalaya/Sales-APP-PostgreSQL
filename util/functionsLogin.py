import mysql.connector
from tkinter import messagebox

from appSale.modules.moduleSales import IntroduceInformationInForm


def validation_username_password_database(introduce_name_user, introduce_password_user, ventana):
    bd = mysql.connector.connect(
            host = "localhost",
            port = 3306,
            user = "root",
            passwd = "¡MessiRonaldoNeymar123789*",
            db = "appsaletkinter"
        )
            
    fcursor = bd.cursor()
    fcursor.execute("SELECT Passwords FROM registerUser WHERE Username = '"+introduce_name_user.get()+"' and Passwords = '"+introduce_password_user.get()+"'")
    
    if fcursor.fetchall():
        #messagebox.showinfo(message="Inicio de Sesión Correcta")
        ventana.destroy()
        IntroduceInformationInForm()
    else:
        messagebox.showinfo(message="Inicio de Sesión Incorrecta")
        
    bd.close()

