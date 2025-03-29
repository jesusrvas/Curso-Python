# LISTAS
# Una caracteristica de las listas es que tenemos la libertad de guardar la información, cualquier tipo de dato
print("\n")
print("La lista to_do, es una lista de las cosas que tengo que hacer hoy por la mañana:")
print("\n")
 
to_do= [
      "Ir a poner gasolina",
      "Conducir hacia caracas",
      "Entrar a la oficina",
      "Actualizar la BD",
      "Hacer pruebas en el sistema"
] 
print("\n")
print("to_do=",to_do)
print("\n")
print("El tipo de dato de la lista to_do es: - ",type(to_do), " - Es tipo List, lista, List es palabra reservada")
print("\n")
print("Podemos crear lista con diferentes tipos de datos , creamos la lista mix")
print("\n")
mix= [
    1,
    "dos",
    3.14,
    True,
    False,
    to_do,
    ["calma", "Seguridad","Confianza"]
]
print("\n")
print("mix=",mix)
print("El tipo de dato de la Lista mix es : - ",type(mix), " - Tipo List") 

# LAS LISTAS AL IGUAL QUE LAS CADENAS , TAMBIEN TIENEN  INDEXACIÓN
# SI NECESITO EXTRAER EL ELEMENTO 4 DE LA LISTA mix lo hago con mix[4]
print("\n")
print("Si necesito extraer de la lista mix el elemento 4 los hago con mix[4]")
mix[4]

print("El elemento que ocupa la pocisión 4 en la lista mix es -:", mix[4])
print("Si necesito extraer de la lista mix el primer elemento  lo  hago con mix[0]")
mix[0]
print("El elemento que ocupa la primera pocisión en la lista mix es -:", mix[0])

# PODEMOS SELECCIONAR PORCIONES DE UNA LISTA O CADENA USANDO SLICING 

print(mix[0:2])  # Imprime hasta una pocisión antes de la que se indica en el corchete, hasta la 1

mix[0]="Uno"
print("Se cambio el primer elemento, 1 por uno",mix)

string= "Hasta la victoria siempre"

print(string[0]) 



print(string[0:5])  # Imprime la palabra Hasta
print("\n") 

#EXISTEN MÉTODOS PROPIOS DE LAS LISTAS PARA AGREGAR ELEMENTOS A LAS LISTA 
print("mix=", mix)
print("Usando el método append:")
mix.append("Nuevo elemento")
print("mix=",mix,"SE AGREGO UN ELEMENTO NUEVO AL FINAL DE LA LISTA")
print("Usando el método inster") # Inserta un elemento en la pocision indicada 
mix.insert(3,"CHUCHO")
print("mix=",mix,"SE AGREGO UN ELEMENTO EN LA POCISIÓN 3 ")

# TAMBIEN SE PUEDE DETERMINAR MÁXIMOS Y MÍNIMOS EN LISTAS DE NÚMEROS CON LAS FUNCIONES MAX Y MIN

numbers=[47,52,17,6,8]

print("El máximo es:",max(numbers)) 

print("El minimo es:",min(numbers)) 

print(type(numbers))



