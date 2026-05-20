class Pila:
    def __init__(self):
        self._items = []

    def push(self, elemento):
        self._items.append(elemento)

    def pop(self):
        if self.empty():
            return None
        return self._items.pop()

    def top(self):
        if self.empty():
            return None
        return self._items[-1]

    def empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def print_stack(self):
        for i in range(len(self._items) - 1, -1, -1):
            print(self._items[i], end=" ")
        print()

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
        
class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente: NodoDoble = None
        self.anterior: NodoDoble = None

class ListaDoble:
    def __init__(self):
        self.frente: NodoDoble = None
        self.fin: NodoDoble = None

    def insertar_inicio(self, dato):
        nuevo_nodo = NodoDoble(dato)
        if self.frente is None:
            self.frente = nuevo_nodo
            self.fin = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.frente
            self.frente.anterior = nuevo_nodo
            self.frente = nuevo_nodo
    
    def insertar_fin(self, dato):
        nuevo_nodo = NodoDoble(dato)
        if self.frente is None:
            self.frente = nuevo_nodo
            self.fin = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.fin
            self.fin.siguiente = nuevo_nodo
            self.fin = nuevo_nodo

    def insertar_luego(self, busqueda, dato):
        if self.frente is None:
            print("Lista vacía", end="\n")
            return
        
        tmp = self.frente
        while tmp is not None and tmp.dato != busqueda:
            tmp = tmp.siguiente
        
        if tmp is None:
            print("Elemento de búsqueda no encontrado", end="\n")
            return
        
        nuevoNodo = NodoDoble(dato)
        nuevoNodo.siguiente = tmp.siguiente
        nuevoNodo.anterior = tmp
        
        if tmp.siguiente is not None:
            tmp.siguiente.anterior = nuevoNodo
        else:
            self.fin = nuevoNodo
        
        tmp.siguiente = nuevoNodo

    def insertar_antes(self, busqueda, dato):
        if self.frente is None:
            print("Lista vacía", end="\n")
            return
        
        tmp = self.frente
        while tmp is not None and tmp.dato != busqueda:
            tmp = tmp.siguiente
        
        if tmp is None:
            print("Elemento de búsqueda no encontrado", end="\n")
            return
        
        nuevoNodo = NodoDoble(dato)
        nuevoNodo.siguiente = tmp
        nuevoNodo.anterior = tmp.anterior
        
        if tmp.anterior is not None:
            tmp.anterior.siguiente = nuevoNodo
        else:
            self.frente = nuevoNodo
        
        tmp.anterior = nuevoNodo

    def borrar_nodo(self, busqueda):
        if self.frente is None:
            print("Lista vacía", end="\n")
            return

        if self.frente.dato == busqueda:
            if self.frente == self.fin:
                self.frente = self.fin = None
            else:
                self.frente = self.frente.siguiente
                if self.frente is not None:
                    self.frente.anterior = None
            return

        tmp = self.frente
        while tmp.siguiente is not None and tmp.siguiente.dato != busqueda:
            tmp = tmp.siguiente

        if tmp.siguiente is None:
            print("Elemento de búsqueda no encontrado", end="\n")
            return

        objetivo = tmp.siguiente
        tmp.siguiente = objetivo.siguiente
        if objetivo.siguiente is not None:
            objetivo.siguiente.anterior = tmp
        else:
            self.fin = tmp

    def borrar_primero(self):
        if self.frente is None:
            print("Lista vacía", end="\n")
            return
        
        if self.frente == self.fin:
            self.frente = self.fin = None
        else:
            self.frente = self.frente.siguiente
            self.frente.anterior = None
    
    def borrar_ultimo(self):
        if self.frente is None:
            print("Lista vacía", end="\n")
            return
        
        if self.frente == self.fin:
            self.frente = self.fin = None
        else:
            self.fin = self.fin.anterior
            self.fin.siguiente = None
    
    def borrar_luego(self, busqueda):
        if self.frente is None:
            print("Lista vacía", end="\n")
            return
        
        tmp = self.frente
        while tmp is not None and tmp.dato != busqueda:
            tmp = tmp.siguiente
        
        if tmp is None or tmp.siguiente is None:
            print("Elemento no encontrado o " \
                    "no hay nodo siguiente para borrar")
            return
        
        tmp.siguiente = tmp.siguiente.siguiente
        if tmp.siguiente is None:
            self.fin = tmp
        else:
            tmp.siguiente.anterior = tmp

    def borrar_antes(self, busqueda):
        if self.frente is None:
            print("Lista vacía", end="\n")
            return
        
        tmp = self.frente
        while tmp is not None and tmp.dato != busqueda:
            tmp = tmp.siguiente
        
        if tmp is None or tmp.anterior is None:
            print("Elemento no encontrado o " \
                    "no hay nodo anterior para borrar")
            return
        
        nodo_borrar = tmp.anterior
        if nodo_borrar.anterior is not None:
            nodo_borrar.anterior.siguiente = tmp
        else:
            self.frente = tmp
        
        tmp.anterior = nodo_borrar.anterior
    
    def recorrerFrenteFin(self):
        tmp = self.frente
        while tmp is not None:
            print(tmp.dato, end="->")
            tmp = tmp.siguiente
        print("null", end="\n")
    
    def recorrerFinFrente(self):
        tmp = self.fin
        while tmp is not None:
            print(tmp.dato, end="<-")
            tmp = tmp.anterior
        print("null", end="\n")

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

class Conductor:
    def __init__(self, cedula, nombre, tipo_servicio, zona_actual):
        self.cedula=cedula
        self.nombre=nombre
        self.tipo_servicio=tipo_servicio  # Tipos:"Estándar", "Mascotas", "Equipaje"
        self.zona_actual=zona_actual
        self.disponible=True

    def __str__(self):
        return f"[{self.cedula}] {self.nombre} ({self.tipo_servicio}) - Estado: {'Libre' if self.disponible else 'Ocupado'}"



