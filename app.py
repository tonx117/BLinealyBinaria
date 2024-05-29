import time

# Generar una lista ordenada con 50000 elementos
vector = [3, 5, 8, 9, 10, 22, 45, 500, 900, 4253]
# La variable puntero será el inicio del vector, que es 0
puntero = 0

# vectorLen contiene la longitud del vector menos 1
vectorLen = len(vector) - 1

# La variable encontrado cambiará su valor, y así el algoritmo sabrá qué hacer
encontrado = False

# Le pedimos al usuario una entrada de un entero
numero = int(input("Ingresar el dato que desea buscar: "))

# Medición del tiempo de ejecución (inicia)
start_time = time.time()

# Creamos un bucle que no se detenga hasta que encontrado sea diferente de False
# y que puntero sea menor o igual que vectorLen
while not(encontrado) and puntero <= vectorLen:

    # Creamos la variable mitad
    mitad = (puntero + vectorLen) // 2

    # Si numero es igual que el índice mitad en vector
    if numero == vector[mitad]:
        # Encontrado será igual a True
        encontrado = True

    elif numero < vector[mitad]:
        # vectorLen será igual que mitad - 1
        vectorLen = mitad - 1
    # De lo contrario
    else:
        # Puntero será igual que mitad + 1
        puntero = mitad + 1

# Medición del tiempo de ejecución (termina)
end_time = time.time()

# Si encontrado es True
if encontrado:
    # Mostramos un mensaje con la posición del Dato en el vector
    print("El dato se encuentra en la posición ", str(mitad + 1))

    # Mostramos el vector ordenado (opcional, esto puede ser muy grande)
    # print(vector)

# De lo contrario
else:
    # Mostramos un mensaje
    print("El dato no se encontró")

print(f"Tiempo de ejecución: {end_time - start_time:.8f} segundos")
