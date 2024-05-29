import time

# Función del Algoritmo: se recorren uno a uno los elementos de la lista 
# y se los compara con el valor x buscado.
def busqueda_lineal(lista, x):
    i = 0 # i tiene la posición actual en la lista, comienza en 0

    # El ciclo recorre todos los elementos de la lista
    for z in lista:
        # Si z es igual a x, devuelve el valor de i
        if z == x:
            return i
        # Incrementa el índice después de cada iteración
        i = i + 1
    
    # Si salió del ciclo sin haber encontrado el valor, devuelve -1
    return -1

# Generar una lista más grande para obtener un tiempo de ejecución medible
lista_ejemplo = list(range(1, 1000000))
valor_buscado = 80000

# Medición del tiempo de ejecución
start_time = time.time()
resultado = busqueda_lineal(lista_ejemplo, valor_buscado)
end_time = time.time()

# Imprimir resultados
print(f"El valor {valor_buscado} se encuentra en la posición: {resultado}")
print(f"Tiempo de ejecución: {end_time - start_time:.8f} segundos")
