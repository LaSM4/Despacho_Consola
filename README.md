# Sistema de Despacho y Almacén (Simulador CLI de Pilas y Colas)

Aplicación interactiva por consola en Python para gestionar y monitorear dos procesos clave en un centro de distribución logístico:

1. **Almacén de Cajas (Pila / LIFO):** Las cajas se apilan verticalmente y se retiran desde la cima (*Last In, First Out*).
2. **Bahía de Camiones (Cola / FIFO):** Los camiones se forman en una fila y se despachan en estricto orden de llegada (*First In, First Out*).

---

## Requisitos Previos

* **Python 3.8+** instalado en el sistema (no requiere librerías externas).

---

## Instalación y Ejecución

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/LaSM4/Despacho_Consola.git
   cd Despacho_Consola
   ```

2. **Ejecutar el programa:**
   ```bash
   python3 despacho.py
   ```
   *(En Windows también puedes usar `python despacho.py`).*

---

## Pasos para Usar el Sistema

Al iniciar el programa, se mostrará el menú interactivo en bucle con las opciones del `1` al `6`:

```text
              == == == == == == == == == == == == == == == == == ==
                 BIENVENIDO AL SISTEMA DE DESPACHO Y ALMACÉN
                         _______________________
                        |LOGISTICA              |h_ __
                        |                       ||=|##L_
                        |________________.====._||_|__._]
                        `(_)(_)`       `(_)(_)'''='=(_)
              == == == == == == == == == == == == == == == == == ==

              1. Apilar caja
              2. Retirar caja
              3. Agregar camión a la fila
              4. Despachar primer camión
              5. Ver estado del almacén y camiones
              6. Salir del programa
              --------------------------------------------------
```

### 1. Apilar una caja (`Opción 1`)
1. Ingresa `1` y presiona **Enter**.
2. Escribe el identificador de la caja (por ejemplo, `Caja-101`) y presiona **Enter**.
3. La caja quedará ubicada en la **cima** del almacén.

### 2. Retirar una caja de la cima (`Opción 2`)
1. Ingresa `2` y presiona **Enter**.
2. El sistema retirará automáticamente la **última caja** que fue apilada y mostrará su identificador.
3. Si el almacén está vacío, mostrará una alerta sin detener el programa.

### 3. Agregar un camión a la fila (`Opción 3`)
1. Ingresa `3` y presiona **Enter**.
2. Escribe la placa o identificador del camión (por ejemplo, `Camion-Alfa`) y presiona **Enter**.
3. El camión se ubicará al **final** de la cola de espera.

### 4. Despachar el primer camión (`Opción 4`)
1. Ingresa `4` y presiona **Enter**.
2. El sistema atenderá y despachará al **primer camión** que llegó a la fila.
3. Si no hay camiones esperando turno, mostrará un aviso informativo.

### 5. Ver estado del almacén y camiones (`Opción 5`)
1. Ingresa `5` y presiona **Enter**.
2. Se mostrará en pantalla el estado actual de ambas estructuras:
   * **Cajas apiladas (`Cima -> Base`):** Orden en que saldrán las cajas al retirarlas.
   * **Fila de camiones (`Frente -> Fin`):** Orden en que serán despachados los camiones.

### 6. Salir del programa (`Opción 6`)
1. Ingresa `6` y presiona **Enter** para finalizar la sesión de forma segura.

---

## Estructura del Proyecto

* `despacho.py`: Script principal ejecutable con la implementación de la Pila, la clase `Queue` (Cola) y la interfaz CLI.
* `instrucciones_de_la_actividad.md`: Especificación técnica y criterios de evaluación del laboratorio.
* `README.md`: Guía de instalación y manual de uso paso a paso.
