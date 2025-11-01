#1. Crear archivo inicial con 3 productos.
with open("productos.txt", "w") as archivo:
    archivo.write("Manzana,300,5\n")
    archivo.write("Leche,1100,3\n")
    archivo.write("Manteca,700,1\n")

print("Escribiendo archivo...\n")

#2. Leer el archivo y mostrar el contenido en el formato.
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        partes = linea.split(",")
        print(f"Producto: {partes[0]} | Precio: {partes[1]} | Cantidad: {partes[2]}")

#3. Pedir al usuario que agregue un producto y escribirlo en el archivo.


print("--Agregar nuevo producto--\n")

nombre = input("Nombre del producto: ").strip().capitalize()
precio = input("Precio: ").strip()
cantidad = input("Cantidad: ").strip()

nuevo = f"{nombre},{precio},{cantidad}\n"

with open("productos.txt", "a") as archivo_append:
    archivo_append.write(nuevo)

#4. Agregar los productos a una lista con diccionarios para cada producto con sus respectivos atributos.
productos = []

with open("productos.txt","r") as archivo:
    for linea in archivo:
        diccionario = {}
        linea = linea.strip()
        partes = linea.split(",")
        diccionario = {
                    "Nombre": partes[0],
                    "Precio": partes[1],
                    "Cantidad": partes[2]
                }
        productos.append(diccionario)

#5. Permitir al usuario buscar un producto por su nombre, y mostrar los resultados si lo encuentra.

print("--Buscar producto por nombre--\n")

buscar = input("Ingrese el producto que quiere buscar: \n ")

encontrado = False

for producto in productos:
    if producto["Nombre"].lower() == buscar.lower():
        print("Producto encontrado!")
        print(f"Nombre: {producto["Nombre"]}")
        print(f"Precio: {producto["Precio"]}")
        print(f"Cantidad: {producto["Cantidad"]}")
        encontrado = True
        break

if not encontrado:
    print(f"El producto {buscar} no fue encontrado")

#6. Sobreescribir el archivo con la lista de productos actualizada. 

print("Actualizando archivo...\n")

with open("productos.txt","w") as archivo:
    for producto_dict in productos:
        nombre = producto["Nombre"]
        precio = producto["Precio"]
        cantidad = producto["Cantidad"]
        linea = f"{nombre},{producto},{cantidad}\n"
        archivo.write(linea)

print("El archivo se guardo correctamente...")
