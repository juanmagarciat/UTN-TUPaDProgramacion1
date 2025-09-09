#Ejercicio 1: Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100.
for i in range(0,101):
    print(i)
#Ejercicio 2: Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contie"ne.
numero = int(input("INGRESE UN NUMERO ENTERO PARA DETERMINAR CUANTOS DIGITOS TIENE: "))
numero = abs(numero)
digitos = 0
while numero > 0:
    numero = numero // 10
    digitos += 1
print(f"EL NUMERO TIENE {digitos} DIGITOS ")
#Ejercicio 3: Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.
numero_1 = int(input("INGRESE EL PRIMER NUMERO PARA HACER LA SUMATORIA: "))
numero_2 = int(input("INGRESE EL SEGUNDO NUMERO PARA HACER LA SUMATORIA: "))
sumatoria = 0
for i in range(numero_1+1, numero_2):
    sumatoria += i
print(f"LA SUMATORIA DE LOS NUMEROS ENTRE {numero_1} Y {numero_2} ES: {sumatoria}")
#Ejercicio 4: Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
numero = 1
sumatoria = 0
while numero != 0:
    print("")
    numero = int(input("INGRESE UN NUMERO PARA AGREGAR A LA SUMATORIA (O INGRESE 0 PARA MOSTRAR EL TOTAL ACUMULADO): "))
    sumatoria += numero
    if numero == 0:
        print("")
        print("SALIENDO...")
print("")
print(f"EL TOTAL ACUMULADO ES {sumatoria}")
#Ejercicio 5: Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
numero_adivinar = random.randint(0,9)
num_usuario = 0
intentos = 0
while num_usuario != numero_adivinar: 
    intentos += 1
    if intentos == 1:
        num_usuario = int(input("ADIVINA EL NUMERO DEL 0 AL 9: "))
    else:
        num_usuario = int(input("INTENTALO DE NUEVO!: "))
print("ADIVINASTE!")
print(f"EL NUMERO ERA {numero_adivinar} Y LO ADIVINASTE EN {intentos} INTENTOS")
#Ejercicio 6: Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
for i in range(100,1,-2):
    print(i)
#Ejercicio 7: Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un \número entero positivo indicado por el usuario.
num_usuario = int(input("INGRESE UN NUMERO POSITIVO PARA LA SUMATORIA ENTRE 0 Y DICHO NUMERO: "))
sumatoria = 0
for i in range(0, num_usuario):
    sumatoria += i
print(f"LA SUMATORIA DE LOS NUMEROS COMPRENDIDOS ENTRE 0 Y {num_usuario} ES: {sumatoria}")
#Ejercicio 8: Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).
pares = 0
impares = 0
positivos = 0
negativos = 0
cantidad_numeros = 10

for i in range(cantidad_numeros):
    numero = int(input(f"INGRESE EL NUMERO {i+1}: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
        
print("NUMEROS PARES:", pares)
print("NUMEROS IMPARES:", impares)
print("NUMEROS POSITIVOS:", positivos)
print("NUMEROS NEGATIVOS:", negativos)
#Ejercicio 9: Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).
suma = 0
cantidad_numeros = 100

for i in range(cantidad_numeros):
    numero = int(input(f"INGRESE EL NUMERO {i+1}: "))
    suma += numero

media = suma / cantidad_numeros
print("LA MEDIA ES:", media)
#Ejercicio 10: ) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
numero = int(input("INGRESE UN NUMERO: "))
negativo = False

if numero < 0:
    negativo = True
    numero = -numero

numero_invertido = 0

while numero > 0:
    digito = numero % 10
    numero_invertido = numero_invertido * 10 + digito
    numero = numero // 10

if negativo:
    numero_invertido = -numero_invertido

print("NUMERO INVERTIDO:", numero_invertido)
