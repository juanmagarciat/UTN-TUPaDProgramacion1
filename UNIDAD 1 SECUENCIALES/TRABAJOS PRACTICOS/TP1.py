#TRABAJO PRACTICO N1 PROGRAMACION
#JUAN MARTIN GARCIA 1PRO4

print("EJERCICIO 1")
print("")

print("Hola mundo!")

print("")
print("EJERCICIO 2")
print("")

nombre=input("INGRESE SU NOMBRE: ")
print(f"Hola!, {nombre}!")

print("")
print("EJERCICIO 3")
print("")


nombre = input("INGRESE SU NOMBRE: ")
apellido = input("INGRESE SU APELLIDO: ")
edad = input("IGRESE SU EDAD: ")
residencia = input("INGRESE SU LUGAR DE RESIDENCIA: ")

print(f"Hola soy {nombre} {apellido} tengo {edad} años y vivo en {residencia}")

print("")
print("EJERCICIO 4")
print("")

import math

print("CALCULAR AREA Y PERIMETRO DEL CIRCULO")

radio_circulo = float(input("INGRESE EL RADIO DEL CIRCULO: "))
area_circulo = round (math.pi* (radio_circulo)**2, 2)
perimetro_circulo = round (2 * math.pi * radio_circulo, 2)

print(f"EL AREA ES {area_circulo} ")
print(f"EL PERIMETRO ES {perimetro_circulo}")

print("")
print("EJERCICIO 5")
print("")

segundos=int(input("INDIQUE UNA CANTIDAD DE SEGUNDOS PARA CONVERTIRLO EN HORAS: "))
horas = round (segundos/3600, 2)

print(f"{segundos} segundos equivalen a {horas} horas")

print("")
print("EJERCICIO 6")
print("")

tabla = int(input("TABLA DE MULTIPLICAR DEL: "))

print(f"{tabla} X 1 = {tabla*1}")
print(f"{tabla} X 2 = {tabla*2}")
print(f"{tabla} X 3 = {tabla*3}")
print(f"{tabla} X 4 = {tabla*4}")
print(f"{tabla} X 5 = {tabla*5}")
print(f"{tabla} X 6 = {tabla*6}")
print(f"{tabla} X 7 = {tabla*7}")
print(f"{tabla} X 8 = {tabla*8}")
print(f"{tabla} X 9 = {tabla*9}")
print(f"{tabla} X 10 = {tabla*10}")

print("")
print("EJERCICIO 7")
print("")

numero_1= int(input("INGRESE EL PRIMER NUMERO DISTINTO DE 0: "))
numero_2= int(input("INGRESE EL SEGUNDO NUMERO DISTINTO DE 0: "))

suma = numero_1+numero_2
resta = numero_1-numero_2
producto = numero_1*numero_2
division = numero_1/numero_2

print(f"LA SUMA DE {numero_1} y {numero_2} es {suma}")
print(f"LA RESTA DE {numero_1} y {numero_2} es {resta}")
print(f"EL PRODUCTO DE {numero_1} y {numero_2} es {producto}")
print(f"LA DIVISION DE {numero_1} y {numero_2} es {division}")

print("")
print("EJERCICIO 8")
print("")

print("CALCULAR IMC")

altura = float(input("INGRESE SU ALTURA EN METROS: "))
peso = float(input("INGRESE SU PESO EN KG: "))

imc = round (peso / (altura)**2, 2)
print(f"SU IMC ES: {imc} ")

print("")
print("EJERCICIO 9")
print("")

print("CONVERTIR CELSIUS A FAHRENTHEIT ")
print("")

c = int(input("INGRESE GRADOS CELSIUS: "))
f = (c*1.8)+32

print(f"{c} GRADOS CELSIUS EQUIVALEN A {f} GRADOS FAHRENTHEIT")

print("")
print("EJERCICIO 10")
print("")

print("CALCULAR PROMEDIO DE 3 NUMEROS ")
print("")

num_1 = int(input("INGRESE EL PRIMER NUMERO: "))
num_2 = int(input("INGRESE EL SEGUNDO NUMERO: "))
num_3 = int(input("INGRESE EL TERCER NUMERO: "))

promedio = round((num_1+num_2+num_3)/3, 2)
print(f"EL PROMEDIO DE LOS TRES NUMEROS ES {promedio}")