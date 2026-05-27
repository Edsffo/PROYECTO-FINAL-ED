class NodoCola:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ColaCircular:
    def __init__(self, capacidad):
        self.frente: NodoCola = None
        self.fin: NodoCola = None
        self.capacidad = capacidad
        self.tamaño = 0

    def is_empty(self):
        return self.tamaño == 0

    def is_full(self):
        return self.tamaño >= self.capacidad

    def encolar(self, valor):
        if self.is_full():
            return False
        nuevo_nodo = NodoCola(valor)
        if self.frente is None:
            self.frente = nuevo_nodo
            self.fin = nuevo_nodo
            nuevo_nodo.siguiente = self.frente
        else:
            self.fin.siguiente = nuevo_nodo
            self.fin = nuevo_nodo
            self.fin.siguiente = self.frente
        self.tamaño += 1
        return True

    def desencolar(self):
        if self.is_empty():
            return None
        valor = self.frente.dato
        if self.frente == self.fin:
            self.frente = None
            self.fin = None
        else:
            self.frente = self.frente.siguiente
            self.fin.siguiente = self.frente
        self.tamaño -= 1
        return valor

    def ver_frente(self):
        return None if self.frente is None else self.frente.dato

    def ver_final(self):
        return None if self.fin is None else self.fin.dato

    def iterar(self):
        if self.is_empty():
            return
        tmp = self.frente
        while True:
            yield tmp.dato
            tmp = tmp.siguiente
            if tmp == self.frente:
                break

    def imprimir(self):
        if self.is_empty():
            print("Cola vacía")
            return
        print("Elementos de la cola:", end=" ")
        for dato in self.iterar():
            print(dato, end=" ")
        print()
