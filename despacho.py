"""Simulador CLI de Pilas y Colas"""

VERDE = '\033[92m'
BOLD = '\033[1m'
GRIS = '\033[90m'
MAGENTA = '\033[95m'
AMARILLO = '\033[93m'
ROJO = '\033[91m'
CYAN = '\033[96m'
RESET = '\033[0m'


def crear_pila():
    """Crea la pila vacía"""
    return []


def pila_vacia(pila):
    """Revisa si la pila está vacía"""
    return len(pila) == 0


def push_pila(pila, caja):
    """Agregamos la caja en la cima"""
    pila.append(caja)


def menu_inicio():
    """Mostrar el menu principal en la consola"""

    almacen_cajas = crear_pila()

    while True:
        print(f"""{CYAN}{BOLD}
              == == == == == == == == == == == == == == == ==
              BIENVENIDO AL SISTEMA DE DESPACHO Y ALMACÉN
              == == == == == == == == == == == == == == == =={RESET}

              {AMARILLO}1. Apilar caja
              2. Retirar caja{RESET}
              {VERDE}3. Agregar camión a la fila
              4. Despachar primer camión{RESET}
              {MAGENTA}5. Ver estado del almacén y camiones{RESET}
              {GRIS}6. Salir del programa{RESET}
              {CYAN}-----------------------------------------------{RESET}
              """)

        opcion = input(f"{BOLD}Seleccione una opción (1 - 6): {RESET}")

        if opcion == "1":
            print("\nApilando caja...")
            nueva_caja = input(
                "\nAgregue el identificador de la caja (Ej.: Caja-101): ")
            push_pila(almacen_cajas, nueva_caja)
            print(f"{VERDE} Caja {nueva_caja} apilada correctamente! {RESET}")
        elif opcion == "2":
            print("""
            Retirando caja de la cima...""")
        elif opcion == "3":
            print("""
            Agregando camion a la fila...""")
        elif opcion == "4":
            print("""
            Despachando camión...""")
        elif opcion == "5":
            print(
                f"\n{MAGENTA}Estado actual del almacén: {almacen_cajas[::-1]}{RESET}")
        elif opcion == "6":
            print("""
            Saliendo del sistema...""")
            break
        else:
            print(f"{ROJO}Opción inválida. Inténtelo de nuevo por favor{RESET}")


if __name__ == "__main__":
    menu_inicio()
