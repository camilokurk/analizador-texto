def cargar_texto(ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        print("Error: El archivo no se encontró.")
        return "El archivo no se encontró."

def limpiar_y_dividir(texto):
    texto = texto.lower()
    caracteres_malos = ",.;:!?\"'()[]{}<>-_\n\t"
    for c in caracteres_malos:
        texto = texto.replace(c, " ")
    palabras = texto.split()
    return palabras

def contar_palabras(lista):
    conteo = {}
    for palabra in lista:
        if palabra in stop_words:
            continue
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo

stop_words = {
    "de", "la", "que", "el", "en", "y", "a", "los", "del", "se", "las", "por",
    "un", "para", "con", "no", "una", "su", "al", "lo", "como", "más", "pero",
    "sus", "le", "ya", "o", "este", "sí", "porque", "esta", "entre", "cuando",
    "muy", "sin", "sobre", "también", "me", "hasta", "hay", "donde", "quien",
    "desde", "todo", "nos", "durante", "todos", "uno", "les", "ni", "contra",
    "otros", "ese", "eso", "ante", "ellos", "e"
}

def top_palabras(diccionario, n=10):
    lista_ordenada = sorted(diccionario.items(), key=lambda item: item[1], reverse=True)
    return lista_ordenada[:n]