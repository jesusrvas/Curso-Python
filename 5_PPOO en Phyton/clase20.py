# PPO: Paradigma de programación que busca representar la realidad mediante el uso de, Clases contentivas de 
# atributos y métodos que son propios de los mismos

#Atributos: Son caracteristicas de los objetos o clases.
#Métodos: Son cosas que pueden realizar los objetos o las clases

##DEFINIENDO MI PRIMERA CLASE
#from curses import def_prog_mode


class Cuenta():
    #Se define el construcctor de la clase, los atibutos y caracteristicas de los objetos  
    def _init_(self,account_holder:str,balance:int):
        self.account_holder=account_holder
        self.balance=balance
        self.is_active=True

    #Se define un método de clase , deposito a las cuentas

    def deposit(self, amount):
     if self.is_active:
         self.balance +=amount
         return print(f"Se ha realizado un deposito por {amount} , y su saldo es {self.balance}")
     else:
         return print(f"No se puede depositar cuaneta inactiva")

    def retiro(self,amount):
        if self.is_active== True:
            self.balance-=amount
            return print(f"Se ha realizado un retiro por {amount} y su saldo en cuenta es {self.balance}")
        else:
            return print("Su cuenta está inactiva , no es posible realizar la operación solicitada")

# Crearemos dos objetos, es decir dos cuentas 

cuenta1=Cuenta("Ana",1500)
cuenta2=Cuenta("Jesus", 2500)

#Llamamos los métodos 

cuenta1.deposit(150)
cuenta2.retiro(1250)





"""        
def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))

"""