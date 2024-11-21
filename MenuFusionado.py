import os
import json
import random

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
def mostrar_datos_validos():
    print("\n" + "="*30)
    print("Datos válidos para la jornada:")
    print(f"- Países válidos: {', '.join(paises_validos)}")
    print(f"- Documentos válidos: {', '.join(documentos_validos)}")
    print(f"- Motivos válidos: {', '.join(razones_entrada_validas)}")
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
def tomar_decision(inmigrante, turno):
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
        return 1 if puntos < 0 else 0

# Función para iniciar el juego
def iniciar_juego():
    limpiar_consola()
    print("¡Iniciando el juego!")
    for dia in range(10):  # Hasta 10 días
        limpiar_consola()
        print(f"\nDía {dia + 1}")
        mostrar_habilidades()
        mostrar_datos_validos()
        errores_dia = 0

        for turno in range(8):  # 8 inmigrantes por día
            inmigrante = Inmigrante()
            errores_dia += tomar_decision(inmigrante, turno)

        if errores_dia >= 3:
            print("\nNoticia: Disturbios en la ciudad debido a inmigrantes ilegales.")

        guardar_datos("logros.json", logros)
        guardar_datos("estadisticas.json", estadisticas)
        guardar_datos("habilidades.json", habilidades)

        continuar = input("¿Quieres continuar con el siguiente día (s/n)? ").lower()
        if continuar != "s":
            break

# Función de la tienda
def tienda():
    limpiar_consola()
    print("Bienvenido a la Tienda. Puedes comprar habilidades con tus puntos.")
    print(f"1. Deshacer decisión (50 puntos): {habilidades['deshacer_disponible']} usos disponibles")
    print(f"2. Puntos extra (100 puntos): {'Activado' if habilidades['puntos_extra'] else 'No activado'}")
    print(f"3. Salir de la Tienda")
    print(f"Puntos disponibles: {estadisticas['puntos']}")
    while True:
        opcion = input("Selecciona una opción: ")
        if opcion == "1" and estadisticas["puntos"] >= 50:
            habilidades["deshacer_disponible"] += 1
            estadisticas["puntos"] -= 50
            print("Has comprado un uso de 'Deshacer decisión'.")
        elif opcion == "2" and estadisticas["puntos"] >= 100:
            habilidades["puntos_extra"] = True
            estadisticas["puntos"] -= 100
            print("Has activado 'Puntos extra'.")
        elif opcion == "3":
            break
        else:
            print("Opción no válida o puntos insuficientes.")
    guardar_datos("habilidades.json", habilidades)
    guardar_datos("estadisticas.json", estadisticas)

# Menú principal
def menu_principal():
    while True:
        limpiar_consola()
        print("\n" + "="*30)
        print("Menú Principal")
        print("1. Iniciar juego")
        print("2. Mostrar logros")
        print("3. Mostrar estadísticas")
        print("4. Tienda")
        print("5. Salir")
        print("="*30)
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            iniciar_juego()
        elif opcion == "2":
            mostrar_logros()
        elif opcion == "3":
            mostrar_estadisticas()
        elif opcion == "4":
            tienda()
        elif opcion == "5":
            break

# Función principal
def main():
    menu_principal()

# Ejecución
if __name__ == "__main__":
    main()

