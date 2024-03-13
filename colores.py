import cv2
import matplotlib.pyplot as plt
import numpy as np

# Función para calcular histogramas de colores
def plot_color_histogram(image):
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        hist, bins = np.histogram(image[:, :, i], bins=256, range=[0, 256])
        plt.plot(hist, color=col, alpha=0.7, label=col.upper())

    plt.title('Histograma de Colores')
    plt.xlabel('Intensidad de color')
    plt.ylabel('Frecuencia')
    plt.legend(loc='upper right')
    plt.show()

# Leer una imagen de ejemplo
sample_img_path = r'C:\Proyecto IA\dataset\Images\n02085620-Chihuahua\n02085620_199.jpg'
sample_img = cv2.imread(sample_img_path)

# Visualizar histogramas de colores
plot_color_histogram(sample_img)