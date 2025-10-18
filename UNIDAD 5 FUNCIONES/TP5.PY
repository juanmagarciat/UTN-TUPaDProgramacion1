#FUNCIONES
def imprimir_hola_mundo():
    print("Hola mundo!")

def saludo_personalizado(nombre):
    print(f"Hola {nombre}!")

def datos_personales(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

def calcular_area_circulo(radio):
    import math
    area = math.pi * radio ** 2
    return area

def calcular_perimetro_circulo(radio):
    import math
    perimetro = 2 * math.pi * radio
    return perimetro
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

print(f"EL AREA DEL CIRCULO DE RADIO {radio} ES {round(area,2)} Y EL PERIMETRO {round(perimetro,2)}")
