import sys

def encoder(cifrado, clave):
    #encripta un texto con el algoritmo de cesar
    #se le pasa por parametro la clave y el texto a cifrar
    #devuelve el texto cifrado
    # TIENE QUE SER ITERATIVO (NO RECURSIVO)
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
    print("Clave: " + clave)
    archivo_entrada = sys.argv[2]
    archivo_salida = sys.argv[3]
    #enviar el texto cifrado al archivo de salida
    with open(archivo_entrada, 'r') as f:
        texto = f.read()
        cifrado = encoder(texto, clave)
        with open(archivo_salida, 'w') as f:
            f.write(cifrado)



