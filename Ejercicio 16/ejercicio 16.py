import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageOps

res=""
res2=""
res3=""
im = Image.open("perro.jpg")

print("quieres voltear la imagen en 90 grados?")
res=input()

if (res=="si"):
    print("para el lado derecho o izquierdo?")
    res2=input()
    
    if (res2=="derecha"):
    ancho, alto = imagen.size


    imagen_rotada = Image.new(imagen.mode, (alto, ancho))


    pixeles_original = imagen.load()
    pixeles_nueva = imagen_rotada.load()


    for x in range(ancho):
        for y in range(alto):
            nuevo_x = alto - 1 - y
            nuevo_y = x
            pixeles_nueva[nuevo_x, nuevo_y] = pixeles_original[x, y]
    
    else:
        
        
else:
    print("quieres voltear la imagen 180°?")
    res3=input()
    
    if (res3=="si"):
        



    else:
        print("entonces para que entras al programa si no vas a voltear nada")

