class NodoCola:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Cola_circular:

    def __init__(self, cantidad):
        self.frente: NodoCola = None
        self.fin: NodoCola = None
        self.cantidad = cantidad
        self.tamaño = 0

    def encolar(self, valor):
        if self.tamaño == self.cantidad:
            return  
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
       
    def desencolar(self):
        if self.frente is None:
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

    def imprimir(self):
        if self.frente is None:
            print("Cola vacía")
            return

        print("Elementos de la cola:", end=" ")
        tmp = self.frente

        while True:
            print(tmp.dato, end=" ")
            tmp = tmp.siguiente

            if tmp == self.frente:
                break
        print()

    def ver_frente(self):
        if self.frente is not None:
            return self.frente.dato
        return None

    def ver_final(self):
        if self.fin is not None:
            return self.fin.dato
        return None