# MÉTODO SLICE: Una forma de utilizar un espacio en memoria distinto al que usamos cuando definimos
# una variable 
print("Definimos las variables a y b")

a= [2,4,6,8,10]
b=a 

print("a=",a)
print("b=",b)

print("Si realizamos una modificación en a, b tambien efectua el cambio")
print("Esto se debe a que ambas comparten el mismo espacio en memoria, veamos:") 
print("Es espacio en memoria de a es:",id(a))
print("Es espacio en memoria de b es:",id(b))

print("Haciendo una modificación en a, ¿Que pasa con b?")

a.append(120)     #append es un método propio de las listas, que agrega un elemento 

print("a=",a)
print("b=",b)

print("b sufre el cambio en a, ya que comparten espacio en memoria")
print("Si definimos una varible c, a partir de a pero usando un SLICE, la nueva variable no subre los cambios de a")

c=a[:]     # Esto es un SLICE 

print("a=",a)
print("b=",b)
print("c=",c)

print("realicemos otra modificación en a")

print("Se procede a elimnar el elemnto 2 de a")
del a[2]
print("a=",a)
print("b=",b)
print("c=",c)
print("Los cambios de a afectaron a b, pero no a c")



