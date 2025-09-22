#EJERCICIO 1
print("")
print("EJERCICIO 1")
numeros = []
for i in range(101):
    if i % 4 == 0:
        numeros.append(i)
print(f"La lista con los multiplos de 4 del 1 al 100 es: {numeros}")
#EJERCICIO 2
print("")
print("EJERCICIO 2")
lista = [1, 2, 3, 4, 5]
print(f"El penultimo elemento de la lista es: {lista[-2]}")
#EJERCICIO 3
print("")
print("EJERCICIO 3")
lista_llenar = []
lista_llenar.append("Uno")
lista_llenar.append("Dos")
lista_llenar.append("Tres")
print(f"La lista llena es: {lista_llenar}")
#EJERCICIO 4
print("")
print("EJERCICIO 4")
animales = ["perro", "gato", "conejo", "pez"]
print(f"La lista original es {animales} ")
animales[1] = "loro"
animales[-1] = "oso"
print(f"La lista modificada es {animales}")
#EJERCICIO 5
print("")
print("EJERCICIO 5")
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
#El anterior programa elimina de la lista el elemento más grande
#EJERCICIO 6
print("")
print("EJERCICIO 6")
numeros = []
for i in range(10, 31, 5):
    numeros.append(i)
print(f"Los primeros 2 elementos de la lista son: {numeros[:2]}")
#EJERCICIO 7
print("")
print("EJERCICIO 7")
autos = ["sedan", "polo", "suran", "gol"]
print(f"La lista sin modificar es {autos}")
autos[1] = "scirocco"
autos[2] = "golf"
print(f"La lista modificada es {autos}")
#EJERCICIO 8
print("") 
print("EJERCICIO 8")
dobles = []
dobles.append(2*5)
dobles.append(2*10)
dobles.append(2*15)
print(dobles)
#EJERCICIO 9
print("") 
print("EJERCICIO 9")
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)
#EJERCICIO 10
print("") 
print("EJERCICIO 10")
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)



