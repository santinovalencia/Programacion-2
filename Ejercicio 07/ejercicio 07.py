from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

fechaN=0
fechaE=""
dif=0
meses=0
mes=0
edad=0
anios=0
naci=0
now=0
diasT=0
dia=0


fechaN = input("Ingrese su fecha de nacimiento (DD/MM/AAAA): ")

fechaE = datetime.strptime(fechaN, "%d/%m/%Y")
dia = datetime.now()

dif = dia - fechaE

print("Su edad en días es de", dif.days)
print("Su fecha de nacimiento es:", fechaE.strftime("%d de %B de %Y"))
