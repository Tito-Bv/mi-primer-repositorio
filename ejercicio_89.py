"""Ejercicio 89: Leer N números y determinar cuántos son positivos, negativos y cero.
Usa: Para + Si."""


def leer_entero_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("Debe ser mayor que 0.")
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")


def leer_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Ingresa un número.")


class ClasificadorSigno:
    def __init__(self, n):
        self.n = n
        self.positivos = 0
        self.negativos = 0
        self.ceros = 0

    def leer_numeros(self):
        for i in range(1, self.n + 1):
            numero = leer_numero(f"Número {i}: ")
            if numero > 0:
                self.positivos += 1
            elif numero < 0:
                self.negativos += 1
            else:
                self.ceros += 1

    def mostrar_resultado(self):
        print(f"\nPositivos: {self.positivos}")
        print(f"Negativos: {self.negativos}")
        print(f"Ceros: {self.ceros}")


if __name__ == "__main__":
    n = leer_entero_positivo("¿Cuántos números deseas ingresar? ")
    app = ClasificadorSigno(n)
    app.leer_numeros()
    app.mostrar_resultado()
