# -*- coding: utf-8 -*-
"""O2 Proyecto

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tm7HGsHc-IN8_D7sYeystmh-2fzYjywL

# **Proyecto** ***Tuneado***
"""

# Commented out IPython magic to ensure Python compatibility.
# %config IPCompleter.greedy=True
import pandas as pd
import numpy as np
import xlrd
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

from google.colab import files

from google.colab import drive

drive.mount('/content/drive')

import pandas as pd
df = pd.read_excel("/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx")
df.shape

#Tamaño de los datos
print('El tamaño de los datos en filas y columnas es de ',df.shape)

pd.read_excel("/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx")

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'
hoja_excel = 'Hoja1'  # Reemplaza 'Hoja1' con el nombre real de la hoja que contiene tus datos

# Carga del archivo Excel
try:
    datos = pd.read_excel(ruta_archivo, sheet_name=hoja_excel)

    # Calcula el promedio de todos los datos en la hoja
    promedio_total = datos.values.flatten().mean()

    print(f"El promedio de todos los datos en la Hoja 1 es: {promedio_total:.2f}")

except FileNotFoundError:
    print("No se encontró el archivo en la ruta especificada. Por favor, verifica la ruta del archivo.")
except Exception as e:
    print(f"Ocurrió un error al cargar los datos: {e}")

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'
hoja_excel = 'Hoja1'  # Reemplaza 'Hoja1' con el nombre real de la hoja que contiene tus datos

# Carga del archivo Excel
try:
    datos = pd.read_excel(ruta_archivo, sheet_name=hoja_excel)

    # Calcula el promedio de la columna correspondiente a enero
    promedio_enero = datos['Enero'].mean()

    print(f"El promedio de temperatura en enero en la {hoja_excel} es: {promedio_enero:.2f}")

except FileNotFoundError:
    print("No se encontró el archivo en la ruta especificada. Por favor, verifica la ruta del archivo.")
except KeyError:
    print("No se encontró la columna 'Enero' en la hoja especificada.")
except Exception as e:
    print(f"Ocurrió un error al cargar los datos: {e}")

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'
hoja_excel = 'Hoja1'  # Reemplaza 'Hoja1' con el nombre real de la hoja que contiene tus datos

# Carga del archivo Excel
try:
    datos = pd.read_excel(ruta_archivo, sheet_name=hoja_excel)

    # Calcula el promedio de la columna correspondiente a febrero
    promedio_febrero = datos['Febrero'].mean()

    print(f"El promedio de temperatura en febrero en la {hoja_excel} es: {promedio_febrero:.2f}")

except FileNotFoundError:
    print("No se encontró el archivo en la ruta especificada. Por favor, verifica la ruta del archivo.")
except KeyError:
    print("No se encontró la columna 'Febrero' en la hoja especificada.")
except Exception as e:
    print(f"Ocurrió un error al cargar los datos: {e}")

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'
hoja_excel = 'Hoja1'  # Reemplaza 'Hoja1' con el nombre real de la hoja que contiene tus datos

# Carga del archivo Excel
try:
    datos = pd.read_excel(ruta_archivo, sheet_name=hoja_excel)

    # Calcula el promedio de la columna correspondiente a marzo
    promedio_marzo = datos['Marzo'].mean()

    print(f"El promedio de temperatura en marzo en la {hoja_excel} es: {promedio_marzo:.2f}")

except FileNotFoundError:
    print("No se encontró el archivo en la ruta especificada. Por favor, verifica la ruta del archivo.")
except KeyError:
    print("No se encontró la columna 'Marzo' en la hoja especificada.")
except Exception as e:
    print(f"Ocurrió un error al cargar los datos: {e}")

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'
hoja_excel = 'Hoja1'  # Reemplaza 'Hoja1' con el nombre real de la hoja que contiene tus datos

# Carga del archivo Excel
try:
    datos = pd.read_excel(ruta_archivo, sheet_name=hoja_excel)

    # Calcula el promedio de la columna correspondiente a abril
    promedio_abril = datos['Abril'].mean()

    print(f"El promedio de temperatura en abril en la {hoja_excel} es: {promedio_abril:.2f}")

except FileNotFoundError:
    print("No se encontró el archivo en la ruta especificada. Por favor, verifica la ruta del archivo.")
except KeyError:
    print("No se encontró la columna 'Abril' en la hoja especificada.")
except Exception as e:
    print(f"Ocurrió un error al cargar los datos: {e}")

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'
hoja_excel = 'Hoja1'  # Reemplaza 'Hoja1' con el nombre real de la hoja que contiene tus datos

# Carga del archivo Excel
try:
    datos = pd.read_excel(ruta_archivo, sheet_name=hoja_excel)

    # Calcula el promedio de la columna correspondiente a mayo
    promedio_mayo = datos['Mayo'].mean()

    print(f"El promedio de temperatura en mayo en la {hoja_excel} es: {promedio_mayo:.2f}")

except FileNotFoundError:
    print("No se encontró el archivo en la ruta especificada. Por favor, verifica la ruta del archivo.")
except KeyError:
    print("No se encontró la columna 'Mayo' en la hoja especificada.")
except Exception as e:
    print(f"Ocurrió un error al cargar los datos: {e}")

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'
hoja_excel = 'Hoja1'  # Reemplaza 'Hoja1' con el nombre real de la hoja que contiene tus datos

# Carga del archivo Excel
try:
    datos = pd.read_excel(ruta_archivo, sheet_name=hoja_excel)

    # Calcula el promedio de la columna correspondiente a junio
    promedio_junio = datos['Junio'].mean()

    print(f"El promedio de temperatura en junio en la {hoja_excel} es: {promedio_junio:.2f}")

except FileNotFoundError:
    print("No se encontró el archivo en la ruta especificada. Por favor, verifica la ruta del archivo.")
except KeyError:
    print("No se encontró la columna 'Junio' en la hoja especificada.")
except Exception as e:
    print(f"Ocurrió un error al cargar los datos: {e}")

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'
hoja_excel = 'Hoja1'  # Reemplaza 'Hoja1' con el nombre real de la hoja que contiene tus datos

# Carga del archivo Excel
try:
    datos = pd.read_excel(ruta_archivo, sheet_name=hoja_excel)

    # Calcula el promedio de la columna correspondiente a julio
    promedio_julio = datos['Julio'].mean()

    print(f"El promedio de temperatura en julio en la {hoja_excel} es: {promedio_julio:.2f}")

except FileNotFoundError:
    print("No se encontró el archivo en la ruta especificada. Por favor, verifica la ruta del archivo.")
except KeyError:
    print("No se encontró la columna 'Julio' en la hoja especificada.")
except Exception as e:
    print(f"Ocurrió un error al cargar los datos: {e}")

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'
hoja_excel = 'Hoja1'  # Reemplaza 'Hoja1' con el nombre real de la hoja que contiene tus datos

# Carga del archivo Excel
try:
    datos = pd.read_excel(ruta_archivo, sheet_name=hoja_excel)

    # Calcula el promedio de la columna correspondiente a agosto
    promedio_agosto = datos['Agosto'].mean()

    print(f"El promedio de temperatura en agosto en la {hoja_excel} es: {promedio_agosto:.2f}")

except FileNotFoundError:
    print("No se encontró el archivo en la ruta especificada. Por favor, verifica la ruta del archivo.")
except KeyError:
    print("No se encontró la columna 'Agosto' en la hoja especificada.")
except Exception as e:
    print(f"Ocurrió un error al cargar los datos: {e}")

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'
hoja_excel = 'Hoja1'  # Reemplaza 'Hoja1' con el nombre real de la hoja que contiene tus datos

# Carga del archivo Excel
try:
    datos = pd.read_excel(ruta_archivo, sheet_name=hoja_excel)

    # Calcula el promedio de la columna correspondiente a septiembre
    promedio_septiembre = datos['Septiembre'].mean()

    print(f"El promedio de temperatura en septiembre en la {hoja_excel} es: {promedio_septiembre:.2f}")

except FileNotFoundError:
    print("No se encontró el archivo en la ruta especificada. Por favor, verifica la ruta del archivo.")
except KeyError:
    print("No se encontró la columna 'Septiembre' en la hoja especificada.")
except Exception as e:
    print(f"Ocurrió un error al cargar los datos: {e}")

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'
hoja_excel = 'Hoja1'  # Reemplaza 'Hoja1' con el nombre real de la hoja que contiene tus datos

# Carga del archivo Excel
try:
    datos = pd.read_excel(ruta_archivo, sheet_name=hoja_excel)

    # Calcula el promedio de la columna correspondiente a octubre
    promedio_octubre = datos['Octubre'].mean()

    print(f"El promedio de temperatura en octubre en la {hoja_excel} es: {promedio_octubre:.2f}")

except FileNotFoundError:
    print("No se encontró el archivo en la ruta especificada. Por favor, verifica la ruta del archivo.")
except KeyError:
    print("No se encontró la columna 'Octubre' en la hoja especificada.")
except Exception as e:
    print(f"Ocurrió un error al cargar los datos: {e}")

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'
hoja_excel = 'Hoja1'  # Reemplaza 'Hoja1' con el nombre real de la hoja que contiene tus datos

# Carga del archivo Excel
try:
    datos = pd.read_excel(ruta_archivo, sheet_name=hoja_excel)

    # Calcula el promedio de la columna correspondiente a noviembre
    promedio_noviembre = datos['Noviembre'].mean()

    print(f"El promedio de temperatura en noviembre en la {hoja_excel} es: {promedio_noviembre:.2f}")

except FileNotFoundError:
    print("No se encontró el archivo en la ruta especificada. Por favor, verifica la ruta del archivo.")
except KeyError:
    print("No se encontró la columna 'Noviembre' en la hoja especificada.")
except Exception as e:
    print(f"Ocurrió un error al cargar los datos: {e}")

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'
hoja_excel = 'Hoja1'  # Reemplaza 'Hoja1' con el nombre real de la hoja que contiene tus datos

# Carga del archivo Excel
try:
    datos = pd.read_excel(ruta_archivo, sheet_name=hoja_excel)

    # Calcula el promedio de la columna correspondiente a diciembre
    promedio_diciembre = datos['Diciembre'].mean()

    print(f"El promedio de temperatura en diciembre en la {hoja_excel} es: {promedio_diciembre:.2f}")

except FileNotFoundError:
    print("No se encontró el archivo en la ruta especificada. Por favor, verifica la ruta del archivo.")
except KeyError:
    print("No se encontró la columna 'Diciembre' en la hoja especificada.")
except Exception as e:
    print(f"Ocurrió un error al cargar los datos: {e}")

import pandas as pd
import matplotlib.pyplot as plt

# Ruta del archivo Excel y lectura de la Hoja 1
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'
datos = pd.read_excel(ruta_archivo, sheet_name='Hoja1')

# Obtener los nombres de las columnas (años)
años = datos.columns.tolist()

# Calcular el promedio de cada año
promedio_por_año = datos.mean()

# Crear gráfico de barras para mostrar el promedio por año
plt.figure(figsize=(10, 6))
plt.bar(años, promedio_por_año)
plt.xlabel('Meses')
plt.ylabel('Temperatura Promedio')
plt.title('Promedio de Temperaturas de todos los Años (Hoja 1)')
plt.xticks(rotation=20)  # Rotar etiquetas del eje X para mejor visualización
plt.tight_layout()

# Mostrar el gráfico
plt.show()

import pandas as pd

# Ruta del archivo Excel
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la Hoja 1 del archivo Excel
datos_hoja_1 = pd.read_excel(ruta_archivo, sheet_name='Hoja1')

# Aplanar los datos en una sola serie
datos_aplanados = datos_hoja_1.stack()

# Calcular la moda de los datos totales
moda_total = datos_aplanados.mode()

# Mostrar la moda total
print("La moda de todos los datos en la Hoja 1 es:", moda_total[0])

import pandas as pd

# Ruta del archivo Excel
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la Hoja 1 del archivo Excel
datos_hoja_1 = pd.read_excel(ruta_archivo, sheet_name='Hoja1')

# Calcular la mediana de todos los datos de la Hoja 1
mediana_hoja_1 = datos_hoja_1.values.flatten()
mediana_hoja_1 = pd.Series(mediana_hoja_1).median()

print(f"La mediana de todos los datos de la Hoja 1 es: {mediana_hoja_1}")

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'
hoja_excel = 'Hoja1'  # Nombre de la hoja que contiene los datos

# Cargar el archivo Excel en un DataFrame
datos_hoja_1 = pd.read_excel(ruta_archivo, sheet_name=hoja_excel)

# Encontrar el valor máximo y mínimo de todos los datos
maximo_valor_hoja_1 = datos_hoja_1.values.max()
minimo_valor_hoja_1 = datos_hoja_1.values.min()

print("El valor máximo de todos los datos en la Hoja 1 es:", maximo_valor_hoja_1)
print("El valor mínimo de todos los datos en la Hoja 1 es:", minimo_valor_hoja_1)

import pandas as pd
import matplotlib.pyplot as plt

# Ruta del archivo Excel y nombre de la hoja
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'
hoja_excel = 'Hoja1'  # Nombre de la hoja que contiene los datos

# Cargar el archivo Excel en un DataFrame
datos_hoja_1 = pd.read_excel(ruta_archivo, sheet_name=hoja_excel)

# Encontrar el valor máximo y mínimo de todos los datos
maximo_valor_hoja_1 = datos_hoja_1.values.max()
minimo_valor_hoja_1 = datos_hoja_1.values.min()

# Crear un gráfico de barras para mostrar el valor máximo y mínimo
fig, ax = plt.subplots()

# Definir los datos a graficar
nombres = ['Máximo', 'Mínimo']
valores = [maximo_valor_hoja_1, minimo_valor_hoja_1]

# Graficar los datos
ax.bar(nombres, valores, color=['red', 'blue'])
ax.set_ylabel('Temperatura')
ax.set_title('Valor Máximo y Mínimo de la Hoja 1')

# Mostrar la gráfica
plt.show()

import pandas as pd

# Ruta del archivo Excel
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la Hoja 1 del archivo Excel
datos_hoja_1 = pd.read_excel(ruta_archivo, sheet_name='Hoja1')

# Calcular la desviación estándar de todos los datos en la Hoja 1
desviacion_estandar_total_hoja_1 = datos_hoja_1.values.flatten().std()

# Mostrar la desviación estándar total de la Hoja 1
print("La desviación estándar de todos los datos en la Hoja 1 es:", desviacion_estandar_total_hoja_1)

import pandas as pd
import matplotlib.pyplot as plt

# Ruta del archivo Excel
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la Hoja 1 del archivo Excel
datos_hoja_1 = pd.read_excel(ruta_archivo, sheet_name='Hoja1')

# Obtener todos los datos en un arreglo unidimensional
datos_flatten = datos_hoja_1.values.flatten()

# Calcular la desviación estándar de todos los datos en la Hoja 1
desviacion_estandar_total_hoja_1 = datos_flatten.std()

# Crear un histograma de los datos
plt.figure(figsize=(8, 6))
plt.hist(datos_flatten, bins=20, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(desviacion_estandar_total_hoja_1, color='red', linestyle='dashed', linewidth=1.5, label='Desviación Estándar')

# Etiquetas y título
plt.xlabel('Valores de temperaturas')
plt.ylabel('Frecuencia')
plt.title('Distribución de los datos con Desviación Estándar')
plt.legend()

# Mostrar el gráfico
plt.show()

import matplotlib.pyplot as plt

años = ['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']
Temperaturas = [39.13191667 , 39.57891667 , 34.94366667 , 33.7525 , 32.44941667 , 31.35691667 , 33.82208333 , 33.61225 , 33.65366667 , 33.67825 , 33.55075 , 34.01283333 , 34.26741667 , 34.2295 , 33.84925 , 34.02675 , 34.50808333 , 34.49625 , 33.84725 , 34.47433333 , 33.31608333 , 34.11441667 , 32.48825 , 32.40975 , 33.2305 , 33.38466667 , 33.45941667 , 33.05041667]

fig, ax = plt.subplots()
ax.set_ylabel('Temperaturas')
ax.set_title('Temperaturas Maximas Promedio Anual')

plt.bar(años, Temperaturas)
# Rotar las etiquetas del eje x para que sean más legibles
plt.xticks(rotation=45)
plt.tight_layout()  # Ajustar el diseño para evitar cortar las etiquetas
plt.show()

"""# **Hoja 2**"""

import pandas as pd

# Ruta del archivo Excel
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la hoja 2 del archivo Excel
datos_hoja_2 = pd.read_excel(ruta_archivo, sheet_name='Hoja 2')

# Mostrar los datos de la hoja 2
print(datos_hoja_2)

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'
hoja_excel = 'Hoja 2'  # nombre real de la hoja que contiene tus datos

# Carga del archivo Excel
try:
    datos = pd.read_excel(ruta_archivo, sheet_name=hoja_excel)

    # Calcula el promedio de todos los datos en la hoja
    promedio_total = datos.values.flatten().mean()

    print(f"El promedio de todos los datos en la {hoja_excel} es: {promedio_total:.2f}")

except FileNotFoundError:
    print("No se encontró el archivo en la ruta especificada. Por favor, verifica la ruta del archivo.")
except Exception as e:
    print(f"Ocurrió un error al cargar los datos: {e}")

import pandas as pd

# Ruta del archivo Excel
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la hoja 2 del archivo Excel
datos_hoja_2 = pd.read_excel(ruta_archivo, sheet_name='Hoja 2')

# Calcular el promedio de la columna de enero
promedio_enero = datos_hoja_2['Enero'].mean()

# Mostrar el promedio de enero
print(f"El promedio de temperatura en enero es: {promedio_enero}")

import pandas as pd

# Ruta del archivo Excel
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la hoja 2 del archivo Excel
datos_hoja_2 = pd.read_excel(ruta_archivo, sheet_name='Hoja 2')

# Calcular el promedio de la columna de febrero
promedio_febrero = datos_hoja_2['Febrero'].mean()

# Mostrar el promedio de febrero
print(f"El promedio de temperatura en febrero es: {promedio_febrero}")

import pandas as pd

# Ruta del archivo Excel
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la hoja 2 del archivo Excel
datos_hoja_2 = pd.read_excel(ruta_archivo, sheet_name='Hoja 2')

# Calcular el promedio de la columna de marzo
promedio_marzo = datos_hoja_2['Marzo'].mean()

# Mostrar el promedio de marzo
print(f"El promedio de temperatura en marzo es: {promedio_marzo}")

import pandas as pd

# Ruta del archivo Excel
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la hoja 2 del archivo Excel
datos_hoja_2 = pd.read_excel(ruta_archivo, sheet_name='Hoja 2')

# Calcular el promedio de la columna de abril
promedio_abril = datos_hoja_2['Abril'].mean()

# Mostrar el promedio de abril
print(f"El promedio de temperatura en abril es: {promedio_abril}")

import pandas as pd

# Ruta del archivo Excel
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la hoja 2 del archivo Excel
datos_hoja_2 = pd.read_excel(ruta_archivo, sheet_name='Hoja 2')

# Calcular el promedio de la columna de mayo
promedio_mayo = datos_hoja_2['Mayo'].mean()

# Mostrar el promedio de mayo
print(f"El promedio de temperatura en mayo es: {promedio_mayo}")

import pandas as pd

# Ruta del archivo Excel
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la hoja 2 del archivo Excel
datos_hoja_2 = pd.read_excel(ruta_archivo, sheet_name='Hoja 2')

# Calcular el promedio de la columna de junio
promedio_junio = datos_hoja_2['Junio'].mean()

# Mostrar el promedio de junio
print(f"El promedio de temperatura en junio es: {promedio_junio}")

import pandas as pd

# Ruta del archivo Excel
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la hoja 2 del archivo Excel
datos_hoja_2 = pd.read_excel(ruta_archivo, sheet_name='Hoja 2')

# Calcular el promedio de la columna de julio
promedio_julio = datos_hoja_2['Julio'].mean()

# Mostrar el promedio de julio
print(f"El promedio de temperatura en julio es: {promedio_julio}")

import pandas as pd

# Ruta del archivo Excel
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la hoja 2 del archivo Excel
datos_hoja_2 = pd.read_excel(ruta_archivo, sheet_name='Hoja 2')

# Calcular el promedio de la columna de agosto
promedio_agosto = datos_hoja_2['Agosto'].mean()

# Mostrar el promedio de agosto
print(f"El promedio de temperatura en agosto es: {promedio_agosto}")

import pandas as pd

# Ruta del archivo Excel
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la hoja 2 del archivo Excel
datos_hoja_2 = pd.read_excel(ruta_archivo, sheet_name='Hoja 2')

# Calcular el promedio de la columna de septiembre
promedio_septiembre = datos_hoja_2['Septiembre'].mean()

# Mostrar el promedio de septiembre
print(f"El promedio de temperatura en septiembre es: {promedio_septiembre}")

import pandas as pd

# Ruta del archivo Excel
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la hoja 2 del archivo Excel
datos_hoja_2 = pd.read_excel(ruta_archivo, sheet_name='Hoja 2')

# Calcular el promedio de la columna de octubre
promedio_octubre = datos_hoja_2['Octubre'].mean()

# Mostrar el promedio de octubre
print(f"El promedio de temperatura en octubre es: {promedio_octubre}")

import pandas as pd

# Ruta del archivo Excel
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la hoja 2 del archivo Excel
datos_hoja_2 = pd.read_excel(ruta_archivo, sheet_name='Hoja 2')

# Calcular el promedio de la columna de noviembre
promedio_noviembre = datos_hoja_2['Noviembre'].mean()

# Mostrar el promedio de noviembre
print(f"El promedio de temperatura en noviembre es: {promedio_noviembre}")

import pandas as pd

# Ruta del archivo Excel
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la hoja 2 del archivo Excel
datos_hoja_2 = pd.read_excel(ruta_archivo, sheet_name='Hoja 2')

# Calcular el promedio de la columna de diciembre
promedio_diciembre = datos_hoja_2['Diciembre'].mean()

# Mostrar el promedio de diciembre
print(f"El promedio de temperatura en diciembre es: {promedio_diciembre}")

import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo Excel y leer la Hoja 2
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'
datos = pd.read_excel(ruta_archivo, sheet_name='Hoja 2')

# Obtener los nombres de las columnas (años)
años = datos.columns.tolist()

# Calcular el promedio de cada año
promedio_por_año = datos.mean()

# Crear gráfico de barras para mostrar el promedio por año
plt.figure(figsize=(10, 6))
plt.bar(años, promedio_por_año)
plt.xlabel('Meses')
plt.ylabel('Temperatura Promedio')
plt.title('Promedio de Temperaturas de todos los Años (Hoja 2)')
plt.xticks(rotation=20)  # Rotar etiquetas del eje X para mejor visualización
plt.tight_layout()

# Mostrar el gráfico
plt.show()

import pandas as pd

# Ruta del archivo Excel
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la Hoja 2 del archivo Excel
datos_hoja_2 = pd.read_excel(ruta_archivo, sheet_name='Hoja 2')

# Aplanar los datos en una sola serie
datos_aplanados = datos_hoja_2.stack()

# Calcular la moda de los datos totales
moda_total = datos_aplanados.mode()

# Mostrar la moda total
print("La moda de todos los datos en la Hoja 2 es:", moda_total[0])

import pandas as pd

# Ruta del archivo Excel
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la Hoja 2 del archivo Excel
datos_hoja_2 = pd.read_excel(ruta_archivo, sheet_name='Hoja 2')

# Calcular la mediana de todos los datos de la Hoja 2
mediana_hoja_2 = datos_hoja_2.values.flatten()
mediana_hoja_2 = pd.Series(mediana_hoja_2).median()

print(f"La mediana de todos los datos de la Hoja 2 es: {mediana_hoja_2}")

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'
hoja_excel = 'Hoja 2'  # Nombre de la hoja que contiene los datos

# Cargar el archivo Excel en un DataFrame
datos_hoja_2 = pd.read_excel(ruta_archivo, sheet_name=hoja_excel)

# Encontrar el valor máximo y mínimo de todos los datos
maximo_valor_hoja_2 = datos_hoja_2.values.max()
minimo_valor_hoja_2 = datos_hoja_2.values.min()

print("El valor máximo de todos los datos en la Hoja 2 es:", maximo_valor_hoja_2)
print("El valor mínimo de todos los datos en la Hoja 2 es:", minimo_valor_hoja_2)

import pandas as pd
import matplotlib.pyplot as plt

# Ruta del archivo Excel y nombre de la hoja
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'
hoja_excel = 'Hoja 2'  # Nombre de la hoja que contiene los datos

# Cargar el archivo Excel en un DataFrame
datos_hoja_2 = pd.read_excel(ruta_archivo, sheet_name=hoja_excel)

# Encontrar el valor máximo y mínimo de todos los datos
maximo_valor_hoja_2 = datos_hoja_2.values.max()
minimo_valor_hoja_2 = datos_hoja_2.values.min()

# Crear un gráfico de barras para mostrar el valor máximo y mínimo
fig, ax = plt.subplots()

# Definir los datos a graficar
nombres = ['Máximo', 'Mínimo']
valores = [maximo_valor_hoja_2, minimo_valor_hoja_2]

# Graficar los datos
ax.bar(nombres, valores, color=['green', 'blue'])
ax.set_ylabel('Valor')
ax.set_title('Valor Máximo y Mínimo de la Hoja 2')

# Mostrar la gráfica
plt.show()

import pandas as pd

# Ruta del archivo Excel
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la Hoja 2 del archivo Excel
datos_hoja_2 = pd.read_excel(ruta_archivo, sheet_name='Hoja 2')

# Calcular la desviación estándar de todos los datos en la Hoja 2
desviacion_estandar_total = datos_hoja_2.values.flatten().std()

# Mostrar la desviación estándar total
print("La desviación estándar de todos los datos en la Hoja 2 es:", desviacion_estandar_total)

import pandas as pd
import matplotlib.pyplot as plt

# Ruta del archivo Excel
ruta_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la Hoja 2 del archivo Excel
datos_hoja_2 = pd.read_excel(ruta_archivo, sheet_name='Hoja 2')

# Obtener todos los datos en un arreglo unidimensional
datos_flatten_hoja_2 = datos_hoja_2.values.flatten()

# Calcular la desviación estándar de todos los datos en la Hoja 2
desviacion_estandar_total_hoja_2 = datos_flatten_hoja_2.std()

# Crear un histograma de los datos de la Hoja 2
plt.figure(figsize=(8, 6))
plt.hist(datos_flatten_hoja_2, bins=20, color='lightgreen', edgecolor='black', alpha=0.7)
plt.axvline(desviacion_estandar_total_hoja_2, color='blue', linestyle='dashed', linewidth=1.5, label='Desviación Estándar')

# Etiquetas y título
plt.xlabel('Valores de temperaturas')
plt.ylabel('Frecuencia')
plt.title('Distribución de los datos de la Hoja 2 con Desviación Estándar')
plt.legend()

# Mostrar el gráfico
plt.show()

import matplotlib.pyplot as plt

años = ['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']
Temperaturas = [18.042 , 17.47516667 , 17.83666667 , 16.65808333 , 17.53433333 , 17.78733333 , 17.43966667 , 19.37225 , 19.25716667 , 18.893 , 19.36283333 , 19.30658333 , 19.72633333 , 19.84175 , 19.66141667 , 19.83083333 , 20.16933333 , 20.01333333 , 19.11875 , 20.08866667 , 19.56908333 , 20.18208333 , 20.05766667 , 20.24016667 , 20.482 , 20.79608333 , 20.32391667 , 20.25391667]

fig, ax = plt.subplots()
ax.set_ylabel('Temperaturas')
ax.set_title('Temperaturas Minimas Promedio Anual')

plt.bar(años, Temperaturas)
# Rotar las etiquetas del eje x para que sean más legibles
plt.xticks(rotation=45)
plt.tight_layout()  # Ajustar el diseño para evitar cortar las etiquetas
plt.show()

import folium

# Coordenadas de la ubicación de la antena
latitud = 19.209336734803742
longitud = -103.8073240612347

# Crea un mapa centrado en las coordenadas especificadas
mapa = folium.Map(location=[latitud, longitud], zoom_start=12)

# Añade un marcador en las coordenadas especificadas
folium.Marker([latitud, longitud], popup='Ubicación').add_to(mapa)

# Guarda el mapa como un archivo HTML
mapa.save('ubicacion.html')

# Muestra el mapa en Jupyter Notebook o en un entorno similar
mapa