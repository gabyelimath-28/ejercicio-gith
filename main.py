# "Escribir una función que tome una lista de nombres y devuelva un diccionario 
# donde la clave sea la inicial y el valor una lista con los nombres correspondientes."

def agrupar_por_inicial(lista_nombres):
    diccionario_iniciales = {}

    for nombre in lista_nombres:
        # Obtenemos la primera letra en mayúscula
        inicial = nombre[0].upper()

        # Si la inicial no existe en el diccionario, creamos una lista vacía para esa clave
        if inicial not in diccionario_iniciales:
            diccionario_iniciales[inicial] = []

        # Agregamos el nombre a la lista correspondiente
        diccionario_iniciales[inicial].append(nombre)

    return diccionario_iniciales


# --- Ejemplo ---
nombres = [
    "Gabriela",
    "Gonzalo",
    "Ana",
    "Carlos",
    "Alberto",
    "Cristina",
    "Beatriz",
]
resultado = agrupar_por_inicial(nombres)

print(resultado)