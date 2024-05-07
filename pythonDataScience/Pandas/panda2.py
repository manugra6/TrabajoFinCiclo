import pandas as pa
import numpy as np

import warnings

from pathlib import Path

datos = pa.read_csv('house.csv')

# EJERCICIO 1
# Añade una una nueva columna al DF con nombre price_grp
# Esta columna tendrá valores entre 0 y 5, siendo 0 el 20% de fila con el precio más barato, 
# y 5, el 20% de casas con el precio más caro.

price_grp = pa.qcut(datos['price'],q=5,labels=np.arange(5))
datos = datos.assign(price_grp = price_grp)

# Comprueba si hay valores missings, si es asi, se sustituye por otro valor

datos.isna().sum() # no hay datos missing

# Cual es el precio medio de las casas

print(datos['price'].mean())

# EJERCICIO 2

# Genera un dataframe que contenga el número medio de baños ('bathrooms') y plantas ('floors') 
# por cada valor de la variable 'condition'.

dfAux1 = datos.groupby('condition').agg({
    'bathrooms': 'mean',
    'floors': 'mean'
})


# Genera otro dataframe con el precio min y máximo (mayores que 0) por cada valor de la 
# variable 'condition'.
dfAux2 = datos.groupby('condition').agg({
    'price' : ['min','max']
})

#Une ambos dataframes para tener un último DF con toda la info
df = dfAux1.join(dfAux2, on = 'condition')


# Genera una pivot table que muestre el precio medio por planta y condición (floors y condition). Es decir, la tabla debe mostrar información del tipo:
pv = pa.pivot_table(data = datos, index = 'condition', columns = 'floors', values = 'price', aggfunc=np.mean)

# Las casa con 1 planta y condición 1 tienen de media un precio de 282560€
# Las casa con 2 planta y condición 3 tienen de media un precio de 622919€
# Rellena los valores missings con 0.
pv.fillna(0, inplace = True)
# Por último, representa los valores de las casas de una planta en un gráfico de barras
pv[1.0].plot(kind = 'bar')