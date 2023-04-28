from tkinter import *

# Bandera De Francia
ventana_principal = Tk()

# ventana
ventana_principal.title("Bandera de Francia")
ventana_principal.geometry("600x600")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="black")

# frame azul
Frame_azul= Frame(ventana_principal)
Frame_azul.config(bg="blue", width=200, height=600)
Frame_azul.place(x=0, y=0)

# frame blanco
Frame_blanco = Frame(ventana_principal)
Frame_blanco.config(bg="white", width=200, height=600)
Frame_blanco.place(x=200, y=0)

# frame rojo
Frame_rojo = Frame(ventana_principal)
Frame_rojo.config(bg="red", width=200, height=600)
Frame_rojo. place(x=400, y=0)

# run
ventana_principal.mainloop()