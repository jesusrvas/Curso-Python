# ESTRUCTRURAS DE CONTROL DE FLUJO , USO DEL IF 
#  JUEGO: PIEDRA PAPEL O TIJERA

playe1=input("JUGADOR 1 Seleciona tu jugada, PIEDRA, PAPEL o TIJERA")
player2=input("JUGADOR 2 Selecciona tu jugada, PIEDRA, PAPEL o TIJERA")

if playe1=="PAPEL":
    if player2=="PIEDRA":
        print("PAPEL ENVUELVE LA PIEDRA, GANA JUGADOR 1")
    elif player2=="TIJERA":
        print("TIJERA CORTA PAPEL, GANA JUGADOR 2")
    elif player2=="PAPEL":
        print("SE REPITE LA JUGADA AMBOS JUGADORES SELECCIONARON PAPEL")
    else:
        print("JUGADOR 2 NO SELECCIONO SU JUGADA CORRECTAMENTE")           
elif playe1=="TIJERA":  
    if player2=="PIEDRA":
        print("PIEDRA APLASTA TIJERA, GANA JUGADOR 2")
    elif player2=="TIJERA":
        print("SE REPITE LA JUGADA, AMBOS JUGADORES SELECCIONARON TIJERA") 
    elif player2=="PAPEL":
        print("TIJERA CORTA PAPEL, GANA JUGADOR 1") 
    else:
        print("JUGADOR 2 NO SELECCIONO SU JUGADA CORRECTAMENTE")
elif playe1=="PIEDRA":  
    if player2=="PIEDRA":
        print("SE REPITE LA JUGADA, AMBOS JUGADORES SELECCIONARON PIEDRA")
    elif player2=="TIJERA":  
        print("PIEDRA APLASTA TIJERA, GANA JUGADOR 1")
    elif player2=="PAPEL":
        print("PAPEL ENVUELVE LA PIEDRA, GANA JUGADOR 2")
    else:
        print("JUGADOR 2 NO SELECCIONO SU JUGADA CORRECTAMENTE")
else:   
    print("no se puede jugar, LOS JUGADORES NO REALIZAN SU JUGADA CORRECTAMENTE")     




#x=50
#if x==50 :
#    print("la variable es igual a 50")
#elif x>50 :
#    print("la variable es mayor que 50")    
#elif x<50:
    #print("la variable es menor que 50") 

#else:
#    print("la variable es menor que 50 por aqui pasa el else") 

