import tkinter as tk

# Creacion ventana principal
root = tk.Tk()

# Titulo para la ventana
root.title("Frames")

#Creacion de marcos
marco_1 = tk.LabelFrame(text="Entrada de datos",
                      padx=20,
                      pady=20)
marco_1.grid(row=0, column= 0, padx=15, pady=15)

marco_2 = tk.LabelFrame(text="Enviar",
                      padx=20,
                      pady=20)
marco_2.grid(row=1, column= 0,padx=15, pady=15)

marco_3 = tk.LabelFrame(text="Resultado",
                      padx=20,
                      pady=20)
marco_3.grid(row=0, column=1,padx=15, pady=15)

#Entrada de datos
entrada = tk.Entry(marco_1, 
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
    tk.Label(marco_3,
             text=f"Hola {nombre}",
             background="skyblue",
             width=27
             ).pack()
    entrada.delete(0, tk.END)
    entrada.insert(0, "Escriba su nombre...")
    
boton = tk.Button(marco_2,
                  text="Enviar",
                  command=enviar,
                  background="deepskyblue",
                  border=3,
                  width=26
                  ).pack()


#Bucle de ejecucion#
root.mainloop()
