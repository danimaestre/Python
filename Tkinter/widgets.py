import tkinter as tk

# Creacion ventana principal
root = tk.Tk()

# Titulo para la ventana
root.title("Widgets practica")

# Dimensiones de ventana y posicionamiento
#root.geometry("400x300+500+150").

#Entrada de datos
entrada = tk.Entry(root, 
                   background="springgreen", 
                   border=3, 
                   foreground="red", 
                   width=30,
                   )
entrada.pack()


#Funcion para el boton
def enviar():
    tk.Label(root,
             text=f"Se ha pulsado el boton: {entrada.get()} ",
             background="skyblue",
             width=26
             ).pack()

#Boton enviar
boton = tk.Button(root, 
                  text="Enviar", 
                  command=enviar,
                  background="deepskyblue",
                  border=3,
                  foreground="gray98",
                  width=25,
                  ).pack()


#Bucle de ejecucion
root.mainloop()