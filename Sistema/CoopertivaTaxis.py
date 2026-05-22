import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.system("cls")

# ----------------------------------------------------- #

from Estructuras.ColaCircular import Cola_circular
from Estructuras.Pila import Pila
from Estructuras.ListaSimple import ListaSimple
from Entidades.Mapa import Mapa
from Entidades.Solicitudes import Solicitud
from Entidades.Conductor import Conductor
from Entidades.Operador import Operador
from Entidades.TipoTaxi import TipoServicio  

# ----------------------------------------------------- #

if __name__ == "__main__":
    # PRIMER FLUJO

    print("\t---- Bienvenido a SamarianTaxi ----")

    while True:
        operacion = int(input("Ingrese el servicio de taxi a elegir\n1. Taxi estándar\n2. Taxi con baúl\n3. Taxi para transporte de mascotas\n4. Salir\nOpción: "))
        match operacion:
            case 1:
                
                break
            case 2:
                break
            case 3:
                break
            case 4:
                print("Saliendo del sistema..")
                break
            case _:
                os.system("cls")
                print("Operacion inválida, ingrese un servicio válido.\n")

    pass
