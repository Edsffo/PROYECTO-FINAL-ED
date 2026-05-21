class TipoServicio:
    def __init__(self, tipo):
        self.tipo=tipo  # Tipos:"Estándar", "Mascotas", "Equipaje"
    
    def __str__(self):
        return f"[TipoServicio: {self.tipo}]"