numero = int(input("INGRESE UN NUMERO ENTERO PARA DETERMINAR CUANTOS DIGITOS TIENE: "))
numero = abs(numero)
digitos = 0
while numero > 0:
    numero = numero // 10
    digitos += 1
print(f"EL NUMERO TIENE {digitos} DIGITOS ")