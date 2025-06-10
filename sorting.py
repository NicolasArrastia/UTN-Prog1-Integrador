import time


def print_step():
    print(".", end="", flush=True)


def bubble_sort(lista_original, delay_segundos=0, mostrar_pasos=False):
    lista = lista_original[:]
    comparaciones = 0
    n = len(lista)

    # Iterar n-1 veces sobre la lista
    for i in range(n - 1):
        # En cada pasada se "burbujea" el valor más grande al final
        for j in range(n - 1 - i):

            comparaciones += 1
            if mostrar_pasos:
                print_step()

            if lista[j] > lista[j + 1]:
                # Intercambiar si están en el orden incorrecto
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            time.sleep(delay_segundos)
    print()  # Nueva línea al finalizar la pasada
    return lista, comparaciones


def insertion_sort(lista_original, delay_segundos=0, mostrar_pasos=False):
    lista = lista_original[:]
    comparaciones = 0
    n = len(lista)

    # Comenzar desde el segundo elemento y recorrer toda la lista
    for i in range(1, n):
        llave = lista[i]
        j = i - 1

        # Mover elementos mayores a la llave hacia la derecha
        while j >= 0 and lista[j] > llave:
            comparaciones += 1
            lista[j + 1] = lista[j]
            j -= 1
            if mostrar_pasos:
                print_step()
            time.sleep(delay_segundos)
        lista[j + 1] = llave

    print()  # Nueva línea al finalizar la pasada
    return lista, comparaciones


def selection_sort(lista_original, delay_segundos=0, mostrar_pasos=False):
    lista = lista_original[:]
    comparaciones = 0
    n = len(lista)

    # Recorrer toda la lista buscando el menor elemento para cada posición
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            comparaciones += 1
            if mostrar_pasos:
                print_step()

            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
            time.sleep(delay_segundos)

        # Intercambiar el menor encontrado con el elemento en la posición i
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]

        time.sleep(delay_segundos)
    print()  # Nueva línea al finalizar la pasada
    return lista, comparaciones


def merge_sort(lista_original, delay_segundos=0, mostrar_pasos=False):
    lista = lista_original[:]
    comparaciones = 0

    def merge_sort_recursivo(sublista):
        nonlocal comparaciones
        if len(sublista) <= 1:
            return sublista

        medio = len(sublista) // 2
        izquierda = merge_sort_recursivo(sublista[:medio])
        derecha = merge_sort_recursivo(sublista[medio:])

        return mergear(izquierda, derecha)

    def mergear(izquierda, derecha):
        nonlocal comparaciones
        resultado = []
        i = j = 0

        while i < len(izquierda) and j < len(derecha):
            comparaciones += 1
            if mostrar_pasos:
                print_step()

            if izquierda[i] <= derecha[j]:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1

            time.sleep(delay_segundos)

        resultado.extend(izquierda[i:])
        resultado.extend(derecha[j:])
        return resultado

    lista = merge_sort_recursivo(lista)
    print()
    return lista, comparaciones


def quick_sort(lista_original, delay_segundos=0, mostrar_pasos=False):
    lista = lista_original[:]
    comparaciones = 0

    def quick_sort_recursivo(sublista, inicio, fin):
        nonlocal comparaciones
        if inicio < fin:
            comparaciones += 1
            if mostrar_pasos:
                print_step()

            # Elegir el último elemento como pivote
            pivote = sublista[fin]
            i = inicio - 1

            for j in range(inicio, fin):

                # Mover elementos menores o iguales al pivote a la izquierda
                if sublista[j] <= pivote:
                    i += 1
                    sublista[i], sublista[j] = sublista[j], sublista[i]

                comparaciones += 1
                if mostrar_pasos:
                    print_step()

                time.sleep(delay_segundos)

            # Colocar pivote en su posición correcta
            sublista[i + 1], sublista[fin] = sublista[fin], sublista[i + 1]
            time.sleep(delay_segundos)

            # Recursión en sublistas izquierda y derecha
            quick_sort_recursivo(sublista, inicio, i)
            quick_sort_recursivo(sublista, i + 2, fin)

    quick_sort_recursivo(lista, 0, len(lista) - 1)

    print()  # Nueva línea al finalizar la pasada
    return lista, comparaciones
