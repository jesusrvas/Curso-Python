#La recursividad o recursión es un concepto que proviene de las matemáticas, y que aplicado al
#mundo de la programación nos permite resolver problemas o tareas donde las mismas pueden
#ser divididas en subtareas cuya funcionalidad es la misma. Dado que los subproblemas a
#resolver son de la misma naturaleza, se puede usar la misma función para resolverlos. Dicho
#de otra manera, una función recursiva es aquella que está definida en función de sí misma, por
#lo que se llama repetidamente a sí misma hasta llegar a un punto de salida.

"""
Cualquier función recursiva tiene dos secciones de código claramente divididas:

1) Por un lado tenemos la sección en la que la función se llama a sí misma.
2) Por otro lado, tiene que existir siempre una condición en la que la función retorna sin volver a llamarse. 
Es muy importante porque de lo contrario, la función se llamaría de manera indefinida.

"""

# RETO: Hacer la sumatoria de los número enteros 

def sumatoria(n):
    if n==1: 
        return n
    else : 
        return sumatoria(n-1)+n

print(sumatoria(6))

    