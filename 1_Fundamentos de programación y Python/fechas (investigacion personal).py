# Es necesario imnportar las dependencias necesarias para trabajar con fechas 
from datetime import date     # Una funcion de python para fechas
from datetime import datetime # Una funcion de python para fechas y hora
from dateutil import date       
# Existen otras librerias para darle formato a los textos en la consola como COLORAMA, se importaran algunas 

# from colorama import Back, Fore, Style, init (Como esta dando problema para la importación se comenta la linea)

# Fecha actual, método today
print("   CONSULTEMOS QUE FECHA ES HOY:")
today=date.today()
print ("Usando 'today' se imprime la fecha de hoy: ", today)

# Fecha actual con la hora, método now
now = datetime.now()
print("Usando,'now', se imprime la fecha de hoy con la hora: ", now)

# Se puede consultar especificamente , día, mes , año, 


print("El dia actual es {}".format(today.day), "Obtenido con el método today")
print("El mes actual es {}".format(today.month),"Obtenido con el método today")
print("El año actual es {}".format(today.year),"Obtenido con el método today")

print("El dia actual es {}".format(now.day),"Obtenido con el método now")
print("El mes actual es {}".format(now.month),"Obtenido con el método now")
print("El año actual es {}".format(now.year),"Obtenido con el método now")

print("La hora actual es {}".format(now.hour))
print("Los minutos actuales son {}".format(now.minute))
print("Los segundos actuales son {}".format(now.second))

format = now.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S')
print(format)

def current_date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "{} de {} del {}".format(day, month, year)

    return messsage

now = datetime.now()
print(current_date_format(now))

fecha=date.today()
fecha = dateutil.parser.parse(fecha)
fecha = fecha.strftime('%d / $m / %Y') # Para dar formato

nombre= "jesus"

print("Cambiar a mayuscula mi nombre ".upper())
print(nombre.upper())



