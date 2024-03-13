import os
import cv2
import pandas as pd

def calculate_statistics(dimensions):
    if dimensions:
        mean_dimensions = tuple(map(lambda x: sum(x) / len(x), zip(*dimensions)))
        median_dimensions = tuple(sorted(dimensions)[len(dimensions) // 2])

        # Cálculo de la desviación estándar
        std_dimensions = tuple(map(lambda x: ((x[0] - mean_dimensions[0]) ** 2, (x[1] - mean_dimensions[1]) ** 2), dimensions))
        std_dimensions = (sum(dim[0] for dim in std_dimensions) / len(dimensions), sum(dim[1] for dim in std_dimensions) / len(dimensions))
        std_dimensions = (std_dimensions[0] ** 0.5, std_dimensions[1] ** 0.5)

        return {
            'Mean_Width': mean_dimensions[0],
            'Mean_Height': mean_dimensions[1],
            'Median_Width': median_dimensions[0],
            'Median_Height': median_dimensions[1],
            'Std_Width': std_dimensions[0],
            'Std_Height': std_dimensions[1],
        }
    else:
        return {
            'Mean_Width': None,
            'Mean_Height': None,
            'Median_Width': None,
            'Median_Height': None,
            'Std_Width': None,
            'Std_Height': None,
        }

def create_dataset_file(base_path):
    # Lista para almacenar los resultados
    data = []

    # Iterar sobre las carpetas de categorías de perro
    for category_folder in os.listdir(base_path):
        category_path = os.path.join(base_path, category_folder)

        # Lista para almacenar las dimensiones de cada imagen en la categoría
        dimensions = []

        # Iterar sobre las imágenes en la categoría
        for filename in os.listdir(category_path):
            if filename.endswith(".jpg"):
                img_path = os.path.join(category_path, filename)
                img = cv2.imread(img_path)
                if img is not None:  # Asegurarse de que la imagen se haya cargado correctamente
                    height, width, _ = img.shape
                    dimensions.append((width, height))

        # Calcular estadísticas descriptivas para las dimensiones
        category_stats = calculate_statistics(dimensions)

        # Agregar resultados a la lista
        data.append({
            'Category': category_folder,
            **category_stats,
        })

    # Crear un DataFrame con los resultados
    df = pd.DataFrame(data)

    # Guardar el DataFrame en un archivo CSV en la carpeta del proyecto
    df.to_csv('dataset_summary.csv', index=False)

if __name__ == "__main__":
    # Ruta del directorio que contiene las carpetas de cada categoría de perro
    base_path = 'dataset\\Images'  # Actualiza la ruta según la estructura de tu proyecto

    # Crear el archivo del dataset
    create_dataset_file(base_path)