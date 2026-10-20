# Informe

Nombre y código: Samuel Agudelo Sosa - 202459419

## Parte 1: tabla de tiempos

| Tarea | Secuencia | Hilos | Procesos |
|---|---:|---:|---:|
| Contar primos | 700.4 ms | 648.3 ms | 226.3 ms |
| Consultas lentas | 4001.1 ms | 1004.2 ms | 1012.9 ms |

**Qué forma ganó en cada tarea y qué papel juega el bloqueo global del intérprete:**

*   **En la tarea de cálculo (Contar primos):** Ganó abrumadoramente la forma con **Procesos**. Los hilos obtuvieron un tiempo muy similar al secuencial porque son víctimas del **GIL (Global Interpreter Lock)** de CPython. El GIL es un mecanismo de seguridad que impide que múltiples hilos nativos ejecuten *bytecode* de Python simultáneamente. Aunque haya varios hilos activos, para tareas puramente de CPU (matemáticas), Python los obliga a turnarse, anulando los beneficios del paralelismo en arquitecturas multinúcleo. Los procesos evaden este problema porque cada proceso tiene su propio intérprete y memoria, logrando paralelismo real.
*   **En la tarea de espera (Consultas lentas):** Ganaron los **Hilos** (estando a la par con los procesos). En tareas limitadas por Entrada/Salida (I/O) como consultas a redes, bases de datos o dormir (`sleep`), el intérprete de Python es inteligente y **libera el GIL** mientras el hilo está inactivo esperando una respuesta. Esto permite que otros hilos se ejecuten durante ese tiempo muerto, logrando una concurrencia excelente. Aunque los procesos logran el mismo tiempo, los hilos son superiores aquí porque consumen muchos menos recursos del sistema operativo y su tiempo de arranque es casi nulo en comparación con instanciar un proceso completo.

## Parte 2: la actualización perdida

Porcentaje de abonos perdidos en las cinco corridas sin cerrojo:

Por qué se pierden, con los tres pasos de un abono en la explicación, y por
qué el cerrojo lo evita:

## Parte 3: memoria compartida

Por qué `llenar_lista` devuelve la lista sin tocar y `llenar_compartido` no:

## Parte 4: la cola

| Trabajadores | Tiempo |
|---:|---:|
| secuencia |  |
| 1 |  |
| 2 |  |
| 4 |  |

Por qué de dos a cuatro trabajadores casi no se gana, y qué tarea marca el
tiempo total:
