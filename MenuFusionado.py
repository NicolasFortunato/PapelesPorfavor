def menuPrincipal():
        import time
        import random
        try:
            print("""█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
        ████████████████████████████████████████████████████████████████       █ █  ██  █████████  ███  ████  █████████████████████████████████████████████████████████████████ 
        ████████████████████████████████████████████████████████████████   █ ███ █  ██  █████████  ██   ████  █████████████████████████████████████████████████████████████████ 
        █████████████████████████████████████████████████████████████████  █   █    ██ ██  ██████  ███  █ █  ██████████████████████████████████████████████████████████████████ 
        █████████████████████████████████████████████████████████████████     ██ ██ █     ████████ ████ ███  ██████████████████████████████████████████████████████████████████ 
        █████████████████████████████████████████████          █████     █                                             █        ███████████████████████████████████████████████ 
        █████████████████████████████████████████████ ████████   ██ ████ █   ████████   █████████  ███       █████████   ███████  █████████████████████████████████████████████ 
        █████████████████████████████████████████████  ██    ███ █  ████  █  ██     ██  ███        ███     █ ███        ██     ██ █████████████████████████████████████████████ 
        █████████████████████████████████████████████  ██    ███ █ ██  ██  █ ██     ██  ████████ █ ███    ██ ████████   ████     ██████████████████████████████████████████████ 
        █████████████████████████████████████████████  ████████ █ ███   ██ █ █████████  ███        ███  ████ ███             ████ █████████████████████████████████████████████ 
        █████████████████████████████████████████████  ██      █  ████████   ██         ███      █ ██      █ ███        ██  █  ██ █████████████████████████████████████████████ 
        █████████████████████████████████████████████ ███ ██████ ██      ██  ██  █    █ █████████  █████████ █████████  █████████ █████████████████████████████████████████████ 
        █████████████████████████████████████████████     ████      ████         ████                                            ██████████████████████████████████████████████ 
        ██████████████████████████████████████           █   ████   █   █████       ██████  ██  ██  █  ██  ███ ██    █████  █ ██        ███████████████████████████████████████ 
        ██████████████████████████████████████ ███   ███   ██    ██   ██    ███   ██        █  ████ ██ ███ ██  ██  ███   ███  ███   ████ ██████████████████████████████████████ 
        ██████████████████████████████████████ ███ ██ ███ ██  ██  ██  ██ ███ ██   ██      ███ ██ ██  ██ ██    ██   ██ ██  ██  ███ ██  ██ ██████████████████████████████████████ 
        ██████████████████████████████████████ ███    ██  ██  ██  ██  ██    ███   ███████  █  ██  ██  █ ███  ██    ██ ██  ██  ███    ██  ██████████████████████████████████████ 
        ██████████████████████████████████████ ████████   ██  ██  ██  ██  ███  █  ██      █  ██   ███ ██ ███ ██ █  ██ ██  ██  ███  ██   ███████████████████████████████████████ 
        ██████████████████████████████████████ ███     ██  ██    ██   ██   ███    ██ ██████ █████████  █  ████  █  ██    ███  ███   ██  ███████████████████████████████████████ 
        ██████████████████████████████████████ ███ ███████  ██████  █ ██ ██  ██   ██ █████  █       ██  █  ███ ███   █████    ███ █  ███ ██████████████████████████████████████ 
        ███████████████████████████████████████    █████████      ███    ███    █    █████    █████    ███    ███████     ████   ████    ██████████████████████████████████████ 
        ███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████ 
        ███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████ 
        \n 1. Iniciar juego\n 2. Opciones\n 3. Estadisticas
        """)
            eleccionMenu = int(input("Seleccione una opcion: "))
            if eleccionMenu == 1:
                menuDos()
            elif eleccionMenu == 2:
                menuOpciones()
            elif eleccionMenu == 3:
                menuEstadisticas()

        except ValueError:
            print("Error en la eleccion")
            menuPrincipal()

def menuDos():
    try:    
        print("""
    █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    ██     █     ██      ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    ██  ███████████████  ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    ██  ████████████████ ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    ██████████   ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    ██  ██████   ██████  ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    ██  ███████  ██████  ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    █████████     ███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    ██  ███████████████  ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    ██  ███████████████  ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    ██      ██    ██     ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    ██       DIA 1       ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    ██    (PRESIONA 1)   ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    █████████████████████████████████████████████████████████████             PRESIONA -1 PARA VOLVER             ███████████████████████████████████████████████████████████
    █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    """)
        eleccionJuego = int(input("Seleccione una opcion: "))
        if eleccionJuego == 1:
            menuTres()
        elif eleccionJuego == -1:
            menuPrincipal()
    except ValueError:
        print("Error en la eleccion, por favor, ingresa una opcion valida.")
        menuDos()
def menuTres():
    try:            
        print("Felicidades! Conseguiste tu primer trabajo.\n  Presiona 1 para continuar.\n Presiona -1 para salir.")
        eleccionJuego = int(input("Seleccione una opcion: "))      
        if eleccionJuego == 1:
            juego()
        else:
            if eleccionJuego == -1:
                menuPrincipal()        
    except IOError:
        print("Error en la opcion elegida")
        menuTres()                

iAceptados = 0
iDeportados = 0

def generacion():
    import random
    import time 
    tiempoInicial = time.time() #Arranca el cronometro
    
    try:
        
        puntaje = 0
        nombres = ["Juan", "Pablo", "Diego", "Gabriel", "Luis", "Ricardo", "Javier", "Martín", "Andrés", "Francisco", "Alejandro", "Manuel", "Nicolás", "Daniel", "Sergio", "Federico", "Carlos", "Mario", "Guillermo", "Enrique", "Ana", "María", "Laura", "Carolina", "Gabriela", "Patricia", "Cecilia", "Marta", "Lucía", "Natalia", "Paula", "Beatriz", "Mariana", "Juliana", "Andrea", "Alejandra", "Verónica", "Claudia", "Sonia", "Elena"]
        apellidos = ["Gómez", "Rodríguez", "Fernández", "González", "Messi", "Pérez", "Martínez", "García", "Silva", "Romero", "Morales", "López", "Fernández", "Bianchi", "Ferrari", "Costa", "Lombardi", "Russo", "Moretti", "Gallo", "Alfieri", "Mancini", "Santoro", "Ricci", "Tognini", "Mazzola", "Romano", "Barone", "Giordano", "Salvi", "Pugliese", "Benedetti", "Colombo", "Ferrari", "Vitale", "Russo", "Marchese", "Eichman", "Karas", "Fortunato" ]
        paises_validos = ['Argentina', 'Perú', 'Brasil', 'Chile']
        dni = [random.randint(1000000,9999999) for i in range(10)] #Lista por compresion 
        paises_no_validos = ['Estados Unidos', 'España', 'Japón', 'Taiwán']
        paises = paises_validos + paises_no_validos 
        
        Personas = open("PersonasArchivo.csv","wt")
        Personas.write(f"(str{nombres}:{apellidos}:{dni}")
        PaisesArchivo = open("Paisesarchivo.csv","wt")
        PaisesArchivo.write(f"(str{paises}")
           
    except FileNotFoundError:
        print("El archivo no se pudo crear correctamente")
    finally:
	    Personas.close()
def juego(paises_validos, nombres, apellidos, paises, dni, puntaje):
    import random
    import time
    global diasJugados

    for i in range(8):

        datos = {
            'nombre': random.choice(nombres), #Transformar todo en lista desde el archivo
            'apellido': random.choice(apellidos),
            'edad': random.randint(1, 100),
            'pais': random.choice(paises),
            'dni' : random.choice(dni),
                }
        print(f"""
    ███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    ███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████ 
    █████████████████████████████████████████████ ████████   ██ ████ █   ████████   █████████  ███       █████████   ███████  █████████████████████████████████████████████ 
    █████████████████████████████████████████████  ██    ███ █  ████  █  ██     ██  ███        ███     █ ███        ██     ██ █████████████████████████████████████████████ 
    █████████████████████████████████████████████  ██    ███ █ ██  ██  █ ██     ██  ████████ █ ███    ██ ████████   ████     ██████████████████████████████████████████████ 
    █████████████████████████████████████████████  ████████ █ ███   ██ █ █████████  ███        ███  ████ ███             ████ █████████████████████████████████████████████ 
    █████████████████████████████████████████████  ██      █  ████████   ██         ███      █ ██      █ ███        ██  █  ██ █████████████████████████████████████████████ 
    █████████████████████████████████████████████ ███ ██████ ██      ██  ██  █    █ █████████  █████████ █████████  █████████ █████████████████████████████████████████████ 
    █████████████████████████████████████████████     ████      ████         ████                                            ██████████████████████████████████████████████ 
    ██████████████████████████████████████           █   ████   █   █████       ██████  ██  ██  █  ██  ███ ██    █████  █ ██        ███████████████████████████████████████ 
    ██████████████████████████████████████ ███   ███   ██    ██   ██    ███   ██        █  ████ ██ ███ ██  ██  ███   ███  ███   ████ ██████████████████████████████████████ 
    ██████████████████████████████████████ ███ ██ ███ ██  ██  ██  ██ ███ ██   ██      ███ ██ ██  ██ ██    ██   ██ ██  ██  ███ ██  ██ ██████████████████████████████████████ 
    ██████████████████████████████████████ ███    ██  ██  ██  ██  ██    ███   ███████  █  ██  ██  █ ███  ██    ██ ██  ██  ███    ██  ██████████████████████████████████████ 
    ██████████████████████████████████████ ████████   ██  ██  ██  ██  ███  █  ██      █  ██   ███ ██ ███ ██ █  ██ ██  ██  ███  ██   ███████████████████████████████████████ 
    ██████████████████████████████████████ ███     ██  ██    ██   ██   ███    ██ ██████ █████████  █  ████  █  ██    ███  ███   ██  ███████████████████████████████████████ 
    ██████████████████████████████████████ ███ ███████  ██████  █ ██ ██  ██   ██ █████  █       ██  █  ███ ███   █████    ███ █  ███ ██████████████████████████████████████ 
    ███████████████████████████████████████    █████████      ███    ███    █    █████    █████    ███    ███████     ████   ████    ██████████████████████████████████████ 
    ███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    ███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    ███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    """)
    print(f"Los paises validos para el dia de la fecha son:\n {paises_validos}.\n Recuerda que cualquier desicion mal tomada va a perjudicarte.")
    
    print(f"PASAPORTE NACIONAL\n Nombre: {datos['nombre']}\n Apellido: {datos['apellido']}\n Edad: {datos['edad']}\n Nacionalidad: {datos['pais']}\n DNI: {datos['dni']}\n Puntaje actual: {puntaje}")

    if datos['edad'] < 18:
        valido = False
    elif datos['pais'] not in paises_validos:
        valido = False
            
    else: valido = True
    validacion()
    # print(valido)
def validacion(valido, puntaje):
    try:
        opcion = int(input('Elige una opción: '))
        if (valido and opcion == 1) or (not valido and opcion == 2):
            puntaje += 1
            print("Correcto, has ganado un punto.")
        else:
            puntaje -= 1
            print("Incorrecto, has perdido un punto.")
    except ValueError:
        print('Opción elegida no válida, por favor, elige una opción correcta.')
    
    # Asegúrate de que estas funciones estén definidas en el código principal
    cont_Inmigrantes_Decision(opcion)
    diaFinalizado()

    return puntaje

def diaFinalizado(puntaje ):
    import time 
    print(f"!Dia finalizado!\n Tu puntaje es: {puntaje}\n Inmigrantes aceptados {iAceptados} y deportados:{iDeportados}\n")
    tiempoTotal = (lambda tiempoInicial: time.time() - tiempoInicial)
    recordTime = None
    if recordTime is None or recordTime < tiempoTotal:
        recordTime = tiempoTotal
    print(f"Tiempo de juego: {tiempoTotal:.2f} segundos\n !felicidades! Conseguiste un nuevo record: {tiempoTotal:.2f} segundos\n 1. Siguiente dia\n 2. Menu principal")
    diasJugados()
    eleccionJuego = int(input("Ingrese una opcion para continuar: "))

    if eleccionJuego == 1:
        juego()
    elif eleccionJuego == 2:
        menuPrincipal()


def cont_Inmigrantes_Decision(opcion):
    global iAceptados, iDeportados  # Usamos las variables globales para no perder su valor
    if opcion == "aceptado":
        iAceptados += 1
        print(f'Inmigrantes aceptados: {iAceptados}')
    elif opcion == "rechazado":
        iDeportados += 1
        print(f'Inmigrantes deportados: {iDeportados}')

def menuEstadisticas(recordTime, diasjugados, iDeportados, iAceptados): #Menu de estadisticas del menu principal, trayendo los parametros como globales para que la funcion estadisticas los pueda leer
    print(f"Mayor tiempo de juego: {recordTime}. \n Inmigrantes deportados: {iDeportados}. \n Inmigrantes aceptados: {iAceptados}. \n Dias alcanzados: {diasjugados}. \n PRESIONA 1 SALIR.")
    eleccionEstadisticas = int(input("Seleccione una opcion: "))
    if eleccionEstadisticas == 1:
        menuPrincipal()
        
def menuOpciones():
    print("1. Cambiar dificultad (Cantdad de Paises). \n")
    print("2. Salir. \n")
    eleccionInmigrante = int(input("Seleccione una opcion: "))
    if eleccionInmigrante == 1:
        print("1. Facil: 4 paises.\n")
        print("2. Normal: 5 paises.\n")
        print("3. Volver. \n")
#Cantidad de inmigrantes
        eleccionInmigrante = int(input("Seleccione una opcion: "))
        if eleccionInmigrante == 3:
                return 
        return eleccionInmigrante  

#Sistema de logros
def logros():
    logros = [
    {"name": "Primer Paso", "description": "Completa el primer día con éxito.", "condition": lambda score, streak: score > 0},
    {"name": "Racha de Experto", "description": "Alcanza una racha de 5 decisiones correctas consecutivas.", "condition": lambda score, streak: streak >= 5},
    {"name": "Novato", "description": "Acumula 10 puntos en total.", "condition": lambda score, streak: score >= 10},
    {"name": "Profesional", "description": "Acumula 50 puntos en total.", "condition": lambda score, streak: score >= 50},
    {"name": "Perfecto", "description": "Completa un día sin errores.", "condition": lambda score, streak, errors: errors == 0},
    ]
    logros_desbloqueados = {logros["name"]: False for logros in logros}

def check_achievements(score, streak, errors, logros, logros_desbloqueados):
    for achievement in logros:
        if not logros_desbloqueados[achievement["name"]] and achievement["condition"](score, streak, errors):
            logros_desbloqueados[achievement["name"]] = True
            print(f"¡Logro desbloqueado: {achievement['name']}! - {achievement['description']}")

def mostrar_logros(logros_desbloqueados, logros):
    print("Logros:")
    for achievement in logros:
        estado = "Desbloqueado" if logros_desbloqueados[achievement["name"]] else "Pendiente"
        print(f"{achievement['name']}: {estado} - {achievement['description']}")

def archivo_de_logros():
    import json

    # Guardar logros
    with open("logros.json", "w") as file:
        json.dump(unlocked_achievements, file)

    # Cargar logros
    with open("logros.json", "r") as file:
        unlocked_achievements = json.load(file)

            




diasjugados = 0 
def diasJugados(diasjugados):
        diasjugados += 1
        print(diasjugados)
            
def main():
    menuPrincipal()
    menuDos()
    menuTres()
    menuOpciones()
    menuEstadisticas()
    juego()
    generacion()
    validacion()
    cont_Inmigrantes_Decision()
    diasJugados()
    diaFinalizado()
    


    

main()


