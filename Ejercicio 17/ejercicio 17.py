from PIL import Image
import numpy as np
imagen = Image.open("perro.jpg")

pixels = np.array(imagen)
alto, ancho, canales = pixels.shape

# Crear imagen de salida (vacía)
salida = np.zeros_like(pixels)

# Crear kernel promedio 5x5
kernel = np.ones((5, 5), dtype=np.float32) / 25

# Rango para bordes (evitamos bordes para no salirnos del array)
margen = 2  # porque kernel es 5x5

# Aplicar convolución en cada canal (R, G, B)
for canal in range(3):
    for i in range(margen, alto - margen):
        for j in range(margen, ancho - margen):
            region = pixels[i - margen:i + margen + 1, j - margen:j + margen + 1, canal]
            valor = np.sum(region * kernel)
            salida[i, j, canal] = int(valor)

# Convertir el array de vuelta a imagen
imagen_desenfocada = Image.fromarray(salida)

# Mostrar ambas imágenes
imagen.show(title="Original")
imagen_desenfocada.show(title="Desenfocada 5x5 RGB")
