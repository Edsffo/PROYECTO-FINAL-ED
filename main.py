import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from Datos.datos_iniciales import (
    obtener_tipos_servicio,
    obtener_conductores,
    obtener_operadores,
    obtener_zonas
)

from Datos.Santa_Marta import (
    Mapa
)

from Sistema.Cooperativa import (
    Cooperativa
)    

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingrese un número válido.")

def leer_entero_rango(mensaje, minimo, maximo):
    while True:
        valor = leer_entero(mensaje)
        if minimo <= valor <= maximo:
            return valor
        print(f"Elige una opción entre {minimo} y {maximo}")

def mostrar_tipos_servicio(tipos):
    print("\nTIPOS DE SERVICIO: ")
    for k, v in tipos.items():
        print(f"{k}. {v['descripcion']}")

def menu_nueva_solicitud(coop, zonas, tipos_servicio):
    print("\n  ╔══════════════════════════════╗")
    print("  ║    NUEVA SOLICITUD DE TAXI   ║")
    print("  ╚══════════════════════════════╝")

    nombre = input("Nombre del cliente: ")
    nombre.strip()
    if not nombre:
        print("Nombre inválido, operación cancelada.")
        return
    
    telefono = input("Teléfono del cliente: ")
    telefono.strip()
    limpiar_pantalla()
    print(f"Solicitud registrada correctamente con datos: [{nombre} | {telefono}]")
    
    coop.mapa.mostrar_zonas()
    zona_origen_cod = leer_entero_rango("Zona de ORIGEN (número): ", 1, 8)
    zona_destino_cod = leer_entero_rango("Zona de DESTINO (número): ", 1, 8)

    zona_origen = zonas[zona_origen_cod]
    zona_destino = zonas[zona_destino_cod]

    mostrar_tipos_servicio(tipos_servicio)
    tipo_cod = leer_entero_rango("Tipo de servicio (número): ", 1, 3)
    tipo_nombre = tipos_servicio[tipo_cod]["nombre"]

    sol = coop.registrar_solicitud(nombre, telefono, zona_origen, zona_destino, tipo_nombre)
    print(f"[Solicitud #{sol.id} registrada y en cola de espera.]")

def menu_atender_solicitud(coop):
    print("\n  ╔══════════════════════════════╗")
    print("  ║    ATENDER SOLICITUD         ║")
    print("  ╚══════════════════════════════╝")

    coop.mostrar_cola_espera()

    solicitud, msg = coop.atender_solicitud()

    if solicitud is None:
        print(f"\n{msg}")
        return
    
    conductor = solicitud.conductor_asignado
    print(f"\n  Solicitud #{solicitud.id} asignada exitosamente:")
    print(f"     Cliente:          {solicitud.usuario} ({solicitud.telefono})")
    print(f"     Ruta:             {solicitud.zona_origen} → {solicitud.zona_destino}")
    print(f"     Tipo servicio:    {solicitud.tipo_servicio}")
    print(f"     ─────────────────────────────────")
    print(f"     Placa:            {conductor.placa}")
    print(f"     Conductor:        {conductor.nombre}")
    print(f"     Cédula:           {conductor.cedula}")
    print(f"     Tiempo recogida:  {solicitud.tiempo_recogida} minutos")
    print(f"     Tarifa estimada:  ${solicitud.tarifa:,} COP")

def menu_cerrar_servicio(coop):
    print("\n  ╔══════════════════════════════╗")
    print("  ║    CERRAR SERVICIO           ║")
    print("  ╚══════════════════════════════╝")

    coop.mostrar_activas()

    if coop.solicitudes_activas.frente is None:
        return
    
    id_sol = leer_entero("ID de la solicitud a cerrar: ")
    print("¿Cómo se cierra?")
    print("1. Finalizado (servicio completado)")
    print("2. Cancelado (cliente o conductor canceló)")
    opcion = leer_entero_rango("Opción: ", 1, 2)
    estado = "Finalizado" if opcion == 1 else "Cancelado"

    ok, msg = coop.cerrar_servicio(id_sol, estado)
    if ok:
        print(f"Solicitud #{id_sol} marcada como {estado}")
    else:
        print(f"{msg}")

def menu_gestion_vias(coop, zonas):
    while True:
        print("\n  ╔══════════════════════════════╗")
        print("  ║    GESTIÓN DE VÍAS           ║")
        print("  ╚══════════════════════════════╝")
        print("1. Ver conexiones activas")
        print("2. Cerrar una vía")
        print("3. Abrir una vía")
        print("0. Volver")

        op = leer_entero_rango("Opción: ",0, 3)
        
        if op == 0:
            break

        elif op == 1:
            coop.mapa.mostrar_conexiones()

        elif op == 2:
            coop.mapa.mostrar_zonas()
            o = leer_entero_rango("Zona de ORIGEN a cerrar (número): ", 1, 8)
            d = leer_entero_rango("Zona de DESTINO a cerrar (número): ", 1, 8)
            origen_str = zonas[o]
            destino_str = zonas[d]
            
            ok = coop.mapa.cerrar_via(origen_str, destino_str)
            if ok:
                print(f"Vía {origen_str} -> {destino_str} cerrada.")
            else:
                print("No se encontro esa conexion")

        elif op == 3:
            coop.mapa.mostrar_zonas()
            o = leer_entero_rango("Zona de ORIGEN a abrir (número): ", 1, 8)
            d = leer_entero_rango("Zona de DESTINO a abrir (número): ", 1, 8)
            distancia = leer_entero("Distancia en metros: ")
            origen_str = zonas[o]
            destino_str = zonas[d]
            ok = coop.mapa.abrir_via(origen_str, destino_str, distancia)
            if ok:
                print(f"Vía {origen_str} -> {destino_str} abierta ({distancia}m).")
            else:
                print(f"Esas zonas tienen no tienen problemas de vias o esa via no es válida.")

def main():
    limpiar_pantalla()
    mapa = Mapa()
    operadores = obtener_operadores()
    conductores = obtener_conductores()
    zonas = obtener_zonas()
    tipos_servicio = obtener_tipos_servicio()

    coop = Cooperativa(mapa, operadores, conductores)

    while True:
        print("  ╔══════════════════════════════════════╗")
        print("  ║   COOPERATIVA DE TAXIS SANTA MARTA   ║")
        print("  ╠══════════════════════════════════════╣")
        print("  ║  1. Nueva solicitud de taxi          ║")
        print("  ║  2. Atender solicitud (asignar taxi) ║")
        print("  ║  3. Cerrar servicio activo           ║")
        print("  ║  4. Ver solicitudes en espera        ║")
        print("  ║  5. Ver servicios en atención        ║")
        print("  ║  6. Ver historial de servicios       ║")
        print("  ║  7. Ver últimas acciones             ║")
        print("  ║  8. Ver conductores                  ║")
        print("  ║  9. Ver operadores                   ║")
        print("  ║  10. Gestión de vías (mapa)          ║")
        print("  ║  0. Salir                            ║")
        print("  ╚══════════════════════════════════════╝")

        op = leer_entero_rango("Opción: ", 0, 10)
        if op == 0:
            limpiar_pantalla()
            print("Sistema ejecutado con éxito.")
            break

        elif op == 1:
            menu_nueva_solicitud(coop, zonas, tipos_servicio)
        elif op == 2:
            menu_atender_solicitud(coop)
        elif op == 3:
            menu_cerrar_servicio(coop)
        elif op == 4:
            coop.mostrar_cola_espera()
        elif op == 5:
            coop.mostrar_activas()
        elif op == 6:
            coop.mostrar_historial()
        elif op == 7:
            coop.mostrar_pila_acciones()
        elif op == 8:
            coop.mostrar_conductores()
        elif op == 9:
            coop.mostrar_operadores()
        elif op == 10:
            menu_gestion_vias(coop, zonas)

if __name__ == "__main__":
    main()