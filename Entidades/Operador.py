class Operador:
    def __init__(self, id_operador, nombre):
        self.id_operador = id_operador
        self.nombre = nombre

        self.disponible = True

    def __str__(self):
        estado = "Libre" if self.disponible else "Ocupado"
        return f"[Operador: {self.id_operador} - {self.nombre} | Estado: {estado}]"