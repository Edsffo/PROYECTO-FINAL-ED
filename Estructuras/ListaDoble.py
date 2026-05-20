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