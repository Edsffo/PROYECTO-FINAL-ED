class Solicitud:
    def __init__(self, id_solicitud, usuario, telefono, zona_origen, zona_destino, tipo_servicio):
        self.id = id_solicitud
        self.usuario = usuario
        self.telefono = telefono
        self.zona_origen = zona_origen
        self.zona_destino = zona_destino
        self.tipo_servicio = tipo_servicio
        self.estado = "En espera" # "en atención, completado, cancelado"
        self.conductor_asignado = None
        self.tarifa = 0
        self.tiempo_recogida = 0
    
    def __str__(self):
        return f"Solicitud #{self.id} - {self.usuario} - {self.estado}"
    
    def resumen(self):
        return {
            "id": self.id,
            "usuario": self.usuario,
            "telefono": self.telefono,
            "origen": self.zona_origen,
            "destino": self.zona_destino,
            "tipo": self.tipo_servicio,
            "estado": self.estado,
            "conductor": self.conductor_asignado.nombre if self.conductor_asignado else "No hay conductor asignado",
            "tarifa": self.tarifa,
            "tiempo_recogida": self.tiempo_recogida
        }