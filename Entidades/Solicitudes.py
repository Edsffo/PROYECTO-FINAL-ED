class Solicitud:
    def __init__(self, id_solicitud, origen, destino, tipo_servicio):
        self.id_solicitud=id_solicitud
        self.origen=origen
        self.destino=destino
        self.tipo_servicio=tipo_servicio
        self.estado="En espera"  #Estados: "Pendiente", "En Proceso", "Completada"
        self.tarifa=0
        self.conductor_asignado=None

    def __str__(self):
        conductor = self.conductor_asignado.nombre if self.conductor_asignado else "Ninguno"
        return f"[Solicitud: {self.id_solicitud} - de:{self.origen} a {self.destino} ({self.tipo_servicio}) - Estado: {self.estado}]- Conductor: {conductor} - Tarifa: {self.tarifa}]"