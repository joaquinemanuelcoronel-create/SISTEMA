import tkinter as tk
from tkinter import ttk

def crear_usuarios(padre):

    frame = tk.Frame(padre)

    tk.Label(
        frame,
        text="Gestión de Usuarios",
        font=("Arial", 20)
    ).pack(pady=10)

    notebook = ttk.Notebook(frame)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)

    # Pestaña Alta
    pestana_alta = tk.Frame(notebook)
    notebook.add(pestana_alta, text="Alta")

    tk.Label(pestana_alta, text="Nombre").pack(pady=5)
    tk.Entry(pestana_alta).pack()

    # Pestaña Modificar
    pestana_modificar = tk.Frame(notebook)
    notebook.add(pestana_modificar, text="Modificar")

    tk.Label(pestana_modificar, text="Modificar usuario").pack(pady=20)

    # Pestaña Consultar
    tab_consultar = tk.Frame(notebook)
    notebook.add(tab_consultar, text="Consultar")

   
    return frame