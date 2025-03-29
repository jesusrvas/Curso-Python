# EXCEPCIONES: Son saltos que se establecen al código , cuando anticipadamente sabemos cual pudiera 
# ser el error que se genera durante la ejecución del mismo , de manera que el flujo de la ejecución
# no se detiene, se marca con la palabra reservada "try" y se anota el mensaje con la palabra reservada 
# "execep"

#Las excepciones en Python están organizadas en una jerarquía de clases, donde lasexcepciones más generales
#se encuentran en la parte superior y las más específicas en la parte inferior.
# Esta organización jerárquica permite a los programadores manejar excepciones de manera más precisa y efectiva.



 

x= 100
divisor=int(input("Ingrese un valor para el divisor:"))
try:
 division=x/divisor     
except ZeroDivisionError:
 print("Error: No es posible la división por cero ") 
try :
   print("El resultado de la dicvisión es :", division)
except NameError:
  print("Error: No se definio una variable")

############################################################################
print("############################################################################")
print("#############JERARQUIA DE EXCEPCIONES#####################################")

def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

# Imprimir la jerarquía comenzando desde la clase base Exception
print_exception_hierarchy(Exception)
