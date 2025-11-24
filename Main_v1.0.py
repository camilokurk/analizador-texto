import tkinter as tk
from tkinter import filedialog
from funciones import cargar_texto, contar_palabras, limpiar_y_dividir, top_palabras, stop_words

ruta_archivo = "" # Variable global para almacenar la ruta del archivo seleccionado

# FUNCIONES

def seleccionar_archivo():
    global ruta_archivo
    ruta = filedialog.askopenfilename(
        title="Seleccionar archivo de texto",
        filetypes=[("Text files", "*.txt")]
    )
    if ruta:
        ruta_archivo = ruta
        label_archivo.config(text=ruta_archivo)

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
    text_resultado.config(state="normal")
    text_resultado.delete("1.0", tk.END)
    text_resultado.insert(tk.END, resultado)
    text_resultado.config(state="disabled")

# Ventana principal
ventana = tk.Tk()
ventana.title("Analizador de Texto")
ventana.geometry("600x500")
ventana.configure(bg="#1e1e1e")

#Título
titulo = tk.Label(ventana, text="Analizador de Texto", font=("Helvetica", 16), bg="#1e1e1e", fg="#ffffff")
titulo.pack(pady=15)

# ----------------------
# Área de resultados con scroll
# ----------------------
frame_resultado = tk.Frame(ventana, bg="#1e1e1e")
frame_resultado.pack(pady=10)

scrollbar = tk.Scrollbar(frame_resultado)
scrollbar.pack(side="right", fill="y")

text_resultado = tk.Text(frame_resultado, width=60, height=10, yscrollcommand=scrollbar.set, bg="#2e2e2e", fg="white", font=("Segoe UI", 12))
text_resultado.pack()
text_resultado.config(state="disabled")
scrollbar.config(command=text_resultado.yview)

# BOTONES
frame_botones = tk.Frame(ventana, bg="#1e1e1e")
frame_botones.pack(pady=15)

# Botón para seleccionar archivo
boton_archivo = tk.Button(frame_botones, text="Seleccionar Archivo", command=seleccionar_archivo,
                          bg="#0078D7", fg="#ffffff", font=("Segoe UI", 12), width=15)
boton_archivo.pack(side="left", padx=10)

# Botón para seleccionar archivo
boton_analizar = tk.Button(frame_botones, text="Analizar", command=analizar_texto,
                          bg="#0078D7", fg="#ffffff", font=("Segoe UI", 12), width=15)
boton_analizar.pack(side="left", padx=10)

# Label para mostrar el archivo seleccionado
label_archivo = tk.Label(ventana, text="Ningún archivo seleccionado")
label_archivo.pack()

# Stop words adicionales
frame_stop = tk.Frame(ventana, bg="#1e1e1e")
frame_stop.pack(pady=10)

tk.Label(frame_stop, text="Stop words adicionales (separadas por comas):", font=("Segoe UI", 12), bg="#1e1e1e", fg="white").pack(side="left", padx=5)
entry_stop = tk.Entry(frame_stop, width=50, bg="#2e2e2e", fg="white", font=("Segoe UI", 12))
entry_stop.pack(side="left", padx=5)

ventana.mainloop()