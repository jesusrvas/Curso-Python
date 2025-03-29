# MATRICES: Son como listas de lista o listas dentro de listas, al igual que las listas de una dimensión
#           son modificables y siguen la misma notación de una sola dimensión, el nombre de la variable
#           y la pocisión entre []

print("Se define la matris, matrix")
matrix=[[1,2,3],
       [4,5,6],
       [7,8,9]]

print("matrix=",matrix)

print("¿Que tipo de objeto o tipo de dato es matrix?")
print(type(matrix))



print("Elemento 0 de matrix=",matrix[0])     # imprime la primera fila de matrix
print("El elemento 1 de matrix=",matrix[1])  # imprime la sefunda fila de matrix
print("El elemento 2 de matrix=",matrix[2])  # imprime la tercera fila de matrix


print("El elemento (0,0) de matrix=",matrix[0][0]) # Imprime el elemento (0,0) de matrix
print("El elemento (0,1) de matrix=",matrix[0][1]) # Imprime el elemento (0,1) de matrix
print("El elemento (0,2) de matrix=",matrix[0][2])
print("El elemento (1,0) de matrix=",matrix[1][0])
print("El elemento (1,1) de matrix=",matrix[1][1])
print("El elemento (1,2) de matrix=",matrix[1][2])
print("El elemento (2,0) de matrix=",matrix[2][0])
print("El elemento (2,1) de matrix=",matrix[2][1])
print("El elemento (2,2) de matrix=",matrix[2][2]) # Imprime el elemento (2,2) de matrix

# TUPLAS: Es otro tipo de arreglo como las matrices , pero estas NO SON MODIFICABLES. 
#         se construllen usando paretesis o sin los parantesis pero siempre separados por (,)

print("\n")
tupla=(1,2,3,4,5,6,7,8,9)
print("El valor que ocupa la pocosión 2 en la tupla es: ",tupla[2]) 
