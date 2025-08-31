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

