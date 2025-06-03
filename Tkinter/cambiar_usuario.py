"""
Modulo que crea radiobuttons con imagenes
"""

import tkinter as tk
import os
from PIL import ImageTk, Image

# Creacion ventana principal
root = tk.Tk()
root.title("Radiobutton")
root.geometry("+600+150")
root.configure(background="gray98")

opcion = tk.StringVar()
opcion.set("Error")

# Creacion Directorios
carpeta_principal = os.path.dirname(__file__)
carpeta_imagenes = os.path.join(carpeta_principal, "imagenes")

# Creacion marco
marco = tk.LabelFrame(root,
                      text="Seleccione un usuario",
                      padx=10,
                      pady=10,
                      border=0)
marco.pack(padx=10, pady=10)
marco.configure(background="gray98")

# **Carga de imágenes**
usuario1 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "img3.png")).resize((200, 200)))
usuario2 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "img2.png")).resize((200, 200)))
usuario3 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "img1.png")).resize((200, 200)))
usuario4 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "img4.png")).resize((200, 200)))

# **Mantener la referencia de la etiqueta en row=0, column=0**
etiqueta_usuario = tk.Label(marco, image=usuario1, background="gray98")
etiqueta_usuario.grid(row=0, column=0)

# Otras etiquetas
tk.Label(marco, image=usuario2, background="gray98").grid(row=0, column=1)
tk.Label(marco, image=usuario3, background="gray98").grid(row=2, column=0)
tk.Label(marco, image=usuario4, background="gray98").grid(row=2, column=1)

# **Función para cambiar usuario**
def cambiar_usuario():
    global usuario5  # Mantener la imagen en memoria
    usuario5 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "img1.png")).resize((200, 200)))

    etiqueta_usuario.config(image=usuario5)  # **Cambia la imagen de la etiqueta existente en row=0, column=0**

# Botón para cambiar usuario
tk.Button(root, text="Cambiar usuario", font=30, command=cambiar_usuario).pack(pady=30)

# Bucle principal
root.mainloop()
