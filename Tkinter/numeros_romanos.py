import tkinter as tk

### FUNCIONES ###

def calcular():
    try:
        num = int(entry1.get()) 
        if 0 < num < 4000:
                M = ["", "M", "MM", "MMM"]
                C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
                D = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
                U = ["", "I","II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
                
                label_salida.config(text=f"{M[num//1000]}{C[(num%1000)//100]}{D[(num%100)//10]}{U[num%10]}")
                
                #print(f"{M[num//1000]}{C[(num%1000)//100]}{D[(num%100)//10]}{U[num%10]}")
        else:
            label_salida.config(text="El numero ingresado debe\n estar en un rango entre 1 y 3999")
        
            
    #except ValueError:
            #label_salida.config(text='Tiene que ser un entero')
            
    except Exception as e:
            label_salida.config(text=f"Valor no valido: \n {e}")
            

### CREACION VENTANA ###

ventana = tk.Tk()
ventana.title ("Conversion Numeros decimales a Romanos")
ventana.geometry ("400x500+600+150")
ventana.config(bg= "light blue")

### CREACION LABEL ###

label1 = tk.Label(ventana, text="Introduce un numero",font=("Arial", 14),bg="light gray" ).pack(pady=30)

### CREACION ENTRY ###

entry1= tk.Entry(ventana, width=10, bg="light gray", font=("Arial",12), justify="center")

entry1.pack(pady=10)

### CREACION LABEL SALIDA ###

label2 = tk.Label(ventana, text="Numero romano",font=("Arial", 14),bg="light gray" ).pack(pady=20)

label_salida = tk.Label(ventana, text="XXLDC",font=("Arial", 14),bg="light gray" )
label_salida.pack(pady=20)

### CREACION BOTON ###

boton_calcular = tk.Button(ventana, text="CALCULAR", command=calcular).pack(pady=20)

ventana.mainloop()