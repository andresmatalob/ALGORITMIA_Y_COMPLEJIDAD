import sys
import time
import turtle

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


# Definir la función encoder


# Definir la función que dibuja el gráfico de la complejidad en función del tamaño de entrada de la función encoder

def dibujar_grafico():

    # Definir el tamaño de las entradas en la función encoder
    tamanos = [1,500,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,200000,300000,400000,500000,600000,700000,800000,900000,1000000,2000000,3000000,4000000,5000000,6000000,7000000,8000000,9000000,10000000]
    # Definir los tiempos de ejecución en función del tamaño de entrada
    tiempos = []

    for tamanio in tamanos:
        # Generar los datos de entrada aleatorios
        cifrado = 'a' * tamanio
        clave = 'a'

        # Calcular el tiempo de ejecución
        inicio = time.time()
        encoder(cifrado, clave)
        fin = time.time()

        # Añadir el tiempo de ejecución al array de tiempos
        tiempos.append(fin - inicio)

    # Dibujar el gráfico de la complejidad con los tiempos obtenidos
    turtle.title("Complejidad de la función encoder")
    turtle.setup(800, 600, 0, 0)
    turtle.penup()
    turtle.goto(-400, -300)
    turtle.pendown()
    turtle.pencolor("blue")
    turtle.pensize(3)
    turtle.setx(-400)
    turtle.sety(-300)
    turtle.setx(400)
    turtle.sety(-300)
    turtle.setx(400)
    turtle.sety(300)
    turtle.setx(-400)
    turtle.sety(300)
    turtle.setx(-400)
    turtle.sety(-300)

    turtle.penup()
    turtle.goto(-400, -300)
    turtle.pendown()
    turtle.setx(-400)
    turtle.sety(300)
    turtle.penup()
    turtle.goto(-400, -300)
    turtle.pendown()
    turtle.setx(400)
    turtle.sety(-300)
    turtle.penup()
    turtle.goto(-400, 0)
    turtle.pendown()
    turtle.setx(400)
    turtle.sety(0)
    turtle.penup()
    turtle.goto(0, -300)
    turtle.pendown()
    turtle.setx(0)
    turtle.sety(300)

    turtle.penup()
    turtle.goto(-400, -300)
    turtle.pendown()
    turtle.pencolor("red")
    turtle.pensize(2)
    #hazlo para que se muestre el grafico de la complejidad en notacion Big O con los tiempos obtenidos  y redondea la curva
    turtle.goto(-400, -300)
    turtle.goto(-400, -300)
    turtle.goto(-400, -300)
    turtle.goto(-400, -300)
    for i in range(len(tamanos)):
        turtle.goto(-400 + 800 * i / len(tamanos), -300 + 600 * tiempos[i] / max(tiempos))
    turtle.goto(400, -300 + 600 * tiempos[len(tamanos) - 1] / max(tiempos))
    turtle.penup()
    turtle.exitonclick()

if __name__ == '__main__':


    # Obtener argumentos de línea de comandos
    if len(sys.argv) != 4:
        print("Uso: python cifrado_cesar.py <clave> <archivo_entrada> <archivo_salida>")
        sys.exit(1)

    #dibujar_grafico()

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






