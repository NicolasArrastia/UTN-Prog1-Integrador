import time


def print_step(i, value):
    print(f"[{i}] -> {value}")


def busqueda_lineal(lista_original, objetivo, delay_segundos=0, mostrar_pasos=False):
    lista = lista_original[:]  # copia superficial
    comparaciones = 0

    for indice, valor in enumerate(lista):
        comparaciones += 1
        if mostrar_pasos:
            print_step(indice, valor)
        time.sleep(delay_segundos)
        if valor == objetivo:
            # devuelve el índice del objetivo y el número de comparaciones
            return indice, comparaciones

    return -1, comparaciones  # -1 indica que no se encontró el objetivo en la lista


def busqueda_binaria(lista_ordenada, objetivo, delay_segundos=0, mostrar_pasos=False):
    lista = lista_ordenada[:]  # copia superficial
    izquierda = 0
    derecha = len(lista) - 1
    comparaciones = 0

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        comparaciones += 1
        if mostrar_pasos:
            print_step(medio, lista[medio])
        time.sleep(delay_segundos)

        if lista[medio] == objetivo:
            return medio, comparaciones
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1, comparaciones
