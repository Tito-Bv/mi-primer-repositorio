"""Ejercicio 92: Menú de figuras geométricas que permita calcular áreas repetidamente.
Usa: Repetir + Según (match) + Si."""
import math


def leer_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            print("El valor debe ser mayor que 0.")
        except ValueError:
            print("Entrada inválida. Ingresa un número.")


class Figuras:
    @staticmethod
    def area_circulo(radio):
        return math.pi * radio ** 2

    @staticmethod
    def area_rectangulo(base, altura):
        return base * altura

    @staticmethod
    def area_triangulo(base, altura):
        return (base * altura) / 2

    @staticmethod
    def area_cuadrado(lado):
        return lado ** 2


class Menu:
    def mostrar(self):
        print("\n--- ÁREAS DE FIGURAS ---")
        print("1. Círculo")
        print("2. Rectángulo")
        print("3. Triángulo")
        print("4. Cuadrado")
        print("5. Salir")

    def ejecutar(self):
        opcion = ""
        while opcion != "5":  # Repetir
            self.mostrar()
            opcion = input("Elige una opción: ").strip()

            match opcion:  # Según
                case "1":
                    radio = leer_positivo("Radio: ")
                    print(f"Área: {Figuras.area_circulo(radio):.2f}")
                case "2":
                    base = leer_positivo("Base: ")
                    altura = leer_positivo("Altura: ")
                    print(f"Área: {Figuras.area_rectangulo(base, altura):.2f}")
                case "3":
                    base = leer_positivo("Base: ")
                    altura = leer_positivo("Altura: ")
                    print(f"Área: {Figuras.area_triangulo(base, altura):.2f}")
                case "4":
                    lado = leer_positivo("Lado: ")
                    print(f"Área: {Figuras.area_cuadrado(lado):.2f}")
                case "5":
                    print("¡Hasta luego!")
                case _:
                    print("Opción inválida.")


if __name__ == "__main__":
    Menu().ejecutar()
