# Autor: Eliahu Maira
# Fecha: Viernes 06/06/2025 a las XX:XX
# Correo: eliahu.en.maira@icloud.com

# Lista de caracteres
lista1 = [
    " ", "a", "b", "c", "d", "e", "f", "g", "h", "i",
    "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r",
    "s", "t", "u", "v", "w", "x", "y", "z", "!", '"',
    "#", "$", "%", "&", "'", "(", ")", "*", "+", ",",
    "-", ".", "/", ":", ";", "<", "=", ">", "?", "@",
    "[", "\\", "]", "^", "_", "{", "|", "}", "~",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]

# Función para cifrar el mensaje
def cifrar_mensaje(lista1):
    mensaje = input("Introduce el mensaje a cifrar: ")
    cifrado = ""
    for letra in mensaje:
        if letra in lista1:
            index = lista1.index(letra)
            longitud = len(str(index))
            # Agregar el dígito indicador seguido del índice
            cifrado += str(longitud) + str(index)
        else:
            print(f"El carácter '{letra}' no está en la lista de caracteres permitidos.")
            return
    print("Mensaje cifrado:", cifrado)
    return cifrado

# Función para descifrar el mensaje
def descifrar_mensaje(lista1):
    mensaje_a_descifrar = input("Introduce el mensaje a descifrar: ")
    descifrado = ""
    conteo = 0
    while conteo < len(mensaje_a_descifrar):
        if not mensaje_a_descifrar[conteo].isdigit():
            print(f"Carácter inesperado en la posición {conteo}.")
            return
        longitud = int(mensaje_a_descifrar[conteo])
        conteo += 1
        indice_str = mensaje_a_descifrar[conteo:conteo + longitud]
        if not indice_str.isdigit():
            print(f"Índice inválido en la posición {conteo}.")
            return
        indice = int(indice_str)
        conteo += longitud
        if indice < len(lista1):
            descifrado += lista1[indice]
        else:
            print(f"Índice {indice} fuera de rango para la lista de caracteres.")
            return
    print("Mensaje descifrado:", descifrado)
    return descifrado

while True:
    nose = input("Si quieres cifrar un mensaje, escribe c, si quieres descifrar un mensaje escribe d, o escribe salir para finalizar: ")

    if nose == 'c':
        cifrar_mensaje(lista1)
    elif nose == 'd':
        descifrar_mensaje(lista1)
    elif nose == 'salir':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elige 'c', 'd' o 'salir'.")