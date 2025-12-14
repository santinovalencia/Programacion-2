resultado=0
caramelos=0
estudiantes=0
sobrante=0

print("cuantos caramelos se van a repartir")
caramelos=int(input())

print("Cuantos estudiantes son?")
estudiantes=int(input())

resultado=caramelos//estudiantes
sobrante=c%estudiantes

print(resultado," caramelos para cada estudiante")
print("le sobran ",sobrante," caramelos.")