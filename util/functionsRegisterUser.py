import mysql.connector
from tkinter import messagebox

def insert_username_password_database(full_name, full_name_company, full_name_user, full_password):
    bd = mysql.connector.connect(
    host = "localhost",
    port=3306,
    user = "root",
    passwd = "¡MessiRonaldoNeymar123789*",
    db = "appsaletkinter"
    )
    
    fcursor = bd.cursor()
    sql = "INSERT INTO registeruser (FullName, CompanyName, Username, Passwords) VALUES ('{0}', '{1}', '{2}', '{3}')".format(full_name.get(), full_name_company.get(), full_name_user.get(), full_password.get())
    
    try: 
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Registro exitoso", title = "Aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="No registrado", title = "Aviso")
    
    bd.close()