#1)
edad = int(input("INGRESE SU EDAD PARA DETERMINAR SI ES MAYOR: "))
if edad >= 18:
    print("ES MAYOR DE EDAD")
else:
    print("NO ES MAYOR DE EDAD")
#2)
nota = int(input("INGRESE LA NOTA: "))
if nota >= 6:
    print("APROBADO")
else:
    print("DESAPROBADO")
#3)
numero = int(input("INGRESE UN NUMERO PAR: "))
if numero % 2 == 0:
    print("EL NUMERO ES PAR")
else:
    print("POR FAVOR INGRESE UN NUMERO PAR")
#4)
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
contrasena = input("INGRESE SU CONTRASEÑA (ENTRE 8 Y 14 CARACTERES): ")
cant_caracters = len(contrasena)
if cant_caracters >= 8 and cant_caracters <= 14:
    print("CONTRASEÑA VALIDA")
else:
    print("CONTRASEÑA NO CUMPLE CON LOS CARACTERES")
#6)

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

#7)
texto = input("INGRESE UN TEXTO O FRASE: ")
if texto[-1].lower() in "aeiou":
    print(f"{texto}!")
else: 
    print(texto)
#8)

