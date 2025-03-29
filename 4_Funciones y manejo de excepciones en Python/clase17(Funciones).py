# FUNCIONES: Se construyen usando la palabra reservada "def" seguida del nombre de la función y finalmente
#            los parametros necesarios para que la función pueda ejecutarse. La función retornara el valor que se 
#            se le indique en linea return


#EJEMPLO 1
"""
def suma(a,b):
    return a+b

#print(suma(2,3))

# EJEMPLO 2: CONSTRUIR UNA CALCULADORA

def resta(a,b):
    return a-b

def multiplicación(a,b):
    return a*b

def división(a,b):
    return a/b

def calculadora():
     while True:   
        print("Seleccione una operación:")
        print("1.Suma")
        print("2.Resta")
        print("3.Multiplicación")
        print("4.División")
        print("5.Salir")
         
        opciones=int(input("Ingrese su opción (1,2,3,4,5): "))
        
        if opciones==5:
            print("Saliendo de la calculadora") 
            break

        else: opciones in [1,2,3,4]:  
        num1=float(input("Ingrese el primer valor"))
        num2=float(input("Ingrese el segundo valor"))

        if opciones==1:

            print("El valor de la suma es: ",suma(num1,num2))
                
        elif opciones==2: 
                 
                print(resta(num1,num2))
                
        elif opciones==3:

                print(multiplicación(num1,num2)) 
                
        elif opciones==4:
                print(división(num1,num2))  

                   
        else:   
              print("La opción ingresada no es válida")   

calculadora() 
"""
#list=[1,2,3,4,5]

#print(type(list))
"""
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calculadora():
    while True:
        print("Seleccione una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        opcion = int(input("Ingrese su opción: "))
        
        if opcion == 5:
            print("Saliendo de la calculadora.")
            break
        
        if opcion in [1, 2, 3, 4]:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            
            if opcion == 1:
                print("La suma es:", suma(num1, num2))
            elif opcion == 2:
                print("La resta es:", resta(num1, num2))
            elif opcion == 3:
                print("La multiplicación es:", multiplicar(num1, num2))
            elif opcion == 4:
                print("La división es:", dividir(num1, num2))
        else:
            print("Opción no válida, por favor intente de nuevo.")

calculadora()
"""

def condicional():
     name=input("Ingrese su nombre: ")

     if len(name) < 6:
          print("su nombre es corto")
     elif 5 < len(name) <8:
          print("Su nombre es medianamente largo")
     elif len(name) >= 8:
          print("Su nombre es muy largo")         
   
     return name         
condicional()