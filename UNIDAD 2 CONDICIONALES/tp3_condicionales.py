#1)
edad = int(input("INGRESE SU EDAD PARA DETERMINAR SI ES MAYOR: "))
if edad >= 18:
    print("ES MAYOR DE EDAD")
else:
    print("NO ES MAYOR DE EDAD")
#2)
print("")
nota = int(input("INGRESE LA NOTA: "))
if nota >= 6:
    print("APROBADO")
else:
    print("DESAPROBADO")
#3)
print("")
numero = int(input("INGRESE UN NUMERO PAR: "))
if numero % 2 == 0:
    print("EL NUMERO ES PAR")
else:
    print("POR FAVOR INGRESE UN NUMERO PAR")
#4)
print("")
edad = int(input("INGRESE SU EDAD: "))
if edad < 12:
    print("ESTAS EN LA CATEGORIA NIÑO/A")
elif edad >= 12 and edad < 18:
    print("ESTAS EN LA CATEGORIA ADOLESCENTE")
elif edad >= 18 and edad < 30:
    print("ESTAS EN LA CATEGORIA ADULTO/A JOVEN")
else:
    print("ESTAS EN LA CATEGORIA ADULTO/A")
#5)
print("")
contrasena = input("INGRESE SU CONTRASEÑA (ENTRE 8 Y 14 CARACTERES): ")
cant_caracters = len(contrasena)
if cant_caracters >= 8 and cant_caracters <= 14:
    print("CONTRASEÑA VALIDA")
else:
    print("CONTRASEÑA NO CUMPLE CON LOS CARACTERES")
#6)
print("")
from statistics import mode, median, mean
import random

print("CALCULO LA MEDIA, LA MODA Y LA MEDIANA Y EL SESGO DE UNA LISTA DE 50 NUMEROS ALEATORIOS:")

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

#CALCULAR LA MODA, MEDIA Y MEDIANA DE LA LISTA

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

#MUESTRO EN PANTALLA LOS RESULTADOS

print(f"LA MODA DE LA LISTA ES {moda}")
print(f"LA MEDIANA DE LA LISTA ES {mediana}")
print(f"LA MEDIA DE LA LISTA ES {media}")

#CALCULAR EL SESGO DE LA LISTA (SI ES POSITIVO, NEGATIVO O SIN SESGO)
if media > mediana and mediana > moda:
    print("LA LISTA TIENE SESGO POSITIVO")
elif media < mediana and mediana < moda:
    print("LA LISTA TIENE SESGO NEGATIVO")
elif media == mediana and mediana == moda:
    print("SIN SESGO")
else:
    print("NO CUMPLE CON NINGUNO DE LOS CASOS")

#7)
print("")
texto = input("INGRESE UN TEXTO O FRASE: ")
if texto[-1].lower() in "aeiou":
    print(f"{texto}!")
else: 
    print(texto)
#8)
print("")
nombre = input("INGRESE SU NOMBRE: ")
opcion = int(input("ELIJA UNA OPCIÓN PARA VISUALIZAR SU NOMBRE (1: EN MAYUSCULAS 2: EN MINUSCULAS 3: PRIMERA EN MAYUSCULA): "))
if opcion == 1:
    nombre = nombre.upper()
    print(nombre)
elif opcion == 2:
    nombre = nombre.lower()
    print(nombre)
elif opcion == 3:
    nombre = nombre.capitalize()
    print(nombre)
else:
    print("ELIJA UNA OPCION VALIDA")
#9
magnitud = float(input("Ingrese la magnitud del terremoto: "))

# Clasificación según la magnitud
if magnitud < 3:
    print("Muy leve (imperceptible).")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else:  # magnitud >= 7
    print("Extremo (puede causar graves daños a gran escala).")
