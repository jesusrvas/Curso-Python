#OPERACIONES DE ENTRADA Y SALIDA EN LA CONSOLA 

print("OPERACIONES DE ENTRADA Y SALIDA EN LA CONSOLA")
print("USO DE LA FUNCIÓN INPUT")
print("Usamos la fución input para capturar información del usuario")
print("Ejemplo: Queremos saber el nombre y la edad")

nombre= input("Indique su Nombre")
print("Para ver el nombre que ingreso el usuario en la consola, usamos la funcion print")
print(nombre)

edad=input("Indique su edad")
print("Para ver la edad que ingreso el usuario en la consola , usamos la función print")
print(edad)   

# EL TIPO DE DATO QUE OFRECE DE LA SALIDA LA FUNCIÓN INPUT , SIEMPRE SERÁ UN STRING
#POR LO QUE PARA PODER OPERAR CON ELLOS ES NECESARIO HACER UN ARTIFICIO QUE SE LLAMA "CASTING"

print("Veamos el tipo de dato de las variables nombre y edad ")

print("El tipo de dato de la variable nombre es - :", type(nombre), "Tipo de dato string")
print("El tipo de dato de la variable edad es - :", type(edad), "Tipo de dato string") 

print("A pesar de que la edad se ingreso como integer , el tipo de dato de salida fue un string")

print("CASTING: Consiste en anteponer a la función input, el tipo de dato que debe esperar como entrada")

print("Por ejemplo int(input(ingrese su edad))") 

edad2=int(input("Ingrese nuevamente su edad")) 

print("El tipo de dato de la edad ahora es: -", type(edad2), " - es Entero como queriamos") 


