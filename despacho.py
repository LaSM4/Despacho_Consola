"""Simulador CLI de Pilas y Colas"""

VERDE = '\033[92m'
BOLD = '\033[1m'
GRIS = '\033[90m'
MAGENTA = '\033[95m'
AMARILLO = '\033[93m'
ROJO = '\033[91m'
CYAN = '\033[96m'
RESET = '\033[0m'
MARGEN = ' ' * 14


def crear_pila():
    """Crea la pila vacía"""
    return []


def pila_vacia(pila):
    """Revisa si la pila está vacía"""
    return len(pila) == 0


def push_pila(pila, caja):
    """Agregamos la caja en la cima"""
    pila.append(caja)


def pop_pila(pila):
    """Retiramos la caja de la cima"""
    if pila_vacia(pila):
        return None
    return pila.pop()


class Queue:
    """creamos el objeto"""

    def __init__(self):
        """Creamos el constructor"""
        self.queue = []

    def is_empty(self):
        """Revisamos si la cola está vacia"""
        return len(self.queue) == 0

    def enqueue(self, camion):
        """metodo de inicio de cola"""
        self.queue.append(camion)

    def dequeue(self):
        """metodo para desencolar o despachar el camion"""
        if self.is_empty():
            return None
        return self.queue.pop(0)


def menu_inicio():
    """Mostrar el menu principal en la consola"""

    almacen_cajas = crear_pila()
    fila_camiones = Queue()

    while True:
        titulo = "BIENVENIDO AL SISTEMA DE DESPACHO Y ALMACÉN"
        print(f"""{CYAN}{BOLD}
              == == == == == == == == == == == == == == == == == ==
                {titulo:^47}
                         _______________________
                        |LOGISTICA              |h_ __
                        |                       ||=|##L_
                        |________________.====._||_|__._]
                        `(_)(_)`       `(_)(_)'''='=(_)
              == == == == == == == == == == == == == == == == == =={RESET}

              {AMARILLO}1. Apilar caja
              2. Retirar caja{RESET}
              {VERDE}3. Agregar camión a la fila
              4. Despachar primer camión{RESET}
              {MAGENTA}5. Ver estado del almacén y camiones{RESET}
              {GRIS}6. Salir del programa{RESET}
              {CYAN}{BOLD}--------------------------------------------------{RESET}
              """)

        opcion = input(
            f"{MARGEN}{BOLD}Seleccione una opción (1 - 6): {RESET}")

        if opcion == "1":
            print(f"\n{MARGEN}Apilando caja...")
            nueva_caja = input(
                f"\n{MARGEN}Agregue el identificador de la caja "
                f"(Ej.: Caja-101): ")
            push_pila(almacen_cajas, nueva_caja)
            print(
                f"\n{MARGEN}{VERDE}La Caja ID: {nueva_caja}, "
                f"fue apilada correctamente!{RESET}")
        elif opcion == "2":
            print(f"\n{MARGEN}Retirando caja de la cima...")
            caja_retirada = pop_pila(almacen_cajas)
            if caja_retirada is None:
                print(
                    f"\n{MARGEN}{ROJO}[!] Error: El almacén está vacío "
                    f"(no hay cajas que retirar).{RESET}")
            else:
                print(
                    f"\n{MARGEN}{VERDE}Caja ID: {caja_retirada}, "
                    f"fue retirada de la cima{RESET}")
        elif opcion == "3":
            print(f"\n{MARGEN}Agregando camión a la fila...")
            nuevo_camion = input(
                f"\n{MARGEN}Agregue el identificador del camión "
                f"(Ej.: Camion-Alfa): ")
            fila_camiones.enqueue(nuevo_camion)
            print(
                f"\n{MARGEN}{VERDE}Camión ID: {nuevo_camion}, "
                f"agregado en la fila{RESET}")
        elif opcion == "4":
            print(f"\n{MARGEN}Despachando camión...")
            camion_despachado = fila_camiones.dequeue()
            if camion_despachado is None:
                print(
                    f"\n{MARGEN}{ROJO}[!] Error: "
                    f"No hay camiones esperando turno.{RESET}")
            else:
                print(
                    f"\n{MARGEN}{VERDE}Camión ID: {camion_despachado} "
                    f"fue despachado exitosamente!{RESET}")
        elif opcion == "5":
            cajas_cima_base = almacen_cajas[::-1]
            camiones_frente_fin = fila_camiones.queue
            print(
                f"""{MAGENTA}
              ---------------------------------------------------
              ESTADO ACTUAL:
              - Cajas apiladas (Cima -> Base): {cajas_cima_base}
              - Fila de camiones (Frente -> Fin): {camiones_frente_fin}
              ---------------------------------------------------{RESET}
              """)
        elif opcion == "6":
            print(f"\n{MARGEN}{ROJO}Hasta pronto!\n{RESET}")
            break
        else:
            print(
                f"\n{MARGEN}{ROJO}Opción inválida. "
                f"Inténtelo de nuevo por favor{RESET}")


if __name__ == "__main__":
    menu_inicio()
