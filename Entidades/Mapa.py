from Estructuras.Grafo import Grafo

class Mapa:
    BARRIOS = [
        "Centro Histórico", "Bastidas", "Galicia", "El prado", "El jardin", "La ciudadela",
        "Ciudad Equidad", "El mercado", "La paz", "Nuevo Milenio", "Nueva Galicia",
        "Pescaito", "Juan23", "Cartagena", "Taminaka", "Ojeda", "Santa Ana", "El pando",
        "11 de Noviembre", "El reposo"
    ]

    def __init__(self):
        self.grafo = Grafo()
        self.inicializar_mapa()

    def _conexion_bidireccional(self, origen, destino, peso):
        self.grafo.agregarArista(origen, destino, peso)
        self.grafo.agregarArista(destino, origen, peso)

    def inicializar_mapa(self):
        for barrio in self.BARRIOS:
            self.grafo.agregarVertice(barrio)

        self._conexion_bidireccional("Centro Histórico", "Bastidas", 2)
        self._conexion_bidireccional("Centro Histórico", "Galicia", 3)
        self._conexion_bidireccional("Centro Histórico", "El prado", 3)
        self._conexion_bidireccional("Centro Histórico", "El jardin", 3)
        self._conexion_bidireccional("Centro Histórico", "La ciudadela", 3)
        self._conexion_bidireccional("Centro Histórico", "Ciudad Equidad", 3)
        self._conexion_bidireccional("Centro Histórico", "El mercado", 3)
        self._conexion_bidireccional("Centro Histórico", "La paz", 3)
        self._conexion_bidireccional("Centro Histórico", "Nuevo Milenio", 3)
        self._conexion_bidireccional("Centro Histórico", "Nueva Galicia", 3)
        self._conexion_bidireccional("Centro Histórico", "Pescaito", 3)
        self._conexion_bidireccional("Centro Histórico", "Juan23", 3)
        self._conexion_bidireccional("Centro Histórico", "Cartagena", 3)
        self._conexion_bidireccional("Centro Histórico", "Taminaka", 3)
        self._conexion_bidireccional("Centro Histórico", "Ojeda", 3)
        self._conexion_bidireccional("Centro Histórico", "Santa Ana", 3)
        self._conexion_bidireccional("Centro Histórico", "El pando", 3)
        self._conexion_bidireccional("Centro Histórico", "11 de Noviembre", 3)
        self._conexion_bidireccional("Centro Histórico", "El reposo", 3)

        self._conexion_bidireccional("Bastidas", "Galicia", 2)
        self._conexion_bidireccional("Bastidas", "El prado", 2.5)
        self._conexion_bidireccional("Bastidas", "Taminaka", 4)

        self._conexion_bidireccional("El prado", "El jardin", 1.5)
        self._conexion_bidireccional("El prado", "La ciudadela", 2)
        self._conexion_bidireccional("El prado", "Galicia", 2.5)

        self._conexion_bidireccional("El jardin", "La ciudadela", 1.8)
        self._conexion_bidireccional("La ciudadela", "Ciudad Equidad", 2)
        self._conexion_bidireccional("Ciudad Equidad", "El mercado", 2.5)
        self._conexion_bidireccional("El mercado", "La paz", 1.5)

        self._conexion_bidireccional("Nuevo Milenio", "Nueva Galicia", 1.5)
        self._conexion_bidireccional("Nueva Galicia", "Pescaito", 2)
        self._conexion_bidireccional("Pescaito", "Juan23", 1.8)

        self._conexion_bidireccional("Cartagena", "Taminaka", 3)
        self._conexion_bidireccional("Taminaka", "Ojeda", 2.5)
        self._conexion_bidireccional("Ojeda", "Santa Ana", 2)

        self._conexion_bidireccional("Santa Ana", "El pando", 2)
        self._conexion_bidireccional("El pando", "11 de Noviembre", 2.5)
        self._conexion_bidireccional("11 de Noviembre", "El reposo", 2)

        self._conexion_bidireccional("La paz", "Nuevo Milenio", 3)
        self._conexion_bidireccional("Juan23", "Cartagena", 3.5)
        self._conexion_bidireccional("El reposo", "Ciudad Equidad", 4)
        self._conexion_bidireccional("Galicia", "Nueva Galicia", 2.5)

    def distancia(self, origen, destino):
        distancias = self.grafo.Dijkstra(origen)
        
        if distancias is None:
            return float('inf')

        for vertice, dist in distancias.items():
            if str(vertice) == destino:
                return dist
                
        return float('inf')

    def habilitar_conexion(self, a, b, peso):
        self._conexion_bidireccional(a, b, peso)

    def quitar_conexion(self, a, b):
        self.grafo.eliminarArista(a, b)
        self.grafo.eliminarArista(b, a)