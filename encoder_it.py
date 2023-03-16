import sys


def encoder(cifrado, clave):
    if not clave.isalpha():
        print("Error: La clave debe contener solo letras del alfabeto.")
        return None
    texto = ""
    index = 0
    for caracter in cifrado:
        if caracter.isalpha():
            desplazamiento = ord(clave[index]) - ord('a')
            codigo = ord(caracter) + desplazamiento % 26
            if caracter.isupper():
                if codigo > ord('Z'):
                    codigo -= 26
                elif codigo < ord('A'):
                    codigo += 26
            else:
                if codigo > ord('z'):
                    codigo -= 26
                elif codigo < ord('a'):
                    codigo += 26
            texto += chr(codigo)
            index = (index + 1) % len(clave)
        else:
            texto += caracter

    return texto


if __name__ == '__main__':
    # Obtener argumentos de línea de comandos
    if len(sys.argv) != 4:
        print("Uso: python cifrado_cesar.py <clave> <archivo_entrada> <archivo_salida>")
        sys.exit(1)

    clave = sys.argv[1]
    archivo_entrada = sys.argv[2]
    archivo_salida = sys.argv[3]

    # Leer el archivo de entrada
    with open(archivo_entrada, 'r') as f:
        texto = f.read()

    # Cifrar el texto
        cifrado = encoder(texto, clave)

    # Escribir el texto cifrado en el archivo de salida
    with open(archivo_salida, 'w') as f:
        f.write(cifrado)

    print("Clave: " + clave)
    print(f"El texto se ha cifrado con éxito con la clave '{clave}' y se ha guardado en el archivo '{archivo_salida}'.")
