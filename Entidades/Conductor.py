from Estructuras.ListaSimple import ListaSimple

class Conductor:
    def __init__(self, placa, nombre, cedula, telefono, zona_actual, servicios_habilitados):
        self.placa = placa
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono
        self.zona_actual = zona_actual
        self.servicios_habilitados = servicios_habilitados  # lista de strings
        self.disponible = True
        self.servicio_actual = None

    def puede_atender(self, tipo_servicio):
        return tipo_servicio in self.servicios_habilitados

    def asignar(self):
        self.disponible = False

    def liberar(self):
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Ocupado"
        return f"{self.nombre} - {self.placa} - {estado}"

    def resumen(self):
        return {
            "nombre": self.nombre,
            "placa": self.placa,
            "cedula": self.cedula,
            "telefono": self.telefono,
            "zona": self.zona_actual,
            "servicios": self.servicios_habilitados,
            "disponible": self.disponible
        }
