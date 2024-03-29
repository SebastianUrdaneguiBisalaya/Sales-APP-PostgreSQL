from tkinter import *
import tkinter as tk
import util.generic as ut1
import os
from functools import partial
from datetime import datetime

from tkinter import Entry
from tkinter import Button
from tkinter import Label
from tkinter import LabelFrame
from ttkbootstrap import Combobox, Button

from ttkbootstrap import DateEntry
# from ttkbootstrap import Combobox, Button

from util.functionsSales import destroy
from util.functionsSales import time
from util.functionsSales import delete_partial_information 
from util.functionsSales import delete_all_information
from util.functionsSales import send_information_sales

class IntroduceInformationInForm:
    def __init__(self):
        
        self.ventanasec = tk.Tk()
        self.ventanasec.title("Introduce Information In Form")
        w, h = 1000,700
        self.ventanasec.geometry("%dx%d+0+0"%(w,h))
        self.ventanasec.config(bg="#fcfcfc")
        
        wtotal = self.ventanasec.winfo_screenwidth()
        htotal = self.ventanasec.winfo_screenheight()
        wventana = 1000
        hventana = 700
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)
        self.ventanasec.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))
        
        self.ventanasec.resizable(width=0,height=0)
        
        absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
        absolute_image_path = os.path.join(absolute_folder_path, "C:/Users/Fabrizio/Documents/PortfolioProjects/Sales-APP/Sales-APP-PostgreSQL/appSale/assets/assetsRegisterSales/imageIntroduceInfo.png")
        background_main = ut1.read_image(absolute_image_path, (1000,700))
        label_background_main = tk.Label(self.ventanasec, image=background_main, bg="#fcfcfc")
        label_background_main.place(x=0,y=0,
                                    relheight=1, relwidth=1)
        
    # Creating the button
      #   Button(self.ventanasec, width=11, pady=4, text="Enviar", bg="#1F3DA7", fg="white",
      #          border=1,font=("Inter", 12), relief="flat", cursor="hand2").place(x=505, y=599)
        
      #   Button(self.ventanasec, width=11, pady=4, text="Limpiar", bg="#E8D051", fg="black",
      #          border=1,font=("Inter", 12), relief="flat", cursor="hand2").place(x=652, y=599)
      #   Button(self.ventanasec, width=16, text="Limpiar Producto", bootstyle = "warning",
      #          cursor="hand2", command=partial(delete_partial_information, product_name, info_category, subcategory_product)).place(x=595, y=599)
        
      #   Button(self.ventanasec, width=11, text = "Limpiar", bootstyle = "info",
      #          cursor="hand2").place(x=730, y=599)
        
      #   Button(self.ventanasec, width=11, pady=4, text="Cerrar", fg="white",
      #          border=1,font=("Inter", 12), relief="flat", cursor="hand2", command=partial(destroy, self.ventanasec)).place(x=799, y=599)
        Button(self.ventanasec, width=9, text="Cerrar", bootstyle = "danger",
               cursor="hand2", command=partial(destroy, self.ventanasec)).place(x=835, y=599)
        
    # Creating the main of secondary screen
      #   tk.Label(self.ventanasec, text="N° de Orden:", font=("Inter", 11), bg="#FFFFFF").place(x=94,y=209)
      #   id_orden = tk.IntVar(0)
      #   tk.Entry(self.ventanasec, width=10, fg="black", border=0,
      #         bg="#D9D9D9", font=("Inter", 11), textvariable = id_orden,
      #         state="readonly", cursor="arrow", justify="center").place(x=190,y=211)
        
        text_time = tk.StringVar(self.ventanasec, value = time())
        tk.Label(self.ventanasec, text="Hora actual: ", font = ("Inter", 11)).place(x=94, y = 209)
        tk.Label(self.ventanasec, textvariable=text_time, font=("Inter",11)).place(x=190, y=209)
        
        self.label_frame_1 = LabelFrame(self.ventanasec, text="Orden", width=820, height=70, font=("Inter", 11), bg="#FFFFFF")
        self.label_frame_1.place(x=94, y=255)
        
        Label(self.label_frame_1, text = "Fecha de orden:", bg="#FFFFFF", font=("Inter",11)).pack(padx=12,pady=12, side="left")
        date= datetime.now()
        date_now = str(date.date().strftime("%Y-%m-%d"))
        order_date = tk.StringVar()
        order_date.set(date_now)
        order_date_e= Entry(self.label_frame_1, width=13, border=0, cursor="arrow", textvariable=order_date, justify="center",
              font = ("Inter", 11)).pack(padx=6,pady=12, side="left")
        
        Label(self.label_frame_1, text = "Fecha de entrega:", bg="#FFFFFF", font=("Inter",11)).pack(padx=12,pady=12, side="left")
        delivery_date = tk.StringVar()
        delivery_date_e = Entry(self.label_frame_1, width=13, border=0, cursor="arrow", textvariable=delivery_date, justify="center",
              font = ("Inter", 11)).pack(padx=12,pady=12, side="left")
        
        Label(self.label_frame_1, text = "Modo de entrega:", bg="#FFFFFF", font=("Inter",11)).pack(padx=12,pady=12, side="left")
        mode_delivery = tk.StringVar()
        mode_delivery_e = Entry(self.label_frame_1, width=14, fg="black", border=0, font=("Inter", 11), bg="#D9D9D9", cursor="arrow",
              justify="center", textvariable=mode_delivery).pack(padx=16,pady=12, side="left")
        
        self.label_frame_2 = LabelFrame(self.ventanasec, text="Cliente", width=820, height=70, font=("Inter", 11), bg="#FFFFFF")
        self.label_frame_2.place(x=94,y=335)
        
        Label(self.label_frame_2, text = "Cliente:", bg="#FFFFFF", font=("Inter",11)).pack(padx=12,pady=12, side="left")
        customer_name = tk.StringVar()
        customer_name_e = Entry(self.label_frame_2, width=30, fg="black", border=0, font=("Inter", 11), bg="#D9D9D9", cursor="arrow",
              justify="center", textvariable=customer_name).pack(padx=24,pady=12, side="left")
        
        Label(self.label_frame_2, text = "Segmento del cliente:", bg="#FFFFFF", font=("Inter",11)).pack(padx=12,pady=12, side="left")
        segment_customer = tk.StringVar()
        segment_customer_e = Entry(self.label_frame_2, width=30, fg="black", border=0, font=("Inter", 11), bg="#D9D9D9", cursor="arrow",
              justify="center", textvariable=segment_customer).pack(padx=21,pady=12, side="left")
        
        self.label_frame_3 = LabelFrame(self.ventanasec, text="Lugar", width=820, height=70, font=("Inter", 11), bg="#FFFFFF")
        self.label_frame_3.place(x=94, y=415)
        
        Label(self.label_frame_3, text = "País:", bg="#FFFFFF", font=("Inter",11)).pack(padx=12,pady=12, side="left")
        country = tk.StringVar()
        country_e = Entry(self.label_frame_3, width=8, fg="black", border=0, font=("Inter", 11), bg="#D9D9D9", cursor="arrow",
              justify="center", textvariable=country).pack(padx=6,pady=12, side="left")
        
        Label(self.label_frame_3, text = "Ciudad:", bg="#FFFFFF", font=("Inter",11)).pack(padx=12,pady=12, side="left")
        city = tk.StringVar()
        city_e = Entry(self.label_frame_3, width=8, fg="black", border=0, font=("Inter", 11), bg="#D9D9D9", cursor="arrow",
              justify="center", textvariable=city).pack(padx=6,pady=12, side="left")
        
        Label(self.label_frame_3, text = "Estado:", bg="#FFFFFF", font=("Inter",11)).pack(padx=12,pady=12, side="left")
        states = tk.StringVar()
        states_e = Entry(self.label_frame_3, width=8, fg="black", border=0, font=("Inter", 11), bg="#D9D9D9", cursor="arrow",
              justify="center", textvariable=states).pack(padx=6,pady=12, side="left")
        
        Label(self.label_frame_3, text = "Código Postal:", bg="#FFFFFF", font=("Inter",11)).pack(padx=12,pady=12, side="left")
        postal_code = tk.IntVar()
        postal_code_e = Entry(self.label_frame_3, width=8, fg="black", border=0, font=("Inter", 11), bg="#D9D9D9", cursor="arrow",
              justify="center", textvariable=postal_code).pack(padx=6,pady=12, side="left")
        
        Label(self.label_frame_3, text = "Region:", bg="#FFFFFF", font=("Inter",11)).pack(padx=12,pady=12, side="left")
        region = tk.StringVar()
        region_e = Entry(self.label_frame_3, width=8, fg="black", border=0, font=("Inter", 11), bg="#D9D9D9", cursor="arrow",
              justify="center", textvariable=region).pack(padx=6,pady=12, side="left")
        
        self.label_frame_4 = LabelFrame(self.ventanasec, text="Producto", width=820, height=70, font=("Inter", 11), bg="#FFFFFF")
        self.label_frame_4.place(x=94, y=495)
        
        Label(self.label_frame_4, text = "Nombre del Producto:", bg="#FFFFFF", font=("Inter",11)).pack(padx=12,pady=12, side="left")
        product_name = tk.StringVar()
        product_name_e = Entry(self.label_frame_4, width=14, fg="black", border=0, font=("Inter", 11), bg="#D9D9D9", cursor="arrow",
              justify="center", textvariable=product_name).pack(padx=7,pady=12, side="left")
        
        Label(self.label_frame_4, text = "Categoría:", bg="#FFFFFF", font=("Inter",11)).pack(padx=12,pady=12, side="left")
        info_category = tk.StringVar()
      #   ttk.Combobox(
      #         self.label_frame_4,
      #         state = "readonly",
      #         values = ["Alimentos", "Limpieza e Higiene", "Snacks", "Gaseosas"],
      #         textvariable = info_category
      #   ).pack(padx=6,pady=12, side="left")
        info_category_e = Combobox(
            self.label_frame_4,
            state = "readonly",
            values = ["Alimentos", "Limpieza e Higiene", "Snacks", "Gaseosas"],
            textvariable = info_category,
            bootstyle="success"
        ).pack(padx=6,pady=12, side="left")
        
        Label(self.label_frame_4, text = "Sub-Categoría:", bg="#FFFFFF", font=("Inter",11)).pack(padx=12,pady=12, side="left")
        subcategory_product = tk.StringVar()
        subcategory_product_e = Entry(self.label_frame_4, width=15, fg="black", border=0, font=("Inter", 11), bg="#D9D9D9", cursor="arrow",
              justify="center", textvariable=subcategory_product).pack(padx=8,pady=12, side="left")
        
        Button(self.ventanasec, width=16, text="Limpiar Producto", bootstyle = "warning",
               cursor="hand2", command=partial(delete_partial_information, product_name, info_category, subcategory_product)).place(x=595, y=599)
        
        Button(self.ventanasec, width=11, text = "Limpiar", bootstyle = "info",
               cursor="hand2", command=partial(delete_all_information, delivery_date, mode_delivery, customer_name, segment_customer, country, city, states, postal_code, region, product_name, info_category, subcategory_product)).place(x=730, y=599)
        
        Button(self.ventanasec, width=11, text="Enviar", bootstyle = "success",
               cursor="hand2", command=partial(send_information_sales, order_date, delivery_date, mode_delivery, customer_name, segment_customer, country, city, states, postal_code, region, product_name, info_category, subcategory_product)).place(x=490, y=599)

        self.ventanasec.mainloop()
        