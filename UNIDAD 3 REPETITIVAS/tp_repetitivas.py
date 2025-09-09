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