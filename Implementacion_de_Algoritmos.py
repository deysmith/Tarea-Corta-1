import random

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

#Parte de ejecución
matriz = generateMatrix(13)
#print(f"antes: {matriz}")
for i in range(len(matriz)):
    matriz[i] = mergeSort(matriz[i])
    #quickSort(matriz[i], 0, len(matriz[i]) - 1) 
    
print("finish")
#print(f"despues: {matriz}")