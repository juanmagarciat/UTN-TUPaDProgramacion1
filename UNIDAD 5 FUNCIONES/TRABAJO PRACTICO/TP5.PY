# FUNCIONES

def imprimir_hola_mundo():
    print("Hola mundo!")

def saludo_personalizado(nombre):
    print(f"Hola {nombre}!")

def datos_personales(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

def calcular_area_circulo(radio):
    import math  # Se importa dentro de la función para usar pi
    area = round(math.pi * radio ** 2, 2)  # Fórmula del área del círculo
    return area

def calcular_perimetro_circulo(radio):
    import math
    perimetro = round(2 * math.pi * radio, 2)  # Fórmula del perímetro del círculo
    return perimetro

def segundos_a_horas(segundos):
    horas = round(segundos / 3600, 2)  # Convierte segundos a horas
    return horas

def tabla_multiplicar(num):
    # Muestra la tabla de multiplicar del número ingresado (1 al 10)
    for i in range(1, 11):
        print(f"{num} X {i} = {num * i}")

def operaciones_basicas(a, b):
    # Realiza las 4 operaciones básicas y devuelve una tupla con los resultados
    suma = a + b
    resta = a - b
    producto = a * b
    division = round(a / b, 2)
    operaciones = (suma, resta, producto, division)
    return operaciones

def calcular_imc(peso, altura):
    # Calcula el Índice de Masa Corporal (IMC)
    return round(peso / (altura ** 2), 2)

def celsius_a_faren(celsius): 
    # Convierte grados Celsius a Fahrenheit
    return round((celsius * 1.8) + 32, 2)

def calcular_promedio(a, b, c):
    # Calcula el promedio de tres números
    promedio = (a + b + c) / 3
    return promedio

# PROGRAMA PRINCIPAL

#1. Imprime un mensaje básico
imprimir_hola_mundo()

#2. Saludo con nombre ingresado por el usuario
nombre_usuario = input("INGRESE SU NOMBRE: ")
saludo_personalizado(nombre_usuario)

#3. Muestra los datos personales ingresados
nombre = input("INGRESE SU NOMBRE: ")
apellido = input("INGRESE SU APELLIDO: ")
edad = input("INGRESE SU EDAD: ")
residencia = input("INGRESE SU LUGAR DE RESIDENCIA: ")
datos_personales(nombre, apellido, edad, residencia)

#4. Calcula el área y perímetro de un círculo según su radio
radio = int(input("INGRESE EL RADIO DEL CIRCULO: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"EL AREA DEL CIRCULO DE RADIO {radio} ES {area} Y EL PERIMETRO {perimetro}")

#5. Convierte segundos a horas
segundos = int(input("INGRESE LOS SEGUNDOS PARA PASARLO A HORAS: "))
print(f"{segundos} SEGUNDO/S SON {segundos_a_horas(segundos)} HORA/S")

#6. Muestra la tabla de multiplicar del número elegido
numero = int(input("INGRESE UN NUMERO Y SE MOSTRARA SU TABLA DE MULTIPLICAR: "))
tabla_multiplicar(numero)

#7. Realiza las operaciones básicas entre dos números
num1 = int(input("INGRESE EL PRIMER NUMERO: "))
num2 = int(input("INGRESE EL SEGUNDO NUMERO: "))
resultados = operaciones_basicas(num1, num2)
print(f"SUMA: {resultados[0]} \nRESTA: {resultados[1]} \nMULTIPLICACION {resultados[2]} \nDIVISION: {resultados[3]}")

#8. Calcula el IMC del usuario
peso = int(input("INGRESE SU PESO EN KG: "))
altura = float(input("INGRESE SU ALTURA EN METROS (EJ: 1.80): "))
print(f"SU IMC ES: {calcular_imc(peso, altura)}")

#9. Convierte grados Celsius a Fahrenheit
celsius = float(input("INGRESE LOS GRADOS EN CELSIUS PARA CONVERTIRLOS A FAHRENHEIT: "))
print(f"{celsius} GRADOS CELSIUS SON {celsius_a_faren(celsius)} GRADOS FAHRENHEIT")

#10. Calcula el promedio de tres números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
resultado = calcular_promedio(num1, num2, num3)
print("EL PROMEDIO DE LOS 3 NUMEROS ES:", resultado)

