"""Ejercicio 99: Leer N edades y determinar cuántas corresponden a niños,
adolescentes, adultos y adultos mayores.
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


def leer_edad(mensaje):
    while True:
        try:
            edad = int(input(mensaje))
            if edad >= 0:
                return edad
            print("La edad no puede ser negativa.")
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")


class ClasificadorEdades:
    def __init__(self, n):
        self.n = n
        self.ninos = 0          # 0 - 11
        self.adolescentes = 0   # 12 - 17
        self.adultos = 0        # 18 - 59
        self.adultos_mayores = 0  # 60+

    def leer_edades(self):
        for i in range(1, self.n + 1):
            edad = leer_edad(f"Edad {i}: ")
            if edad <= 11:
                self.ninos += 1
            elif edad <= 17:
                self.adolescentes += 1
            elif edad <= 59:
                self.adultos += 1
            else:
                self.adultos_mayores += 1

    def mostrar_resultado(self):
        print(f"\nNiños (0-11): {self.ninos}")
        print(f"Adolescentes (12-17): {self.adolescentes}")
        print(f"Adultos (18-59): {self.adultos}")
        print(f"Adultos mayores (60+): {self.adultos_mayores}")


if __name__ == "__main__":
    n = leer_entero_positivo("¿Cuántas edades deseas ingresar? ")
    clasificador = ClasificadorEdades(n)
    clasificador.leer_edades()
    clasificador.mostrar_resultado()
