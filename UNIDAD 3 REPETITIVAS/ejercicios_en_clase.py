#EJERCICIO 1(FOR) 
corrimiento = int(input("INGRESE EL CORRIMIENTO DEL ENCRIPTADO: "))  
#ASIGNAMOS VALOR A CADA LETRA

abecedario = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")  
encriptado = ""

for i in range(5):
    mensaje = input("INGRESE EL MENSAJE A ENCRIPTAR: ")  
    mensaje = mensaje.upper()
    for letra in range(len(mensaje)):
        letra = mensaje[letra]  # SEPARA EL TEXTO POR CADA LETRA EN CADA CICLO FOR
        posicion = abecedario.index(letra)  # SACAR POSICION DE CADA LETRA EN LA LISTA ABECEDARIO
        posicion_corrida = posicion + corrimiento  # CALCULAR LA POSICION CON EL CORRIMIENTO EN LA LISTA
        if posicion_corrida > 25:
            posicion_corrida = posicion_corrida - 26
        letra_corrida = abecedario[posicion_corrida]  # CALCULA A QUE LETRA CORRESPONDE LA POSICION CORRIDA
        encriptado = encriptado + letra_corrida  # JUNTA TODAS LAS LETRAS PARA MOSTRAR EL MENSAJE ENCRIPTADO
    print(encriptado)
    encriptado = ""

#EJERCICIO 2 (WHILE)
#JUEGO DE PIEDRA PAPEL O TIJERA CONTRA LA COMPUTADORA
print("JUEGO DE PIEDRA PAPEL O TIJERA")
opciones = {1: "PIEDRA", 2: "PAPEL", 3: "TIJERA"}
print(opciones)
juega = 1
import random
ganadas_usuario = 0
ganadas_computadora = 0
empates = 0
while juega != 0:
    try:
        eleccion_usuario = int(input("LA OPCION ELEGIDA ES (1/2/3): "))
    except ValueError:
        print("INGRESE UNA OPCION VALIDA (1, 2 o 3)")
        continue
    if eleccion_usuario > 3 or eleccion_usuario < 1:
        print("INGRESE UNA OPCION VALIDA (1, 2 o 3)")
        continue
    eleccion_computadora = random.randint(1, 3)
    if eleccion_usuario == 1:
        if eleccion_computadora == 3:
            ganadas_usuario = ganadas_usuario + 1
            print(f"USUARIO: {opciones[eleccion_usuario]}")
            print(f"COMPUTADORA: {opciones[eleccion_computadora]}")
            print("GANASTE!!")
        elif eleccion_computadora == 2:
            ganadas_computadora = ganadas_computadora + 1
            print(f"USUARIO: {opciones[eleccion_usuario]}")
            print(f"COMPUTADORA: {opciones[eleccion_computadora]}")
            print("PERDISTE!!")
        elif eleccion_computadora == 1:
            empates = empates + 1
            print(f"USUARIO: {opciones[eleccion_usuario]}")
            print(f"COMPUTADORA: {opciones[eleccion_computadora]}")
            print("EMPATE!!")
    elif eleccion_usuario == 2:
        if eleccion_computadora == 3:
            ganadas_computadora = ganadas_computadora + 1
            print(f"USUARIO: {opciones[eleccion_usuario]}")
            print(f"COMPUTADORA: {opciones[eleccion_computadora]}")
            print("PERDISTE!!")
        elif eleccion_computadora == 2:
            empates = empates + 1
            print(f"USUARIO: {opciones[eleccion_usuario]}")
            print(f"COMPUTADORA: {opciones[eleccion_computadora]}")
            print("EMPATE!!")
        elif eleccion_computadora == 1:
            ganadas_usuario = ganadas_usuario + 1
            print(f"USUARIO: {opciones[eleccion_usuario]}")
            print(f"COMPUTADORA: {opciones[eleccion_computadora]}")
            print("GANASTE!!")
    elif eleccion_usuario == 3:
        if eleccion_computadora == 3:
            empates = empates + 1
            print(f"USUARIO: {opciones[eleccion_usuario]}")
            print(f"COMPUTADORA: {opciones[eleccion_computadora]}")
            print("EMPATE!!")
        elif eleccion_computadora == 2:
            ganadas_usuario = ganadas_usuario + 1
            print(f"USUARIO: {opciones[eleccion_usuario]}")
            print(f"COMPUTADORA: {opciones[eleccion_computadora]}")
            print("GANASTE!!")
        elif eleccion_computadora == 1:
            ganadas_computadora = ganadas_computadora + 1
            print(f"USUARIO: {opciones[eleccion_usuario]}")
            print(f"COMPUTADORA: {opciones[eleccion_computadora]}")
            print("PERDISTE!!")
    try:
        juega = int(input("QUIERES JUGAR OTRA RONDA O SALIR DEL JUEGO [1: PARA CONTINUAR, 0: PARA SALIR]: "))
    except ValueError:
            print("ERROR (SALIENDO DEL JUEGO...)")
            break
    if juega not in (0, 1):
        print("ERROR (SALIENDO DEL JUEGO...)")
        break
print("")
print(f"GANADAS USUARIO: {ganadas_usuario}")
print(f"GANADAS COMPUTADORA: {ganadas_computadora}")
print(f"EMPATES: {empates}")