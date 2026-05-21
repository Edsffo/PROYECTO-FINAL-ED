class Solicitud:
    def __init__(self, id_solicitud, origen, destino,tipo_taxi):
        self.id_solicitud=id_solicitud
        self.origen=origen
        self.destino=destino
        self.tipo_requerido=tipo_taxi
        self.estado="En espera"  #Estados: "Pendiente", "En Proceso", "Completada"
        self.tarifa=0
        self.tiempo_estimado=0
        self.conductor_asignado=None

    def __str__(self):
        conductor = self.conductor_asignado.nombre if self.conductor_asignado else "Ninguno"
        servicio_pedido = self.tipo_requerido.servicio
        return f"Solicitud: [{self.id_solicitud} - de:{self.origen} a {self.destino} con servicio: ({servicio_pedido})] - Tiempo estimado: [{self.tiempo_estimado}] min - Estado: {self.estado}]- Conductor: {conductor} - Tarifa: {self.tarifa}]"