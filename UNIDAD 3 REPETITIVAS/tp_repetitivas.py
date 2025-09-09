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