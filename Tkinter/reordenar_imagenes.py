import tkinter as tk
import os
from PIL import ImageTk, Image
import random  # Para generar nuevas posiciones aleatorias

# Crear ventana
root = tk.Tk()
root.title("Radiobutton")
root.geometry("+600+150")
root.configure(background="gray98")

# Directorios
carpeta_principal = os.path.dirname(__file__)
carpeta_imagenes = os.path.join(carpeta_principal, "imagenes")

# Marco
marco = tk.LabelFrame(root, text="Seleccione un usuario", padx=10, pady=10, border=0)
marco.pack(padx=10, pady=10)
marco.configure(background="gray98")

# Carga de imágenes
imagenes = [
    ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "img3.png")).resize((200, 200))),
    ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "img2.png")).resize((200, 200))),
    ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "img1.png")).resize((200, 200))),
    ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "img4.png")).resize((200, 200)))
]

# **Lista de etiquetas para manipular**
etiquetas = [tk.Label(marco, image=imagenes[i], background="gray98") for i in range(4)]

# **Ubicación inicial de las imágenes**
posiciones = [(0,0), (0,1), (2,0), (2,1)]
for i, etiqueta in enumerate(etiquetas):
    etiqueta.grid(row=posiciones[i][0], column=posiciones[i][1])

# **Función para reordenar posiciones**
def reordenar():
    random.shuffle(posiciones)  # Mezclar posiciones aleatoriamente
    for i, etiqueta in enumerate(etiquetas):
        etiqueta.grid(row=posiciones[i][0], column=posiciones[i][1])  # Aplicar nueva posición

# Botón para cambiar posiciones
tk.Button(root, text="Reordenar usuarios", font=30, command=reordenar).pack(pady=30)

# Bucle principal
root.mainloop()
