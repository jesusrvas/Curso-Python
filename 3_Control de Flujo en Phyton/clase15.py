# BLUCLES Y CONTROL DE ITERACCIONES 

# BUCLE FOR: Significa para.. se sefiere a que, para cada valor de una SECUENCIA o GRUPO , realizara
#            una determinada acción, lo que significa que el flujo es finito, o se termina cuando haga todo el recorrido

numbers=[1,2,3,4,5,6,7,8,9]

for i in numbers :
    i
    if i==5:
        #break            # Para el flujo inmediatamente e imprime solo hasta 4 < 5 
        continue          # Continua con el flujo saltando el valor i=5 

    print("El valor de i en esta vuelta es:", i)


# BUCLE WHILE : El bucle while ejecuta un bloque de código mientras se cumpla una condición.
#               hay que estar pendinente de la condición ya que se puede generar bucle infinito. 


ege= int(input("ingresa tu edad"))
while ege<57 :
    print("Te falta aún para la Jubilación, ahorita tienes:",ege)
    ege+=1

    if ege>=50 and ege < 55 : 
         print("Mosca te estás poniendo viejo, tienes:", ege)
    elif ege >= 55 and ege < 60:
         print("Oficialmente eres adulto mayor, ahora tienes:", ege)
    else:
         print("Ya pide tu jubilación,tienes:", ege) 

