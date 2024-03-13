import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('dataset_summary.csv')

# Calcular una métrica de dispersión, por ejemplo, la suma de las desviaciones estándar de ancho y alto
df['Dispersion'] = df['Std_Width'] + df['Std_Height']

# Ordenar las categorías por la métrica de dispersión de mayor a menor
df_sorted = df.sort_values(by='Dispersion', ascending=False)



# Visualizar las categorías con mayor dispersión
plt.figure(figsize=(12, 6))
bar_plot = plt.bar(df_sorted['Category'], df_sorted['Dispersion'], color='skyblue')
plt.xlabel('Categoría')
plt.ylabel('Dispersion (Std_Width + Std_Height)')
plt.title('Categorías con Mayor Dispersion de Datos')
plt.xticks([], [])  # Quitar las etiquetas del eje x
plt.tight_layout()
plt.show()

# Visualizar las categorías con mayor dispersión
print(df_sorted[['Category', 'Dispersion']])