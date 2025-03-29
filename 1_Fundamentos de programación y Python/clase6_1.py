#CLASE 6 
#OPERADORES ARITMETICOS EN PYTHON
print("OPERADORES ARITMETICOS")
print("Se definen las variables x e y:")
x=10
y=3
print("x =", x)
print("y =", y)
print("La suma (+) es:", x+y)
print("La resta (-) es:", x-y)
print("La multiplicación (*) es:", x*y)
print("x con pontencia (**) y es:", x**y)
print("x dividido (/) y es:", x/y)
print("Es residuo (%), resto o modulo de x/y es:", x % y)
print("La parte entera (//) de x/y es:", x//y)

print("La regla que se sigue para seguir un orden en las operaciones matematicas, memotecicamente se recuerda como:")
print("Las operaciones se ejecutan de izquierda a derecha")
print("P.E.M.D.A.S")
print("P: Parentesis")
print("E: Exponetes o potenciación")
print("M: Multiplicación")
print("D: División")
print("A: Adición")
print("S: Sustracción")
#P.E.M.D.A.S
#Parentesis0
#Exponenciación 
#Multiplicación
#División
#Adición 
#Sustracción

print("Ejemplo 1: Operacion_1= 2*5+6")

operacion_1= 2*5+6   # Aplicando PEMDAS, sin parentesis 
print("El resltado es:", operacion_1)
operacion_2= 2*(5+6) #En esta opercación se le indica el orden, es decir tiene parentesis, según PEMDAS se inicia por el parentesis 

print("Ejemplo 2: Operacion_2= 2*(5+6)")
print("El resultado es:", operacion_2)


print("Ejemplo 3: Operacion_3= 5/6 + 3/2")
operacion_3= 5/6 + 3/2
print("Elresultado es:",operacion_3) # NO se indica la operación, la operación se realiza de izquierda a derecha Aplicando PEMDAS

print("Ejemplo 4: Operacion_3= 5/(6 + 3)/2")
operacion_4= 5/(6+3)/2
print("El resultado es:",operacion_4) # Se indica la operación y la realiza de izquiera a derecha

#OTRA FORMA DE HACER OPERACIONES MATEMATICAS

print("OTRA FORMA DE EFECTUAR OPERACIONES MATEMÁTICAS ES CON ATAJOS O SHORTCUTS:")

# SUMA
print("SUMA") 
print("Si a = 4 , a+4 se puede hacer tambien como:")
print("a+=4")
a= 4
a+=4
print("El valor de a+4  es:",a )

# MULTIPLICACIÓN
print("MULTIPLICACIÓN") 
print("Si a = 4 , a*3 se puede hacer tambien como:")
print("a*=3")
a= 4
a*=3
print("El valor de a*3  es:",a )

# DIVISIÓN
print("DIVISIÓN") 
print("Si a = 4 , a/2 se puede hacer tambien como:")
print("a/=2")
a= 4
a/=2
print("El valor de a/2  es:",a )

print("OPERADORES BOOLEANOS Y OPERADORES DE COMPARACIÓN")

print("Se definen a=10 y b=3")

a=10 
b=3 
a>b
a<b 

print("Si comparamos: ¿a>b? el resultado es:", a>b, ";- Es verdadero" )
print("Si comparamos: ¿a<b? el resultado es:", a<b, ";- Es Falso" )