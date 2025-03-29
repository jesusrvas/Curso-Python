# PPO: Paradigma de programación que busca representar la realidad mediante el uso de, Clases contentivas de 
# atributos y métodos que son propios de los mismos

#Atributos: Son caracteristicas de los objetos o clases.
#Métodos: Son cosas que pueden realizar los objetos o las clases

#########################EJEMPLO DE LA CUENTA DE BANCO##################

class BankAccount:
    #Se define el construcctor de la clase, los atibutos y caracteristicas de los objetos  
    def __init__(self,account_holder:str,balance:int):
        self.account_holder=account_holder
        self.balance=balance
        self.is_active=True

    #Se define un método de clase , deposit (Deposito)

    def deposit(self, amount):
     if self.is_active:
         self.balance +=amount
         return print(f"Se ha realizado un deposito por {amount} , y su saldo es {self.balance}")
     else:
         return print(f"No se puede depositar cuaneta inactiva")

    #Se define un método de clase , withdraw (Retiro)
    def withdraw(self,amount):
        if self.is_active== True:
            self.balance-=amount
            return print(f"Se ha realizado un retiro por {amount} y su saldo en cuenta es {self.balance}")
        else:
            return print("Su cuenta está inactiva , no es posible realizar la operación solicitada")

    # Se define el método para desactivar cuenta

    def inactive_account(self):
        self.is_active=False
        print("La cuenta fue desactivada")

    # Se define el método para activar cuenta

    def active_account(self):
        self.is_active=True
        print("La cuenta fue activada")    


# Crearemos dos objetos, es decir dos cuentas 

cuenta1=BankAccount("Ana",1500)
cuenta2=BankAccount("Jesus", 2500)

#Llamamos los métodos 

cuenta1.deposit(150)
cuenta2.withdraw(1250)
cuenta1.inactive_account()
cuenta1.withdraw(500)





