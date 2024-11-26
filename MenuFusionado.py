import os
import json
import random
import time

# Función para limpiar consola
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

# Datos base y configuraciones
paises_validos = ["Argentina", "Chile", "Uruguay", "Bolivia", "Paraguay", "Brasil"]
razones_entrada_validas = ["Turismo", "Trabajo", "Estudio", "Residencia"]
documentos_validos = ["DNI", "Pasaporte", "Permiso de Trabajo"]

# Función para cargar datos JSON
def cargar_datos(nombre_archivo, datos_por_defecto):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r") as archivo:
            return json.load(archivo)
    return datos_por_defecto

# Datos iniciales
logros = cargar_datos("logros.json", {
    "aprobaciones_perfectas": False,
    "negaciones_correctas": False,
    "primera_aprobacion": False,
    "primer_rechazo": False,
    "deshacer_decision": False
})

estadisticas = cargar_datos("estadisticas.json", {
    "aprobaciones": 0,
    "rechazos": 0,
    "puntos": 0
})

habilidades = cargar_datos("habilidades.json", {
    "deshacer_disponible": 0,
    "puntos_extra": False
})

# Función para guardar datos JSON
def guardar_datos(nombre_archivo, datos):
    with open(nombre_archivo, "w") as archivo:
        json.dump(datos, archivo, indent=4)

# Clase Inmigrante
class Inmigrante:
    def __init__(self):
        self.nombre = random.choice(["Juan", "Maria", "Carlos", "Ana", "Pedro", "Lucia"])
        self.pais_origen = random.choice(paises_validos + ["Peru", "Ecuador", "Venezuela", "Colombia"])
        self.razon = random.choice(razones_entrada_validas + ["Negocios", "Visita médica"])
        self.documento = random.choice(documentos_validos + ["Carnet de Estudiante", "Permiso Temporal"])
        self.dni = "".join([str(random.randint(0, 9)) for _ in range(8)])

    def es_valido(self):
        return (self.pais_origen in paises_validos and
                self.razon in razones_entrada_validas and
                self.documento in documentos_validos)

# Funciones para mostrar datos válidos y habilidades
def mostrar_datos_validos(paises_validos_dia, razones_validas_dia, documentos_validos_dia):
    print("\n" + "="*30)
    print("Condiciones para la jornada:")
    print(f"- Países válidos: {', '.join(paises_validos_dia)}")
    print(f"- Documentos válidos: {', '.join(documentos_validos_dia)}")
    print(f"- Motivos válidos: {', '.join(razones_validas_dia)}")
    print("="*30)

def mostrar_habilidades():
    print("\nHabilidades compradas:")
    if habilidades["deshacer_disponible"] > 0:
        print(f"- 'Deshacer decisión': Disponible ({habilidades['deshacer_disponible']} usos restantes)")
    if habilidades["puntos_extra"]:
        print("- 'Puntos extra': Activado")
    print("="*30)

# Función para mostrar logros
def mostrar_logros():
    limpiar_consola()
    print("\n" + "="*30)
    print("Logros Desbloqueados:")
    for logro, desbloqueado in logros.items():
        estado = "Desbloqueado" if desbloqueado else "Bloqueado"
        print(f"- {logro.replace('_', ' ').capitalize()}: {estado}")
    print("="*30)
    input("\nPresiona Enter para volver al menú principal.")

# Función para mostrar estadísticas
def mostrar_estadisticas():
    limpiar_consola()
    print("\n" + "="*30)
    print("Estadísticas del Juego:")
    print(f"- Aprobaciones correctas: {estadisticas['aprobaciones']}")
    print(f"- Rechazos correctos: {estadisticas['rechazos']}")
    print(f"- Puntos actuales: {estadisticas['puntos']}")
    print("="*30)
    input("\nPresiona Enter para volver al menú principal.")

# Función para tomar decisiones
def tomar_decision(inmigrante, turno, paises_validos_dia, razones_validas_dia, documentos_validos_dia):
    print(f"\nInmigrante #{turno + 1}:")
    print(f"Nombre: {inmigrante.nombre}")
    print(f"País de origen: {inmigrante.pais_origen}")
    print(f"Razón de entrada: {inmigrante.razon}")
    print(f"Documento: {inmigrante.documento}")
    print(f"DNI: {inmigrante.dni}")
    print(f"Puntos actuales: {estadisticas['puntos']}")

    decision_correcta = inmigrante.es_valido()
    while True:
        decision = input("¿Aprobar (s) o rechazar (n)? ").lower()
        if decision not in ["s", "n"]:
            print("Por favor, ingresa 's' o 'n'.")
            continue

        puntos = 10 if (decision == "s" and decision_correcta) or (decision == "n" and not decision_correcta) else -5
        if habilidades["puntos_extra"]:
            puntos += 5
        estadisticas["puntos"] += puntos

        if puntos > 0:
            print("¡Decisión correcta!")
            if decision == "s":
                estadisticas["aprobaciones"] += 1
            else:
                estadisticas["rechazos"] += 1
        else:
            print("¡Decisión incorrecta!")
            if habilidades["deshacer_disponible"] > 0:
                deshacer = input("¿Quieres deshacer esta decisión? (s/n): ").lower()
                if deshacer == "s":
                    habilidades["deshacer_disponible"] -= 1
                    estadisticas["puntos"] -= puntos
                    print("Decisión deshecha. Hazla de nuevo.")
                    continue
        break

# Función para iniciar el juego
def iniciar_juego():
    global dificultad
    limpiar_consola()
    print("¡Iniciando el juego!")

    # Selección aleatoria de las condiciones del día
    paises_validos_dia = random.sample(paises_validos, min(4, len(paises_validos)))
    razones_validas_dia = random.sample(razones_entrada_validas, min(4, len(razones_entrada_validas)))
    documentos_validos_dia = random.sample(documentos_validos, min(4, len(documentos_validos)))

    mostrar_datos_validos(paises_validos_dia, razones_validas_dia, documentos_validos_dia)
    mostrar_habilidades()

    # Ajuste de tiempo según dificultad
    tiempo_restante = 0
    if dificultad == 2:
        tiempo_restante = 30  # 30 segundos para dificultad media
    elif dificultad == 3:
        tiempo_restante = 45  # 45 segundos para dificultad difícil
    else:
        tiempo_restante = float('inf')  # Sin tiempo en dificultad fácil

    for dia in range(10):  # Hasta 10 días
        if dificultad > 1:  # Si hay límite de tiempo
            for t in range(tiempo_restante, 0, -1):
                print(f"\nTiempo restante para este día: {t} segundos", end="\r")
                time.sleep(1)
            print("\nSe acabó el tiempo para este día.")

        errores_dia = 0
        for turno in range(8):  # 8 inmigrantes por día
            inmigrante = Inmigrante()
            tomar_decision(inmigrante, turno, paises_validos_dia, razones_validas_dia, documentos_validos_dia)

        # Fin del día, no hay que preguntar si continuar
        decision = input("¿Quieres jugar el proximo dia (s) o volver al menu (n)? ").lower()
        if decision not in ["s", "n"]:
            print("Por favor, ingresa 's' o 'n'.")
        if decision == "s":
            iniciar_juego()
        else:
            menu_principal()
        print("\nEl día ha terminado.")
        time.sleep(1)

# Función Tienda
def tienda():
    print("Bienvenido a la tienda!")
    while True:
        print("\nOpciones disponibles:")
        print("1. Comprar habilidad: Deshacer Decisión (20 puntos)")
        print("2. Comprar habilidad: Puntos Extra (50 puntos)")
        print("3. Volver al menú principal")
        
        opcion = input("Selecciona una opción: ")
        if opcion == "1" and estadisticas["puntos"] >= 20:
            habilidades["deshacer_disponible"] += 1
            estadisticas["puntos"] -= 20
            print("Habilidad 'Deshacer Decisión' comprada.")
        elif opcion == "2" and estadisticas["puntos"] >= 50:
            habilidades["puntos_extra"] = True
            estadisticas["puntos"] -= 50
            print("Habilidad 'Puntos Extra' activada.")
        elif opcion == "3":
            break
        else:
            print("No tienes suficientes puntos o la opción es incorrecta.")

# Menú principal
def menu_principal():
    global dificultad
    while True:
        limpiar_consola()
        print("Menú Principal")
        print("1. Iniciar juego")
        print("2. Ver logros")
        print("3. Ver estadísticas")
        print("4. Ir a la tienda")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            dificultad = int(input("Selecciona dificultad (1 = Fácil, 2 = Media, 3 = Difícil): "))
            iniciar_juego()
        elif opcion == "2":
            mostrar_logros()
        elif opcion == "3":
            mostrar_estadisticas()
        elif opcion == "4":
            tienda()
        elif opcion == "5":
            print("Gracias por jugar!")
            break

# Ejecutar el menú principal
menu_principal()
