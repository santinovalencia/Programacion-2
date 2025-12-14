nombre=""
Edad=0
fechaNA=0
year=0

print("¿como te llamas?")
nombre=input()

print("¿en que year naciste?")
fechaNA=int(input())

print("ingrese año actual")
year=int(input())

Edad=year-fechaNA

print("hola",nombre, "tu edad es:", Edad)