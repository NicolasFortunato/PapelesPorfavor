import os
import json
import random
import time

# Función para limpiar consola
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para cargar datos JSON
def cargar_datos(nombre_archivo, datos_por_defecto):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r") as archivo:
            return json.load(archivo)
    return datos_por_defecto

# Función para guardar datos JSON
def guardar_datos(nombre_archivo, datos):
    with open(nombre_archivo, "w") as archivo:
        json.dump(datos, archivo, indent=4)

# Función para generar inmigrantes
def generar_inmigrantes(n):
    return [{
        "nombre": random.choice(["Juan", "Maria", "Carlos", "Ana", "Pedro", "Lucia"]),
        "pais_origen": random.choice(["Argentina", "Chile", "Uruguay", "Bolivia", "Paraguay", "Brasil"]),
        "razon": random.choice(["Turismo", "Trabajo", "Estudio", "Residencia"]),
        "documento": random.choice(["DNI", "Pasaporte", "Permiso de Trabajo"]),
        "dni": "".join([str(random.randint(0, 9)) for _ in range(8)])
    } for _ in range(n)]

# Validar inmigrante
def validar_inmigrante(inmigrante, paises_validos, razones_validas, documentos_validos):
    return (
        inmigrante["pais_origen"] in paises_validos and
        inmigrante["razon"] in razones_validas and
        inmigrante["documento"] in documentos_validos
    )

# Inicio de sesión
def inicio_sesion():
    usuarios = cargar_datos("usuarios.json", {})
    limpiar_consola()
    print("=== Inicio de Sesión ===")
    usuario = input("Ingresa tu nombre de usuario: ").strip()

    if usuario in usuarios:
        print("Bienvenido de nuevo,", usuario)
    else:
        print("Usuario no encontrado. Creando un nuevo perfil...")
        usuarios[usuario] = {
            "estadisticas": {"aprobaciones": 0, "rechazos": 0, "puntos": 0},
            "habilidades": {"deshacer_disponible": 0, "puntos_extra": False},
            "logros": []
        }
        guardar_datos("usuarios.json", usuarios)
        print("Perfil creado con éxito.")

    time.sleep(1)
    return usuario, usuarios[usuario]

# Menú principal
def menu_principal(usuario, datos_usuario):
    while True:
        limpiar_consola()
        print(f"=== Menú Principal - Usuario: {usuario} ===")
        print("1. Iniciar juego")
        print("2. Ver estadísticas")
        print("3. Tienda")
        print("4. Ver logros")
        print("5. Salir")

        opcion = input("Selecciona una opción: ").strip()
        if opcion == "1":
            iniciar_juego(usuario, datos_usuario)
        elif opcion == "2":
            mostrar_estadisticas(datos_usuario["estadisticas"])
        elif opcion == "3":
            tienda(datos_usuario)
        elif opcion == "4":
            mostrar_logros(datos_usuario["logros"])
        elif opcion == "5":
            usuarios = cargar_datos("usuarios.json", {})
            usuarios[usuario] = datos_usuario
            guardar_datos("usuarios.json", usuarios)
            print("Gracias por jugar. ¡Hasta luego!")
            break
        else:
            print("Opción no válida.")
            time.sleep(1)

# Mostrar estadísticas
def mostrar_estadisticas(estadisticas):
    limpiar_consola()
    print("=== Estadísticas ===")
    print(f"Aprobaciones correctas: {estadisticas['aprobaciones']}")
    print(f"Rechazos correctos: {estadisticas['rechazos']}")
    print(f"Puntos acumulados: {estadisticas['puntos']}")
    input("Presiona Enter para volver al menú principal.")

# Tienda
def tienda(datos_usuario):
    while True:
        limpiar_consola()
        print("=== Tienda ===")
        print(f"Puntos disponibles: {datos_usuario['estadisticas']['puntos']}")
        print("1. Comprar habilidad: Deshacer decisión (20 puntos)")
        print("2. Comprar habilidad: Puntos extra (50 puntos)")
        print("3. Volver al menú principal")

        opcion = input("Selecciona una opción: ").strip()
        if opcion == "1":
            if datos_usuario["estadisticas"]["puntos"] >= 20:
                datos_usuario["habilidades"]["deshacer_disponible"] += 1
                datos_usuario["estadisticas"]["puntos"] -= 20
                print("Habilidad 'Deshacer decisión' comprada.")
            else:
                print("No tienes suficientes puntos.")
        elif opcion == "2":
            if datos_usuario["estadisticas"]["puntos"] >= 50:
                datos_usuario["habilidades"]["puntos_extra"] = True
                datos_usuario["estadisticas"]["puntos"] -= 50
                print("Habilidad 'Puntos extra' activada.")
            else:
                print("No tienes suficientes puntos.")
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")
        time.sleep(1)

# Mostrar logros
def mostrar_logros(logros):
    limpiar_consola()
    print("=== Logros ===")
    print("1. Primer día completado: Juega y completa un día.")
    print("2. Experto en decisiones: Logra 10 aprobaciones correctas.")
    print("3. Maestría en puntos: Obtén 100 puntos acumulados.")
    print("\nTus logros obtenidos:")
    if logros:
        for logro in logros:
            print(f"- {logro}")
    else:
        print("Aún no has conseguido ningún logro.")
    input("\nPresiona Enter para volver al menú principal.")

# Inicio del juego
def iniciar_juego(usuario, datos_usuario):
    limpiar_consola()
    print("¡Iniciando el juego!")

    while True:
        try:
            dificultad = input("Selecciona dificultad (1 = Fácil, 2 = Media, 3 = Difícil): ").strip()
            if not dificultad.isdigit():
                raise ValueError("La dificultad debe ser un número (1, 2 o 3).")
            
            dificultad = int(dificultad)
            if dificultad not in [1, 2, 3]:
                raise ValueError("Por favor, elige una opción válida (1, 2 o 3).")
            
            tiempo_dia = {1: float('inf'), 2: 45, 3: 30}[dificultad]
            break
        except ValueError as e:
            print(f"Error: {e}")
            time.sleep(1)

    paises_validos_dia = random.sample(
        ["Argentina", "Chile", "Uruguay", "Bolivia", "Paraguay", "Brasil"], 4
    )
    razones_validas_dia = random.sample(
        ["Turismo", "Trabajo", "Estudio", "Residencia"], 4
    )
    documentos_validos_dia = random.sample(
        ["DNI", "Pasaporte", "Permiso de Trabajo"], 3
    )
    inicio_dia = time.time()

    print(f"\n=== Día iniciado ===")
    print(f"Países válidos: {', '.join(paises_validos_dia)}")
    print(f"Razones válidas: {', '.join(razones_validas_dia)}")
    print(f"Documentos válidos: {', '.join(documentos_validos_dia)}")
    print(f"Habilidades disponibles: {datos_usuario['habilidades']}")
    print(f"Puntos actuales: {datos_usuario['estadisticas']['puntos']}\n")

    for turno in range(8):  # Hasta 8 inmigrantes por día
        if time.time() - inicio_dia > tiempo_dia:
            print("\n¡El tiempo para este día se ha terminado!")
            break

        inmigrante = generar_inmigrantes(1)[0]
        decision_correcta = validar_inmigrante(
            inmigrante, paises_validos_dia, razones_validas_dia, documentos_validos_dia
        )

        print(f"\nInmigrante #{turno + 1}: {inmigrante}")
        while True:
            decision = input("1. Aprobar\n2. Rechazar\nTu decisión: ").strip()
            if decision in ["1", "2"]:
                break
            print("Opción no válida.")

        if decision == "1" and decision_correcta:
            print("¡Aprobación correcta!")
            datos_usuario["estadisticas"]["aprobaciones"] += 1
            datos_usuario["estadisticas"]["puntos"] += 10
        elif decision == "2" and not decision_correcta:
            print("¡Rechazo correcto!")
            datos_usuario["estadisticas"]["rechazos"] += 1
            datos_usuario["estadisticas"]["puntos"] += 10
        else:
            print("Decisión incorrecta.")
            datos_usuario["estadisticas"]["puntos"] -= 5
            if datos_usuario["habilidades"]["deshacer_disponible"] > 0:
                deshacer = input("¿Quieres deshacer esta decisión (S/N)? ").strip().lower()
                if deshacer == "s":
                    print("Decisión deshecha. Rehaciendo...")
                    datos_usuario["habilidades"]["deshacer_disponible"] -= 1
                    # Aquí se vuelve a preguntar la decisión.
                    while True:
                        decision = input("1. Aprobar\n2. Rechazar\nTu decisión: ").strip()
                        if decision in ["1", "2"]:
                            break
                    # Recalcular puntos
                    if decision == "1" and decision_correcta:
                        print("¡Aprobación correcta!")
                        datos_usuario["estadisticas"]["aprobaciones"] += 1
                        datos_usuario["estadisticas"]["puntos"] += 10
                    elif decision == "2" and not decision_correcta:
                        print("¡Rechazo correcto!")
                        datos_usuario["estadisticas"]["rechazos"] += 1
                        datos_usuario["estadisticas"]["puntos"] += 10
                    else:
                        print("Decisión incorrecta.")
                        datos_usuario["estadisticas"]["puntos"] -= 5
                elif deshacer == "n":
                    pass
                else:
                    print("Opción no válida.")
        
        # Verificar logros
        if turno == 7 and "Primer día completado" not in datos_usuario["logros"]:
            print("\n¡Has conseguido el logro: Primer día completado!")
            datos_usuario["logros"].append("Primer día completado")
        if datos_usuario["estadisticas"]["aprobaciones"] >= 10 and "Experto en decisiones" not in datos_usuario["logros"]:
            print("\n¡Has conseguido el logro: Experto en decisiones!")
            datos_usuario["logros"].append("Experto en decisiones")
        if datos_usuario["estadisticas"]["puntos"] >= 100 and "Maestría en puntos" not in datos_usuario["logros"]:
            print("\n¡Has conseguido el logro: Maestría en puntos!")
            datos_usuario["logros"].append("Maestría en puntos")

        time.sleep(1)

    # Final del día
    while True:
        continuar = input("\n¿Deseas continuar jugando (S/N)? ").strip().lower()
        if continuar in ["s", "n"]:
            break
        print("Opción no válida.")
    
    if continuar == "n":
        print("\nVolviendo al menú principal...")
        return

# Ejecutar el juego
def main():
    usuario, datos_usuario = inicio_sesion()
    menu_principal(usuario, datos_usuario)

if __name__ == "__main__":
    main()
