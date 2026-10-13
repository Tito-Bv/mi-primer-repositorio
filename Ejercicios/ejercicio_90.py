"""Ejercicio 90: Mostrar la tabla de multiplicar de un número y permitir repetir
el proceso para diferentes números.
Usa: Repetir + Para."""


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")


class TablaMultiplicar:
    def __init__(self, numero, limite=10):
        self.numero = numero
        self.limite = limite

    def mostrar(self):
        print(f"\nTabla del {self.numero}")
        for i in range(1, self.limite + 1):
            print(f"{self.numero} x {i} = {self.numero * i}")


class Programa:
    def ejecutar(self):
        while True:  # Repetir
            numero = leer_entero("Ingresa un número: ")
            TablaMultiplicar(numero).mostrar()
            respuesta = input("\n¿Deseas ver otra tabla? (s/n): ").strip().lower()
            if respuesta != "s":
                break
        print("¡Hasta luego!")


if __name__ == "__main__":
    Programa().ejecutar()
