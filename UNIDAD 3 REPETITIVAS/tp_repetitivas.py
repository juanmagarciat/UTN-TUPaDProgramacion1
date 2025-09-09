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