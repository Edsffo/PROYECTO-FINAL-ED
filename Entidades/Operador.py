class Operador:
    def __init__(self, id_operador, nombre, cedula, telefono):
        self.id_operador = id_operador
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} - ID: {self.id_operador}"
    
    def resumen(self):
        return {
            "id": self.id_operador,
            "nombre": self.nombre,
            "cedula": self.cedula,
            "telefono": self.telefono
        }