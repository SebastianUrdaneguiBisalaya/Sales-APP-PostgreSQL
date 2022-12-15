import mysql.connector

from tkinter import messagebox

global introduce_name_user
global introduce_password_user

def insert_username_password_database():
    bd = mysql.connector.connect(
        host = "localhost",
        port=3306,
        user = "root",
        passwd = "¡MessiRonaldoNeymar123789*",
        db = "appsaletkinter"
    )
    
    fcursor = bd.cursor()
    sql = "INSERT INTO login (username, passwords) VALUES ('{0}', '{1}')".format(introduce_name_user.get(), introduce_password_user.get())
    
    try: 
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Registro exitoso", title = "Aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="No registrado", title = "Aviso")
    
    bd.close()