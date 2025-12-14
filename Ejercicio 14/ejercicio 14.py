import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageOps

im = Image.open("perro.JPG")
im_gris = ImageOps.grayscale(im)
matriz = np.array(im_gris)

plt.imshow(matriz, cmap="grey")
plt.show()