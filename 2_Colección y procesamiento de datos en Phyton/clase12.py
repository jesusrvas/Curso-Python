# DICCIONARIOS: Son estructuras que guardan basicamente dos datos, la clave y el valor  

print("Este es un diccionario con mis datos:")
mis_datos= {"Nombre":"Jesús","Apellido":"Rivas","Edad":47}

print(mis_datos) 
print("TIPO:",type(mis_datos))
llaves= mis_datos.keys()

print("Estas son las llaves:",llaves)

popitem= mis_datos.popitem()

print("Esta es el resultado del método popitem:",popitem)

valores=mis_datos.values()
print("Este es el resultado del método valores:",valores)


pairs=mis_datos.items()
print("Este es resultado del método items:",pairs)  

# HAREMOS UN DICIONARIO DE DICIONARIO 

grupo_familiar={"Charallave":{"integrantes":4,"niños":2},
                "La pastora":{"integrantes":3,"niños":1},
                "La candelaria":{"integrantes":3,"niños":1},
                "los magallanes1":{"integrantes":2,"niños":0},
                "los magallanes2":{"integrantes":4,"niños":2},
               }

print("Este es un diccionario de diccionario:", grupo_familiar)

# SELECCIONAMOS ELEMENTOS DEL DICIONARIO 

print("este es el dato que ocupa la pocición 2 en mis datos: ", mis_datos["Apellido"])
                 
print(grupo_familiar["Charallave"]) 
           
print(grupo_familiar["Charallave"]["niños"])                