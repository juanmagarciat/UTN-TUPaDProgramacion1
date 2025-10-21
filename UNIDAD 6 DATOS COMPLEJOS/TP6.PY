# 1. Añadir Frutas a un diccionario.
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

# Mostrar el diccionario de frutas
print("\nDiccionario de frutas con precios añadidos:")
print(precios_frutas)
print("")

# 2. Actualizo precios de las frutas.
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

# Mostrar el diccionario con precios actualizados
print("Precios actualizados de las frutas:")
print(precios_frutas)
print("")

# 3. Mostrar solo las frutas en una lista
# .keys() devuelve todas las claves del diccionario
frutas = precios_frutas.keys()
print("Lista de frutas disponibles:")
print(list(frutas))
print("")

# 4. Programa para almacenar y consultar números telefónicos
print("Guia Telefonica\n")

# Crear el diccionario y asignarle keys y valores
contactos = {}
for i in range(5):
    print("")
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ").capitalize()
    contactos[nombre] = int(input(f"Ingrese el numero telefonico de {nombre}: "))

# Consulta por un nombre, si existe devuelve el valor, sino devuelve no encontrado
consulta = input("\nConsulta el numero de un contacto por su nombre: ").capitalize()
encontrado = contactos.get(consulta, False)
print("")
if not encontrado:
    print("Contacto no encontrado.")
else:
    print(f"El Numero de {consulta} es: {encontrado}")
print("")

# 5. Solicitar al usuario frase y mostrar palabras únicas y el recuento.
frase = input("Ingrese una frase: ").lower() 

# Separar la frase por palabra y obtener las palabras únicas
palabras = frase.split()
palabras_unicas = set(palabras)

# Contar cuantas veces aparece cada palabra
contador = {}
# El bucle recorre la lista palabra por palabra, si ya existe le agrega 1 al contador, sino le asigna 1
for palabra in palabras:
    contador[palabra] = contador.get(palabra, 0) + 1

print("\nPalabras únicas encontradas:")
print(palabras_unicas)
print("\nRecuento de palabras:")
print(contador)
print("")

# 6. Ingresar 3 alumnos, 3 notas c/u y su promedio.
libreta = {}
for i in range(1, 4):
    nombre = input(f"Ingrese el nombre del alumno {i}: ")
    notas = []
    for j in range(1, 4):
        nota = float(input(f"Ingrese la nota {j} de {nombre}: "))
        notas.append(nota)
    libreta[nombre] = tuple(notas)
    print("")

print("Libreta de alumnos:")
print(libreta)
print("")

# Calcular promedio de cada alumno
for nombre, notas in libreta.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es: {round(promedio,2)}")
print("")

# 7. Utiliza 2 sets con numeros que representan cada estudiante que aprobo el parcial
parcial_1 = {1, 2, 3, 4, 5}
parcial_2 = {4, 5, 6, 7}

# Los numeros representan cada alumno, se podría realizar con nombres también
# parcial_1 = {"Emma", "Leonel", "Tiziano", "Francisco", "Tomas"}
# parcial_2 = {"Francisco", "Tomas", "Lucia", "Sofia"}

# Utiliza simbolos de los metodos de conjuntos
ambos = parcial_1 & parcial_2  # Intersección, unicamente los que aprobaron ambos parciales.
solo_uno = parcial_1 ^ parcial_2  # Diferencia simetrica, los que aprobaron solo un parcial.
al_menos_uno = parcial_1 | parcial_2  # Unión, todos sin repetir, los que aprobaron al menos 1 parcial

print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno de los dos:", solo_uno)
print("Aprobaron al menos un parcial:", al_menos_uno)
print("")

# 8. Armar un diccionario con el stock de productos.
stock = {"Leche": 8, "Cacao": 4, "Manteca": 1, "Agua": 3, "Harina": 5, "Azucar": 7}

print("Bienvenido al Software de Stock de Productos\n")

while True:
    print("--------MENU--------")
    print("1. CONSULTAR STOCK DE UN PRODUCTO")
    print("2. AGREGAR PRODUCTO O UNIDADES")
    print("3. SALIR")

    decision = int(input("¿Qué desea hacer?: "))

    if decision == 1:
        producto = input("Ingrese el nombre del producto a consultar: ").capitalize()
        # Usando .get() podemos dar un valor por defecto si no existe
        stock_producto = stock.get(producto, "Producto no encontrado")
        print(f"\n{producto}: {stock_producto}\n")

    elif decision == 2:
        producto = input("Ingrese el nombre del producto a agregar: ").capitalize()
        unidades = int(input("Ingrese la cantidad de unidades: "))
        # Si existe, sumamossi no, se crea con esa cantidad
        stock[producto] = stock.get(producto, 0) + unidades
        print(f"\nStock actualizado: {producto} -> {stock[producto]} unidades\n")

    elif decision == 3:
        print("\nSaliendo del sistema...")
        break
    else:
        print("\nOpción no válida, intente de nuevo.\n")
print("")

# 9. Armar diccionario de eventos con dia y hora
mi_agenda = {
    ("Lunes", "8:00"): "Facultad",
    ("Martes", "15:00"): "Trabajo",
    ("Miercoles", "12:00"): "Gimnasio",
    ("Jueves", "20:00"): "Juntada",
    ("Viernes", "21:00"): "Partido"
}

consulta = tuple(input("Consulta la agenda (EJ: Lunes 12:00): ").capitalize().split())
evento = mi_agenda.get(consulta, 0)

if evento != 0:
    print(f"\nEl {consulta[0]} a las {consulta[1]} hay {evento}.")
else:
    print("\nNo hay nada para esta fecha.")
print("")

# 10. Diccionario de paises y capitales
paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción",
    "Perú": "Lima",
    "Colombia": "Bogotá",
    "México": "Ciudad de México"
}

print("Diccionario Original:")
print(paises)


capitales = {}  # Creamos el diccionario invertido
# Con un bucle for y el metodo paises.items() asigna a las variables pais, capital los valores respectivos
# Dentro del for, lo invierte, dentro del diccionario invertido la capital como llave y el pais como valor
for pais, capital in paises.items():
    capitales[capital] = pais

print("Diccionario invertido de capitales a países:")
print(capitales)
print("")



