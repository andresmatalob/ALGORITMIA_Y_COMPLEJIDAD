import sys
import matplotlib.pyplot as plt
import time

def encoder(cifrado, clave, index=0):
    # Base case: if the cipher text is empty, return an empty string
    if not cifrado:
        return ""

    # Recursive case: encrypt the first character and recurse on the rest of the text
    caracter = cifrado[0]
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
        return chr(codigo) + encoder(cifrado[1:], clave, (index + 1) % len(clave))
    else:
        return caracter + encoder(cifrado[1:], clave, index)

if __name__ == '__main__':
    # Obtener argumentos de línea de comandos
    if len(sys.argv) != 4:
        print("Uso: python cifrado_cesar.py <clave> <archivo_entrada> <archivo_salida>")
        sys.exit(1)

    clave = sys.argv[1]
    archivo_entrada = sys.argv[2]
    archivo_salida = sys.argv[3]

    # Medir el tiempo de ejecución del cifrado César
    tiempos = []
    longitudes = []
    with open(archivo_entrada, 'r') as f:
        texto = f.read()

        for longitud in range(100, len(texto), 100):
            cifrado = texto[:longitud]
            start_time = time.time()
            encoder(cifrado, clave)
            elapsed_time = time.time() - start_time
            tiempos.append(elapsed_time)
            longitudes.append(longitud)

    # Graficar los resultados
    plt.plot(longitudes, tiempos)
    plt.title('Tiempo de ejecución del cifrado César')
    plt.xlabel('Longitud del texto de entrada')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.show()

    # Escribir el texto cifrado en el archivo de salida
    with open(archivo_salida, 'w') as f:
        cifrado = encoder(texto, clave)
        f.write(cifrado)

    print("Clave: " + clave)
    print(f"El texto se ha cifrado con éxito con la clave '{clave}' y se ha guardado en el archivo '{archivo_salida}'.")
