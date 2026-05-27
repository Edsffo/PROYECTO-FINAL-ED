class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaSimple:
    def __init__(self):
        self.frente = None
        self.fin = None

    def insertar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.frente is None:
            self.frente = nuevo_nodo
            self.fin = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.frente
            self.frente = nuevo_nodo

    def insertar_fin(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.frente is None:
            self.frente = nuevo_nodo
            self.fin = nuevo_nodo
        else:
            self.fin.siguiente = nuevo_nodo
            self.fin = nuevo_nodo

    def borrar_inicio(self):
        if self.frente is None:
            return None
        valor = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.fin = None
        return valor

    def borrar_fin(self):
        if self.frente is None:
            return None
        valor = self.fin.dato
        if self.frente == self.fin:
            self.frente = None
            self.fin = None
        else:
            tmp = self.frente
            while tmp.siguiente != self.fin:
                tmp = tmp.siguiente
            self.fin = tmp
            self.fin.siguiente = None
        return valor

    def buscar(self, criterio):
        tmp = self.frente
        while tmp:
            if criterio(tmp.dato):
                return tmp.dato
            tmp = tmp.siguiente
        return None

    def eliminar(self, criterio):
        anterior = None
        actual = self.frente
        while actual:
            if criterio(actual.dato):
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.frente = actual.siguiente
                if actual == self.fin:
                    self.fin = anterior
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def iterar(self):
        tmp = self.frente
        while tmp:
            yield tmp.dato
            tmp = tmp.siguiente

    def recorrer(self):
        tmp = self.frente
        while tmp is not None:
            print(tmp.dato, end="->")
            tmp = tmp.siguiente
        print("null", end="\n")
