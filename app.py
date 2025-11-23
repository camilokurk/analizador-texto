import tkinter as tk
from tkinter import filedialog
from funciones import cargar_texto, contar_palabras, limpiar_y_dividir, top_palabras, stop_words

ruta_archivo = "" # Variable global para almacenar la ruta del archivo seleccionado

# Ventana principal
ventana = tk.Tk()
ventana.title("Analizador de Texto")
ventana.geometry("500x400")

def seleccionar_archivo():
    global ruta_archivo
    ruta = filedialog.askopenfilename(
        title="Seleccionar archivo de texto",
        filetypes=[("Text files", "*.txt")]
    )
    if ruta:
        ruta_archivo = ruta
        label_archivo.config(text=ruta_archivo)

# Botón para seleccionar archivo
boton_archivo = tk.Button(ventana, text="Seleccionar Archivo", command=seleccionar_archivo)
boton_archivo.pack(pady=20)

# Label para mostrar el archivo seleccionado
label_archivo = tk.Label(ventana, text="Ningún archivo seleccionado")
label_archivo.pack()

#Entry para stop words adicionales
tk.Label(ventana, text="Stop words adicionales (separadas por comas):").pack(pady=5)
entry_stop = tk.Entry(ventana, width=50)
entry_stop.pack()

# Label para mostrar resultados
label_resultado = tk.Label(ventana, text="", justify="left")
label_resultado.pack(pady=10)

def analizar_texto():
    if not ruta_archivo:
        label_archivo.config(text="Por favor, seleccione un archivo primero.")
        return
    
    texto = cargar_texto(ruta_archivo)
    palabras = limpiar_y_dividir(texto)

    # Stop words adicionales
    entrada = entry_stop.get()
    if entrada:
        nuevas_stop = [p.strip() for p in entrada.split(",")]
        stop_words.extend(nuevas_stop)

    conteo = contar_palabras(palabras)
    top10 = top_palabras(conteo, 10)

    resultado = "\n".join([f"{palabra}: {cantidad}" for palabra, cantidad in top10])
    label_resultado.config(text=resultado)

# Botón para analizar texto
boton_analizar = tk.Button(ventana, text="Analizar Texto", command=analizar_texto)
boton_analizar.pack(pady=10)


ventana.mainloop()