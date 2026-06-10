import tkinter as tk

def crear_reportes(padre):
    frame = tk.Frame(padre, bg="#f2f2f2")

    tk.Label(
        frame,
        text="Productos",
        font=("Arial", 24, "bold"),
        bg="#f2f2f2",
        fg="#2c3e50"
    ).pack(pady=30)

    tk.Label(
        frame,
        text="Aquí se mostrarían las métricas e informes.",
        font=("Arial", 14),
        bg="#f2f2f2"
    ).pack()

    return frame