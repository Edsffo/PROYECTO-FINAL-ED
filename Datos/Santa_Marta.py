from Estructuras.Grafo import Grafo
import math

class Mapa:
    def __init__(self):
        self.grafo = Grafo()
        self._inicializar_zonas()
        self._inicializar_conexiones()

    def _inicializar_zonas(self):
        self.zonas = {
            1: "1. Rodadero",
            2: "2. Centro Histórico",
            3: "3. Bastidas",
            4: "4. Pozos Colorados",
            5: "5. Mamatoco",
            6: "6. Taganga",
            7: "7. Bonda",
            8: "8. Gaira"
        }

        for zona in self.zonas.values():
            self.grafo.agregarVertice(zona)

    def _inicializar_conexiones(self):
        conexiones = [
            ("1. Rodadero", "2. Centro Histórico", 4500),
            ("1. Rodadero", "8. Gaira", 2500),
            ("1. Rodadero", "4. Pozos Colorados", 6000),
            ("1. Rodadero", "6. Taganga", 8000),
            ("2. Centro Histórico", "3. Bastidas", 3000),
            ("2. Centro Histórico", "5. Mamatoco", 4000),
            ("3. Bastidas", "4. Pozos Colorados", 7000),
            ("3. Bastidas", "5. Mamatoco", 2000),
            ("4. Pozos Colorados", "7. Bonda", 9000),
            ("5. Mamatoco", "7. Bonda", 5000),
            ("6. Taganga", "2. Centro Histórico", 6000),
            ("8. Gaira", "4. Pozos Colorados", 4000),
        ]

        for origen, destino, distancia in conexiones:
            self.grafo.agregarArista(origen, destino, distancia)

    def mostrar_zonas(self):
        print("  ╔══════════════════════════════╗")
        print("  ║    ZONAS DE SANTA MARTA      ║")
        print("  ╚══════════════════════════════╝")
        for num, zona in self.zonas.items():
            nombre = zona[3:] if zona[0].isdigit() else zona
            print(f"    {num}. {nombre}")

    def mostrar_zonas_codigo(self):
        print("\tZONAS DE SANTA MARTA\t")
        for num, zona in self.zonas.items():
            print(f"    {num}.{zona}")

    def obtener_zona_codigo(self, codigo):
        return self.zonas.get(codigo)
    
    def validar_zona(self, codigo):
        return codigo in self.zonas
    
    def calcular_distancia(self, origen, destino):
        if origen not in self.zonas.values() or destino not in self.zonas.values():
            return float('inf')
        
        distancias = self.grafo.Dijkstra(origen)
        vertice_destino = self.grafo.buscarVertice(destino)

        if vertice_destino and distancias:
            return distancias.get(vertice_destino, float('inf'))
        return float('inf')
    
    def calcular_tiempo_recogida(self, zona_conductor, zona_origen_cliente):
        if zona_conductor == zona_origen_cliente:
            return 5
        
        distancia = self.calcular_distancia(zona_conductor, zona_origen_cliente)
        if distancia == float('inf'):
            return float('inf')
        
        return math.ceil(distancia/500)
    
    def existe_ruta(self, origen, destino):
        distancia = self.calcular_distancia(origen, destino)
        return distancia != float('inf')
    
    def cerrar_via(self, origen, destino):
        vertice_origen = self.grafo.buscarVertice(origen)
        vertice_destino = self.grafo.buscarVertice(destino)

        if vertice_origen and vertice_destino:
            self.grafo.eliminarArista(origen, destino)
            return True
        return False
    
    def abrir_via(self, origen, destino, distancia):
        vertice_origen = self.grafo.buscarVertice(origen)
        vertice_destino = self.grafo.buscarVertice(destino)
        
        if vertice_origen and vertice_destino:
            if not vertice_origen.listaAdyacencia.buscarAdyacencia(vertice_destino):
                self.grafo.agregarArista(origen, destino, distancia)
                return True
            return False
        
    def mostrar_grafo(self):
        print("\tMAPA DE CONEXIONES ACTIVAS\t")
        self.grafo.mostrar()

    def mostrar_conexiones(self):
        print("\tCONEXIONES HABILITADAS\t")
        tmp = self.grafo.primero
        while tmp:
            vertice = tmp
            print(f"\n{vertice.dato}")
            arista = vertice.listaAdyacencia.primera
            if arista is None:
                print("Sin conexiones activas")
            while arista:
                print(f"{arista.destino.dato} {arista.peso}m")
                arista = arista.siguiente
            tmp = tmp.siguiente

    def get_zonas_lista(self):
        return list(self.zonas.values())
    
    def get_zonas_dict(self):
        return self.zonas.copy()