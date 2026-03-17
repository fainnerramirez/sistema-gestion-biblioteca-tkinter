from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Crear ventana principal
root = Tk()
root.title("Mi Aplicación")
root.geometry("600x400")
root.resizable(True, True)

# Frame principal con padding
main_frame = ttk.Frame(root, padding=15)
main_frame.grid(row=0, column=0, sticky=(N, S, E, W))

# Configurar para que se adapte al redimensionamiento
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)

# Título
title = ttk.Label(main_frame, text="Ejemplo Simple", 
                  font=("Arial", 16, "bold"))
title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Etiqueta y campo de entrada
ttk.Label(main_frame, text="Nombre:").grid(row=1, column=0, sticky=W, pady=10)
nombre_entry = ttk.Entry(main_frame, width=30)
nombre_entry.grid(row=1, column=1, sticky=(E, W), pady=10)

ttk.Label(main_frame, text="Mensaje:").grid(row=2, column=0, sticky=W, pady=10)
mensaje_entry = ttk.Entry(main_frame, width=30)
mensaje_entry.grid(row=2, column=1, sticky=(E, W), pady=10)

# Función para el botón
def saludar():
    nombre = nombre_entry.get()
    mensaje = mensaje_entry.get()
    
    if nombre:
        resultado = f"Hola {nombre}!"
        if mensaje:
            resultado += f"\n{mensaje}"
        messagebox.showinfo("Saludo", resultado)
    else:
        messagebox.showwarning("Error", "Por favor ingresa un nombre")

# Función para limpiar campos
def limpiar():
    nombre_entry.delete(0, END)
    mensaje_entry.delete(0, END)

# Frame para botones
button_frame = ttk.Frame(main_frame)
button_frame.grid(row=3, column=0, columnspan=2, sticky=(E, W), pady=20)

btn_saludo = ttk.Button(button_frame, text="Saludar", command=saludar)
btn_saludo.pack(side=LEFT, padx=5)

btn_limpiar = ttk.Button(button_frame, text="Limpiar", command=limpiar)
btn_limpiar.pack(side=LEFT, padx=5)

btn_salir = ttk.Button(button_frame, text="Salir", command=root.destroy)
btn_salir.pack(side=RIGHT, padx=5)

if __name__ == "__main__":
    root.mainloop()