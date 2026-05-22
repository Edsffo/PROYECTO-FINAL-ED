from Estructuras.ListaSimple import ListaSimple

class Conductor:
    def __init__(self, cedula, nombre,zona_actual, placa):
        self.cedula=cedula
        self.nombre=nombre
        self.zona_actual=zona_actual
        self.placa=placa
        self.disponible=True
        self.servicios_habilitados=ListaSimple()

    def habilitar_tipo_servicio(self, tipo_servicio):
        self.servicios_habilitados.insertar_fin(tipo_servicio)

    def es_habilitado_para(self, tipo_servicio):
        tmp = self.servicios_habilitados.frente
        while tmp is not None:
            if tmp.dato.tipo.lower() == tipo_servicio.tipo.lower():
                return True
            tmp = tmp.siguiente
        return False
    
    def obtener_servicios_habilitados(self):
        servicios = []
        tmp = self.servicios_habilitados.frente
        while tmp is not None:
            servicios.append(tmp.dato.tipo)
            tmp = tmp.siguiente
        return ", ".join(servicios) if servicios else "Ninguno"

    def __str__(self):
        estado = "Libre" if self.disponible else "Ocupado"
        return f"[Conductor: [{self.placa},{self.cedula},{self.nombre}]- Tipo servicio: [{self.obtener_servicios_habilitados()}] - Estado: [{estado}]"



