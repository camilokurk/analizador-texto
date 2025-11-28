from customtkinter import *
from pywinstyles import *
from funciones import cargar_texto, contar_palabras, limpiar_y_dividir, top_palabras, stop_words

import os

ruta_archivo = "" # Variable global para almacenar la ruta del archivo seleccionado
nombre_archivo = ""

# FUNCIONES

def seleccionar_archivo():
    global ruta_archivo, nombre_archivo
    ruta = filedialog.askopenfilename(
        title="Seleccionar archivo de texto",
        filetypes=[("Text files", "*.txt")]
    )
    if ruta:
        nombre_archivo = os.path.basename(ruta)
        mostrar_ruta.configure(text=f"Nombre: {nombre_archivo}")
        boton_archivo.configure(fg_color="#D88313")  # Cambiar color del botón al seleccionar archivo

def analizar_texto():
    if not nombre_archivo:
        mostrar_ruta.configure(text="Por favor, seleccione un archivo primero.")
        return
    
    texto = cargar_texto(nombre_archivo)
    palabras = limpiar_y_dividir(texto)
    total_palabras = len(palabras)

     
    conteo = contar_palabras(palabras)
    top10 = top_palabras(conteo, 10)

    resultado = "\n".join([f"{palabra}: {cantidad}" for palabra, cantidad in top10])
    frame_resultado.configure(state="normal")
    frame_resultado.delete("1.0", END)
    frame_resultado.insert(END, resultado)
    frame_resultado.configure(state="disabled")
    total_label.configure(text=f"Palabras totales: {total_palabras}")
    boton_analizar.configure(fg_color="#D88313")  # Cambiar color del botón al analizar texto

def cambiar_colores():
    if boton_analizar.cget("border_color") == "#D88313":
        boton_analizar.configure(border_color="#D8138C", hover_color="#D8138C")
        boton_archivo.configure(border_color="#D8138C", hover_color="#D8138C")
        boton_colores.configure(border_color="#D8138C", hover_color="#D8138C")
        frame_resultado.configure(border_color="#D8138C")
    else:
        boton_analizar.configure(border_color="#D88313", hover_color="#D88313")
        boton_archivo.configure(border_color="#D88313", hover_color="#D88313")
        boton_colores.configure(border_color="#D88313", hover_color="#D88313")
        frame_resultado.configure(border_color="#D88313")

# Ventana principal
ventana = CTk()
ventana.title("Analizador de Texto")
ventana.geometry("600x500")
ventana.minsize(600, 500)
ventana.maxsize(600, 500)
#ventana.configure(fg_color="#082541")

ventana.grid_columnconfigure(0, weight=0)  
ventana.grid_columnconfigure(1, weight=1)  

ventana.grid_rowconfigure(1, weight=1)  
ventana.grid_rowconfigure(2, weight=1) 



# Panel principal (resultado)
panel_principal = CTkFrame(ventana, fg_color="transparent")
panel_principal.grid(row=1, column=1, sticky="nsew", padx=(10, 20), pady=20)

panel_principal.grid_columnconfigure(0, weight=1)

panel_principal.grid_rowconfigure(0, weight=0)
panel_principal.grid_rowconfigure(1, weight=1)



# Título
titulo = CTkLabel(
    panel_principal, 
    text="Analizador de Texto", 
    font=("Segoe UI", 22))
titulo.grid(row=0, column=0, pady=(0, 10))

# Resultado
frame_resultado = CTkTextbox(
    panel_principal, 
    font=("Segoe UI", 16),
    state=DISABLED, 
    width=336, 
    height=250, 
    border_width=2, 
    border_color="#D88313", 
    corner_radius=10)
frame_resultado.grid(row=1, column=0, pady=(0, 0))

# Ruta de archivo
mostrar_ruta_frame = CTkFrame(
    panel_principal, 
    fg_color="#1E1E1E", height=30)
mostrar_ruta_frame.grid(row=2, column=0, sticky="we", pady=(0,10))
mostrar_ruta_frame.grid_propagate(False)

mostrar_ruta = CTkLabel(
    mostrar_ruta_frame, 
    text="Nombre:", 
    font=("Segoe UI", 18),
    text_color="#D88313")
mostrar_ruta.grid(row=2, column=0, sticky="w", padx=10, pady=(0,10))

# Total de palabras
total_frame = CTkFrame(
    panel_principal, 
    fg_color="#1E1E1E", height=30)
total_frame.grid(row=3, column=0, sticky="we", pady=(0,10))
total_frame.grid_propagate(False)

total_label = CTkLabel(
    total_frame,
    text="Palabras totales:",
    font=("Segoe UI", 18),
    text_color="#D88313")
total_label.grid(row=3, column=0, sticky="w", padx=10, pady=(0,10))

# PANEL LATERAL PRINCIPAL
panel_lateral = CTkFrame(ventana, fg_color="transparent")
panel_lateral.grid(row=1, column=0, rowspan=2, sticky="nsew")

panel_lateral.grid_rowconfigure(0, weight=1)
panel_lateral.grid_rowconfigure(1, weight=1)
panel_lateral.grid_columnconfigure(0, weight=1)

# Panel lateral arriba (botones)
panel_lateral_arriba = CTkFrame(panel_lateral, fg_color="#1E1E1E")
panel_lateral_arriba.grid(row=0, column=0, sticky="nsew", padx=(20, 10), pady=(20, 10))

panel_lateral_arriba.grid_propagate(False)

panel_lateral_arriba.grid_columnconfigure(0, weight=1)

panel_lateral_arriba.grid_rowconfigure(0, weight=0)
panel_lateral_arriba.grid_rowconfigure(1, weight=0)

# Instrucciónes
instrucciones_frame = CTkFrame(
    panel_lateral_arriba, 
    fg_color="#D88313",
    corner_radius=10,
    height=60)
instrucciones_frame.grid(row=0, column=0, pady=(10,0), padx=10, sticky="ew")

instrucciones = CTkLabel(
    instrucciones_frame, 
    text="Seleccione un archivo de texto (.txt)", 
    font=("Segoe UI", 16, "italic"),
    wraplength=165,
    corner_radius=10)
instrucciones.grid(row=0, column=0, pady=10)

# Botón de seleccionar archivo
boton_archivo = CTkButton(
    panel_lateral_arriba, 
    command=seleccionar_archivo, 
    fg_color="transparent", 
    hover_color= "#D88313", 
    border_color="#D88313", 
    border_width=2,
    text="Seleccionar Archivo", 
    corner_radius=10, 
    font=("Segoe UI", 18),  
    height=45)
boton_archivo.grid(row=1, column=0, pady=20, padx=10, sticky="ew")

# Botón de analizar texto
boton_analizar = CTkButton(
    panel_lateral_arriba, 
    command=analizar_texto, 
    fg_color="transparent", 
    hover_color= "#D88313", 
    border_color="#D88313", 
    border_width=2,
    text="Analizar", 
    corner_radius=10, 
    font=("Segoe UI", 18), 
    height=45)
boton_analizar.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="ew")



# Panel lateral bajo
panel_lateral_abajo = CTkFrame(panel_lateral, fg_color="#1E1E1E")
panel_lateral_abajo.grid(row=1, column=0, sticky="nsew", padx=(20, 10), pady=(10, 20))

panel_lateral_abajo.grid_propagate(False)

panel_lateral_abajo.grid_columnconfigure(0, weight=1)

panel_lateral_abajo.grid_rowconfigure(0, weight=0)
panel_lateral_abajo.grid_rowconfigure(1, weight=0)



# Boton Colores
boton_colores = CTkButton(
    panel_lateral_abajo,
    command=cambiar_colores,
    text="Cambiar Colores",
    fg_color="transparent",
    hover_color="#D88313",
    font=("Segoe UI", 18),
    border_color="#D88313",
    border_width=2,
    corner_radius=10)
boton_colores.grid(row=0, column=0, pady=10, padx=10, sticky="ew")


ventana.mainloop()