import tkinter as tk

### FUNCIONES ###

def calcular():
    try:
   
        valores_romanos ={
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        } 
        
        numero_romano = entry_romano.get()
        numero_romano = numero_romano.upper()
        
        num_entero = 0
        valor_anterior = 0
        
        for caracter in numero_romano[::-1]:
            valor_actual = valores_romanos.get(caracter, 0)
            
            if valor_actual < valor_anterior:
                num_entero -= valor_actual
            else:
                num_entero += valor_actual
            valor_anterior = valor_actual
                
        label_salida.config(text=f"Resultado: {num_entero}")

    except Exception as e:
        print("Inrgrese in numero romano valido: {e}")

### CREACION VENTANA ###

ventana = tk.Tk()
ventana.title ("Conversion Numeros decimales a Romanos")
ventana.geometry ("500x500+600+150")
ventana.config(bg= "light blue")

### CREACION LABEL ###

label_titulo = tk.Label(ventana, text="CONVERTIDOR NUMEROS ROMANOS\nA DECIMALES", font=("arial", 18), relief=tk.SUNKEN, bg="light green").pack()

label_romano = tk.Label(ventana, text="Introduce un\n numero romano",font=("Arial", 14),bg="light gray", relief=tk.SUNKEN ).pack(pady=30)

### CREACION ENTRY ###

entry_romano= tk.Entry(ventana, width=10, bg="light gray", font=("Arial",18), justify="center")

entry_romano.pack(pady=10)

### CREACION LABEL SALIDA ###

label_numero = tk.Label(ventana, text="Numero decimal",font=("Arial", 14),bg="light gray" ).pack(pady=20)

label_salida = tk.Label(ventana, bg="light blue",font=("Arial", 14) )
label_salida.pack(pady=20)

### CREACION BOTON ###

boton_calcular = tk.Button(ventana, text="CALCULAR", command=calcular).pack(pady=20)

ventana.mainloop()