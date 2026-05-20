class Vertice:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente: Vertice = None
        self.listaAdyacencia = ListaAdyacencia()

    def __str__(self):
        return str(self.dato)

# Arista o Arco
class Arista:
    def __init__(self, destino: Vertice, peso = None):
        self.peso = peso
        self.siguiente: Arista = None
        self.destino = destino

# Lista de Adyacencia
class ListaAdyacencia:
    def __init__(self):
        self.primera: Arista = None
        self.ultima: Arista = None

    def __str__(self):
        lista_str = ""
        temporal = self.primera
        while temporal is not None:
            lista_str += str(temporal.destino.dato)
            if temporal.peso is not None:
                lista_str += "(" + str(temporal.peso) + ")"
            lista_str += " -> "
            temporal = temporal.siguiente
        lista_str += "None"
        return lista_str    
    
    def esVacia(self):
        return self.primera is None

    def buscarAdyacencia(self, destino: Vertice):
        temporal = self.primera
        while temporal is not None:
            if str(temporal.destino) == str(destino):
                return True
            temporal = temporal.siguiente
        return False

    def agregar(self, destino: Vertice, peso = None):
        if not self.buscarAdyacencia(destino):
            self.agregarArista(Arista(destino, peso))

    def agregarArista(self, nuevaArista: Arista):
        if self.esVacia():
            self.primera = nuevaArista
            self.ultima = nuevaArista
            return

        dato = str(nuevaArista.destino)

        if dato < str(self.primera.destino):
            nuevaArista.siguiente = self.primera
            self.primera = nuevaArista
            return

        if dato > str(self.primera.destino):
            self.ultima.siguiente = nuevaArista
            self.ultima = nuevaArista
            return

        temporal = self.primera
        while temporal.siguiente is not None and dato > str(temporal.destino):
            temporal = temporal.siguiente

        nuevaArista.siguiente = temporal.siguiente
        temporal.siguiente = nuevaArista

    def eliminar(self, destino: Vertice):
        if self.esVacia():
            return

        if self.primera.destino.dato == destino.dato:
            self.primera = self.primera.siguiente
            if self.primera is None:
                self.ultima = None
            return

        temporal = self.primera
        
        while temporal.siguiente is not None and temporal.siguiente.destino.dato != destino.dato:
            temporal = temporal.siguiente

        if temporal.siguiente is not None:
            temporal.siguiente = temporal.siguiente.siguiente
            if temporal.siguiente is None:
                self.ultima = temporal

class Grafo:
    def __init__(self):
        self.primero: Vertice = None
        self.ultimo: Vertice = None

    def __str__(self):
        temporal = self.primero
        grafo_str = ""
        while temporal is not None:
            grafo_str += str(temporal.dato) + " -> " + \
                    str(temporal.listaAdyacencia) + "\n"
            temporal = temporal.siguiente
        return grafo_str

    def agregarArista(self, origen, destino, peso = None):
        verticeOrigen = self.buscarVertice(origen)
        verticeDestino = self.buscarVertice(destino)
        if verticeOrigen is not None and verticeDestino is not None:
            verticeOrigen.listaAdyacencia.agregar(verticeDestino, peso)

    def eliminarArista(self, origen, destino):
        verticeOrigen = self.buscarVertice(origen)
        verticeDestino = self.buscarVertice(destino)
        if verticeOrigen is not None and verticeDestino is not None:
            verticeOrigen.listaAdyacencia.eliminar(verticeDestino)

    def agregarVertice(self, dato):
        if self.buscarVertice(dato) is not None:
            return

        nuevoVertice = Vertice(dato)
        if self.esVacio():
            self.primero = nuevoVertice
            self.ultimo = nuevoVertice
            return

        nuevoDato = str(dato)
        if nuevoDato < str(self.primero):
            nuevoVertice.siguiente = self.primero
            self.primero = nuevoVertice
            return

        if nuevoDato > str(self.primero):
            self.ultimo.siguiente = nuevoVertice
            self.ultimo = nuevoVertice
            return

        temporal = self.primero
        while temporal.siguiente is not None and nuevoDato > str(temporal):
            temporal = temporal.siguiente

        nuevoVertice.siguiente = temporal.siguiente
        temporal.siguiente = nuevoVertice

    def eliminarVertice(self, dato):
        if self.esVacio():
            return

        verticeBorrar: Vertice = None

        if str(self.primero) == str(dato):
            verticeBorrar = self.primero
            self.primero = self.primero.siguiente
            if self.primero is None:
                self.ultimo = None
        else:
            temporal = self.primero
            while temporal.siguiente is not None and temporal.siguiente.__str__() != str(dato):
                temporal = temporal.siguiente

            if temporal.siguiente is not None:
                verticeBorrar = temporal.siguiente
                temporal.siguiente = temporal.siguiente.siguiente
                if temporal.siguiente is None:
                    self.ultimo = temporal

        if verticeBorrar is not None:
            temporal = self.primero
            while temporal is not None:
                temporal.listaAdyacencia.eliminar(verticeBorrar)
                temporal = temporal.siguiente

    def esVacio(self):
        return self.primero is None

    def buscarVertice(self, dato):
        temporal = self.primero
        while temporal is not None:
            if str(temporal) == str(dato):
                return temporal
            temporal = temporal.siguiente
        return None
    
    def mostrar(self):
        print(self.__str__())