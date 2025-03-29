# COMPREHESION LIST : Una forma más simplificada de construir listas usando 
# el FOR y el if en una sola linea de código

matrix=[[1,2,3],
        [4,5,6],
        [7,8,9],
        [10,11,12]]

matrix2=[[1,2,3,20],
        [4,5,6,21],
        [7,8,9,22],
        ]

#print(matrix[0])
#print(matrix2[0])

transpose=[[row[i] for row in matrix] for i in range(len(matrix[0]))]


#print(matrix)
#print(transpose)

#print(matrix[1])
#print(matrix2[1]) 

#print(len(matrix[1]))
#print(len(matrix2[1]))




#print("Numero de filasd de matrix=",len(matrix))
#print("Número de filas de matrix2=", len(matrix2))


# CÓDIGO PARA HALLAR LA TRANSPUESTA DE UNA MATRIZ, MEDIANTE ESTRUCTURAS DE CONTROL DE FLUJO

# Se define la variable que almacenara la matriz transpuesta

transpuesta=[]

for i in range(len(matrix[0])):
        transposed_row=[]      #Almacena la fila i-esima de la transpuesta
        for row in matrix:
           
           transposed_row.append(row[i])
        transpuesta.append(transposed_row)

#print(transpuesta)                    
 
 #EJERCICIOS.
 # 1) Doble de los números: 
num=[1,2,3,4,5]

doble_num=[2*num[i] for i in range(len(num))]

#print("Resultado del ejercicio 1 =",doble_num)

#print(len(num))

# 2) Filtrar y transformar en solo paso: Obtener una nuebva lista con las palabras que contengan.
#    más de tres (3) letras y estén en mayusculas

palabras=["sol","mar","montaña","rio","estrella"]

palabras2=[palabras[i].upper() for i in range(len(palabras)) if len(palabras[i])>3]

#print("Resultado del ejercicio 2:",palabras2)

#EJERCICIO 3: CREAR UN DICCIONARIO CON LIST COMPREHENSIONS: Tienes dos listas , una de claves y otra de
# valores. Crear un diccionario combinando ambas listas usando una list comprehensions 

claves=["Nombre","Edad","Ocupación"]
valores=["Juan",30,"Ingeniero"] 

dicionario={claves[i]:valores[i]  for i in range(len(claves))}

#print("Este es el dicionario usando List comprehnsions: ", dicionario)

# EJERCICO 4: EL MISMO DE LA CLASE

#EJERCICIO 5 : Extraer información de una lista de diccionarios. Dado una lista de dicionarios
# que representa personas, extrae una lista de nombres que viven en "Madrid" y tienen más de 
# 30 años   
 
personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]
#personas[1]

#print(personas[0].values())

#filtro=[personas[i].values() for i in range(len(personas)) if "ciudad"=="Madrid" and "edad" > 30]

#print(len(personas))

filtro=[personas["nombre"] for personas in personas if personas["ciudad"]=="Madrid" and personas["edad"] > 30]
print(filtro)


# LIST COMPRENHENSIONS CON UN ELSE: Dada una lista de números , crea una nueva lista multiplicando por dos.
#los números pares y dejando los impares como estan.
# 


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nueva_lista = [2*x if x%2==0 else x for x in numeros]

print(nueva_lista)

print(matrix[0])
