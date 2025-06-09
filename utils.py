import random
import time


def timer(func, *args):
    start = time.perf_counter()
    resultado = func(*args)
    end = time.perf_counter()
    return resultado, end - start


def generar_lista_desordenada(cantidad=10):
    """Devuelve una lista desordenada con los números desde 1 hasta cantidad(10 default), sin repeticiones."""
    return random.sample(range(1, cantidad+1), cantidad)
