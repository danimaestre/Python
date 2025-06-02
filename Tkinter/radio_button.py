import tkinter as tk

# Creacion ventana principal
root = tk.Tk()

# Titulo para la ventana
root.title("Radiobutton")

opcion = tk.IntVar()
opcion.set(2)

# Funcion para el boton de envio
def actualiza_radio(valor):
    tk.Label(root, text=valor).pack()

# Radiobutton
tk.Radiobutton(root,
               text="Rojo",
               variable=opcion,
               value=1).pack()

tk.Radiobutton(root,
               text="Verde",
               variable=opcion,
               value=2).pack()

tk.Radiobutton(root,
               text="Azul",
               variable=opcion,
               value=3).pack()

tk.Radiobutton(root,
               text="Amarillo",
               variable=opcion,
               value=4).pack()

# Boton de envio
tk.Button(root, 
          text="Enviar",
          command=lambda: actualiza_radio(opcion.get())).pack()

# Bucle principal
root.mainloop()