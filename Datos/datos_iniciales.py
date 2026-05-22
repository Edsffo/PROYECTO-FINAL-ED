from Entidades.Operador import Operador
from Entidades.Conductor import Conductor

def obtener_operadores():
    return [
        Operador(1, "Carlos López", "12345678", "3001112233"),
        Operador(2, "Ana Martínez", "87654321", "3002223344"),
        Operador(3, "Jorge Rodríguez", "11223344", "3003334455"),
    ]

def obtener_conductores():
    return [
        Conductor("RCD123", "Javier Hernández", "1002345678", "3112223344", "1. Rodadero", ["estandar", "baul"]),
        Conductor("SMA789", "María López", "1003456789", "3113334455", "2. Centro Histórico", ["estandar"]),
        Conductor("STG456", "Pedro Martínez", "1004567890", "3114445566", "3. Bastidas", ["estandar", "mascotas"]),
        Conductor("TAG123", "Luisa Fernández", "1005678901", "3115556677", "6. Taganga", ["estandar", "baul", "mascotas"]),
        Conductor("PCR789", "Andrés Castro", "1006789012", "3116667788", "4. Pozos Colorados", ["estandar", "baul"]),
        Conductor("GIR456", "Carmen Díaz", "1007890123", "3117778899", "8. Gaira", ["estandar"]),
        Conductor("MAM123", "Roberto Jiménez", "1008901234", "3118889900", "5. Mamatoco", ["estandar", "mascotas"]),
    ]

def obtener_tipos_servicio():
    return {
        1: {"nombre": "estandar", "descripcion": "Estándar (viaje normal)"},
        2: {"nombre": "baul", "descripcion": "Baúl / Parrilla (equipaje voluminoso)"},
        3: {"nombre": "mascotas", "descripcion": "Mascotas (transporte de animales)"}
    }

def obtener_zonas():
    return {
        1: "1. Rodadero",
        2: "2. Centro Histórico",
        3: "3. Bastidas",
        4: "4. Pozos Colorados",
        5: "5. Mamatoco",
        6: "6. Taganga",
        7: "7. Bonda",
        8: "8. Gaira"
    }