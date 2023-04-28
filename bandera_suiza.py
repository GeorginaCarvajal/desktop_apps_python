from tkinter import *

# Bandera De España
ventana_principal = Tk()

# ventana
ventana_principal.title("Bandera de España")
ventana_principal.geometry("500x500")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="red")

# frame blanco
Frame_blanco1 = Frame(ventana_principal)
Frame_blanco1.config(bg="white", width=100, height=300)
Frame_blanco1.place(x=200, y=100)


# frame blanco
Frame_blanco1 = Frame(ventana_principal)
Frame_blanco1.config(bg="white", width=300, height=100)
Frame_blanco1.place(x=100, y=200)


# run
ventana_principal.mainloop()