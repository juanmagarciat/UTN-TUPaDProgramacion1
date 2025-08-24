#1)
numero1 = 10
#2)
numero2 = 10.5
#3)
suma = numero1 + numero2
#4)
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
print(f"SUMA: {suma} RESTA: {resta} DIVISIÓN: {division} MULTIPLICACIÓN: {multiplicacion}")
#5)
nombre = "Juan Martin"
#6)
precio = 912.18
#7)
descuento = 0.31
#8)
precio_final = precio * (1-descuento)
#9)
cadena = "Hola, que tal?"
#10)
longitud = len(cadena)
#11)
precio = int(912.18)
#12)
nombre = "Juan Martin"
apellido = "Garcia"
nombre_completo = f"{nombre} {apellido}"
#13)
edad = (19 + 5) - 10
#14)
altura = (1.80 * 4) / 3
#15)
nombre_mayus = "JUAN MARTIN"
nombre_minus = nombre_mayus.lower()
#16)
nombre_titulo = nombre_minus.title()

#EJERCICIO CALCULADORA DE PROPINAS EN UN RESTAURANTE

print("CALCULADORA DE PROPINAS")

monto_total = int(input("INGRESE EL MONTO TOTAL DE LA CUENTA: 3"))
propina_sugerida_10 = monto_total * 0.10
print(f"PROPINA SUGERIDA (10%): {propina_sugerida_10}")
propina_sugerida_15 = monto_total * 0.15
print(f"PROPINA SUGERIDA (15%): {propina_sugerida_15}")
total_10 = monto_total + propina_sugerida_10
print(f"TOTAL A PAGAR (10%): {total_10}")
total_15 = monto_total + propina_sugerida_15
print(f"TOTAL A PAGAR (15%): {total_15}")

