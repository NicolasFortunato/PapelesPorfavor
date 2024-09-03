#Papeles Porfavor es la adaptacion criolla del famoso puzzle de simulacion Papers Please.
#En esta adaptacion nos encontraremos con cambios significativos para el juego tal y como nuevos nombres para
#los paises, provincias, ciudadanos, nuevos requisitos de acceso y mucho mas!
#MENU DE OPCIONES 

def mostrar_menu(tiempoRecord, ):
    print("Bienvenido a Papeles, Por Favor. \n")
    print("1. Iniciar juego")
    print("2. Opciones")
    print("3. Estadisticas")
    print("4. Salir al escritorio")

    eleccionMenu = int(input("Seleccione una opcion: "))
#Jugar
    if eleccionMenu == 1:
        print("1. Juego nuevo")
        print("2. Cargar juego")
        eleccionJuego = int(input("Seleccione una opcion: "))
        if eleccionJuego == 1:
            return eleccionJuego
#Cargar partida guardada
        else:
            partidaGuardada1 = print("1. Partida Guardada numero 1.")
            partidaGuardada2 = print("2. Partida Guardada numero 2.\n")
            eleccionPartidaGuardada = int(input("Seleccione una opcion: "))
            return eleccionPartidaGuardada
#Opciones
    else:
        if eleccionMenu == 2:
            print("1. Cantdad de inmigrantes \n")
            eleccionInmigrante = int(input("S8eleccione una opcion: "))
            if eleccionInmigrante == 1:
                print("1. 2 Inmigrantes.\n")
                print("2. 3 Inmigrantes")
        #Cantidad de inmigrantes
                eleccionInmigrante = int(input("Seleccione una opcion"))
                return eleccionInmigrante
#Estadisticas       
        else:
            if eleccionMenu == 3:
                print("ESTADISTICAS\n")
                print("Mayor timepo de juego: ",tiempoRecord)
                print("Inmigrantes deportados: ",iDeportados)
                print("Inmigrantes aceptados: ",iAceptados)
                print("Dias alcanzados: ",diasJugados)
                print("1. Salir")
                """Capaz conviene returnear y ya esta"""
                eleccionEstadisticas = int(input("Seleccione una opcion: "))
                if eleccionEstadisticas == 1:
                    return 
            else:
                print("Gracias por jugar Papeles, Por Favor.")
                
    return eleccionMenu

#CRONOMETRO (hay que importar TIME)

import time 
tiempoRecord = None


def menu_estadisticas(recordTime):
    tiempoInicial = time.time() #Arranca el cronometro
    print("Presiona Enter cuando termine el juego...")

    timepoFinal = time.time() #Se detiene el cronometro
    tiempoTotal = timepoFinal - tiempoInicial 

    print("Tiempo de juego: {tiempoTotal:.2f} segundos") #.2f se refiere a que hayan 2 digitos despues de la coma
    
    if recordTime is None or recordTime < recordTime:
        recordTime = tiempoTotal
        print("!Hay un nuevo record, y ese es: ",recordTime,"!")
    
    return recordTime
