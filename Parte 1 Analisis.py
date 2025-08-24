# ------------------------------------------------------------------------------------------------------
# Tarea Corta #1 Implementacion y Analisis del Algoritmos
# Autores : Alice Arias, Hyldia Thomas , Deywenie Smith 
# Fecha: 2025-8-25
# Curso : Analisis de Datos
# Parte 1: Implementacion y Analisis de Algoritmos de Ordenamiento
# --------------------------------------------------------------------------------------------------------

import random
import time
import sys # Para calcular memoria aproximada

# ---------------------------------------------------------------------------------------------------------------
# Nombre: generateMatrix
# Entradas: tamaño de la matriz cuadrada a generar
# Restricciones: tamaño debe ser un número entero positivo
# Cómo funciona: Crea una matriz cuadrada de tamaño n x n con números aleatorios entre 1 y 1000
# Qué nos da de resultado: Devuelve una matriz con números aleatorios
# ---------------------------------------------------------------------------------------------------------------
def generateMatrix(tamano):
    """matriz = []
    for i in range(tamano):
        matriz += [[]]
        for j in range(tamano):
            num_random = random.randint(1, 1000) #El rango se puede cambiar
            matriz[i].append(num_random)
    return matriz"""
    return [[random.randint(1, 1000) for _ in range(tamano)] for _ in range(tamano)] # Reduce el tiempo a la mitad



# -----------------------------------------------------------------------------------------------------------------------------------
# Nombre: quickSort(ordenamiento rápido)
# Entradas: 
#          lista - lista de números a ordenar
#          bajo  - índice inicial de la lista o sublista
#          alto   - índice final de la lista o sublista
# Restricciones:
#  - La lista debe contener valores que se puedan comparar entre sí, como números o letras.
#  - Los parámetros bajo y alto deben ser posiciones válidas dentro de la lista (ni negativas ni mayores que el tamaño de la lista).

# Cómo funciona: Ordena la lista de manera recursiva usando el método QuickSort. 
# Elige un número de la lista como referencia (pivote), mueve los números más pequeños a un lado y los más grandes al otro, y repite lo mismo con cada grupo hasta que todo quede ordenado.
# Qué nos da de resultado: Modifica la lista original ordenándola de forma ascendente 
# --------------------------------------------------------------------------------------------------------------------
def quickSort(lista, bajo, alto):

    while bajo < alto:
        indice_pivote = particion(lista, bajo, alto)

        if indice_pivote - bajo < alto - indice_pivote:
            quickSort(lista, bajo, indice_pivote-1)
            bajo = indice_pivote + 1

        else:
            quickSort(lista, indice_pivote + 1, alto)
            alto = indice_pivote - 1


# -----------------------------------------------------------------------------------------------------------------------------------
# Nombre: particion
# Cómo funciona: Toma el último elemento como referencia, coloca todos los elementos menores a la izquierda 
#                y los mayores a la derecha, devolviendo la posición final del pivote
# Qué nos da de resultado: Retorna el índice donde queda el pivote después de la partición
# -----------------------------------------------------------------------------------------------------------------------------------    
def particion(lista, bajo, alto):
    pivote = lista[alto]
    i = bajo - 1

    for j in range(bajo, alto):
        if lista[j] < pivote:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i+1], lista[alto] = lista[alto], lista[i+1]
    return i+1


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# Nombre: countingSort
# Entradas: lista - lista de números enteros a ordenar
# Restricciones: los números de la lista deben ser enteros no negativos
# Cómo funciona: 
#   1. Encuentra el valor máximo de la lista
#   2. Crea una lista de conteo de tamaño max+1
#   3. Cuenta cuántas veces aparece cada número
#   4. Reconstruye la lista ordenada usando la lista de conteo
# Qué nos da de resultado: Devuelve una nueva lista con los elementos ordenados de forma ascendente
# ----------------------------------------------------------------------------------------------------------------------------------------------------------
def countingSort(lista):

    valor_maximo = max(lista) #Utilizando max para encontrar el valor máximo (el rango siempre es entre 1 y 1000), pero por si las moscas
    conteo = [0] * (valor_maximo + 1)
    
    for num in lista:
        conteo[num] += 1
    
    lista_ordenada = []
    
    for i in range(len(conteo)):
        lista_ordenada.extend([i] * conteo[i])
        
    return lista_ordenada

# -------------------------------------------------------------------------------------------------------------v---------------
# Nombre: copiar_matriz
# Entradas: matriz 
# Cómo funciona: recorre cada fila de la matriz original, hace una copia de la fila y la agrega a una nueva matriz
# Resultado: devuelve una nueva matriz idéntica a la original, pero independiente
# ----------------------------------------------------------------------------------------------------------------------------
def copiar_matriz(matriz):
    copia = []
    for fila in matriz:
        copia.append(fila[:])  # copia independiente de la fila
    return copia


# ----------------------------------
# Función para calcular memoria aproximada de la matriz
# ----------------------------------
def memory_usage(matriz):
    return sys.getsizeof(matriz) + sum(sys.getsizeof(fila) for fila in matriz)

# ----------------------------------
# Tamaños de pruebas 
# ----------------------------------
tamaños = [10,100, 1000, 10000] # con 100000 no me sirve

for tamano in tamaños:
    print("\n-----------------------------------------------------------------------------------------")
    print(f"\nTamaño de la matriz: {tamano}x{tamano}")

    matriz_original = generateMatrix(tamano)
    

    # ---------------- CountingSort ----------------
    matriz = copiar_matriz(matriz_original)
    inicio = time.time()
    
    print("\n=== Matriz desordenada ===")
    if tamano == 10:
        for fila in matriz:
            print(fila)
    else:
        print("\n No se muestra la matriz por ser muy grande)")

    # Imprimir matriz ordenada
    for i in range(len(matriz)):
        matriz[i] = countingSort(matriz[i])
    fin = time.time()
    tiempo_counting = fin - inicio
    memoria_counting = memory_usage(matriz)
    
    if tamano == 10:
        print("\nMatriz ordenada con CountingSort:\n")
        for fila in matriz:
            print(fila)
    
    print(f"\nCountingSort -> Tiempo: {tiempo_counting:.6f}s | Memoria aprox: {memoria_counting} bytes")
    
    # ---------------- QuickSort ----------------
    #matriz = copiar_matriz(matriz_original)
    #inicio = time.time()
    #for i in range(len(matriz)):
        #quickSort(matriz[i], 0, len(matriz[i])-1)
    #fin = time.time()
    #tiempo_quick = fin - inicio
    #memoria_quick = memory_usage(matriz)
    
    #if tamano == 10:
        #print("\nMatriz ordenada con QuickSort:")
        #for fila in matriz:
            #print(fila)
    
    #print(f"\nQuickSort   -> Tiempo: {tiempo_quick:.6f}s | Memoria aprox: {memoria_quick} bytes")

