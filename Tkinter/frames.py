import tkinter as tk

# Creacion ventana principal
root = tk.Tk()

# Titulo para la ventana
root.title("Frames")

#Creacion de marco
marco = tk.LabelFrame(text="Marco en la ventana principal",
                      padx=10,
                      pady=10)
marco.pack(padx=20, pady=20)

#Entrada de datos
entrada = tk.Entry(marco, 
                   background="springgreen", 
                   border=5, 
                   foreground="red", 
                   width=30,
                   )

entrada.pack()
entrada.insert(0, "Escriba su nombre...")
entrada.bind("<Button-1>", lambda e: entrada.delete(0,tk.END))

#Funcion para el boton
def enviar():
    nombre = entrada.get() #Obtiene y almacena el texto de la entrada
    tk.Label(marco,
             text=f"Hola {nombre}",
             background="skyblue",
             width=27
             ).pack()
    entrada.delete(0, tk.END)
    entrada.insert(0, "Escriba su nombre...")
    
boton = tk.Button(marco,
                  text="Enviar",
                  command=enviar,
                  background="deepskyblue",
                  border=3,
                  width=26
                  ).pack()


#Bucle de ejecucion
root.mainloop()

#