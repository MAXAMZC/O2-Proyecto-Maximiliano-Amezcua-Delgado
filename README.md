# O2-Proyecto-Maximiliano-Amezcua-Delgado
![](RackMultipart20231212-1-lfup93_html_957da2369959fe46.png)

**FACULTAD**** DE INGENIERIA CIVIL**

**INGENIERO**** TOPOGRAFO ****GEOMATICO**

**"Temperatura Máxima y Mínima Promedio Mensual en Coquimatlán en 1990 - 2017****"**

**Maestro** :Sebastián Gonzales Zepeda

**Autores** :

Maximiliano Amezcua Delgado

**Grado y**** Grupo**: 3ºB

Coquimatlán, Colima a 12/12/202

**Resumen**

En este proyecto lo que tenemos básicamente es una tabla de datos de Excel en la cual vienen los datos sobre cual fue la temperatura máxima promedio mensual y la mínima promedio mensual de Coquimatlán desde 1990 hasta el 2017.

Esto para saber si es que la temperatura promedio máxima o mínima ha aumentado en los últimos años o de lo contrario si el planeta se ha enfriado un poco más, aunque es obvio que lo más probable es que se haya calentado más.

**Introducción**

En este proyecto lo que debemos de realizar es un programa en el cual nos pueda graficar sobre un archivo de Excel en el cual están muchos datos sobre cual fue la temperatura promedia mensual sobre los años de 1990 – 2017, puede ser que el programa nos arroje datos como lo son, cual es el valor que mas se repite (moda), cual es el promedio de todo, cual es el promedio de un año, la frecuencia, el valor mínimo, el valor máximo, entre otras cosas.

La obtención de información no siempre es tan sencilla como parece y esto lo pudimos constatar porque nuestro proyecto original hablaba de la deserción de alumnos de topógrafo geomático de primero a tercer semestre, sin embargo, nos fue complicado obtener esta información debido a problemas o situaciones ajenas que nosotros no podíamos solventar.

Por eso decidimos cambiar al proyecto de temperatura máxima y mínima mensual del municipio de Coquimatlán, Colima desde el año 1990 hasta el año 2017, lo elegimos para saber si hubo algún aumento de la temperatura promedio durante estos 27 años, si es que el calentamiento global afecto en eso o si realmente sigue igual, entre otras cosas.

Y aprovechar que estos datos nos sirven realmente a nosotros (locales), ya que es información del lugar donde vivimos y podemos comprobar si es cierto que la temperatura ha aumentado.

La información fue muy fácil de recabar ya que todos estos datos venían organizados en una tabla del Servicio Meteorológico Nacional y solo se trasladaron los datos que estaban en esa tabla y se organizaron en una tabla de Excel.

**Desarrollo**

Básicamente lo que vamos a hacer en este proyecto es saber cuál es la temperatura máxima y mínima promedio mensual de Coquimatlán desde el año de 1990 hasta 2017, en este proyecto lo que buscamos hacer es realizar gráficas donde se muestren los datos de cuáles fueron las temperaturas promedio de cada año, así como también la temperatura más alta, saber cuáles son las temperaturas que más se frecuentan en este rango de años, entre otras cosas.

Todo esto se saca o se sacó desde la página de servicio meteorológico nacional en la parte del historial de temperaturas promedio, en este caso de la localidad de Coquimatlán, de ahí los datos se traslada a una tabla de Excel en los cuales serán procesados para poder realizar lo que es el código que esta materia y el maestro necesitan para que puedan ser evaluadas en el ordinario.

Lo que se realizó en la actualización de este proyecto de forma individual fue que ya todos los datos los sacamos de manera directa y mas automatizada, por que la otra vez el código que hicimos hacia estas cosas, pero de manera manual, es decir que no sacaba la información del Excel como lo hace ahora.

Se le agregaron más graficas para su mejor representación, se coloco el mapa en donde se puede observar la ubicación de la antena de donde se toman los datos.

También se muestran algunos datos adicionales los cuales no se veían anteriormente, pero esta vez se los agregue, como por ejemplo lo es el valor mas grande y el mas pequeño de ambas hojas de cálculo.

**Manejo de datos**

Para el manejo de datos, lo que realizaremos es una tabla de Excel en la cual pondremos todos nuestros datos ahí, y después con un código de Python mandaremos a llamar todos los datos para así saber cuáles son las respuestas de las preguntas que tenemos como base.

![](RackMultipart20231212-1-lfup93_html_a5cd4b4385cf9de9.gif)

# **Código**

%config IPCompleter.greedy=True

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

df = pd.read\_excel("/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx")

df.shape

#Tamaño de los datos

print('El tamaño de los datos en filas y columnas es de ',df.shape)

pd.read\_excel("/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx")

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

hoja\_excel = 'Hoja1'  # Reemplaza 'Hoja1' con el nombre real de la hoja que contiene tus datos

# Carga del archivo Excel

try:

    datos = pd.read\_excel(ruta\_archivo, sheet\_name=hoja\_excel)

    # Calcula el promedio de todos los datos en la hoja

    promedio\_total = datos.values.flatten().mean()

    print(f"El promedio de todos los datos en la Hoja 1 es: {promedio\_total:.2f}")

except FileNotFoundError:

    print("No se encontró el archivo en la ruta especificada. Por favor, verifica la ruta del archivo.")

except Exception as e:

    print(f"Ocurrió un error al cargar los datos: {e}")

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

hoja\_excel = 'Hoja1'  # Reemplaza 'Hoja1' con el nombre real de la hoja que contiene tus datos

# Carga del archivo Excel

try:

    datos = pd.read\_excel(ruta\_archivo, sheet\_name=hoja\_excel)

    # Calcula el promedio de la columna correspondiente a enero

    promedio\_enero = datos['Enero'].mean()

    print(f"El promedio de temperatura en enero en la {hoja\_excel} es: {promedio\_enero:.2f}")

except FileNotFoundError:

    print("No se encontró el archivo en la ruta especificada. Por favor, verifica la ruta del archivo.")

except KeyError:

    print("No se encontró la columna 'Enero' en la hoja especificada.")

except Exception as e:

    print(f"Ocurrió un error al cargar los datos: {e}")

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

hoja\_excel = 'Hoja1'  # Reemplaza 'Hoja1' con el nombre real de la hoja que contiene tus datos

# Carga del archivo Excel

try:

    datos = pd.read\_excel(ruta\_archivo, sheet\_name=hoja\_excel)

    # Calcula el promedio de la columna correspondiente a febrero

    promedio\_febrero = datos['Febrero'].mean()

    print(f"El promedio de temperatura en febrero en la {hoja\_excel} es: {promedio\_febrero:.2f}")

except FileNotFoundError:

    print("No se encontró el archivo en la ruta especificada. Por favor, verifica la ruta del archivo.")

except KeyError:

    print("No se encontró la columna 'Febrero' en la hoja especificada.")

except Exception as e:

    print(f"Ocurrió un error al cargar los datos: {e}")

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

hoja\_excel = 'Hoja1'  # Reemplaza 'Hoja1' con el nombre real de la hoja que contiene tus datos

# Carga del archivo Excel

try:

    datos = pd.read\_excel(ruta\_archivo, sheet\_name=hoja\_excel)

    # Calcula el promedio de la columna correspondiente a marzo

    promedio\_marzo = datos['Marzo'].mean()

    print(f"El promedio de temperatura en marzo en la {hoja\_excel} es: {promedio\_marzo:.2f}")

except FileNotFoundError:

    print("No se encontró el archivo en la ruta especificada. Por favor, verifica la ruta del archivo.")

except KeyError:

    print("No se encontró la columna 'Marzo' en la hoja especificada.")

except Exception as e:

    print(f"Ocurrió un error al cargar los datos: {e}")

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

hoja\_excel = 'Hoja1'  # Reemplaza 'Hoja1' con el nombre real de la hoja que contiene tus datos

# Carga del archivo Excel

try:

    datos = pd.read\_excel(ruta\_archivo, sheet\_name=hoja\_excel)

    # Calcula el promedio de la columna correspondiente a abril

    promedio\_abril = datos['Abril'].mean()

    print(f"El promedio de temperatura en abril en la {hoja\_excel} es: {promedio\_abril:.2f}")

except FileNotFoundError:

    print("No se encontró el archivo en la ruta especificada. Por favor, verifica la ruta del archivo.")

except KeyError:

    print("No se encontró la columna 'Abril' en la hoja especificada.")

except Exception as e:

    print(f"Ocurrió un error al cargar los datos: {e}")

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

hoja\_excel = 'Hoja1'  # Reemplaza 'Hoja1' con el nombre real de la hoja que contiene tus datos

# Carga del archivo Excel

try:

    datos = pd.read\_excel(ruta\_archivo, sheet\_name=hoja\_excel)

    # Calcula el promedio de la columna correspondiente a mayo

    promedio\_mayo = datos['Mayo'].mean()

    print(f"El promedio de temperatura en mayo en la {hoja\_excel} es: {promedio\_mayo:.2f}")

except FileNotFoundError:

    print("No se encontró el archivo en la ruta especificada. Por favor, verifica la ruta del archivo.")

except KeyError:

    print("No se encontró la columna 'Mayo' en la hoja especificada.")

except Exception as e:

    print(f"Ocurrió un error al cargar los datos: {e}")

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

hoja\_excel = 'Hoja1'  # Reemplaza 'Hoja1' con el nombre real de la hoja que contiene tus datos

# Carga del archivo Excel

try:

    datos = pd.read\_excel(ruta\_archivo, sheet\_name=hoja\_excel)

    # Calcula el promedio de la columna correspondiente a junio

    promedio\_junio = datos['Junio'].mean()

    print(f"El promedio de temperatura en junio en la {hoja\_excel} es: {promedio\_junio:.2f}")

except FileNotFoundError:

    print("No se encontró el archivo en la ruta especificada. Por favor, verifica la ruta del archivo.")

except KeyError:

    print("No se encontró la columna 'Junio' en la hoja especificada.")

except Exception as e:

    print(f"Ocurrió un error al cargar los datos: {e}")

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

hoja\_excel = 'Hoja1'  # Reemplaza 'Hoja1' con el nombre real de la hoja que contiene tus datos

# Carga del archivo Excel

try:

    datos = pd.read\_excel(ruta\_archivo, sheet\_name=hoja\_excel)

    # Calcula el promedio de la columna correspondiente a julio

    promedio\_julio = datos['Julio'].mean()

    print(f"El promedio de temperatura en julio en la {hoja\_excel} es: {promedio\_julio:.2f}")

except FileNotFoundError:

    print("No se encontró el archivo en la ruta especificada. Por favor, verifica la ruta del archivo.")

except KeyError:

    print("No se encontró la columna 'Julio' en la hoja especificada.")

except Exception as e:

    print(f"Ocurrió un error al cargar los datos: {e}")

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

hoja\_excel = 'Hoja1'  # Reemplaza 'Hoja1' con el nombre real de la hoja que contiene tus datos

# Carga del archivo Excel

try:

    datos = pd.read\_excel(ruta\_archivo, sheet\_name=hoja\_excel)

    # Calcula el promedio de la columna correspondiente a agosto

    promedio\_agosto = datos['Agosto'].mean()

    print(f"El promedio de temperatura en agosto en la {hoja\_excel} es: {promedio\_agosto:.2f}")

except FileNotFoundError:

    print("No se encontró el archivo en la ruta especificada. Por favor, verifica la ruta del archivo.")

except KeyError:

    print("No se encontró la columna 'Agosto' en la hoja especificada.")

except Exception as e:

    print(f"Ocurrió un error al cargar los datos: {e}")

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

hoja\_excel = 'Hoja1'  # Reemplaza 'Hoja1' con el nombre real de la hoja que contiene tus datos

# Carga del archivo Excel

try:

    datos = pd.read\_excel(ruta\_archivo, sheet\_name=hoja\_excel)

    # Calcula el promedio de la columna correspondiente a septiembre

    promedio\_septiembre = datos['Septiembre'].mean()

    print(f"El promedio de temperatura en septiembre en la {hoja\_excel} es: {promedio\_septiembre:.2f}")

except FileNotFoundError:

    print("No se encontró el archivo en la ruta especificada. Por favor, verifica la ruta del archivo.")

except KeyError:

    print("No se encontró la columna 'Septiembre' en la hoja especificada.")

except Exception as e:

    print(f"Ocurrió un error al cargar los datos: {e}")

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

hoja\_excel = 'Hoja1'  # Reemplaza 'Hoja1' con el nombre real de la hoja que contiene tus datos

# Carga del archivo Excel

try:

    datos = pd.read\_excel(ruta\_archivo, sheet\_name=hoja\_excel)

    # Calcula el promedio de la columna correspondiente a octubre

    promedio\_octubre = datos['Octubre'].mean()

    print(f"El promedio de temperatura en octubre en la {hoja\_excel} es: {promedio\_octubre:.2f}")

except FileNotFoundError:

    print("No se encontró el archivo en la ruta especificada. Por favor, verifica la ruta del archivo.")

except KeyError:

    print("No se encontró la columna 'Octubre' en la hoja especificada.")

except Exception as e:

    print(f"Ocurrió un error al cargar los datos: {e}")

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

hoja\_excel = 'Hoja1'  # Reemplaza 'Hoja1' con el nombre real de la hoja que contiene tus datos

# Carga del archivo Excel

try:

    datos = pd.read\_excel(ruta\_archivo, sheet\_name=hoja\_excel)

    # Calcula el promedio de la columna correspondiente a noviembre

    promedio\_noviembre = datos['Noviembre'].mean()

    print(f"El promedio de temperatura en noviembre en la {hoja\_excel} es: {promedio\_noviembre:.2f}")

except FileNotFoundError:

    print("No se encontró el archivo en la ruta especificada. Por favor, verifica la ruta del archivo.")

except KeyError:

    print("No se encontró la columna 'Noviembre' en la hoja especificada.")

except Exception as e:

    print(f"Ocurrió un error al cargar los datos: {e}")

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

hoja\_excel = 'Hoja1'  # Reemplaza 'Hoja1' con el nombre real de la hoja que contiene tus datos

# Carga del archivo Excel

try:

    datos = pd.read\_excel(ruta\_archivo, sheet\_name=hoja\_excel)

    # Calcula el promedio de la columna correspondiente a diciembre

    promedio\_diciembre = datos['Diciembre'].mean()

    print(f"El promedio de temperatura en diciembre en la {hoja\_excel} es: {promedio\_diciembre:.2f}")

except FileNotFoundError:

    print("No se encontró el archivo en la ruta especificada. Por favor, verifica la ruta del archivo.")

except KeyError:

    print("No se encontró la columna 'Diciembre' en la hoja especificada.")

except Exception as e:

    print(f"Ocurrió un error al cargar los datos: {e}")

import pandas as pd

import matplotlib.pyplot as plt

# Ruta del archivo Excel y lectura de la Hoja 1

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

datos = pd.read\_excel(ruta\_archivo, sheet\_name='Hoja1')

# Obtener los nombres de las columnas (años)

años = datos.columns.tolist()

# Calcular el promedio de cada año

promedio\_por\_año = datos.mean()

# Crear gráfico de barras para mostrar el promedio por año

plt.figure(figsize=(10,6))

plt.bar(años, promedio\_por\_año)

plt.xlabel('Meses')

plt.ylabel('Temperatura Promedio')

plt.title('Promedio de Temperaturas de todos los Años (Hoja 1)')

plt.xticks(rotation=20)  # Rotar etiquetas del eje X para mejor visualización

plt.tight\_layout()

# Mostrar el gráfico

plt.show()

import pandas as pd

# Ruta del archivo Excel

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la Hoja 1 del archivo Excel

datos\_hoja\_1 = pd.read\_excel(ruta\_archivo, sheet\_name='Hoja1')

# Aplanar los datos en una sola serie

datos\_aplanados = datos\_hoja\_1.stack()

# Calcular la moda de los datos totales

moda\_total = datos\_aplanados.mode()

# Mostrar la moda total

print("La moda de todos los datos en la Hoja 1 es:", moda\_total[0])

import pandas as pd

# Ruta del archivo Excel

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la Hoja 1 del archivo Excel

datos\_hoja\_1 = pd.read\_excel(ruta\_archivo, sheet\_name='Hoja1')

# Calcular la mediana de todos los datos de la Hoja 1

mediana\_hoja\_1 = datos\_hoja\_1.values.flatten()

mediana\_hoja\_1 = pd.Series(mediana\_hoja\_1).median()

print(f"La mediana de todos los datos de la Hoja 1 es: {mediana\_hoja\_1}")

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

hoja\_excel = 'Hoja1'  # Nombre de la hoja que contiene los datos

# Cargar el archivo Excel en un DataFrame

datos\_hoja\_1 = pd.read\_excel(ruta\_archivo, sheet\_name=hoja\_excel)

# Encontrar el valor máximo y mínimo de todos los datos

maximo\_valor\_hoja\_1 = datos\_hoja\_1.values.max()

minimo\_valor\_hoja\_1 = datos\_hoja\_1.values.min()

print("El valor máximo de todos los datos en la Hoja 1 es:", maximo\_valor\_hoja\_1)

print("El valor mínimo de todos los datos en la Hoja 1 es:", minimo\_valor\_hoja\_1)

import pandas as pd

import matplotlib.pyplot as plt

# Ruta del archivo Excel y nombre de la hoja

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

hoja\_excel = 'Hoja1'  # Nombre de la hoja que contiene los datos

# Cargar el archivo Excel en un DataFrame

datos\_hoja\_1 = pd.read\_excel(ruta\_archivo, sheet\_name=hoja\_excel)

# Encontrar el valor máximo y mínimo de todos los datos

maximo\_valor\_hoja\_1 = datos\_hoja\_1.values.max()

minimo\_valor\_hoja\_1 = datos\_hoja\_1.values.min()

# Crear un gráfico de barras para mostrar el valor máximo y mínimo

fig, ax = plt.subplots()

# Definir los datos a graficar

nombres = ['Máximo','Mínimo']

valores = [maximo\_valor\_hoja\_1, minimo\_valor\_hoja\_1]

# Graficar los datos

ax.bar(nombres, valores, color=['red','blue'])

ax.set\_ylabel('Temperatura')

ax.set\_title('Valor Máximo y Mínimo de la Hoja 1')

# Mostrar la gráfica

plt.show()

import pandas as pd

# Ruta del archivo Excel

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la Hoja 1 del archivo Excel

datos\_hoja\_1 = pd.read\_excel(ruta\_archivo, sheet\_name='Hoja1')

# Calcular la desviación estándar de todos los datos en la Hoja 1

desviacion\_estandar\_total\_hoja\_1 = datos\_hoja\_1.values.flatten().std()

# Mostrar la desviación estándar total de la Hoja 1

print("La desviación estándar de todos los datos en la Hoja 1 es:", desviacion\_estandar\_total\_hoja\_1)

import pandas as pd

import matplotlib.pyplot as plt

# Ruta del archivo Excel

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la Hoja 1 del archivo Excel

datos\_hoja\_1 = pd.read\_excel(ruta\_archivo, sheet\_name='Hoja1')

# Obtener todos los datos en un arreglo unidimensional

datos\_flatten = datos\_hoja\_1.values.flatten()

# Calcular la desviación estándar de todos los datos en la Hoja 1

desviacion\_estandar\_total\_hoja\_1 = datos\_flatten.std()

# Crear un histograma de los datos

plt.figure(figsize=(8,6))

plt.hist(datos\_flatten, bins=20, color='skyblue', edgecolor='black', alpha=0.7)

plt.axvline(desviacion\_estandar\_total\_hoja\_1, color='red', linestyle='dashed', linewidth=1.5, label='Desviación Estándar')

# Etiquetas y título

plt.xlabel('Valores de temperaturas')

plt.ylabel('Frecuencia')

plt.title('Distribución de los datos con Desviación Estándar')

plt.legend()

# Mostrar el gráfico

plt.show()

import matplotlib.pyplot as plt

años = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']

Temperaturas = [39.13191667,39.57891667,34.94366667,33.7525,32.44941667,31.35691667,33.82208333,33.61225,33.65366667,33.67825,33.55075,34.01283333,34.26741667,34.2295,33.84925,34.02675,34.50808333,34.49625,33.84725,34.47433333,33.31608333,34.11441667,32.48825,32.40975,33.2305,33.38466667,33.45941667,33.05041667]

fig, ax = plt.subplots()

ax.set\_ylabel('Temperaturas')

ax.set\_title('Temperaturas Maximas Promedio Anual')

plt.bar(años, Temperaturas)

# Rotar las etiquetas del eje x para que sean más legibles

plt.xticks(rotation=45)

plt.tight\_layout()  # Ajustar el diseño para evitar cortar las etiquetas

plt.show()

# Hoja 2

import pandas as pd

# Ruta del archivo Excel

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la hoja 2 del archivo Excel

datos\_hoja\_2 = pd.read\_excel(ruta\_archivo, sheet\_name='Hoja 2')

# Mostrar los datos de la hoja 2

print(datos\_hoja\_2)

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

hoja\_excel = 'Hoja 2'  # nombre real de la hoja que contiene tus datos

# Carga del archivo Excel

try:

    datos = pd.read\_excel(ruta\_archivo, sheet\_name=hoja\_excel)

    # Calcula el promedio de todos los datos en la hoja

    promedio\_total = datos.values.flatten().mean()

    print(f"El promedio de todos los datos en la {hoja\_excel} es: {promedio\_total:.2f}")

except FileNotFoundError:

    print("No se encontró el archivo en la ruta especificada. Por favor, verifica la ruta del archivo.")

except Exception as e:

    print(f"Ocurrió un error al cargar los datos: {e}")

import pandas as pd

# Ruta del archivo Excel

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la hoja 2 del archivo Excel

datos\_hoja\_2 = pd.read\_excel(ruta\_archivo, sheet\_name='Hoja 2')

# Calcular el promedio de la columna de enero

promedio\_enero = datos\_hoja\_2['Enero'].mean()

# Mostrar el promedio de enero

print(f"El promedio de temperatura en enero es: {promedio\_enero}")

import pandas as pd

# Ruta del archivo Excel

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la hoja 2 del archivo Excel

datos\_hoja\_2 = pd.read\_excel(ruta\_archivo, sheet\_name='Hoja 2')

# Calcular el promedio de la columna de febrero

promedio\_febrero = datos\_hoja\_2['Febrero'].mean()

# Mostrar el promedio de febrero

print(f"El promedio de temperatura en febrero es: {promedio\_febrero}")

import pandas as pd

# Ruta del archivo Excel

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la hoja 2 del archivo Excel

datos\_hoja\_2 = pd.read\_excel(ruta\_archivo, sheet\_name='Hoja 2')

# Calcular el promedio de la columna de marzo

promedio\_marzo = datos\_hoja\_2['Marzo'].mean()

# Mostrar el promedio de marzo

print(f"El promedio de temperatura en marzo es: {promedio\_marzo}")

import pandas as pd

# Ruta del archivo Excel

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la hoja 2 del archivo Excel

datos\_hoja\_2 = pd.read\_excel(ruta\_archivo, sheet\_name='Hoja 2')

# Calcular el promedio de la columna de abril

promedio\_abril = datos\_hoja\_2['Abril'].mean()

# Mostrar el promedio de abril

print(f"El promedio de temperatura en abril es: {promedio\_abril}")

import pandas as pd

# Ruta del archivo Excel

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la hoja 2 del archivo Excel

datos\_hoja\_2 = pd.read\_excel(ruta\_archivo, sheet\_name='Hoja 2')

# Calcular el promedio de la columna de mayo

promedio\_mayo = datos\_hoja\_2['Mayo'].mean()

# Mostrar el promedio de mayo

print(f"El promedio de temperatura en mayo es: {promedio\_mayo}")

import pandas as pd

# Ruta del archivo Excel

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la hoja 2 del archivo Excel

datos\_hoja\_2 = pd.read\_excel(ruta\_archivo, sheet\_name='Hoja 2')

# Calcular el promedio de la columna de junio

promedio\_junio = datos\_hoja\_2['Junio'].mean()

# Mostrar el promedio de junio

print(f"El promedio de temperatura en junio es: {promedio\_junio}")

import pandas as pd

# Ruta del archivo Excel

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la hoja 2 del archivo Excel

datos\_hoja\_2 = pd.read\_excel(ruta\_archivo, sheet\_name='Hoja 2')

# Calcular el promedio de la columna de julio

promedio\_julio = datos\_hoja\_2['Julio'].mean()

# Mostrar el promedio de julio

print(f"El promedio de temperatura en julio es: {promedio\_julio}")

import pandas as pd

# Ruta del archivo Excel

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la hoja 2 del archivo Excel

datos\_hoja\_2 = pd.read\_excel(ruta\_archivo, sheet\_name='Hoja 2')

# Calcular el promedio de la columna de agosto

promedio\_agosto = datos\_hoja\_2['Agosto'].mean()

# Mostrar el promedio de agosto

print(f"El promedio de temperatura en agosto es: {promedio\_agosto}")

import pandas as pd

# Ruta del archivo Excel

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la hoja 2 del archivo Excel

datos\_hoja\_2 = pd.read\_excel(ruta\_archivo, sheet\_name='Hoja 2')

# Calcular el promedio de la columna de septiembre

promedio\_septiembre = datos\_hoja\_2['Septiembre'].mean()

# Mostrar el promedio de septiembre

print(f"El promedio de temperatura en septiembre es: {promedio\_septiembre}")

import pandas as pd

# Ruta del archivo Excel

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la hoja 2 del archivo Excel

datos\_hoja\_2 = pd.read\_excel(ruta\_archivo, sheet\_name='Hoja 2')

# Calcular el promedio de la columna de octubre

promedio\_octubre = datos\_hoja\_2['Octubre'].mean()

# Mostrar el promedio de octubre

print(f"El promedio de temperatura en octubre es: {promedio\_octubre}")

import pandas as pd

# Ruta del archivo Excel

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la hoja 2 del archivo Excel

datos\_hoja\_2 = pd.read\_excel(ruta\_archivo, sheet\_name='Hoja 2')

# Calcular el promedio de la columna de noviembre

promedio\_noviembre = datos\_hoja\_2['Noviembre'].mean()

# Mostrar el promedio de noviembre

print(f"El promedio de temperatura en noviembre es: {promedio\_noviembre}")

import pandas as pd

# Ruta del archivo Excel

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la hoja 2 del archivo Excel

datos\_hoja\_2 = pd.read\_excel(ruta\_archivo, sheet\_name='Hoja 2')

# Calcular el promedio de la columna de diciembre

promedio\_diciembre = datos\_hoja\_2['Diciembre'].mean()

# Mostrar el promedio de diciembre

print(f"El promedio de temperatura en diciembre es: {promedio\_diciembre}")

import pandas as pd

import matplotlib.pyplot as plt

# Cargar el archivo Excel y leer la Hoja 2

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

datos = pd.read\_excel(ruta\_archivo, sheet\_name='Hoja 2')

# Obtener los nombres de las columnas (años)

años = datos.columns.tolist()

# Calcular el promedio de cada año

promedio\_por\_año = datos.mean()

# Crear gráfico de barras para mostrar el promedio por año

plt.figure(figsize=(10,6))

plt.bar(años, promedio\_por\_año)

plt.xlabel('Meses')

plt.ylabel('Temperatura Promedio')

plt.title('Promedio de Temperaturas de todos los Años (Hoja 2)')

plt.xticks(rotation=20)  # Rotar etiquetas del eje X para mejor visualización

plt.tight\_layout()

# Mostrar el gráfico

plt.show()

import pandas as pd

# Ruta del archivo Excel

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la Hoja 2 del archivo Excel

datos\_hoja\_2 = pd.read\_excel(ruta\_archivo, sheet\_name='Hoja 2')

# Aplanar los datos en una sola serie

datos\_aplanados = datos\_hoja\_2.stack()

# Calcular la moda de los datos totales

moda\_total = datos\_aplanados.mode()

# Mostrar la moda total

print("La moda de todos los datos en la Hoja 2 es:", moda\_total[0])

import pandas as pd

# Ruta del archivo Excel

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la Hoja 2 del archivo Excel

datos\_hoja\_2 = pd.read\_excel(ruta\_archivo, sheet\_name='Hoja 2')

# Calcular la mediana de todos los datos de la Hoja 2

mediana\_hoja\_2 = datos\_hoja\_2.values.flatten()

mediana\_hoja\_2 = pd.Series(mediana\_hoja\_2).median()

print(f"La mediana de todos los datos de la Hoja 2 es: {mediana\_hoja\_2}")

import pandas as pd

# Ruta del archivo Excel y nombre de la hoja

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

hoja\_excel = 'Hoja 2'  # Nombre de la hoja que contiene los datos

# Cargar el archivo Excel en un DataFrame

datos\_hoja\_2 = pd.read\_excel(ruta\_archivo, sheet\_name=hoja\_excel)

# Encontrar el valor máximo y mínimo de todos los datos

maximo\_valor\_hoja\_2 = datos\_hoja\_2.values.max()

minimo\_valor\_hoja\_2 = datos\_hoja\_2.values.min()

print("El valor máximo de todos los datos en la Hoja 2 es:", maximo\_valor\_hoja\_2)

print("El valor mínimo de todos los datos en la Hoja 2 es:", minimo\_valor\_hoja\_2)

import pandas as pd

import matplotlib.pyplot as plt

# Ruta del archivo Excel y nombre de la hoja

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

hoja\_excel = 'Hoja 2'  # Nombre de la hoja que contiene los datos

# Cargar el archivo Excel en un DataFrame

datos\_hoja\_2 = pd.read\_excel(ruta\_archivo, sheet\_name=hoja\_excel)

# Encontrar el valor máximo y mínimo de todos los datos

maximo\_valor\_hoja\_2 = datos\_hoja\_2.values.max()

minimo\_valor\_hoja\_2 = datos\_hoja\_2.values.min()

# Crear un gráfico de barras para mostrar el valor máximo y mínimo

fig, ax = plt.subplots()

# Definir los datos a graficar

nombres = ['Máximo','Mínimo']

valores = [maximo\_valor\_hoja\_2, minimo\_valor\_hoja\_2]

# Graficar los datos

ax.bar(nombres, valores, color=['green','blue'])

ax.set\_ylabel('Valor')

ax.set\_title('Valor Máximo y Mínimo de la Hoja 2')

# Mostrar la gráfica

plt.show()

import pandas as pd

# Ruta del archivo Excel

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la Hoja 2 del archivo Excel

datos\_hoja\_2 = pd.read\_excel(ruta\_archivo, sheet\_name='Hoja 2')

# Calcular la desviación estándar de todos los datos en la Hoja 2

desviacion\_estandar\_total = datos\_hoja\_2.values.flatten().std()

# Mostrar la desviación estándar total

print("La desviación estándar de todos los datos en la Hoja 2 es:", desviacion\_estandar\_total)

import pandas as pd

import matplotlib.pyplot as plt

# Ruta del archivo Excel

ruta\_archivo = '/content/drive/MyDrive/Colab Notebooks/Programacion 2/Parcial 4/Temperatura Maxima y Minima Promedio Mensual de Coquimatlán.xlsx'

# Leer la Hoja 2 del archivo Excel

datos\_hoja\_2 = pd.read\_excel(ruta\_archivo, sheet\_name='Hoja 2')

# Obtener todos los datos en un arreglo unidimensional

datos\_flatten\_hoja\_2 = datos\_hoja\_2.values.flatten()

# Calcular la desviación estándar de todos los datos en la Hoja 2

desviacion\_estandar\_total\_hoja\_2 = datos\_flatten\_hoja\_2.std()

# Crear un histograma de los datos de la Hoja 2

plt.figure(figsize=(8,6))

plt.hist(datos\_flatten\_hoja\_2, bins=20, color='lightgreen', edgecolor='black', alpha=0.7)

plt.axvline(desviacion\_estandar\_total\_hoja\_2, color='blue', linestyle='dashed', linewidth=1.5, label='Desviación Estándar')

# Etiquetas y título

plt.xlabel('Valores de temperaturas')

plt.ylabel('Frecuencia')

plt.title('Distribución de los datos de la Hoja 2 con Desviación Estándar')

plt.legend()

# Mostrar el gráfico

plt.show()

import matplotlib.pyplot as plt

años = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']

Temperaturas = [18.042,17.47516667,17.83666667,16.65808333,17.53433333,17.78733333,17.43966667,19.37225,19.25716667,18.893,19.36283333,19.30658333,19.72633333,19.84175,19.66141667,19.83083333,20.16933333,20.01333333,19.11875,20.08866667,19.56908333,20.18208333,20.05766667,20.24016667,20.482,20.79608333,20.32391667,20.25391667]

fig, ax = plt.subplots()

ax.set\_ylabel('Temperaturas')

ax.set\_title('Temperaturas Minimas Promedio Anual')

plt.bar(años, Temperaturas)

# Rotar las etiquetas del eje x para que sean más legibles

plt.xticks(rotation=45)

plt.tight\_layout()  # Ajustar el diseño para evitar cortar las etiquetas

plt.show()

import folium

# Coordenadas de la ubicación de la antena

latitud = 19.209336734803742

longitud = -103.8073240612347

# Crea un mapa centrado en las coordenadas especificadas

mapa = folium.Map(location=[latitud, longitud], zoom\_start=12)

# Añade un marcador en las coordenadas especificadas

folium.Marker([latitud, longitud], popup='Ubicación').add\_to(mapa)

# Guarda el mapa como un archivo HTML

mapa.save('ubicacion.html')

# Muestra el mapa en Jupyter Notebook o en un entorno similar

mapa

**Resultados**

![](RackMultipart20231212-1-lfup93_html_aff555d3a0e21c.gif)

![](RackMultipart20231212-1-lfup93_html_cdcc66afcfc991c0.gif)

![](RackMultipart20231212-1-lfup93_html_f5e1554ac2dd5c5c.png)

![](RackMultipart20231212-1-lfup93_html_253b5bd58fa11f0c.png)

![](RackMultipart20231212-1-lfup93_html_bf18a8b52d74c21b.gif)

![](RackMultipart20231212-1-lfup93_html_c6b8fe43de3c98f5.gif)

![](RackMultipart20231212-1-lfup93_html_4f28a9d131799f9d.png)

![](RackMultipart20231212-1-lfup93_html_56edb673daffa87.png)

Hoja 2

![](RackMultipart20231212-1-lfup93_html_acc4f737ca155ff3.png)

![](RackMultipart20231212-1-lfup93_html_8209dca334f5e393.png)

![](RackMultipart20231212-1-lfup93_html_f9617498edad0537.png)

![](RackMultipart20231212-1-lfup93_html_c864b5f765577edb.png) ![](RackMultipart20231212-1-lfup93_html_74714716c5b0e5a9.png)

**Conclusión**

La experiencia de llevar a cabo un proyecto inicial sobre la falta de estudiantes en una carrera especifica y las dificultades para obtener la información necesaria destacó la complejidad en la recolección de datos.

La transición hacia un nuevo proyecto que se enfocó en el análisis de las temperaturas máximas y mínimas mensuales en Coquimatlán, Colima, desde 1990 hasta 2017 permitió abordar un tema de relevancia local, como el cambio climático y sus posibles efectos en la región, utilizando datos fácilmente accesibles de fuentes confiables, como el Servicio Meteorológico Nacional.

La importancia de la disponibilidad y accesibilidad de la información se destaca por la facilidad con la que se obtuvieron los datos para el segundo proyecto. Este cambio no solo dio a la comunidad local la oportunidad de investigar un tema relevante, sino que también permitió una verificación precisa y localizable de los efectos del cambio climático en el área.

En conclusión, lidiar con problemas de obtención de datos en el proyecto inicial llevó a un cambio reflexivo y productivo hacia un proyecto nuevo y apropiado. Este proceso destaca la importancia de la adaptabilidad y la flexibilidad en la investigación, así como la relevancia de la información local y su utilidad para comprender y abordar problemas importantes de la comunidad.

Durante el proyecto en equipo hubo algunas cosas en las cuales tuvimos problemas, por ejemplo, al sacar los promedios totales de los datos, lo tuvimos que hacer de manera manual, pero en esta actualización del proyecto ya todo es automatizado.
