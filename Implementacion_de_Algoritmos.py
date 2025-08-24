import random
import time

def generateMatrix(tamano):
    """
    Genera una matriz de la dimensión indicada

    Parámetros:
        tamano (int): Orden de la matriz.

    Retorna:
        list: Una lista de listas que contiene números enteros
    """
    """matriz = []
    for i in range(tamano):
        matriz += [[]]
        for j in range(tamano):
            num_random = random.randint(1, 1000) #El rango se puede cambiar
            matriz[i].append(num_random)
    return matriz"""
    return [[random.randint(1, 1000) for _ in range(tamano)] for _ in range(tamano)] #Redeuce el tiempo a la mitad

def quickSort(lista, bajo, alto):
    """
    Ordena de forma ascendente los elementos dentro de una lista.

    Parámetros:
        lista (list): Lista que se desea ordenar.

    Retorna:
        list: Retorna la lista con sus elementos ordenados.
    """
    while bajo < alto:
        indice_pivote = particion(lista, bajo, alto);
        if indice_pivote - bajo < alto - indice_pivote:
            quickSort(lista, bajo, indice_pivote-1)
            bajo = indice_pivote + 1
        else:
            quickSort(lista, indice_pivote + 1, alto)
            alto = indice_pivote - 1
            
def particion(lista, bajo, alto):
    pivote = lista[alto]
    i = bajo - 1
    for j in range(bajo, alto):
        if lista[j] < pivote:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i+1], lista[alto] = lista[alto], lista[i+1]
    return i+1

def mergeSort(lista):
    """
    Ordena de forma ascendente los elementos dentro de una lista.

    Parámetros:
        lista (list): Lista que se desea ordenar.

    Retorna:
        list: Retorna la lista con sus elementos ordenados.
    """
    if len(lista) <= 1:
        return lista
    mitad = len(lista)//2
    izquierda = mergeSort(lista[:mitad])
    derecha = mergeSort(lista[mitad:])
    return mergeAux(izquierda, derecha)

def mergeAux(izquierda, derecha):
    resultado = []
    i = 0
    j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
            
    resultado.extend(izquierda[i:]) #El extend añade los elementos que quedan
    resultado.extend(derecha[j:])
    return resultado

def countingSort(lista):
    """
    Ordena de forma ascendente los elementos dentro de una lista.

    Parámetros:
        lista (list): Lista que se desea ordenar.

    Retorna:
        list: Retorna la lista con sus elementos ordenados.
    """
    valor_maximo = max(lista) #Utilizando max para encontrar el valor máximo (el rango siempre es entre 1 y 1000), pero por si las moscas
    
    conteo = [0] * (valor_maximo + 1)
    
    for num in lista:
        conteo[num] += 1
        
    lista_ordenada = []
    
    for i in range(len(conteo)):
        lista_ordenada.extend([i] * conteo[i])
        
    return lista_ordenada




# Algoritmos de búsqueda
#1. Búsqueda lineal
def busqueda_lineal(matriz, numero):
    """
    Busca un número dentro de una matriz.
    
    paráramteros:
        matriz (lista): Matriz donde se realizará la búsqueda.
        numero (int): Número que se desea buscar.
    
    Retorna:
        int: Retorna la posoción de la matriz donde se encuenta el número. Si no lo encuentra retorna -1.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                return (i, j)
    return -1



#2. Búsqueda binaria
def busqueda_binaria(lista, numero):
    """
    Busca un número dentro de una lista ordenada.
    
    parárametros:
        lista (lista): Lista donde se realizará la búsqueda.
        numero (int): Número que se desea buscar.
        
    Retorna:
        int: Retorna la posoción de la lista donde se encuenta el número. Si
    """
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

def busqueda_en_matriz(matriz, numero):
    """
    Busca un número dentro de una matriz ordenada.
    
    parárametros:
        matriz (lista): Matriz donde se realizará la búsqueda.
        numero (int): Número que se desea buscar.
    
    Retorna:
        int: Retorna la posoción de la matriz donde se encuenta el número. Si no lo encuentra retorna -1.
    """
    for i in range(len(matriz)):
        indice = busqueda_binaria(matriz[i], numero)
        if indice != -1:
            return (i, indice)
    return -1
    

#3. Hashing
def Hashing(matriz, numero):
    """
    Busca un número dentro de una matriz.
    
    parárametros:
        matriz (lista): Matriz donde se realizará la búsqueda.
        numero (int): Número que se desea buscar.
        
    Retorna:
        int: Retorna la posoción de la matriz donde se encuenta el número. Si no lo encuentra retorna -1.
    """
    diccionario = {}
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            diccionario[matriz[i][j]] = (i, j)
    return diccionario.get(numero, -1)



#Parte de ejecución
matriz = generateMatrix(50)
print("\nMatriz Generada:")
for fila in matriz:
    print(fila)
"""
#Busqueda lineal
inicio = time.time()
resultado = busqueda_lineal(matriz, 933)
fin = time.time()
print("\nPosición numero (búsqueda lineal):", resultado, "\nTiempo:", fin - inicio)
"""

"""
#Busqueda binaria
inicio = time.time()
matriz_ordenada = []
for i in range(len(matriz)):
    matriz_ordenada.append(countingSort(matriz[i]))
resultado = busqueda_en_matriz(matriz_ordenada, 30)
fin = time.time()
print("\nPosición numero (búsqueda binaria):", resultado, "\nTiempo:", fin - inicio)
"""


#Hashing
inicio = time.time()
resultado = Hashing(matriz, 40)
fin = time.time()
print("\nPosición numero (Hashing):", resultado, "\nTiempo:", fin - inicio)


"""
#Ordenamiento
inicio = time.time()
for i in range(len(matriz)):
    matriz[i] = countingSort(matriz[i])
    #matriz[i] = mergeSort(matriz[i])
    #quickSort(matriz[i], 0, len(matriz[i]) - 1) 
#imperimir la matriz ordenada
print("\nMatriz Ordenada:")
for fila in matriz:
    print(fila)
fin = time.time()
print("Tiempo:", fin - inicio)
"""