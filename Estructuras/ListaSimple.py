class Nodo:    
    def __init__(self, dato):
        self.dato = dato
        self.siguiente: Nodo = None

class ListaSimple:
    def __init__(self):
        self.frente: Nodo = None
        self.fin: Nodo = None
    
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

    def recorrer(self):
        tmp = self.frente
        while tmp is not None:
            print(tmp.dato, end="->")
            tmp = tmp.siguiente
        print("null", end="\n")