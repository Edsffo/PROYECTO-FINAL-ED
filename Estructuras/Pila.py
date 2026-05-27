class NodoPila:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self._cima = None
        self.tamaño = 0

    def push(self, elemento):
        nuevo_nodo = NodoPila(elemento)
        nuevo_nodo.siguiente = self._cima
        self._cima = nuevo_nodo
        self.tamaño += 1
        return True

    def pop(self):
        if self.empty():
            return None
        dato = self._cima.dato
        self._cima = self._cima.siguiente
        self.tamaño -= 1
        return dato

    def top(self):
        return None if self.empty() else self._cima.dato

    def empty(self):
        return self._cima is None

    def size(self):
        return self.tamaño

    def iterar(self):
        actual = self._cima
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente

    def print_stack(self):
        for dato in self.iterar():
            print(dato, end=" ")
        print()
