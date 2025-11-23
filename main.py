from funciones import cargar_texto, contar_palabras, limpiar_y_dividir, top_palabras

texto = cargar_texto('texto.txt')
palabras = limpiar_y_dividir(texto)
conteo = contar_palabras(palabras)
top10 = top_palabras(conteo, 10)


print("Top 10 palabras más comunes:")
for palabra, cantidad in top10:
    print(f"{palabra}: {cantidad}")