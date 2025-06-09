import matplotlib.pyplot as plt
import random
from searching import busqueda_lineal, busqueda_binaria
import os
import time
from sorting import bubble_sort, selection_sort, insertion_sort, quick_sort
from utils import generar_lista_desordenada, timer

SORT_DELAY = 0  # Tiempo de espera entre pasos de ordenamiento en segundos
SEARCH_DELAY = 0  # Tiempo de espera entre pasos de busqueda en segundos
AMOUNT = 5000  # Cantidad de elementos en el arreglo desordenado
DECIMALS = 5  # Decimales para mostrar los tiempos de ejecución
# Mostrar o no los pasos de ordenamiento, búsqueda y el arreglo desordenado
SHOW_STEPS = True

SHOW_SORTING = True  # Mostrar o no los pasos de ordenamiento


os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola
print("=== Algoritmos de Ordenamiento y Búsqueda ===\n")

print(f"Generado un arreglo desordenado de {AMOUNT} elementos:")

arreglo_desordenado = generar_lista_desordenada(AMOUNT)

if SHOW_STEPS:
    print("Arreglo desordenado:", arreglo_desordenado)

if SHOW_SORTING:
    print("\n=== Ordenamiento ===")

    input("\n> Bubble Sorting")
    resultado_bubble, tiempo_bubble = timer(
        bubble_sort, arreglo_desordenado, SORT_DELAY, SHOW_STEPS)
    print(f"Tiempo de ejecución: {tiempo_bubble:.{DECIMALS}f} segundos")

input("\n> Insertion Sorting")
resultado_insertion, tiempo_insertion = timer(
    insertion_sort, arreglo_desordenado, SORT_DELAY, SHOW_STEPS)
print(f"Tiempo de ejecución: {tiempo_insertion:.{DECIMALS}f} segundos")

input("\n> Selection Sorting")
resultado_selection, tiempo_selection = timer(
    selection_sort, arreglo_desordenado, SORT_DELAY, SHOW_STEPS)
print(f"Tiempo de ejecución: {tiempo_selection:.{DECIMALS}f} segundos")

input("\n> Quick Sorting")
resultado_quick, tiempo_quick = timer(
    quick_sort, arreglo_desordenado, SORT_DELAY, SHOW_STEPS)
print(f"Tiempo de ejecución: {tiempo_quick:.{DECIMALS}f} segundos")

comparaciones_bubble = resultado_bubble[1]
comparaciones_insertion = resultado_insertion[1]
comparaciones_selection = resultado_selection[1]
comparaciones_quick = resultado_quick[1]

print("\nComparaciones realizadas:")
print(f"Bubble Sort: {comparaciones_bubble}")
print(f"Insertion Sort: {comparaciones_insertion}")
print(f"Selection Sort: {comparaciones_selection}")
print(f"Quick Sort: {comparaciones_quick}")

print("\nTiempos de ejecución:")
print(f"Bubble Sort: {tiempo_bubble:.{DECIMALS}f} segundos")
print(f"Insertion Sort: {tiempo_insertion:.{DECIMALS}f} segundos")
print(f"Selection Sort: {tiempo_selection:.{DECIMALS}f} segundos")
print(f"Quick Sort: {tiempo_quick:.{DECIMALS}f} segundos")

print("\n=== Búsqueda ===")

random_number = random.choice(range(1, AMOUNT + 1))
print(f"\nBuscando el número {random_number} en el arreglo desordenado:")

input("\n> Linear Search")
resultado_lineal, tiempo_lineal = timer(
    busqueda_lineal, arreglo_desordenado, random_number, SEARCH_DELAY, SHOW_STEPS)

print(
    f"\nÍndice encontrado: {resultado_lineal[0]}, Comparaciones: {resultado_lineal[1]}")
print(f"Tiempo de ejecución: {tiempo_lineal:.{DECIMALS}f} segundos")

input("\n> Binary Search")
resultado_binario, tiempo_binario = timer(busqueda_binaria, sorted(
    arreglo_desordenado), random_number, SEARCH_DELAY, SHOW_STEPS)
print(
    f"\nÍndice encontrado: {resultado_binario[0]}, Comparaciones: {resultado_binario[1]}")
print(f"Tiempo de ejecución: {tiempo_binario:.{DECIMALS}f} segundos")

print("\n=== Resumen ===")

print("\nTiempos de ejecución:")

if SHOW_SORTING:
    input("\n> Algoritmos de Ordenamiento\n")

    print(f"Bubble Sort: {tiempo_bubble:.{DECIMALS}f} segundos")
    print(f"Insertion Sort: {tiempo_insertion:.{DECIMALS}f} segundos")
    print(f"Selection Sort: {tiempo_selection:.{DECIMALS}f} segundos")
    print(f"Quick Sort: {tiempo_quick:.{DECIMALS}f} segundos")

input("\n> Algoritmos de búsqueda:")

print("\n- Linear Search -")
print(f"Tiempo: {tiempo_lineal:.{DECIMALS}f} segundos")
print(f"Comparaciones: {resultado_lineal[1]}")

print("\n- Binary Search -")
print(f"Tiempo: {tiempo_binario:.{DECIMALS}f} segundos")
print(f"Comparaciones: {resultado_binario[1]}")


# === Graficos ===

# === Graficos de Ordenamiento ===
ordenamiento_nombres = ["Bubble Sort",
                        "Insertion Sort", "Selection Sort", "Quick Sort"]
ordenamiento_tiempos = [tiempo_bubble,
                        tiempo_insertion, tiempo_selection, tiempo_quick]
comparaciones_ordenamiento = [
    comparaciones_bubble, comparaciones_insertion, comparaciones_selection, comparaciones_quick]

plt.figure(figsize=(10, 5))
plt.bar(ordenamiento_nombres, ordenamiento_tiempos, color="skyblue")
plt.title("Tiempos de Algoritmos de Ordenamiento")
plt.ylabel("Tiempo (segundos)")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
plt.bar(ordenamiento_nombres, comparaciones_ordenamiento, color="lightcoral")
plt.title("Comparaciones en Algoritmos de Ordenamiento")
plt.ylabel("Cantidad de Comparaciones")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

# === Graficos de Búsqueda ===

busqueda_nombres = ["Búsqueda Lineal", "Búsqueda Binaria"]
busqueda_tiempos = [tiempo_lineal, tiempo_binario]

plt.figure(figsize=(10, 5))
plt.bar(busqueda_nombres, busqueda_tiempos, color="salmon")
plt.title("Tiempos de Algoritmos de Búsqueda")
plt.ylabel("Tiempo (segundos)")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

# Comparaciones

comparaciones_lineal = resultado_lineal[1]
comparaciones_binario = resultado_binario[1]
comparaciones = [comparaciones_lineal, comparaciones_binario]

plt.figure(figsize=(10, 5))
plt.bar(busqueda_nombres, comparaciones, color="lightgreen")
plt.title("Comparaciones en Algoritmos de Búsqueda")
plt.ylabel("Cantidad de Comparaciones")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
