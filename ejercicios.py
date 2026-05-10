### Ejercicio 1 de ciclos for
## Enunciado: Dada una lista de valores, imprimir simultáneamente el primer y último valor, el segundo y el penúltimo, el tercero y el antepenúltimo, etc.
# Respuesta: 
# lista_valores = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
# cantidad_de_valores = len(lista_valores) # length 
# # print(cantidad_de_valores) # 20

# for i in range(0, int(cantidad_de_valores/2)):
#     print(f"valor 1 = {lista_valores[i]}")
#     print(f"valor 2 = {lista_valores[cantidad_de_valores - 1 - i]} \n")
#     print(f"valor 2 = {lista_valores[-1 - i]} \n")

### Ejercicio 2 de ciclo for
## Enunciado: Dada una lista de frutras, eliminar todas las manzanas
# Respuesta ["Pera", "Naranja", "Banana", "Uva"]
# lista = ["Manzana", "Pera", "Naranja", "Banana", "Uva", "Manzana", "Manzana", "Manzana"]
# copia_lista = lista.copy()
# for fruta in lista:
#     if fruta == "Manzana":
#         copia_lista.remove(fruta)
# print(copia_lista) # ['Pera', 'Naranja', 'Banana', 'Uva']


### Ejercicio 3 
# Suma de elementos
# Dado un arreglo de números, calcula la suma total usando for.
# arr = [3, 5, 7, 2, 8]



### Ejercicio 4
# Contar ocurrencias
# Dado un arreglo de números y un valor específico,
# cuenta cuántas veces aparece un número específico en una lista.
# arr = [1, 2, 3, 2, 4, 2, 5]
# valor = 2



### Ejercicio 5
# Encontrar el máximo
# Encuentra el valor más grande del arreglo sin usar max().
# arr = [10, 3, 25, 7, 18]


### Ejercicio 6
# Contar números pares
# Cuenta cuántos números pares hay en la lista.
# arr = [1, 4, 6, 9, 10, 13]


### Ejercicio 7
# Invertir lista
# Crea una nueva lista con los elementos en orden inverso usando for.
# arr = [1, 2, 3, 4, 5]


### Ejercicio 8
# Filtrar valores mayores a X
# Construye una nueva lista con los valores mayores a un número dado.
# arr = [5, 12, 7, 20, 3]
# x = 10


### Ejercicio 9
# Contar vocales en un string
# Cuenta cuántas vocales hay en un texto.
# texto = "data science"


### Ejercicio 10
# Eliminar duplicados (sin usar set)
# Crea una nueva lista sin elementos repetidos, respetando el orden original.
# arr = [1, 2, 2, 3, 4, 3, 5]