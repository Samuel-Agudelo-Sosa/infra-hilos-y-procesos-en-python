import multiprocessing


def _trabajador(funcion, cola_tareas, cola_resultados):
    while True:
        item = cola_tareas.get()
        if item is None:
            break
        indice, argumento = item
        resultado = funcion(argumento)
        cola_resultados.put((indice, resultado))


def con_cola(funcion, argumentos, procesos):
    cola_tareas = multiprocessing.Queue()
    cola_resultados = multiprocessing.Queue()
    trabajadores = []
    
    # Corregido: usamos '_' o 'p_id' en el bucle para no sobrescribir la lista
    for _ in range(procesos):
        p = multiprocessing.Process(
            target=_trabajador, 
            args=(funcion, cola_tareas, cola_resultados)
        )
        p.start()
        trabajadores.append(p)

    for indice, arg in enumerate(argumentos):
        cola_tareas.put((indice, arg))

    for _ in range(procesos):
        cola_tareas.put(None)

    # Corregido: se lee de cola_resultados
    resultados_desordenados = [cola_resultados.get() for _ in range(len(argumentos))]

    for p in trabajadores:
        p.join()

    resultados_desordenados.sort(key=lambda x: x[0])

    return [resultado for _, resultado in resultados_desordenados]