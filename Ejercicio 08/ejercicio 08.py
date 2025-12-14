radio=0
altura=0
volumen=0

import math

print("cuanto mide la radio de tu circulo")

radio=int(input())

def areacirculo(radio):
    return math.pi * radio**2

print(areacirculo(radio),"es el area de tu circulo")

print("que tan alto es tu cilindro")

altura=int(input())

volumen=areacirculo(radio)* altura

print("tu cilindro tiene un volumen de: ",volumen)




    
    