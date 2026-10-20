class Nodo:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, codigo, descripcion):
        nuevo = Nodo(codigo, descripcion)
        # TODO 1: agrega el nodo al final sin perder los anteriores
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.codigo, actual.descripcion)
            actual = actual.siguiente

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        # TODO 2: agrega el elemento a la cima
        self.items.append(elemento)

    def desapilar(self):
        # TODO 3: devuelve y elimina el último elemento;
        # controla el caso de pila vacía
        if len(self.items) == 0:
            return "La pila está vacía"
        return self.items.pop()

    # Reto individual: muestra la cima sin retirarla
    def cima(self):
        if len(self.items) == 0:
            return "La pila está vacía"
        return self.items[-1]

class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        # TODO 4: agrega el elemento al final
        self.items.append(elemento)

    def desencolar(self):
        # TODO 5: devuelve y elimina el primer elemento;
        # controla el caso de cola vacía
        if len(self.items) == 0:
            return "La cola está vacía"
        return self.items.pop(0)

# ---------------- PRUEBAS ----------------
lista = ListaEnlazada()
pila = Pila()
cola = Cola()

# Datos de prueba
lista.agregar("T01", "Teclado")
lista.agregar("T02", "Internet")
lista.agregar("T03", "Pantalla")

cola.encolar("T01")
cola.encolar("T02")
cola.encolar("T03")

pila.apilar("T01")
pila.apilar("T02")
pila.apilar("T03")

print(" Lista enlazada ")
lista.mostrar()

print(" Cola (FIFO) ")
print(cola.desencolar())  # T01
print(cola.desencolar())  # T02
print(cola.desencolar())  # T03
print(cola.desencolar())  # cola vacía

print("\nPila (LIFO) ")
print("Cima sin retirar:", pila.cima())  # T03
print(pila.desapilar())  # T03
print(pila.desapilar())  # T02
print(pila.desapilar())  # T01
print(pila.desapilar())  # pila vacía