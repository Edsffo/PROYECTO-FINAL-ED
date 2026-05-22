from Entidades.Solicitudes import Solicitud
from Estructuras.ListaSimple import ListaSimple
from Estructuras.ListaDoble import ListaDoble
from Estructuras.ColaCircular import Cola_circular
from Estructuras.Pila import Pila

class Cooperativa:
    def __init__(self, mapa, operadores_iniciales, conductores_iniciales):
        self.mapa = mapa
        self.operadores = ListaSimple()
        for operador in operadores_iniciales:
            self.operadores.insertar_fin(operador)

        self.conductores = ListaSimple()
        for conductor in conductores_iniciales:
            self.conductores.insertar_fin(conductor)

        self.cola_espera = Cola_circular(10)

        self.solicitudes_activas = ListaDoble()
        self.historial = ListaDoble()
        self.pila_acciones = Pila()
        self.contador_solicitudes = 0 # Para asignar IDS unicos a cada solicitud.

        def calcular_tarifa(self, distancia):
            tarifa_base = 5000
            if distancia <= 1000:
                adicional = 2000
            elif distancia <= 3000:
                adicional = 4000
            elif distancia <= 6000:
                adicional = 7000
            elif distancia <= 10000:
                adicional = 10000
            else:
                adicional = 12000
            return tarifa_base + adicional
        
        def registrar_solicitud(self, nombre, telefono, zona_origen, zona_destino, tipo_servicio):
            self.contador_solicitudes += 1
            nueva = Solicitud(
                self.contador_solicitudes,
                nombre,
                telefono,
                zona_origen,
                zona_destino,
                tipo_servicio
            )
            self.cola_espera.encolar(nueva)
            self.pila_acciones.push(f"[SOLICITUD NUEVA] #{nueva.id} - {nombre} desde {zona_origen}")
            return nueva
        
        def buscar_conductor_disponible(self, zona_origen, tipo_servicio):
            mejor_conductor = None
            mejor_tiempo = float('inf')

            tmp = self.conductores.frente
            while tmp is not None:
                conductor = tmp.dato

                if not conductor.disponible:
                    tmp = tmp.siguiente
                    continue

                if tipo_servicio not in conductor.servicios_habilitados:
                    tmp = tmp.siguiente
                    continue

                if not self.mapa.existe_ruta(conductor.zona_actual, zona_origen):
                    tmp = tmp.siguiente
                    continue

                tiempo = self.mapa.calcular_tiempo_recogida(conductor.zona_actual, zona_origen)

                if tiempo < mejor_tiempo:
                    mejor_tiempo = tiempo
                    mejor_conductor = conductor

                tmp = tmp.siguiente
            return mejor_conductor, mejor_tiempo
        

