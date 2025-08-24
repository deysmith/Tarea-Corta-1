# ------------------------------------------------------------------------------------------------------
# Tarea Corta #1: Implementación y Análisis de Algoritmos de Búsqueda
# Autores : Alice Arias, Hyldia Thomas , Deywenie Smith 
# Fecha: 2025-8-25
# Curso : Análisis de Datos
# Parte 1: Implementación y Análisis de Algoritmos de Búsqueda
# --------------------------------------------------------------------------------------------------------
import random
import time
import sys 
from Parte1_ordenamiento import generateMatrix, countingSort, memory_usage 

# ---------------------------------------------------------------------------------------------------------------
# Nombre: busqueda_lineal
# Entradas: 
#   matriz - matriz donde se realizará la búsqueda
#   numero - número que se desea buscar
# Restricciones: 
# La matriz debe contener números comparables
# Cómo funciona: Recorre fila por fila y columna por columna hasta encontrar el número
# Qué nos da de resultado: Retorna la posición fila, columna si lo encuentra, o -1 si no se encuentra
# ---------------------------------------------------------------------------------------------------------------
def busqueda_lineal(matriz, numero):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                return (i, j) 
    return -1 

# ---------------------------------------------------------------------------------------------------------------
# Nombre: busqueda_binaria para la comparacion solo
# Entradas: 
#   lista - lista ordenada donde se realizará la búsqueda
#   numero - número que se desea buscar
# Restricciones:
#   La lista debe estar ordenada
# Cómo funciona: Divide la lista en mitades repetidamente para encontrar el número
# Qué nos da de resultado: Retorna el índice donde se encuentra el número, o -1 si no está
# ---------------------------------------------------------------------------------------------------------------
def busqueda_binaria(lista, numero):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == numero:
            return medio
        elif lista[medio] < numero:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# ---------------------------------------------------------------------------------------------------------------
# Nombre: busqueda_en_matriz
# Entradas:
#   matriz - matriz donde se realizará la búsqueda
#   numero - número que se desea buscar
# Restricciones:
#   Cada fila de la matriz debe estar ordenada
# Cómo funciona: Aplica búsqueda binaria en cada fila de la matriz
# Qué nos da de resultado: Retorna la posición (fila, columna) si lo encuentra, o -1 si no SE ENCUENTRA
# ---------------------------------------------------------------------------------------------------------------
def busqueda_en_matriz(matriz, numero):
    for i in range(len(matriz)):
        indice = busqueda_binaria(matriz[i], numero)
        if indice != -1:
            return (i, indice)
    return -1

# -------------------------------------------------------------------------------------
# Aquí estamos aplicando el punto 4:
# Se realizan pruebas con números aleatorios en matrices de tamaños 10, 100 y 500.
# Mostramos los resultados obtenidos en tiempo de ejecución y memoria utilizada.
# con matrices que son cuadradas
# --------------------------------------------------------------------------------------
tamaños = [10, 100, 500]

numero_lineal = random.randint(1, 1000)
numero_binaria = random.randint(1, 1000)

print("\n------------------------------------------- ALGORITMO DE BÚSQUEDA ------------------------------------------------------\n")
for tamano in tamaños:
    matriz = generateMatrix(tamano)
    print(f"\n-------------------- Tamaño de la matriz: {tamano}x{tamano} --------------------")
    if tamano == 10:
        print("Matriz generada:")
        for fila in matriz:
            print(fila)
    else:
        print("Matriz no se imprime por ser grande.\n")

    # Búsqueda Lineal 
    inicio = time.time()
    res_lineal = busqueda_lineal(matriz, numero_lineal)
    fin = time.time()
    tiempo_lineal = (fin - inicio) * 1000
    memoria_lineal = memory_usage(matriz)

    # ESTE ES PARA LA COMPARACION 
    
    # Búsqueda Binaria 
    inicio = time.time()
    matriz_ordenada = []
    for i in range(len(matriz)):
        matriz_ordenada.append(countingSort(matriz[i])) # se esta ordenando ya que la necesita ordenada
    tiempo_ordenamiento = (time.time() - inicio) * 1000  # Tiempo ordenando
    #---------------------
    inicio = time.time()
    res_binaria = busqueda_en_matriz(matriz_ordenada, numero_binaria)
    fin = time.time()
    tiempo_busqueda_binaria = (fin - inicio) * 1000
    memoria_binaria = memory_usage(matriz_ordenada)


    print("\n------------------------------------------------------ Comparación de Búsquedas ------------------------------------------------------")
    print(f"{'Algoritmo':<20}{'Número':<10}{'Fila':<6}{'Columna':<8}{'Tiempo(segundos)':<12}{'Memoria(bytes)':<15}")
    print("---------------------------------------------------------------------------------------------------------------------------------------")

    fila, columna = res_lineal if res_lineal != -1 else (-1, -1)
    print(f"{'Lineal':<20}{numero_lineal:<10}{fila:<6}{columna:<8}{tiempo_lineal:<12.6f}{memoria_lineal:<15}")

    fila, columna = res_binaria if res_binaria != -1 else (-1, -1)
    print(f"{'Binaria':<20}{numero_binaria:<10}{fila:<6}{columna:<8}{tiempo_busqueda_binaria:<12.6f}{memoria_binaria:<15} (Tiempo ordenando: {tiempo_ordenamiento:.6f}segundos)")
