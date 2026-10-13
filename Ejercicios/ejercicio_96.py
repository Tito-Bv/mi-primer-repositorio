"""Ejercicio 96: Ingresar productos y precios hasta seleccionar Finalizar.
Mostrar el total.
Usa: Repetir + Según (match) + acumulador."""


def leer_precio(mensaje):
    while True:
        try:
            precio = float(input(mensaje))
            if precio >= 0:
                return precio
            print("El precio no puede ser negativo.")
        except ValueError:
            print("Entrada inválida. Ingresa un número.")


class Carrito:
    def __init__(self):
        self.productos = []
        self.total = 0.0  # acumulador

    def agregar(self, nombre, precio):
        self.productos.append((nombre, precio))
        self.total += precio

    def mostrar_resumen(self):
        print("\n--- RESUMEN DE COMPRA ---")
        for nombre, precio in self.productos:
            print(f"{nombre}: {precio:.2f}")
        print(f"TOTAL: {self.total:.2f}")


class Menu:
    def __init__(self):
        self.carrito = Carrito()

    def mostrar(self):
        print("\n1. Agregar producto")
        print("2. Finalizar")

    def ejecutar(self):
        opcion = ""
        while opcion != "2":  # Repetir
            self.mostrar()
            opcion = input("Elige una opción: ").strip()

            match opcion:  # Según
                case "1":
                    nombre = input("Nombre del producto: ").strip()
                    precio = leer_precio("Precio: ")
                    self.carrito.agregar(nombre, precio)
                case "2":
                    self.carrito.mostrar_resumen()
                case _:
                    print("Opción inválida.")


if __name__ == "__main__":
    Menu().ejecutar()
