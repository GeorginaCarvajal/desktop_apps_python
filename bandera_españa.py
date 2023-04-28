from tkinter import *

# Bandera De España
ventana_principal = Tk()

# ventana
ventana_principal.title("Bandera de España")
ventana_principal.geometry("400x400")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="red")

# frame rojo
Frame_rojo= Frame(ventana_principal)
Frame_rojo.config(bg="red", width=100, height=400)
Frame_rojo.place(x=0, y=0)

# frame amarillo
Frame_amarillo = Frame(ventana_principal)
Frame_amarillo.config(bg="yellow", width=200, height=400)
Frame_amarillo.place(x=0, y=100)

# frame rojo
Frame_rojo= Frame(ventana_principal)
Frame_rojo.config(bg="red", width=100, height=400)
Frame_rojo.place(x=0, y=300)

# run
ventana_principal.mainloop()