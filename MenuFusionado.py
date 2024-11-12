import os
import json
import random
import time

# Función para limpiar consola
def limpiar_consola():
    """
    Limpia la consola en función del sistema operativo.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

# Datos base y configuraciones
paises_validos = ["Argentina", "Chile", "Uruguay", "Bolivia", "Paraguay", "Brasil"]
paises_invalidos = ["Peru", "Ecuador", "Venezuela", "Colombia", "Guyana"]

razones_entrada_validas = ["Turismo", "Trabajo", "Estudio", "Residencia"]
razones_entrada_invalidas = ["Negocios", "Visita médica", "Evento Deportivo"]

documentos_validos = ["DNI", "Pasaporte", "Permiso de Trabajo"]
documentos_invalidos = ["Carnet de Estudiante", "ID Nacional", "Permiso Temporal"]

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

def guardar_logros():
    """Guarda los logros en un archivo JSON."""
    with open("logros.json", "w") as f:
        json.dump(logros, f, indent=4)

def guardar_estadisticas():
    """Guarda las estadísticas en un archivo JSON."""
    with open("estadisticas.json", "w") as f:
        json.dump(estadisticas, f, indent=4)

# Clase Inmigrante
class Inmigrante:
    def __init__(self):
        """Inicializa un inmigrante con atributos aleatorios."""
        self.nombre = random.choice(["Juan", "Maria", "Carlos", "Ana", "Pedro", "Lucia"])
        self.pais_origen = random.choice(paises_validos + paises_invalidos)
        self.razon = random.choice(razones_entrada_validas + razones_entrada_invalidas)
        self.documento = random.choice(documentos_validos + documentos_invalidos)
        self.dni = "".join([str(random.randint(0, 9)) for _ in range(8)])

def mostrar_criterios_validos():
    """Muestra los criterios válidos de entrada en la consola."""
    limpiar_consola()
    print("\n" + "="*30)
    print("Criterios de entrada válidos:")
    print(f"- Países: {paises_validos}")
    print(f"- Razones de entrada: {razones_entrada_validas}")
    print(f"- Documentos válidos: {documentos_validos}")
    print("="*30)

def calcular_puntaje(datos_juego):
    """
    Calcula el puntaje del jugador basado en criterios específicos.

    Parámetros:
    datos_juego (dict): Datos relacionados con el juego actual.

    Retorna:
    int: Puntaje calculado basado en datos del juego.
    """
    puntaje = 0
    # Implementa lógica específica para calcular puntaje.
    return puntaje

def imprimir_datos_jugador(datos):
    """
    Imprime los datos del jugador.

    Parámetros:
    datos (dict): Información del jugador.
    """
    print('Puntaje actual:', datos.get("puntaje", 0))
    print('------------------------------')
    print('Nombre:', datos['nombre'])
    print('Apellido:', datos['apellido'])
    print('Edad:', datos['edad'])
    print('Nacionalidad:', datos['pais'])
    print('DNI:', datos['dni'])
    print('------------------------------')

# Manejo de excepciones en entradas
def obtener_input_int(mensaje):
    """Solicita un entero al usuario y maneja excepciones en caso de error."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Función  de recursividad
def contar_regresivo(numero):
    """
    Realiza una cuenta regresiva recursiva desde el número dado.

    Parámetros:
    numero (int): Número desde el cual iniciar la cuenta regresiva.
    """
    if numero <= 0:
        print("¡Cuenta regresiva completa!")
    else:
        print(numero)
        contar_regresivo(numero - 1)