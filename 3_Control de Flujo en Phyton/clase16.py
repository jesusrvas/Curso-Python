#GENERADORES E ITERADORES

  # Una clase iterable es una clase que puede ser iterada. Dentro de Python hay gran cantidad de clases iterables
  # como las listas, strings, diccionarios o ficheros. Si tenemos una clase iterable, podemos usarla a la derecha
  # del for de la siguiente manera.  
        # for elemento in [clase iterable]
  #ITERADORES: Va iterando cada uno de los elementos sin utilizar indices
  #Se podría explicar la diferencia entre iteradores e iterables usando un libro como analogía.
  # El libro sería nuestra clase iterable, ya que tiene diferentes páginas a las que podemos acceder.
  # El libro podría ser una lista, y cada página un elemento de la lista. Por otro lado, el iterador sería un
  # marcapáginas, es decir, una referencia que nos indica en qué posición estamos del libro, y que puede ser usado
  # para “navegar” por él.
    
#EJEMPLO DE ITERADOR

my_list=[1,2,3,4]    #Se crea una lista         

my_iter=iter(my_list)  #Obtener el iterador

#Usando el Iterador

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


# UNA FUNCION 

def fucion1():
    return 500

print(fucion1())


#OTRA FUNCION

def funcion2(a,b):
    c=a+b
    return c

print("Este es el valor de funcion2 evaluada en (2,3)=", funcion2(2,3))


# EJEMPLO DE GENERADOR : La aplicación que he visto hasta el momento es la construcción o GENERACIÓN DE SERIES 
# como la serie de Finonacci [0,1,1,2,3,5,8,13,21,34,.....], el siguiente valor de la serie se obtiene sumando los dos 
# valores anteriores

def Fibonacci(limit):
    a,b=0,1
    while a < limit:
           yield a
           a=b
           b=a+b

#print(Fibonacci(3))

""""
print(next(Fibonacci(3)))
print(next(Fibonacci(3)))
print(next(Fibonacci(3)))

"""
for num in Fibonacci(1): 
     print(num)


# RETO: Crear los generadores para los numeros pares e impares
#serie_par[2,4,6,8,10,...]
#serie_impar=[3,5,7,9..]

"""""
#SERIE PAR
def serie_par(limit):
     a=0
     
     while  a < limit :
          if   a%2==0:
            yield a
          a+=1  
    

for num2 in serie_par(21):
     print(num2)
"""     

# SERIE IMPAR 

def serie_par(limit):
     a=0
     
     while  a < limit :
          if   a%2==1:
            yield a
          a+=1  
    

for num2 in serie_par(21):
     print(num2)  



