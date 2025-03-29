# CONTINUACIÓN CLASE 3

# INDEXACIÓN EN LAS CADENAS O STRINGS: En toda cadadena, cada caracter tiene una pocisión asignada 
firstname='JESUS ramón' 
lastname= '      Rivas   Herrera      '
print("Imprime la pocisión cero en el string firstname:", firstname [0])
print(firstname [6])
print(firstname [5])
print(firstname [6])
print("Imprime la última pocisión string firstname:", firstname [-1]) # la pocisión [-1] es la última del string
print(firstname [-2])   # la pocisión [-2] es la penúltima pocisión del string
print(firstname [-3])
print("Imprime 3 veces sin espacio el string firstname: ",3*firstname)
print("Imprimendo la variable lastname:",lastname)
print("Aplicando el método strip:",lastname.strip())  # El método strip propio de los strings, elimina a la izquierda y derecha 
                                                      #el carácter que se le introduce. Si se llama sin parámetros elimina los 
                                                      # espacios. Muy útil para limpiar cadenas.
print("Aplicando el método strip:",firstname.strip("J"))

is_true=True 
is_false=False 
print(is_false)         
print(type(is_true))   #Tipo de dato Booleano

print("MÉTODOS PROPIOS DE LOS STRING \n (CADENAS DE CARACTERES)")
print(len(firstname))   # len, es una funcion que cuenta cuantos caracteres tiene un string
print(firstname.upper()) # upper, Es un método de los strings, para colocar todo el string en MAYUSCULA
print(firstname.lower()) # lower, Es un método de los strings, para colocar todo el string en MINUSCULA
print(firstname.capitalize()) # capitalize, Es un método de los strings, coloca la primera letra en mayúscula y el resto en minúscula
#prueba="@"
print("Cuenta las veces que aparece el caracter J en el string firstname:",firstname.count("J"))   # count, es un método de los strings que cuenta las apariciones dentro del strig 
                              # del catacter que se indica dentro del parentesi
                              
                                 









