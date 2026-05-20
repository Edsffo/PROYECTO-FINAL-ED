
class Conductor:
    def __init__(self, cedula, nombre, tipo_servicio, zona_actual):
        self.cedula=cedula
        self.nombre=nombre
        self.tipo_servicio=tipo_servicio  # Tipos:"Estándar", "Mascotas", "Equipaje"
        self.zona_actual=zona_actual
        self.disponible=True

    def __str__(self):
        return f"[{self.cedula}] {self.nombre} ({self.tipo_servicio}) - Estado: {'Libre' if self.disponible else 'Ocupado'}"



