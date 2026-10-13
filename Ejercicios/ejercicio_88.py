"""Ejercicio 88: Leer N números y calcular suma y promedio.
Usa: Para + acumulador."""


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


class SumaPromedio:
    def __init__(self, n):
        self.n = n
        self.suma = 0.0

    def leer_numeros(self):
        for i in range(1, self.n + 1):
            self.suma += leer_numero(f"Número {i}: ")

    def promedio(self):
        return self.suma / self.n

    def mostrar_resultado(self):
        print(f"\nSuma: {self.suma}")
        print(f"Promedio: {self.promedio():.2f}")


if __name__ == "__main__":
    n = leer_entero_positivo("¿Cuántos números deseas ingresar? ")
    app = SumaPromedio(n)
    app.leer_numeros()
    app.mostrar_resultado()
