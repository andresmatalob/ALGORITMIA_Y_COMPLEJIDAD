import sys

def decoder(cifrado, clave, index=0):
    # Base case: si el texto cifrado es vacío, devolver una cadena vacía
    if not cifrado:
        return ""

    # Recursive case: descifrar el primer carácter y recursar en el resto del texto
    caracter = cifrado[0]
    if caracter.isalpha():
        desplazamiento = ord(clave[index]) - ord('a')
        codigo = ord(caracter) - desplazamiento % 26
        if caracter.isupper():
            if codigo < ord('A'):
                codigo += 26
            elif codigo > ord('Z'):
                codigo -= 26
        else:
            if codigo < ord('a'):
                codigo += 26
            elif codigo > ord('z'):
                codigo -= 26
        return chr(codigo) + decoder(cifrado[1:], clave, (index + 1) % len(clave))
    else:
        return caracter + decoder(cifrado[1:], clave, index)


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
        cifrado = decoder(texto, clave)

    # Escribir el texto cifrado en el archivo de salida
    with open(archivo_salida, 'w') as f:
        f.write(cifrado)

    print("Clave: " + clave)
    print(f"El texto se ha cifrado con éxito con la clave '{clave}' y se ha guardado en el archivo '{archivo_salida}'.")
