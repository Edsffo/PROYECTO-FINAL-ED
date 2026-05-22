from Estructuras.ListaSimple import ListaSimple

class Conductor:
    def __init__(self, placa, nombre, cedula, zona_actual, servicios_habilitados):
        self.placa = placa
        self.nombre = nombre
        self.cedula = cedula
        self.zona_actual = zona_actual
        self.servicios_habilitados = servicios_habilitados
        self.disponible = True
        self.servicio_actual = None

    def __str__(self):
        estado = "Disponible" if self.disponible else "Ocupado"
        return f"{self.nombre} - {self.placa} - {estado}"
        
    def resumen(self):
        return {
            "nombre": self.nombre,
            "placa": self.placa,
            "cedula": self.cedula,
            "zona": self.zona_actual,
            "servicios": self.servicios_habilitados,
            "disponible": self.disponible
        }