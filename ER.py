import re
import tkinter as tk
from tkinter import messagebox

def validar_cadenas():
    expresion = entrada_expresion.get()
    cadenas = entrada_cadenas.get("1.0", tk.END).strip().splitlines()  # Obtiene cada línea como una cadena

    try:
        patron = re.compile(expresion)  # Compila la expresión regular
    except re.error as e:
        messagebox.showerror("Error", f"Expresión regular no válida: {e}")
        return

    resultados_texto = ""
    for cadena in cadenas:
        if patron.fullmatch(cadena):
            resultados_texto += f"Cadena '{cadena}': Aceptada\n"
        else:
            resultados_texto += f"Cadena '{cadena}': Rechazada\n"

    resultados.config(state=tk.NORMAL)
    resultados.delete("1.0", tk.END)
    resultados.insert(tk.END, resultados_texto)
    resultados.config(state=tk.DISABLED)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Validador de Expresiones Regulares")

# Entrada de Expresión Regular
tk.Label(ventana, text="Expresión Regular:").grid(row=0, column=0, padx=10, pady=10)
entrada_expresion = tk.Entry(ventana, width=50)
entrada_expresion.grid(row=0, column=1, padx=10, pady=10)

# Entrada de Cadenas
tk.Label(ventana, text="Cadenas (una por línea):").grid(row=1, column=0, padx=10, pady=10)
entrada_cadenas = tk.Text(ventana, width=50, height=10)
entrada_cadenas.grid(row=1, column=1, padx=10, pady=10)

# Botón de Validación
boton_validar = tk.Button(ventana, text="Validar", command=validar_cadenas)
boton_validar.grid(row=2, column=1, padx=10, pady=10)

# Área de Resultado
tk.Label(ventana, text="Resultados:").grid(row=3, column=0, padx=10, pady=10)
resultados = tk.Text(ventana, width=50, height=10, state=tk.DISABLED)
resultados.grid(row=3, column=1, padx=10, pady=10)

# Iniciar la interfaz gráfica
ventana.mainloop()
