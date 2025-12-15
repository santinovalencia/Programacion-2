import tkinter as tk
from tkinter import messagebox


def cifrar_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            resultado += chr((ord(caracter) - base + desplazamiento) % 26 + base)
        else:
            resultado += caracter
    return resultado

def descifrar_cesar(texto, desplazamiento):
    return cifrar_cesar(texto, -desplazamiento)

def ejecutar(opcion):
    texto = entrada_texto.get()
    try:
        desplazamiento = int(entrada_desplazamiento.get())
    except ValueError:
        messagebox.showerror("Error", "El desplazamiento debe ser un número entero.")
        return

    if opcion == "cifrar":
        resultado = cifrar_cesar(texto, desplazamiento)
    else:
        resultado = descifrar_cesar(texto, desplazamiento)

    salida_texto.delete(0, tk.END)
    salida_texto.insert(0, resultado)

bg = "#E8F0FE"           
color_principal = "#4A90E2"  
color_secundario = "#D9EAFD" 
color_texto = "#0A2540"      
fuente = ("Segoe UI", 10)

ventana = tk.Tk()
ventana.title("Cifrado César")
ventana.geometry("420x380")
ventana.configure(bg=bg)

titulo = tk.Label(
    ventana, text="Cifrado César", 
    font=("Segoe UI", 16, "bold"),
    fg=color_texto, bg=bg
)
titulo.pack(pady=10)

tk.Label(ventana, text="Texto que quiera cifrar o desifrar:", font=fuente, bg=bg, fg=color_texto).pack()
entrada_texto = tk.Entry(ventana, width=45, font=fuente, bg=color_secundario, relief="flat", justify="center")
entrada_texto.pack(pady=5, ipady=4)


tk.Label(ventana, text="Desplazamiento de letras:", font=fuente, bg=bg, fg=color_texto).pack()
entrada_desplazamiento = tk.Entry(ventana, width=10, font=fuente, bg=color_secundario, relief="flat", justify="center")
entrada_desplazamiento.pack(pady=5, ipady=3)


btn_cifrar = tk.Button(
    ventana, text="Cifrar", 
    font=fuente, bg=color_principal, fg="white", 
    activebackground="#357ABD", activeforeground="white",
    relief="flat", width=20, command=lambda: ejecutar("cifrar")
)
btn_cifrar.pack(pady=7)

btn_descifrar = tk.Button(
    ventana, text="Descifrar", 
    font=fuente, bg=color_principal, fg="white",
    activebackground="#357ABD", activeforeground="white",
    relief="flat", width=20, command=lambda: ejecutar("descifrar")
)
btn_descifrar.pack(pady=7)

tk.Label(ventana, text="lo que dice:", font=fuente, bg=bg, fg=color_texto).pack()
salida_texto = tk.Entry(ventana, width=45, font=fuente, bg=color_secundario, relief="flat", justify="center")
salida_texto.pack(pady=5, ipady=4)

ventana.mainloop()
