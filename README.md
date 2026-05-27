1. Introducción

Las ciudades modernas tienen una curiosa habilidad para convertir algo tan simple como “tomar un taxi” en una coreografía de decisiones invisibles. Un conductor que está demasiado lejos. Una vía cerrada por obras. Un servicio que requiere transportar mascotas. Un cliente impaciente mirando el reloj como si pudiera negociar con el tráfico. Y, en medio de ese pequeño caos urbano, aparece este proyecto: un sistema de gestión para una cooperativa de taxis diseñado para organizar solicitudes, asignar conductores y mantener funcionando la maquinaria cotidiana del transporte público.

El objetivo principal del sistema es administrar de manera eficiente las solicitudes de servicio, considerando variables reales como la ubicación geográfica, el tipo de vehículo requerido, la disponibilidad de los conductores y el estado dinámico de la red vial. Porque, al final, una ciudad no es un tablero estático: cambia de humor como el mar antes de una tormenta.

Más allá de resolver el problema funcional, el proyecto pone el foco en algo esencial dentro del curso de Estructuras de Datos: la implementación manual de estructuras personalizadas. En tiempos donde las librerías automatizan casi todo, construir listas, pilas, colas y grafos desde cero tiene algo de oficio artesanal. Casi una pequeña rebelión académica contra la comodidad del lenguaje moderno.

2. Arquitectura del Proyecto

El sistema se organiza en módulos independientes que facilitan tanto la comprensión como el mantenimiento del código. Una decisión sensata, porque pocos enemigos son tan peligrosos para un programador como un proyecto desordenado que crece sin control.

Datos:
Aquí se almacena la información inicial del sistema: zonas geográficas, operadores, conductores y tipos de servicio disponibles. Es, por decirlo de alguna manera, la memoria inicial del programa.

Entidades:
Define las clases principales del sistema: Conductores, Operadores y Solicitudes. Cada una representa actores concretos dentro de la lógica del negocio, como piezas de una ciudad miniatura construida en código.

Estructuras:
Contiene las implementaciones personalizadas de listas, pilas, colas y grafos. Esta sección constituye el corazón académico del proyecto y demuestra el cumplimiento de los requisitos técnicos del curso.

Sistema:
Incluye la lógica central del programa, especialmente la clase Cooperativa, encargada de coordinar las operaciones y conectar todos los componentes.

main.py:
Es el punto de entrada de la aplicación y funciona como interfaz de interacción con el usuario mediante un menú de opciones.

3. Estructuras de Datos Personalizadas y Cumplimiento Técnico

Uno de los requisitos más importantes del proyecto consiste en evitar depender de estructuras nativas del lenguaje como solución principal. Una exigencia que, honestamente, obliga a mirar debajo del capó de la programación y entender cómo funcionan realmente las cosas.

ListaSimple.py:
Implementa una lista simplemente enlazada utilizada para almacenar operadores y conductores.

Su funcionamiento recuerda a una fila de vagones conectados entre sí: cada nodo conoce únicamente quién viene después. Minimalista, eficiente y sorprendentemente útil cuando las inserciones y eliminaciones ocurren principalmente en los extremos.

Cumplimiento:
- Gestión de listas de conductores y operadores.

ListaDoble.py:
Implementa una lista doblemente enlazada, permitiendo recorrer elementos hacia adelante y hacia atrás.

Esta estructura resulta especialmente útil para manejar solicitudes activas e historiales de servicios. A diferencia de la lista simple —que avanza como alguien obstinado mirando solo al frente— aquí cada nodo conserva memoria del pasado y conocimiento del futuro.

Cumplimiento:
- Historial de servicios y solicitudes activas.

ColaCircular.py:
Implementa una cola circular enlazada con capacidad máxima de diez elementos.

Las solicitudes que no pueden atenderse de inmediato ingresan aquí siguiendo el principio FIFO (First In, First Out). Es decir: quien llega primero, sale primero. Una idea profundamente democrática… al menos hasta que el tráfico decide intervenir.

La estructura circular evita desperdiciar espacio y permite reutilizar posiciones disponibles de manera eficiente.

Cumplimiento:
- Gestión de solicitudes en espera.

Pila.py:
Implementa una pila enlazada bajo el modelo LIFO (Last In, First Out).

Se utiliza para registrar las acciones recientes del sistema: asignaciones, registros y cierres de servicio. Funciona como una memoria inmediata, casi como esos escritorios donde el documento más reciente siempre termina encima de todos los demás.

Cumplimiento:
- Historial operativo y control de acciones.

Grafo.py

El grafo representa las zonas de la ciudad y las conexiones viales entre ellas.

Cada zona funciona como un vértice y cada vía como una arista con peso asociado a la distancia. Sobre esta estructura se implementa el algoritmo de Dijkstra para calcular rutas mínimas.

Y aquí aparece uno de los aspectos más interesantes del proyecto: la ciudad deja de ser una simple colección de calles y se convierte en una red dinámica, casi orgánica, donde cerrar una vía altera rutas, tiempos y decisiones. Como si una arteria bloqueada cambiara el ritmo completo del cuerpo urbano.

Cumplimiento:
- Modelado de zonas y vías mediante grafos.

4. Funcionalidades Principales del Sistema

Datos Iniciales:
El módulo datos_iniciales.py carga la información base del sistema:

Operadores predefinidos.
Conductores con zonas actuales y servicios habilitados.
Tipos de servicio:
- Taxi estándar.
- Taxi con baúl o parrilla.
- Taxi para mascotas.
Zonas geográficas de Santa Marta.

Esto permite iniciar el sistema con una estructura funcional desde el primer momento.

Clase Mapa (Santa_Marta.py):
La clase Mapa administra la lógica vial de la ciudad.

Entre sus funciones destacan:

Representación de zonas y conexiones.
Apertura y cierre dinámico de vías.
Recalculo automático de rutas.
Estimación de tiempos de recogida.

La implementación del algoritmo de Dijkstra permite encontrar la ruta más corta considerando únicamente las conexiones habilitadas. Dicho de otro modo: el sistema entiende que una calle cerrada deja de existir temporalmente, algo que cualquier conductor de ciudad aprende con resignación y algo de rabia.

Además, si el conductor ya se encuentra en la zona del pasajero, el tiempo estimado de recogida se fija en cinco minutos.

Entidades del Sistema.

Conductor:
Incluye información como:

- Placa.
- Nombre.
- Cédula.
- Teléfono.
- Zona actual.
- Servicios habilitados.
- Estado de disponibilidad.
- Operador

Representa al personal encargado de gestionar solicitudes dentro de la cooperativa.

Solicitud
Almacena:

- ID de servicio.
- Datos del cliente.
- Origen y destino.
- Tipo de servicio.
- Estado actual.
- Conductor asignado.
- Tarifa estimada.
- Tiempo de llegada.

Los estados posibles son:

- En espera.
- En atención.
- Cancelada.
- Finalizada.

5. Clase Cooperativa: El Núcleo del Sistema

La clase Cooperativa concentra toda la lógica operativa.

Registro de Solicitudes:
Las nuevas solicitudes ingresan a la cola de espera y la acción queda registrada en la pila de operaciones.
Aquí el sistema actúa casi como una recepción organizada en medio del caos urbano.

Búsqueda de Conductores:
El sistema selecciona el conductor más adecuado considerando:

- Disponibilidad.
- Compatibilidad con el servicio solicitado.
- Existencia de conexión vial válida.

No basta con tener un taxi libre; debe ser el taxi correcto y además capaz de llegar.

Atención de Solicitudes:
Cuando se atiende una solicitud:

- Se desencola la petición.
- Se asigna un conductor.
- Se calcula tarifa y tiempo estimado.
- El servicio pasa a solicitudes activas.

El conductor queda marcado como no disponible hasta finalizar el trayecto.

Cierre de Servicios:

Los servicios pueden:

- Finalizar exitosamente.
- Cancelarse.

Al cerrarse:

- El conductor vuelve a estar disponible.
- La solicitud pasa al historial.
- Se registra la acción en la pila.

El historial funciona como la memoria institucional del sistema. Porque incluso en software, olvidar suele salir caro.

Cálculo de Tarifas:

La tarifa se calcula usando la distancia recorrida según el grafo vial y la tabla estándar establecida. Nuestra propuesta para la solucion del calculo fue utilizar el metodo de caminos minimos dijkstra, esto hace que el algoritmo escoga las rutas mas rapidas para llegar de un vertice a otro (de un barrio a otro) segun el peso de sus aristas (su distancia), a parte el calculo del tiempo estimado se hizo con el la funcion de math.ceil, que divide la distancia entre 500 suponiendo que los taxis viajan 500 metros por minuto y lo redondea hacia arriba.