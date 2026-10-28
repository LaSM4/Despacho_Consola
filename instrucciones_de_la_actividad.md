# Actividad Práctica de Laboratorio: Simulador CLI de Pilas y Colas
  
**Entregable:** Un único script ejecutable (ej. `despacho.py`)  

---

## 1. Contexto del Problema

Una empresa de logística necesita un sistema de consola sencillo para monitorear dos procesos en su centro de distribución:

1. **El Almacén de Cajas (Pila / LIFO):** Las cajas se apilan verticalmente. Solo se puede colocar una caja sobre la cima o retirar la última caja colocada.
2. **La Bahía de Camiones (Cola / FIFO):** Los camiones de carga esperan en una fila india. Llegan por el final y son despachados en estricto orden de llegada.

El equipo debe programar una aplicación por consola que se ejecute en un bucle interactivo y permita controlar ambas estructuras sin cerrarse.

---

## 2. Requerimientos de la Interfaz de Terminal

El programa debe correr dentro de un ciclo infinito (`while`) y presentar el siguiente menú de opciones tras cada acción:

```text
==================================================
        SISTEMA DE DESPACHO Y ALMACÉN
==================================================
1. [PILA] Apilar caja (push)
2. [PILA] Retirar caja de la cima (pop)
3. [COLA] Llega camión a la fila (enqueue)
4. [COLA] Despachar primer camión (dequeue)
5. Ver estado del almacén y camiones
6. Salir del programa
--------------------------------------------------
Seleccione una opción (1-6): 
```

---

## 3. Especificación de Operaciones

### Opción 1: Apilar caja (`push`)
* Solicita al usuario el identificador o nombre de la caja (ej. `Caja-101`).
* Inserta el elemento en la cima de la pila.
* Muestra un mensaje de confirmación: `-> Caja [Caja-101] apilada con éxito.`

### Opción 2: Retirar caja (`pop`)
* Retira la caja ubicada en la cima de la pila y muestra cuál fue extraída.
* **Manejo de errores:** Si la pila está vacía, no debe lanzar un error ni detenerse el programa; debe mostrar un aviso claro: `[!] Error: El almacén está vacío (no hay cajas que retirar).`

### Opción 3: Llegada de camión (`enqueue`)
* Solicita la placa o identificador del vehículo (ej. `Camión-Alfa`).
* Agrega el vehículo al final de la cola de espera.
* Muestra un mensaje de confirmación: `-> Camión [Camión-Alfa] formado en la fila.`

### Opción 4: Despachar camión (`dequeue`)
* Atiende y retira al camión que esté al frente de la fila.
* **Manejo de errores:** Si la cola está vacía, debe notificar amigablemente: `[!] Error: No hay camiones esperando turno.`

### Opción 5: Ver estado actual
* Imprime la representación de ambas estructuras en ese momento para fines de monitoreo.
* Formato sugerido de salida:
  ```text
  --------------------------------------------------
  ESTADO ACTUAL:
  - Cajas apiladas (Cima -> Base): ['Caja-103', 'Caja-102', 'Caja-101']
  - Fila de camiones (Frente -> Fin): ['Camión-Alfa', 'Camión-Beta']
  --------------------------------------------------
  ```

### Opción 6: Salir
* Muestra un mensaje de despedida y finaliza la ejecución de forma limpia (`break` o salida ordenada).

---

## 4. Reglas Técnicas

1. **Principio LIFO / FIFO:** Se debe respetar estrictamente el orden. No se permite acceder, modificar ni borrar elementos que estén en posiciones intermedias.
2. **Robustez ante entradas inválidas:** Si el usuario ingresa una letra o una opción fuera del rango (ej. `9`), el programa debe notificar el error y volver a desplegar el menú sin colapsar.
3. **No romper por excepciones de índice:** Toda operación de extracción (`pop` / `dequeue`) debe verificar primero si la estructura contiene elementos.

---

## 5. Criterios de Evaluación en Vivo (Checklist de Aprobación)

Al concluir el tiempo, el docente validará el funcionamiento en la máquina del equipo con la siguiente secuencia:

| Prueba | Acción del docente | Comportamiento esperado | Estado |
| :--- | :--- | :--- | :---: |
| **Prueba LIFO (Pila)** | Ingresar `Caja 1`, luego `Caja 2`, y seleccionar opción 2. | Debe salir primero `Caja 2`. | `[ ]` |
| **Prueba FIFO (Cola)** | Ingresar `Camión A`, luego `Camión B`, y seleccionar opción 4. | Debe salir primero `Camión A`. | `[ ]` |
| **Validación de vaciado** | Seleccionar opción 2 y 4 con las estructuras vacías. | Mensaje de advertencia; no colapso de terminal. | `[ ]` |
| **Control de flujo** | Ingresar caracteres inválidos en el menú. | Vuelve al menú sin interrumpir la ejecución. | `[ ]` |