# array ( listas, tuplas)
# lista1 = ("Juan", "Maria", "Pedro", "Ana", "Luis") # lista de usuarios
# lista2 = ["Manzana", "Pera", "Naranja", "Banana", "Uva"] # lista de contraseñas

# print(lista1[1])
# tupla1 = (1, 2)
# print(tupla1[0])

# ciclos o bucles
# usuario = "Pedro"
# contraseña = "Naranja"

# 1. forma simple sin conocer la posición
# for i in lista1:
#     print(i)


# 2. forma que me permite conocer la posición (índice (index) / key) y el elemento (valor / value)
# for pos, nombre in enumerate(lista1):
#     if nombre == usuario:
#         if contraseña == lista2[pos]:
#             print(f"Bienvenido {usuario} a Facebook de Fernando")
#             break
#         else:
#             print(f"Estimado {usuario} por favor verifique su contraseña")
#             break


# # ciclos o bucles
# usuario = "Pedro"
# contrasena_usuario = "1234"

# # 3.  forma para recorrer dos listas o más de forma simultánea
# for nombre, contrasena in zip(lista1, lista2):
#     if usuario == nombre:
#         if contrasena_usuario == contrasena:
#             print(f"Bienvenido {usuario} a Facebook de Fernando")
#             break
#         else:
#             print(f"Estimado {usuario} por favor verifique su contraseña")
#             break
        
### Diferencias entre una lista y una tupla
# nombres = ["Juan", "Maria", "Pedro", "Ana", "Luis"] # tupla de usuarios
# print (f"Antes de modificar la tupla: {nombres}") # ('Juan', 'Maria', 'Pedro', 'Ana', 'Luis')

# nombres[0] = "Jose"
# print(f"Después de modificar la tupla: {nombres}") # ('Jose', 'Maria', 'Pedro', 'Ana', 'Luis')

# carrito_de_compra = ["Manzana", "Pera", "Naranja", "Banana", "Uva"] # lista de contraseñas
# copia_carrito = tuple(carrito_de_compra)
# copia2 = carrito_de_compra.copy()

# print(f"Carrito de compra antes de la modificación: {carrito_de_compra}")
# print(f"Copia del carrito de compra antes de la modificación: {copia_carrito}")


# carrito_de_compra[0] = "Durazno"

# print(f"Carrito de compra después de la modificación: {carrito_de_compra}")
# print(f"Copia del carrito de compra después de la modificación: {copia_carrito}")
# print(f"Copia 2 del carrito de compra después de la modificación: {copia2}")


# ## comandos importantes del día a día en el uso de tuplas o listas
# len(lista) # cantidad de elementos de una lista o tupla
# copia = lista.copy() # crea una copia de la lista, es decir, una nueva lista con los mismos elementos.
# lista.append("nuevo elemento") # agrega un nuevo elemento al final de la lista.
# lista.extend(["nuevo elemento 1", "nuevo elemento 2"]) # agrega varios elementos al final de la lista.
# lista.remove("elemento a eliminar") # elimina la primera aparición del elemento especificado de la lista.
# lista.insert(posición, "nuevo elemento") # inserta un nuevo elemento en la posición especificada de la lista.
# lista.pop(posición) # elimina el elemento en la posición especificada de la lista y lo devuelve. Si no se especifica la posición, elimina y devuelve el último elemento de la lista.



# carrito_de_compra = ["Manzana", "Pera", "Naranja", "Banana", "Uva"]
# # carrito_de_compra.append("Durazno")
# # carrito_de_compra.extend(["Durazno", "Melón"])
# # carrito_de_compra.append(["Durazno", "Melón"])
# # carrito_de_compra.remove("Manzana")
# # carrito_de_compra.insert(0, "Durazno")
# elemento_borrado = carrito_de_compra.pop(0)


# print(carrito_de_compra) # ['Pera', 'Naranja', 'Banana', 'Uva']
# print(f"Elemento borrado: {elemento_borrado}") # Elemento borrado: Manzana

##############################
# Ciclos con While
# is_done = False
# contador = 1
# while is_done == False:
#     print(f"Hola, esta es mi ejecución número {contador}")
    
#     contador += 1
#     if contador >= 21:
#         is_done = True
        
# Ejercicio 1: ciclos while
lista = ["Juan", "Maria", "Pedro", "Ana", "Luis"] # lista de usuarios
nombre_usuario = "Ana"

is_done = False
contador = 0
while is_done == False:
    
    if lista[contador] == nombre_usuario:
        print(f"Bienvenido {nombre_usuario} a Facebook de Fernando")
        is_done = True
    
    else:
        print(f"Se encuentra en el usuario {lista[contador]}")
        contador += 1

        
    # Forma en negativo (no recomendable)
    # if lista[contador] != nombre_usuario:
    #     contador += 1
    # else: 
    #     print(f"Bienvenido {nombre_usuario} a Facebook de Fernando")
    #     is_done = True
    
# numero_maximo_de_reintentos = 20
# contador = 0
# while contador < numero_maximo_de_reintentos:
#     print(f"Introduzca su contraseña")
#     contador += 1
    
    
limite_de_la_suma = 20
suma = 0
while suma < limite_de_la_suma:
    print(f"El valor de la suma es: {suma}")
    suma = suma + 2