# -*- coding: utf-8 -*-
"""Practica6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wqkArnm1T0Kfx1QD6QfmJNY6-yP5X08P
"""

import pandas as pd
import matplotlib as plit
import seaborn as sns
from matplotlib import pyplot
import openpyxl

from google.colab import files

df = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/autos2.csv")

df.price.min()

df.price.max()

df.price.moda()

df.price.media()

df.price.mediana()

df.price.std()

df.describe()

plit.pyplot.hist(df.price, bins=18)
pyplot.title("Tabla de precios")
pyplot.xlabel("Precios de vehiculos")
pyplot.show()

"""En mi conclusion sobre los precios, estan vistos que los precios de ellos son en su mayoria bajos, ya que estan dentro de los 5 mil hasta los 20 mil, siendo la mayoria en ese rango, mientras que la minoria abarca desde los 25 mil hasta los 45 mil pesos de los vehiculos."""

pyplot.figure(figsize=(10, 6))
sns.boxplot(y='body-style' ,x='price', data=df)
pyplot.ylabel('Tipo de Vehículo')
pyplot.xlabel('Precio del Automóvil')
pyplot.title('Relación entre Precio y Tipo de Vehículo')
pyplot.grid(axis='y')
pyplot.show()

"""Las conclusiones sobre los precios que se tienen y sobre los vehiculos, se ven de gran forma que si quiere tener sobre dos tipos de carros, es que estan puestos sobre el precio que se tienen en ellos por calidad, ya que estan desde precios bajos hasta precios altos, excepto por dos marcas que estan por bajo precio, siendo a consideracion para querer tener un tipo de vehiculo al gusto de nuestro presupuesto."""

pyplot.figure(figsize=(10, 6))
sns.boxplot(y='drive-wheels' ,x='price', data=df)
pyplot.ylabel('Tipo de rueda')
pyplot.xlabel('Precio del Automóvil')
pyplot.title('Relación entre Precio y Tipo de rueda')
pyplot.grid(axis='y')  # Agregamos una cuadrícula horizontal
pyplot.show()

"""<h5>Las conclusiones sobre los tipos de rueda, ya que se nota que dos de ellos tienen un precio con poca alteracion, mientras que el primero se nota a gran medida que tiene mucha variedad de precios, siendo desde bajo precio a alto precio por la rueda, pensando que seria mas para otros tipos de vehiculos<h5>"""

pyplot.figure(figsize=(10, 6))
sns.boxplot(y='engine-location' ,x='price', data=df)
pyplot.ylabel('localizacion de motor')
pyplot.xlabel('Precio del Automóvil')
pyplot.title('Relación entre Precio y Localizacion del motor')
pyplot.grid(axis='y')  # Agregamos una cuadrícula horizontal
pyplot.show()

"""Por ultima conclusion de la localizacion del motor de los vehiculos, se nota que es mucho menor costo tener en la parte de enfrente para poder generar mayor cantidad de vehiculos a un precio menor que los vehiculos que tienen en la parte detras, siendo hasta casi el triple de caros que los de enfrente.

<h1>Conclusiones<h1>
<h4>Las conclusiones sobre la practica es que sobre la cuestion de los precios sobre diferentes partes de los vehiculos son muy variados, ya que esta bien visto sobre essos cambios con cierta forma de ver que tenemos que tener en cuenta sobre al momento de comprar piezas<h4>
"""