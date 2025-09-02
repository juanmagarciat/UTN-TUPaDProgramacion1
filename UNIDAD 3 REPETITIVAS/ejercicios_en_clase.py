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