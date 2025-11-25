from customtkinter import *
from pywinstyles import *
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
        mostrar_ruta.configure(text=ruta_archivo)

def analizar_texto():
    if not ruta_archivo:
        mostrar_ruta.configure(text="Por favor, seleccione un archivo primero.")
        return
    
    texto = cargar_texto(ruta_archivo)
    palabras = limpiar_y_dividir(texto)
    total_palabras = len(palabras)

    
    conteo = contar_palabras(palabras)
    top10 = top_palabras(conteo, 10)

    resultado = "\n".join([f"{palabra}: {cantidad}" for palabra, cantidad in top10])
    frame_resultado.configure(state="normal")
    frame_resultado.delete("1.0", END)
    frame_resultado.insert(END, resultado)
    frame_resultado.configure(state="disabled")
    total_label.configure(text=f"Total: {total_palabras}")

# Ventana principal
ventana = CTk()
ventana.title("Analizador de Texto")
ventana.geometry("600x500")
ventana.minsize(600, 500)

# Título
titulo = CTkLabel(
    ventana, 
    text="Analizador de Texto", 
    font=("Segoe UI", 22))
titulo.place(relx=0.5, rely=0.1, anchor=CENTER)

# Resultado
frame_resultado = CTkTextbox(
    ventana, 
    font=("Segoe UI", 16),
    state=DISABLED, 
    width=500, 
    height=200, 
    border_width=2, 
    border_color="#D88313", 
    corner_radius=10)
frame_resultado.place(relx=0.5, rely=0.4, anchor=CENTER)

# Botón de seleccionar archivo
boton_archivo = CTkButton(
    ventana, 
    command=seleccionar_archivo, 
    fg_color="transparent", 
    hover_color= "#D88313", 
    border_color="#D88313", 
    border_width=2,
    text="Seleccionar Archivo", 
    corner_radius=32, 
    font=("Segoe UI", 18), 
    width=15, 
    height=35)
boton_archivo.place(relx=0.085, rely=0.7, anchor=W)

# Botón de analizar texto
boton_analizar = CTkButton(
    ventana, 
    command=analizar_texto, 
    fg_color="transparent", 
      hover_color= "#D88313", 
    border_color="#D88313", 
    border_width=2,
    text="Analizar Archivo", 
    corner_radius=32, 
    font=("Segoe UI", 18), 
    width=35, 
    height=35)
boton_analizar.place(relx=0.085, rely=0.8, anchor=W)

# Ruta de archivo
mostrar_ruta = CTkLabel(
    ventana, 
    text="", 
    font=("Segoe UI", 18))
mostrar_ruta.place(relx=0.5, rely=0.9, anchor=CENTER)

# Total de palabras
total_label = CTkLabel(
    ventana,
    text="",
    font=("Segoe UI", 18)
    )
total_label.place(relx=0.9, rely=0.65, anchor=E)

ventana.mainloop()
