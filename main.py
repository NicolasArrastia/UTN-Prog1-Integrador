import matplotlib.pyplot as plt
import random
from searching import busqueda_lineal, busqueda_binaria
import os
from sorting import bubble_sort, merge_sort, selection_sort, insertion_sort, quick_sort
from utils import generar_lista_desordenada, timer

SORT_DELAY = 0  # Tiempo de espera entre pasos de ordenamiento en segundos
SEARCH_DELAY = 0  # Tiempo de espera entre pasos de busqueda en segundos
AMOUNT = 2000  # Cantidad de elementos en el arreglo desordenado
DECIMALS = 5  # Decimales para mostrar los tiempos de ejecución
# Mostrar o no los pasos de ordenamiento, búsqueda y el arreglo desordenado
SHOW_STEPS = False


os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola
print("=== Algoritmos de Ordenamiento y Búsqueda ===\n")

arreglo_desordenado = generar_lista_desordenada(AMOUNT)

print(f"Generado un arreglo desordenado de {AMOUNT} elementos:")

print("\n=== Ordenamiento ===")

# Bubble Sort
input("\n> Bubble Sort")
resultado_bubble, tiempo_bubble = timer(
    bubble_sort, arreglo_desordenado, SORT_DELAY, SHOW_STEPS)
print(f"Tiempo de ejecución: {tiempo_bubble:.{DECIMALS}f} segundos")

# Insertion Sort
input("\n> Insertion Sort")
resultado_insertion, tiempo_insertion = timer(
    insertion_sort, arreglo_desordenado, SORT_DELAY, SHOW_STEPS)
print(f"Tiempo de ejecución: {tiempo_insertion:.{DECIMALS}f} segundos")

# Selection Sort
input("\n> Selection Sort")
resultado_selection, tiempo_selection = timer(
    selection_sort, arreglo_desordenado, SORT_DELAY, SHOW_STEPS)
print(f"Tiempo de ejecución: {tiempo_selection:.{DECIMALS}f} segundos")

# Merge Sort
input("\n> Merge Sort")
resultado_merge, tiempo_merge = timer(
    merge_sort, arreglo_desordenado, SORT_DELAY, SHOW_STEPS)
print(f"Tiempo de ejecución: {tiempo_merge:.{DECIMALS}f} segundos")

# Quick Sort
input("\n> Quick Sort")
resultado_quick, tiempo_quick = timer(
    quick_sort, arreglo_desordenado, SORT_DELAY, SHOW_STEPS)
print(f"Tiempo de ejecución: {tiempo_quick:.{DECIMALS}f} segundos")

comparaciones_bubble = resultado_bubble[1]
comparaciones_insertion = resultado_insertion[1]
comparaciones_selection = resultado_selection[1]
comparaciones_merge = resultado_merge[1]
comparaciones_quick = resultado_quick[1]
input(f"\n> Mostrar Resultados")

print("\nComparaciones realizadas:")
print(f"Bubble Sort:\t\t{comparaciones_bubble}")
print(f"Insertion Sort:\t\t{comparaciones_insertion}")
print(f"Selection Sort:\t\t{comparaciones_selection}")
print(f"Merge Sort:\t\t{comparaciones_merge}")
print(f"Quick Sort:\t\t{comparaciones_quick}")

print("\nTiempos de ejecución:")
print(f"Bubble Sort:\t\t{tiempo_bubble:.{DECIMALS}f} segundos")
print(f"Insertion Sort:\t\t{tiempo_insertion:.{DECIMALS}f} segundos")
print(f"Selection Sort:\t\t{tiempo_selection:.{DECIMALS}f} segundos")
print(f"Merge Sort:\t\t{tiempo_merge:.{DECIMALS}f} segundos")
print(f"Quick Sort:\t\t{tiempo_quick:.{DECIMALS}f} segundos")

print("\n=== Búsqueda ===")

random_number = random.choice(range(1, AMOUNT + 1))
print(f"\nBuscando el número {random_number} en el arreglo ordenado:")

# Linear Search
input("\n> Linear Search")
resultado_lineal, tiempo_lineal = timer(
    busqueda_lineal, resultado_bubble[0], random_number, SEARCH_DELAY, SHOW_STEPS)
print(
    f"\nÍndice encontrado: {resultado_lineal[0]}, Comparaciones: {resultado_lineal[1]}")
print(f"Tiempo de ejecución: {tiempo_lineal:.{DECIMALS}f} segundos")

# Binary Search
input("\n> Binary Search")
resultado_binario, tiempo_binario = timer(busqueda_binaria, sorted(
    resultado_bubble[0]), random_number, SEARCH_DELAY, SHOW_STEPS)
print(
    f"\nÍndice encontrado: {resultado_binario[0]}, Comparaciones: {resultado_binario[1]}")
print(f"Tiempo de ejecución: {tiempo_binario:.{DECIMALS}f} segundos")

input("\n> Mostrar gráficos de resultados")

# === Graficos ===

# === Graficos de Ordenamiento ===
ordenamiento_nombres = ["Bubble Sort",
                        "Insertion Sort", "Selection Sort", "Merge Sort", "Quick Sort"]
ordenamiento_tiempos = [tiempo_bubble,
                        tiempo_insertion, tiempo_selection, tiempo_merge, tiempo_quick]
comparaciones_ordenamiento = [
    comparaciones_bubble, comparaciones_insertion, comparaciones_selection, comparaciones_merge, comparaciones_quick]

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
