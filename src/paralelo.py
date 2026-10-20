from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


"""Tres formas de ejecutar la misma lista de tareas.

Cada función recibe la función a ejecutar y la lista de argumentos, y devuelve
la lista de resultados en el mismo orden de los argumentos.
"""


def en_secuencia(funcion, argumentos):
    """Ejecuta las tareas una tras otra. Es el punto de comparación."""
    return [funcion(a) for a in argumentos]


def con_hilos(funcion, argumentos):
    num_hilos = 4
    with ThreadPoolExecutor(max_workers=num_hilos) as pool:

        return list(pool.map(funcion, argumentos)) 


def con_procesos(funcion, argumentos):

    num_procesos = 4
    with ProcessPoolExecutor(max_workers=num_procesos) as pool:

        return list(pool.map(funcion, argumentos)) 