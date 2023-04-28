from tkinter import *

# Bandera De Noruega
ventana_principal = Tk()

# ventana
ventana_principal.title("Bandera de Noruega")
ventana_principal.geometry("800x800")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="white")

# frame rojo
Frame_rojo = Frame(ventana_principal)
Frame_rojo.config(bg="red", width=200, height=800)
Frame_rojo. place(x=0, y=0)

# frame blanco
Frame_blanco = Frame(ventana_principal)
Frame_blanco.config(bg="white", width=800, height=200)
Frame_blanco.place(x=0, y=270)


# frame rojo
Frame_rojo = Frame(ventana_principal)
Frame_rojo.config(bg="red", width=400, height=800)
Frame_rojo. place(x=400, y=0)

# frame blanco
Frame_blanco = Frame(ventana_principal)
Frame_blanco.config(bg="white", width=800, height=200)
Frame_blanco.place(x=0, y=270)

# frame azul
Frame_azul= Frame(ventana_principal)
Frame_azul.config(bg="blue4", width=800, height=100)
Frame_azul.place(x=0, y=320)

# frame azul
Frame_azul= Frame(ventana_principal)
Frame_azul.config(bg="blue4", width=100, height=800)
Frame_azul.place(x=250, y=0)

# run
ventana_principal.mainloop()