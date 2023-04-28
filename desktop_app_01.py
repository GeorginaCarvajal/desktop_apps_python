#------------------------
# Desktop app No.1
#------------------------

# se importa la libreria tkinder con todas sus funciones
from tkinter import *

#-----------------------
# Funciones de la app
#-----------------------

#-----------------------
#Ventana principal de la app
#-----------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Bandera de Colombia")

# tamaño de la ventana
ventana_principal.geometry("500x500")

# desahabilitar boton de maximizar
ventana_principal.resizable(False, False)

#color de fondo de la ventana
ventana_principal.config(bg="purple3")

# frame amarillo
Frame_amarillo = Frame(ventana_principal)
Frame_amarillo.config(bg="yellow", width=500, height=250)
Frame_amarillo.place(x=0, y=0)

# frame azul
Frame_azul= Frame(ventana_principal)
Frame_azul.config(bg="blue", width=500, height=125)
Frame_azul.place(x=0, y=250)

# frame rojo
Frame_rojo = Frame(ventana_principal)
Frame_rojo.config(bg="red", width=500, height=125)
Frame_rojo. place(x=0, y=375)

# se ejecuta el metodo mainloop() Tk() a travesde instancia venta_principal, este metodo despliega la 
# ventana en pantalla y queda a la espera de o que el usuario haga (click en un boton, escribir, etc). 
# Cada accion del usuario se conoce como un venteo. el metdo mainloop()es un bucle infinito.

# run
ventana_principal.mainloop()