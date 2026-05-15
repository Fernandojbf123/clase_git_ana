#### Operadores lógicos ####
# igual que   == 
# diferente de !=
# mayor que   >
# menor que   <
# mayor o igual que >=
# menor o igual que <=

# num1 = 5
# num2 = 5
# resultado = num1 == num2
# print(resultado) # True

# num1 = 5
# num2 = 5
# resultado = num1 != num2
# print(resultado) # False

# print(5 > 3)  # True
# print(5 < 3)  # False
# print(5 >= 5) # True
# print(5 <= 3) # False

########## and y or se conocen como condicionales ############
# num1 = 5
# num2 = 3
# num3 = 9
# num4 = 10

# # resultado = (num1 > num2) and (num3 > num4) and (num1 > num3)
# # print(resultado) # False

# resultado = (num1 > num2) or (num3 > num4)
# print(resultado) # True


###########################################
#Tambien sirven para palbras

archivos = ("20260506_clase.txt", "20260507_clase.txt", "20260508_clase.txt", "20260505_carga.txt", "20260506_carga.txt","20260507_carga.txt", "20260508_carga.txt")
archivo4 = archivos[4]

resultado = "clase" not in archivo4 and "historia" not in archivo4
print(resultado)