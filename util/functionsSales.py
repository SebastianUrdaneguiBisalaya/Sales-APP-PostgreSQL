from tkinter import *
from datetime import datetime

def destroy(ventanasec):
    ventanasec.destroy()
    
def time():
    return datetime.now().strftime("%H:%M:%S")

def delete_all_information(mode_delivery, customer_name, segment_customer, country, city, state, postal_code, region, product_name, info_category, subcategory_product):
    mode_delivery.set("")
    customer_name.set("")
    segment_customer.set("")
    country.set("")
    city.set("")
    state.set("")
    postal_code.set("")
    region.set("")
    product_name.set("")
    info_category.set("")
    subcategory_product.set("")

def delete_partial_information(product_name, info_category, subcategory_product):
    product_name.set("")
    info_category.set("")
    subcategory_product.set("")