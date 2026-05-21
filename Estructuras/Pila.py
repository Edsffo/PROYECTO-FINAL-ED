class NodoPila:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self._cima = None

    def push(self, elemento):
        nuevo_nodo = NodoPila(elemento)
        nuevo_nodo.siguiente = self._cima
        self._cima = nuevo_nodo
        self.tamaño += 1

    def pop(self):
        if self.empty():
            return None
        dato = self._cima.dato
        self._cima = self._cima.siguiente
        self.tamaño -= 1
        return dato

    def top(self):
        if self.empty():
            return None
        return self._cima.dato

    def empty(self):
        return self._cima is None

    def size(self):
        return self.tamaño

    def print_stack(self):
        actual = self._cima
        while actual is not None:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()