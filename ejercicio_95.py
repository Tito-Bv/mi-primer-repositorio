"""Ejercicio 95: Leer números hasta 0 y determinar pares, impares, positivos y negativos.
Usa: Mientras + operadores."""


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")


class AnalizadorNumeros:
    def __init__(self):
        self.pares = 0
        self.impares = 0
        self.positivos = 0
        self.negativos = 0

    def analizar(self, numero):
        if numero % 2 == 0:
            self.pares += 1
        else:
            self.impares += 1

        if numero > 0:
            self.positivos += 1
        elif numero < 0:
            self.negativos += 1

    def leer_numeros(self):
        numero = leer_entero("Número (0 para terminar): ")
        while numero != 0:
            self.analizar(numero)
            numero = leer_entero("Número (0 para terminar): ")

    def mostrar_resultado(self):
        print(f"\nPares: {self.pares}")
        print(f"Impares: {self.impares}")
        print(f"Positivos: {self.positivos}")
        print(f"Negativos: {self.negativos}")


if __name__ == "__main__":
    analizador = AnalizadorNumeros()
    analizador.leer_numeros()
    analizador.mostrar_resultado()
