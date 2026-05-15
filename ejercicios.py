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
arr = [3, 5, 7, 2, 8]

suma = 0

for numero in arr:
    suma = suma + numero

print(suma)


### Ejercicio 4
# Contar ocurrencias    
# Cuenta cuántas veces aparece un número específico en la lista.
arr = [1, 2, 3, 4, 2, 5, 2]
valor = 2       

contador = 0
for numero in arr:
    if numero == valor:
        contador +=1

print(f"El numero {valor} aparece {contador} veces en arr")



### Ejercicio 5
# Encontrar el máximo
# Encuentra el valor más grande del arreglo sin usar max().
arr = [3, 5, 7, 2, 8]
maximo = arr[0]

for numero in arr:
    if numero > maximo:
        maximo = numero

print(f"Encuentra el maximo valor mas grande sin usar max() = {maximo}")


### Ejercicio 6
# Contar números pares
arr = [1, 4, 6, 9, 10, 13]
contado = 0

for numero in arr:
    if numero /2 == 0:
        contador +=1

print(f"cuantos numeros pares hay en arr = {contador}")


### Ejercicio 7
# Invertir lista
# Crea una nueva lista con los elementos en orden inverso usando for.

# lista original de arr
arr = [1, 2, 3, 4, 5]

# nueva lista de arr inversa
lista_arr_inversa = []

# for i in range(len(arr)-1, -1, -1):
#     lista_arr_inversa.append(arr[i])

for numero in arr:
    lista_arr_inversa.insert(0, numero)


print(f"lista arr original = {arr}")
print(f"lista arr inversa = {lista_arr_inversa}")


### Ejercicio 8
# Filtrar valores mayores a X
# Construye una nueva lista con los valores mayores a un número dado.
arr = [5, 12, 7, 20, 3]
x = 10
resultado =[]

for numero in arr:
    if numero > x:
        resultado.append(numero)

print(f"valores mayores a {x} in arr = {resultado}")


### Ejercicio 9
# Contar vocales en un string
# Cuenta cuántas vocales hay en un texto.
texto = "data science"

vocales = "aeiouAEIOU"
contador = 0

for letra in texto:
    if letra in vocales:
        contador +=1

print(f"cantidad de vocales en el texto = {contador}")


### Ejercicio 10
# Eliminar duplicados (sin usar set)
# Crea una nueva lista sin elementos repetidos, respetando el orden original.

arr = [1, 2, 2, 3, 4, 3, 5]
resultado = []
for numero in arr:
    if numero not in resultado:
        resultado.append(numero)

print(resultado)

