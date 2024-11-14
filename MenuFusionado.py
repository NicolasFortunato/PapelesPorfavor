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

logros = {
    "aprobaciones_perfectas": False,
    "negaciones_correctas": False,
    "primera_aprobacion": False,
    "primer_rechazo": False,
    "deshacer_decision": False,
    "decisiones_extra_puntos": False
}

estadisticas = {
    "aprobaciones": 0,
    "rechazos": 0,
    "puntos": 0
}

# Variables de control para habilidades adquiridas
deshacer_disponible = 0  # Para controlar el uso de deshacer decisión
puntos_extra = False     # Indica si la habilidad de puntos extra está activa

# Funciones para guardar y cargar logros y estadísticas
def guardar_logros():
    with open("logros.json", "w") as f:
        json.dump(logros, f, indent=4)

def guardar_estadisticas():
    with open("estadisticas.json", "w") as f:
        json.dump(estadisticas, f, indent=4)

def cargar_logros():
    try:
        with open("logros.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return logros

def cargar_estadisticas():
    try:
        with open("estadisticas.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return estadisticas

# Clase Inmigrante
class Inmigrante:
    def __init__(self):
        self.nombre = random.choice(["Juan", "Maria", "Carlos", "Ana", "Pedro", "Lucia"])
        # Generar país, razón y documento de manera aleatoria
        self.pais_origen = random.choice(paises_validos + ["Peru", "Ecuador", "Venezuela", "Colombia", "Guyana"])
        self.razon = random.choice(razones_entrada_validas + ["Negocios", "Visita médica", "Evento Deportivo"])
        self.documento = random.choice(documentos_validos + ["Carnet de Estudiante", "ID Nacional", "Permiso Temporal"])
        self.dni = "".join([str(random.randint(0, 9)) for _ in range(8)])

    def es_valido(self):
        # Verifica que el inmigrante cumpla todos los criterios válidos
        return (self.pais_origen in paises_validos and
                self.razon in razones_entrada_validas and
                self.documento in documentos_validos)

def mostrar_criterios_validos():
    limpiar_consola()
    print("\n" + "="*30)
    print("Criterios de entrada válidos:")
    print(f"- Países permitidos: {', '.join(paises_validos)}")
    print(f"- Razones de entrada permitidas: {', '.join(razones_entrada_validas)}")
    print(f"- Documentos aceptables: {', '.join(documentos_validos)}")
    print("="*30 + "\n")

# Función para mostrar el estado de las habilidades
def mostrar_habilidades():
    print(f"\nHabilidades Compradas y Activadas:")
    print(f"- Deshacer decisión: {'Comprada' if logros['deshacer_decision'] else 'No comprada'}, {'Activa' if deshacer_disponible > 0 else 'No activa'}")
    print(f"- Decisiones extra puntos: {'Comprada' if logros['decisiones_extra_puntos'] else 'No comprada'}, {'Activa' if puntos_extra else 'No activa'}")
    print("="*30)

# Función principal del juego
def iniciar_juego():
    global deshacer_disponible, puntos_extra

    limpiar_consola()
    print("\n¡Iniciando el juego!\n")
    
    dias_con_errores = 0

    for dia in range(1, 4):
        print(f"\nDía {dia}")
        mostrar_criterios_validos()
        mostrar_habilidades()  # Mostrar habilidades antes de cada día
        
        errores_dia = 0

        for turno in range(8):
            inmigrante = Inmigrante()
            print(f"\nInmigrante #{turno + 1}:")
            print(f"Nombre: {inmigrante.nombre}")
            print(f"País de origen: {inmigrante.pais_origen}")
            print(f"Razón de entrada: {inmigrante.razon}")
            print(f"Documento: {inmigrante.documento}")
            print(f"DNI: {inmigrante.dni}")
            print(f"Puntos actuales: {estadisticas['puntos']}")

            # Verificar si la entrada es válida
            decision_correcta = inmigrante.es_valido()
            
            while True:
                decision = input("¿Apruebas (s) o rechazas (n) la entrada? ")
                if decision.lower() not in ["s", "n"]:
                    print("Por favor, ingresa 's' para aprobar o 'n' para rechazar.")
                    continue

                # Determinar puntos y tipo de decisión
                puntos_obtenidos = 10 if (decision.lower() == "s" and decision_correcta) or \
                                          (decision.lower() == "n" and not decision_correcta) else -5

                if puntos_extra:
                    puntos_obtenidos += 5

                estadisticas["puntos"] += puntos_obtenidos
                if decision_correcta and decision.lower() == "s":
                    estadisticas["aprobaciones"] += 1
                elif not decision_correcta and decision.lower() == "n":
                    estadisticas["rechazos"] += 1
                else:
                    errores_dia += 1

                # Verificar si hay un error en la decisión y si el jugador puede deshacer
                if not decision_correcta and decision.lower() == "s":
                    print("Decisión incorrecta.")
                    if logros["deshacer_decision"] and deshacer_disponible > 0:
                        deshacer = input("¿Quieres deshacer la última decisión incorrecta? (s/n): ")
                        if deshacer.lower() == "s":
                            estadisticas["puntos"] -= puntos_obtenidos  # Revertir los puntos
                            deshacer_disponible -= 1
                            print("Has deshecho la última decisión. Vuelve a tomar una decisión.")
                            continue  # Permite repetir la decisión para el mismo inmigrante
                else:
                    print("¡Decisión correcta!" if decision_correcta else "Decisión incorrecta.")

                break

            time.sleep(0.5)
            print("\n" + "-"*30)

        guardar_logros()
        guardar_estadisticas()

        if errores_dia >= 3:
            dias_con_errores += 1
        else:
            dias_con_errores = 0
        
        if dias_con_errores >= 2:
            print("Noticia: Disturbios en el centro del país debido a una nueva ola de inmigrantes ilegales.")
        
        while True:
            continuar = input("¿Deseas continuar al siguiente día o volver al menú principal? (c/m): ")
            if continuar.lower() == 'm':
                return
            elif continuar.lower() == 'c':
                break
            else:
                print("Debe ingresar 'c' o 'm'.")

    print("\nJuego terminado.")
    input("\nPresiona Enter para volver al menú principal...")

# Funciones de menú y otras opciones
def menu_principal():
    limpiar_consola()
    print("\n" + "="*30)
    print("¡Bienvenido a 'Fronteras Argentinas'!")
    print("1. Iniciar Juego")
    print("2. Ver Reglas")
    print("3. Ver Estadísticas")
    print("4. Ver Logros")
    print("5. Ir a la Tienda")
    print("6. Salir")
    print("="*30)

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
    print("Logros alcanzados:")
    for logro, estado in logros.items():
        print(f"{logro}: {'Alcanzado' if estado else 'No alcanzado'}")
    print("="*30)
    input("\nPresiona Enter para volver al menú principal...")

def tienda():
    global deshacer_disponible, puntos_extra
    limpiar_consola()
    print("\n" + "="*30)
    print("Tienda")
    print(f"Puntos actuales: {estadisticas['puntos']}")
    print("1. Comprar deshacer decisión (100 puntos)")
    print("2. Comprar puntos extra en decisiones (150 puntos)")
    print("="*30)

    while True:
        opcion = input("¿Qué deseas comprar? (1/2) o (s) para salir: ")
        if opcion == '1' and estadisticas["puntos"] >= 100:
            logros["deshacer_decision"] = True
            deshacer_disponible += 1
            estadisticas["puntos"] -= 100
            print("¡Has comprado la opción de deshacer decisión!")
        elif opcion == '2' and estadisticas["puntos"] >= 150:
            logros["decisiones_extra_puntos"] = True
            puntos_extra = True
            estadisticas["puntos"] -= 150
            print("¡Has comprado puntos extra en decisiones!")
        elif opcion == 's':
            break
        else:
            print("Opción no válida o puntos insuficientes.")
        
        guardar_logros()
        guardar_estadisticas()
        break

    input("\nPresiona Enter para volver al menú principal...")

# Loop principal
def main():
    global logros, estadisticas
    logros = cargar_logros()
    estadisticas = cargar_estadisticas()
    
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
            print("¡Gracias por jugar!")
            break
        else:
            print("Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
