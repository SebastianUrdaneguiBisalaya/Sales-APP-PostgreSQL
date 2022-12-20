import mysql.connector
from tkinter import *
from tkinter import messagebox
from datetime import datetime

def destroy(ventanasec):
    ventanasec.destroy()
    
def time():
    return datetime.now().strftime("%H:%M:%S")

def delete_all_information(delivery_date, mode_delivery, customer_name, segment_customer, country, city, states, postal_code, region, product_name, info_category, subcategory_product):
    delivery_date.set("")
    mode_delivery.set("")
    customer_name.set("")
    segment_customer.set("")
    country.set("")
    city.set("")
    states.set("")
    postal_code.set("")
    region.set("")
    product_name.set("")
    info_category.set("")
    subcategory_product.set("")

def delete_partial_information(product_name, info_category, subcategory_product):
    product_name.set("")
    info_category.set("")
    subcategory_product.set("")
    
def send_information_sales(order_date, delivery_date, mode_delivery, customer_name, segment_customer, country, city, states, postal_code, region, product_name, info_category, subcategory_product):
    bd = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        passwd = "¡MessiRonaldoNeymar123789*",
        db = "appsaletkinter"
    )
    
    fcursor = bd.cursor()
    sql = "INSERT INTO informationSales (OrderDate, OrderDelivery, ModeDelivery, CustomerName, SegmentCustomer, Country, City, States, PostalCode, Region, ProductName, CategoryName, SubCategoryName) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}')".format(order_date.get(), delivery_date.get(), mode_delivery.get(), customer_name.get(), segment_customer.get(), country.get(), city.get(), states.get(), postal_code.get(), region.get(), product_name.get(), info_category.get(), subcategory_product.get())
    
    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Se registró correctamente la información", title = "Aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="¡Ocurrió un error!", title="Aviso")
    
    bd.close()