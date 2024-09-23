import random

nombres = ['Blanca', 'José', 'Luisa', 'Mario']
apellidos = ['Martínez', 'Romero', 'Perez', 'Alonso']
paises_validos = ['Argentina', 'Perú', 'Brasil', 'Chile']
paises_no_validos = ['Estados Unidos', 'España', 'Japón', 'Taiwán']
paises = paises_validos + paises_no_validos


def generar_documento(): # Genera un documento totalmente al azar a partir de los datos cargados
    datos = {
        'nombre': random.choice(nombres),
        'apellido': random.choice(apellidos),
        'edad': random.randint(1, 100),
        'pais': random.choice(paises),
        'dni': random.randint(1000000, 99999999),
    }
    return datos


def validar_documento(datos): # Recibe un documento generado al azar y devuelve True si es válido y False si no lo es
    if datos['edad'] < 18:
        return False
    if datos['pais'] not in paises_validos:
        return False
    
    return True


def iniciar_juego():

    
    puntaje = 0

    for i in range(8):

        datos = generar_documento()
        print('Puntaje actual:', puntaje)
        print('------------------------------')
        print('Nombre:', datos['nombre'])
        print('Apellido:', datos['apellido'])
        print('Edad:', datos['edad'])
        print('Nacionalidad:', datos['pais'])
        print('DNI:', datos['dni'])
        print('------------------------------')

        valido = validar_documento(datos)
        # print(valido)

        print('1. Aceptar')
        print('2. Denegar')
        opcion = int(input('Elige una opción: '))

        if valido == True and opcion == 1:
            puntaje += 1
            print('Ganaste 1 punto')

        elif valido == True and opcion == 2:
            puntaje -= 1
            print('Perdiste 1 punto')

        elif valido == False and opcion == 1:
            puntaje -= 1
            print('Perdiste 1 punto')

        elif valido == False and opcion == 2:
            puntaje += 1
            print('Ganaste 1 punto')

        else:
            print('Opción elegida no válida')
            print('Perdiste 1 punto')
            # Pierde puntos
        
        print()

    print('Partida finalizada')
    print('Puntaje final:', puntaje)