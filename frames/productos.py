import tkinter as tk

def crear_productos(padre):
    frame = tk.Frame(padre, bg="#f2f2f2")

    tk.Label(
        frame,
        text="Productos",
        font=("Arial", 24, "bold"),
        bg="#f2f2f2",
        fg="#2c3e50"
    ).pack(pady=30)

    return frame