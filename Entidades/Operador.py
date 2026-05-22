class Operador:
    def __init__(self, id_operador, nombre):
        self.id_operador = id_operador
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre} - ID: {self.id_operador}"
    
    def resumen(self):
        return {
            "id": self.id_operador,
            "nombre": self.nombre
        }