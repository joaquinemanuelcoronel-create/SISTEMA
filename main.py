import tkinter as tk

from frames.inicio import crear_inicio
from frames.usuarios import crear_usuarios
from frames.reportes import crear_reportes
from frames.configuracion import crear_configuracion
from frames.productos import crear_productos

ventana = tk.Tk()
ventana.title("Sistema")
ventana.geometry("800x500")

"""menu_lateral = tk.Frame(ventana, bg="#2c3e50", width=180)
menu_lateral.pack(side="right", fill="y")

contenedor = tk.Frame(ventana, bg="#f2f2f2")
contenedor.pack(side="left", fill="both", expand=True)
"""

menu_superior = tk.Frame(ventana, bg="#2c3e50", height=60)
menu_superior.pack(side="top", fill="x") 

contenedor = tk.Frame(ventana, bg="#f2f2f2")
contenedor.pack(side="bottom", fill="both", expand=True) 
#---------------

frames = {}

#Busca el frame correspondiente dentro del diccionario frames
def mostrar_frame(nombre):
    frames[nombre].tkraise()


# Crear menú
"""tk.Label(
    menu_lateral,
    text="Mi Sistema",
    bg="#2c3e50",
    fg="white",
    font=("Arial", 18, "bold")
).pack(pady=20)
"""

tk.Label(
    menu_superior,
    text="Mi Sistema",
    bg="#2c3e50",
    fg="white",
    font=("Arial", 18, "bold")
).pack(side="left", padx=20) 
#-------------------

botones = [
    ("Inicio", "inicio"),
    ("Usuarios", "usuarios"),
    ("Reportes", "reportes"),
    ("Configuración", "configuracion"),
    ("Productos", "productos")
]

#Botones
"""for texto, nombre in botones:
    tk.Button(
        menu_superior,
        text=texto,
        width=18,
        command=lambda n=nombre: mostrar_frame(n)
    ).pack(pady=10)
"""
for texto, nombre in botones:
    tk.Button(
        menu_superior,
        text=texto,
        command=lambda n=nombre: mostrar_frame(n)
    ).pack(side="left", padx=10, pady=10)
#------------------------

# Crear pantallas
frames["inicio"] = crear_inicio(contenedor)
frames["usuarios"] = crear_usuarios(contenedor)
frames["reportes"] = crear_reportes(contenedor)
frames["configuracion"] = crear_configuracion(contenedor)
frames["productos"] = crear_productos(contenedor)

for frame in frames.values():
    frame.place(x=0, y=0, relwidth=1, relheight=1)

mostrar_frame("inicio")

ventana.mainloop()

"""
1. Agregar el botón a la lista
botones = [
    ...
    ("Productos", "productos")
]

2. Crear el Frame
frames/
    productos.py

3. Importarlo y registrarlo
Arriba en main.py:
-> from frames.productos import crear_productos
Y donde creás los frames:
-> frames["productos"] = crear_productos(contenedor)
"""