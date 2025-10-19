#FUNCIONES
def imprimir_hola_mundo():
    print("Hola mundo!")

def saludo_personalizado(nombre):
    print(f"Hola {nombre}!")

def datos_personales(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

def calcular_area_circulo(radio):
    import math
    area = round(math.pi * radio ** 2, 2)
    return area

def calcular_perimetro_circulo(radio):
    import math
    perimetro = round (2 * math.pi * radio,2)
    return perimetro

def segundos_a_horas(segundos):
    horas = round (segundos / 3600, 2)
    return horas

def tabla_multiplicar(num):
    for i in range(1, 11):
        print(f"{num} X {i} = {num * i}")

def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    producto = a * b
    division = round (a / b, 2)
    operaciones = (suma, resta, producto, division)
    return operaciones

#PROGRAMA PRINCIPAL
#1
imprimir_hola_mundo()
#2
nombre_usuario = input("INGRESE SU NOMBRE: ")
saludo_personalizado(nombre_usuario)
#3
nombre = input("INGRESE SU NOMBRE: ")
apellido = input("INGRESE SU APELLIDO: ")
edad = input("INGRESE SU EDAD: ")
residencia = input("INGRESE SU LUGAR DE RESIDENCIA: ")
datos_personales(nombre, apellido, edad, residencia)
#4
radio = int(input("INGRESE EL RADIO DEL CIRCULO: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"EL AREA DEL CIRCULO DE RADIO {radio} ES {(area)} Y EL PERIMETRO {perimetro}")
#5
segundos = int(input("INGRESE LOS SEGUNDOS PARA PASARLO A HORAS: "))
print(f"{segundos} SEGUNDO/S SON {segundos_a_horas(segundos)} HORA/S")
#6
numero = int(input("INGRESE UN NUMERO Y SE MOSTRARA SU TABLA DE MULTIPLICAR: "))
tabla_multiplicar(numero)
#7
num1 = int(input("INGRESE EL PRIMER NUMERO: "))
num2 = int(input("INGRESE EL SEGUNDO NUMERO: "))
resultados = operaciones_basicas(num1,num2)
print(f"SUMA: {resultados[0]} \nRESTA: {resultados[1]} \nMULTIPLICACION {resultados[2]} \nDIVISION: {resultados[3]}")
#8

