from Entidades.Solicitudes import Solicitud
from Estructuras.ListaSimple import ListaSimple
from Estructuras.ListaDoble import ListaDoble
from Estructuras.ColaCircular import ColaCircular
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

        self.cola_espera = ColaCircular(10)

        self.solicitudes_activas = ListaDoble()
        self.historial = ListaDoble()
        self.pila_acciones = Pila()
        self.contador_solicitudes = 0  # Para asignar IDs únicos a cada solicitud.

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
        # intentar encolar; si la cola está llena, devolver error para que el llamador lo maneje
        if not self.cola_espera.encolar(nueva):
            return None, "Cola de espera llena"
        self.pila_acciones.push(f"[SOLICITUD NUEVA] #{nueva.id} - {nombre} desde {zona_origen}")
        return nueva, "ok"

    def buscar_conductor_disponible(self, zona_origen, tipo_servicio):
        mejor_conductor = None
        mejor_tiempo = float('inf')

        # usar el iterador de ListaSimple
        for conductor in self.conductores.iterar():
            if not conductor.disponible:
                continue
            if not conductor.puede_atender(tipo_servicio):
                continue
            if not self.mapa.existe_ruta(conductor.zona_actual, zona_origen):
                continue
            tiempo = self.mapa.calcular_tiempo_recogida(conductor.zona_actual, zona_origen)
            if tiempo < mejor_tiempo:
                mejor_tiempo = tiempo
                mejor_conductor = conductor

        return mejor_conductor, mejor_tiempo

    def atender_solicitud(self):
        solicitud = self.cola_espera.ver_frente()
        if solicitud is None:
            return None, "No hay solicitudes en espera"

        conductor, tiempo = self.buscar_conductor_disponible(
            solicitud.zona_origen,
            solicitud.tipo_servicio
        )

        if conductor is None:
            return None, "No hay conductores disponibles en este momento"

        # desencolar ahora que sabemos que vamos a atender
        self.cola_espera.desencolar()

        distancia = self.mapa.calcular_distancia(solicitud.zona_origen, solicitud.zona_destino)
        if distancia == float('inf'):
            return None, "No existe una ruta entre el origen y el destino del cliente"

        tarifa = self.calcular_tarifa(distancia)

        # usar la API de Solicitud y Conductor
        solicitud.asignar_conductor(conductor, tarifa, tiempo)
        conductor.asignar()
        conductor.servicio_actual = solicitud

        self.solicitudes_activas.insertar_fin(solicitud)
        self.pila_acciones.push(
            f"[ASIGNADO] #{solicitud.id} -> {conductor.nombre} ({conductor.placa})"
        )

        return solicitud, "ok"

    def cerrar_servicio(self, id_solicitud, estado_final):
        # buscar en solicitudes_activas usando iterador de ListaDoble si existe
        solicitud_encontrada = None
        for s in self.solicitudes_activas.iterar_adelante():
            if s.id == id_solicitud:
                solicitud_encontrada = s
                break

        if solicitud_encontrada is None:
            return False, "Solicitud no encontrada en servicios activos"

        # normalizar estado final a minúsculas
        estado_final_norm = estado_final.lower()
        solicitud_encontrada.estado = estado_final_norm

        conductor = solicitud_encontrada.conductor_asignado
        if conductor:
            conductor.liberar()
            if estado_final_norm == "finalizada" or estado_final_norm == "finalizado":
                conductor.zona_actual = solicitud_encontrada.zona_destino
            conductor.servicio_actual = None

        self.solicitudes_activas.borrar_nodo(solicitud_encontrada)
        self.historial.insertar_fin(solicitud_encontrada)
        self.pila_acciones.push(
            f"[{estado_final_norm.upper()}] #{solicitud_encontrada.id} - {solicitud_encontrada.usuario}"
        )

        return True, "ok"

    def mostrar_cola_espera(self):
        print("\n\t--- COLA DE ESPERA ---")
        if self.cola_espera.is_empty():
            print("Sin solicitudes en espera")
            return
        i = 1
        for s in self.cola_espera.iterar():
            print(f"{i}. #{s.id} | {s.usuario} | {s.zona_origen} -> {s.zona_destino} | {s.tipo_servicio}")
            i += 1

    def mostrar_activas(self):
        print("\n\t--- SERVICIOS EN ATENCION ---")
        if self.solicitudes_activas.frente is None:
            print("Sin servicios activos")
            return
        for s in self.solicitudes_activas.iterar_adelante():
            conductor = s.conductor_asignado
            print(f"{s.id} | {s.usuario} | {s.zona_origen} -> {s.zona_destino}")
            if conductor:
                print(f"Conductor: {conductor.nombre} ({conductor.placa})")
            print(f"Tarifa: ${s.tarifa:,} | Tiempo recogida: {s.tiempo_recogida} min")

    def mostrar_historial(self):
        print("\n\t--- HISTORIAL DE SERVICIOS ---")
        if self.historial.frente is None:
            print("Sin registro en el historial")
            return
        for s in self.historial.iterar_adelante():
            nombre_conductor = s.conductor_asignado.nombre if s.conductor_asignado else "N/A"
            print(f" #{s.id} | {s.usuario} | {s.estado}")
            print(f" Ruta: {s.zona_origen} -> {s.zona_destino} | Tipo: {s.tipo_servicio}")
            print(f" Conductor: {nombre_conductor} | Tarifa: {s.tarifa:,}")

    def mostrar_conductores(self):
        print("\n\t--- CONDUCTORES REGISTRADOS ---")
        for c in self.conductores.iterar():
            estado = "Disponible" if c.disponible else "Ocupado"
            servicios = ", ".join(c.servicios_habilitados)
            print(f"{c.placa} | {c.nombre} | {estado} | Zona: {c.zona_actual}")
            print(f" Servicios: {servicios}")

    def mostrar_operadores(self):
        print("\n\t--- OPERADORES REGISTRADOS ---")
        for op in self.operadores.iterar():
            print(f"ID {op.id_operador} | {op.nombre} | Tel: {op.telefono}")

    def mostrar_pila_acciones(self):
        print("\n\t--- ULTIMAS ACCIONES ---")
        if self.pila_acciones.empty():
            print("Sin acciones registradas")
            return
        for accion in self.pila_acciones.iterar():
            print(f"{accion}")
