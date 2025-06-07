import tkinter as tk

class GridButtonsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Botones en Cuadrícula")
        self.root.geometry("+700+200")

        # Crear un Label para mostrar el mensaje
        self.label = tk.Label(root, text="Pulsa un botón", font=("Arial", 14), bg="white")
        self.label.grid(row=3, column=0, columnspan=3, pady=10)

        self.crearBotones()

    def mostrarMensaje(self, numero_boton):
        self.label.config(text=f"***Has pulsado el botón {numero_boton}***")

    def crearBotones(self):
        for i in range(3):
            for j in range(3):
                numero_boton = i * 3 + j + 1
                btn = tk.Button(self.root, text=f"Botón {numero_boton}", background="#aa99aa", fg="white", border=5, width=10, height=3, 
                                command=lambda num=numero_boton: self.mostrarMensaje(num))
                btn.grid(row=i, column=j, padx=5, pady=5)

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = GridButtonsApp(root)
    root.mainloop()
