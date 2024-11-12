import os
import json
import random
import time

# Función para limpiar consola
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

# Datos base y configuraciones
paises_validos = ["Argentina", "Chile", "Uruguay", "Bolivia", "Paraguay", "Brasil"]
paises_invalidos = ["Peru", "Ecuador", "Venezuela", "Colombia", "Guyana"]

razones_entrada_validas = ["Turismo", "Trabajo", "Estudio", "Residencia"]
razones_entrada_invalidas = ["Negocios", "Visita médica", "Evento Deportivo"]

documentos_validos = ["DNI", "Pasaporte", "Permiso de Trabajo"]
documentos_invalidos = ["Carnet de Estudiante", "ID Nacional", "Permiso Temporal"]

# Estructura de reglas y logros
logros = {
    "aprobaciones_perfectas": False,
    "negaciones_correctas": False,
    "primera_aprobacion": False,
    "primer_rechazo": False,
    "deshacer_decision": False,  # Nuevo logro: deshacer decisiones
    "decisiones_extra_puntos": False  # Nuevo logro: decisiones correctas extra puntos
}

estadisticas = {
    "aprobaciones": 0,
    "rechazos": 0,
    "puntos": 0
}

# Funciones para guardar logros y estadísticas
def guardar_logros():
    with open("logros.json", "w") as f:
        json.dump(logros, f, indent=4)

def guardar_estadisticas():
    with open("estadisticas.json", "w") as f:
        json.dump(estadisticas, f, indent=4)

# Clase Inmigrante
class Inmigrante:
    def __init__(self):
        self.nombre = random.choice(["Juan", "Maria", "Carlos", "Ana", "Pedro", "Lucia"])
        self.pais_origen = random.choice(paises_validos + paises_invalidos)
        self.razon = random.choice(razones_entrada_validas + razones_entrada_invalidas)
        self.documento = random.choice(documentos_validos + documentos_invalidos)
        self.dni = "".join([str(random.randint(0, 9)) for _ in range(8)])

# Mostrar los criterios de entrada válidos antes de cada día
def mostrar_criterios_validos():
    limpiar_consola()
    print("\n" + "="*30)
    print("Criterios de entrada válidos:")
    print(f"- Países permitidos: {', '.join(paises_validos)}")
    print(f"- Razones de entrada permitidas: {', '.join(razones_entrada_validas)}")
    print(f"- Documentos aceptables: {', '.join(documentos_validos)}")
    print("="*30 + "\n")

# Función para mostrar puntos acumulados durante el día
def mostrar_puntos_acumulados():
    print(f"\nPuntos acumulados: {estadisticas['puntos']}")

# Función principal del juego
def iniciar_juego():
    limpiar_consola()
    print("\n¡Iniciando el juego!\n")

    errores_consecutivos = 0  # Contador de errores consecutivos para disparar la noticia

    for dia in range(1, 4):  # Vamos a simular tres días de trabajo, como ejemplo
        print(f"\nDía {dia}")
        mostrar_criterios_validos()

        for turno in range(8):  # Cada día se procesarán 8 inmigrantes
            inmigrante = Inmigrante()
            print(f"\nInmigrante #{turno + 1}:")
            print(f"Nombre: {inmigrante.nombre}")
            print(f"País de origen: {inmigrante.pais_origen}")
            print(f"Razón de entrada: {inmigrante.razon}")
            print(f"Documento: {inmigrante.documento}")
            print(f"DNI: {inmigrante.dni}")

            # Mostrar puntos acumulados antes de cada decisión
            mostrar_puntos_acumulados()

            # Validación de entrada
            while True:
                try:
                    decision = input("¿Apruebas (s) o rechazas (n) la entrada? ")
                    if decision.lower() not in ["s", "n"]:
                        raise ValueError("Por favor, ingresa 's' para aprobar o 'n' para rechazar.")
                    
                    # Lógica para manejar la decisión y actualizar estadísticas
                    if decision.lower() == "s":
                        print("Decisión de aprobar.")
                        if inmigrante.pais_origen in paises_validos:
                            estadisticas["aprobaciones"] += 1
                            estadisticas["puntos"] += 10  # Sumar puntos por decisión correcta
                            print("¡Decisión correcta! Has ganado 10 puntos.")
                            if not logros["primera_aprobacion"]:
                                logros["primera_aprobacion"] = True
                                print("¡Has desbloqueado el logro 'Primera Aprobación'!")
                        else:
                            errores_consecutivos += 1
                            print("¡Decisión incorrecta! Has perdido 5 puntos.")
                            estadisticas["puntos"] -= 5
                            if not logros["aprobaciones_perfectas"]:
                                logros["aprobaciones_perfectas"] = True
                                print("¡Has desbloqueado el logro 'Aprobaciones Perfectas'!")
                    else:
                        print("Decisión de rechazar.")
                        if inmigrante.pais_origen not in paises_validos:
                            estadisticas["rechazos"] += 1
                            estadisticas["puntos"] += 10  # Sumar puntos por decisión correcta
                            print("¡Decisión correcta! Has ganado 10 puntos.")
                            if not logros["primer_rechazo"]:
                                logros["primer_rechazo"] = True
                                print("¡Has desbloqueado el logro 'Primer Rechazo'!")
                        else:
                            errores_consecutivos += 1
                            print("¡Decisión incorrecta! Has perdido 5 puntos.")
                            estadisticas["puntos"] -= 5
                            if not logros["negaciones_correctas"]:
                                logros["negaciones_correctas"] = True
                                print("¡Has desbloqueado el logro 'Negaciones Correctas'!")
                    
                    # Si hay 2 días consecutivos con más de 3 errores, mostramos la noticia
                    if errores_consecutivos > 3:
                        print("\n¡Noticia de último momento!")
                        print("Disturbios en el centro del país por la nueva ola de inmigrantes ilegales.")
                        errores_consecutivos = 0  # Reseteamos los errores
                    break
                except ValueError as e:
                    print(e)

            time.sleep(0.5)
            print("\n" + "-"*30)

        guardar_logros()
        guardar_estadisticas()

        # Preguntar si desean continuar al siguiente día o volver al menú principal
        while True:
            try:
                continuar = input("¿Deseas continuar al siguiente día o volver al menú principal? (c/m): ")
                if continuar.lower() not in ['c', 'm']:
                    raise ValueError("Debe ingresar 'c' o 'm'")
                if continuar.lower() == 'm':
                    return
                break
            except ValueError as e:
                print(e)

    print("\nJuego terminado.")
    input("\nPresiona Enter para volver al menú principal...")

# Menú principal
def menu_principal():
    limpiar_consola()
    print("\n" + "="*30)
    print("¡Bienvenido a 'Argentina, Papeles por favor'!")
    print("1. Iniciar Juego")
    print("2. Ver Reglas")
    print("3. Ver Estadísticas")
    print("4. Ver Logros")
    print("5. Ir a la Tienda")
    print("6. Salir")
    print("="*30)

# Otras funciones de menú
def mostrar_reglas():
    limpiar_consola()
    print("\n" + "="*30)
    print("Reglas del Juego:")
    print("1. Verifica que el inmigrante tenga un documento válido.")
    print("2. Asegúrate de que la razón de entrada sea válida.")
    print("3. Responde con 's' para aprobar y 'n' para rechazar.")
    print("4. Cada decisión correcta suma puntos.")
    print("="*30)
    input("\nPresiona Enter para volver al menú principal...")

def mostrar_estadisticas():
    limpiar_consola()
    print("\n" + "="*30)
    print("Estadísticas del Juego:")
    print(f"Aprobaciones correctas: {estadisticas['aprobaciones']}")
    print(f"Rechazos correctos: {estadisticas['rechazos']}")
    print(f"Puntos acumulados: {estadisticas['puntos']}")
    print("="*30)
    input("\nPresiona Enter para volver al menú principal...")

def mostrar_logros():
    limpiar_consola()
    print("\n" + "="*30)
    print("Logros Desbloqueados:")
    for logro, desbloqueado in logros.items():
        estado = "Desbloqueado" if desbloqueado else "Pendiente"
        print(f"{logro.replace('_', ' ').title()}: {estado}")
    print("="*30)
    input("\nPresiona Enter para volver al menú principal...")

def tienda():
    limpiar_consola()
    print("\n" + "="*30)
    print("Bienvenido a la Tienda:")
    print("1. Comprar puntos adicionales (100 puntos)")
    print("2. Desbloquear mejora 'Segunda Oportunidad' (200 puntos)")
    print("3. Volver al menú principal")
    print("="*30)

    try:
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            if estadisticas["puntos"] >= 100:
                print("Has comprado puntos adicionales.")
                estadisticas["puntos"] -= 100
            else:
                print("No tienes suficientes puntos.")
        elif opcion == "2":
            if estadisticas["puntos"] >= 200:
                print("¡Has desbloqueado la mejora 'Segunda oportunidad'!")
                logros['deshacer_decision'] = True
                guardar_logros()
            else:
                print("No tienes suficientes puntos.")
        elif opcion == "3":
            return
        else:
            print("Opción no válida.")
    except ValueError as e:
        print(e)

# Ejecutar el menú principal
while True:
    menu_principal()
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        iniciar_juego()
    elif opcion == "2":
        mostrar_reglas()
    elif opcion == "3":
        mostrar_estadisticas()
    elif opcion == "4":
        mostrar_logros()
    elif opcion == "5":
        tienda()
    elif opcion == "6":
        break
    else:
        print("Opción no válida.")
