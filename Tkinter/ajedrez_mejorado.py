import tkinter as tk

# Creación ventana principal
root = tk.Tk()

# Título para la ventana
root.title("Tablero ajedrez")
root.geometry("+600+150")

for i in range(10):
    for j in range(10):
        color = "cyan2" if (i+j) % 2 == 0 else "firebrick1"
        marco = tk.Frame(root, background=color, width=50, height=50, border=0)
        marco.grid(row=i, column=j)

# Bucle principal
root.mainloop()
