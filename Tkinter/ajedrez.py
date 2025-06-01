import tkinter as tk

# Creacion ventana principal
root = tk.Tk()

# Titulo para la ventana
root.title("Tablero ajedrez")
root.geometry("+600+150")

for i in range(10):
    for j in range(10):
        if (i+j) % 2 == 0 :
            marco_1 = tk.Frame(root,
                            background="cyan2",
                            width=50,
                            height=50,
                            border=0)
            marco_1.grid(row=i,column=j)
        else:
            marco_1 = tk.Frame(root,
                            background="firebrick1",
                            width=50,
                            height=50,
                            border=0)
            marco_1.grid(row=i,column=j)
        


#Bucle principal de fichero
root.mainloop()