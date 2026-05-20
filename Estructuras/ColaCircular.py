class Cola_circular:

    def __init__(self, cantidad):
        self.frente = -1
        self.fin = -1
        self.cantidad = cantidad
        self.items = [None] * cantidad

    def encolar(self, valor):
        nuevo_fin = (self.fin + 1) % self.cantidad

        if nuevo_fin == self.frente:
            print("Cola llena")
            return

        self.fin = nuevo_fin
        self.items[self.fin] = valor

        if self.frente == -1:
            self.frente = 0

        print("Elemento", valor, "encolado")

    def desencolar(self):
        if self.frente == -1:
            print("Cola vacía")
            return None

        valor = self.items[self.frente]
        print("Elemento:", valor, "desencolado")

        if self.frente == self.fin:
            self.frente = self.fin = -1
        else:
            self.frente = (self.frente + 1) % self.cantidad

        return valor

    def imprimir(self):
        if self.frente == -1:
            print("Cola vacía")
            return

        print("Elementos de la cola:", end=" ")
        i = self.frente

        while i != self.fin:
            print(self.items[i], end=" ")
            i = (i + 1) % self.cantidad

        print(self.items[self.fin])

    def ver_frente(self):
        if self.frente <= self.fin:
            return self.items[self.frente]
        else:
            return None

    def ver_final(self):
        if self.frente <= self.fin:
            return self.items[self.fin]
        else:
            return None