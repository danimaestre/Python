import tkinter as tk
import os
from PIL import ImageTk, ImageColor, Image

# Funciones
def enviar():
    if opcion.get()== "Error":
        tk.Label(root,
                 text="¡No has seleccionado ninguna cuenta. ¡Por favor, intentelo de nuevo",
                 background="red2",
                 foreground="gray98").pack()
    else:
        tk.Label(root, text=f"hola {opcion.get()}. Accediendo a tu cuenta").pack()
        

# Creacion ventana principal
root = tk.Tk()

# Titulo para la ventana
root.title("Radiobutton")
root.geometry("+600+150")
root.configure(background="gray98")

opcion = tk.StringVar()
opcion.set("Error")

# Creacion imagenes
# Creacion de Directorios

carpeta_principal = os.path.dirname(__file__)
carpeta_imagenes = os.path.join(carpeta_principal, "imagenes")
print(carpeta_principal, carpeta_imagenes)

# Creacion marco
marco = tk.LabelFrame(root,
                    text="Seleccione un usuario",
                    padx=10,
                    pady=10,
                    border=0)
marco.pack(padx=10,pady=10)
marco.configure(background="gray98")



# Carga de imagenes

# Usuario 1
usuario1 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "img3.png")).resize((200,200)))

etiqueta = tk.Label(marco, image=usuario1, background="gray98")
etiqueta.grid(row=0, column=0)

# Usuario 2
usuario2 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "img2.png")).resize((200,200)))

etiqueta = tk.Label(marco,image=usuario2, background="gray98")
etiqueta.grid(row=0, column=1)

# Usuario 3
usuario3 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "img1.png")).resize((200,200)))

etiqueta = tk.Label(marco, image=usuario3, background="gray98")
etiqueta.grid(row=2, column=0)

# Usuario 4
usuario4 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "img4.png")).resize((200,200)))

etiqueta = tk.Label(marco, image=usuario4, background="gray98")
etiqueta.grid(row=2, column=1)


# Radiobutton
tk.Radiobutton(marco,
               text="Emma",
               variable=opcion,
               value="Emma",
               background="yellow").grid(row=1, column=0)

tk.Radiobutton(marco,
               text="Jacobo",
               variable=opcion,
               value="Jacobo",
               background="#9c5412",
               ).grid(row=1, column=1)

tk.Radiobutton(marco,
               text="Noha",
               variable=opcion,
               value="Noha",
               background="#3C4976").grid(row=3, column=0)

tk.Radiobutton(marco,
               text="Sophia",
               variable=opcion,
               value="Sophia",
               background="light blue").grid(row=3, column=1)

# Creacion boton
boton = tk.Button(root,
                  text="Entrar",
                  command=enviar)
boton.pack(pady=30)

# Bucle pincipal
root.mainloop()