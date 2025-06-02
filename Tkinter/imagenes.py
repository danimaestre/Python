import tkinter as tk
import os
from PIL import ImageTk, ImageColor, Image

# ---Carga de directorios---
# Obtiene ruta principal de forma dinamica
carpeta_principal = os.path.dirname(__file__)
#print(carpeta_principal)

# Carpeta imagenes
carpeta_imagenes = os.path.join(carpeta_principal, "imagenes")
#print(carpeta_imagenes)
carpeta_paisajes = os.path.join(carpeta_imagenes, "paisajes")
#print(carpeta_paisajes)

# Creacion de la ventana principal
root = tk.Tk()

# Titulo de la ventana
root.title("Carga de imagenes")

# Icono de ventana
root.iconbitmap(os.path.join(carpeta_imagenes, "molecula.ico"))

# Carga de imagen
bosque = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_paisajes, "paisaje1.jpg")).resize((350,200)))

etiqueta = tk.Label(image=bosque)
etiqueta.pack()

# Bucle de ejecucion
root.mainloop()

