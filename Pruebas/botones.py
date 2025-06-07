import tkinter as tk

class GridButtonsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Botones en Cuadrícula")
        self.root.geometry("+700+200")

        # Crear una cuadrícula de 3x3 de botones
        
        
        
    def crearBotones(self):
        for i in range(3):
            for j in range(3):
                num_boton = i*3 + j + 1
                btn = tk.Button(root, text=f"Botón {num_boton}", background="#aa99aa", fg="white", border=5, width=10, height=3)
                btn.grid(row=i, column=j, padx=5, pady=5)
                
    
# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = GridButtonsApp(root)
    app.crearBotones()
    root.mainloop()
