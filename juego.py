import random

nombres = ['Blanca', 'José', 'Luisa', 'Mario']
paises_validos = ['Argentina', 'Perú', 'Brasil', 'Chile']
paises = paises_validos + ['Estados Unidos', 'España', 'Japón']


def generar_documento(): # Genera un documento totalmente al azar a partir de los datos cargados
    datos = []
    datos.append(random.choice(nombres))
    datos.append(random.randint(1, 100))
    datos.append(random.choice(paises))
    datos.append(random.randint(1000000, 99999999))
    return datos


def validar_documento(datos): # Recibe un documento generado al azar y devuelve True si es válido y False si no lo es
    if datos[1] < 18:
        return False
    if datos[2] not in paises_validos:
        return False
    
    return True


def iniciar_juego():
    datos = generar_documento()

    print('------------------------------')
    print('Nombre:', datos[0])
    print('Edad:', datos[1])
    print('Nacionalidad:', datos[2])
    print('DNI:', datos[3])
    print('------------------------------')

    valido = validar_documento(datos)
    # print(valido)

    print('1. Aceptar')
    print('2. Denegar')
    opcion = int(input('Elige una opción: '))