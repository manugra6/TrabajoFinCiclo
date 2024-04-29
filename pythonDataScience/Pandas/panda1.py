import pandas as pa
import numpy as np

from pathlib import Path

datos = pa.read_csv('house.csv')
# EJERCICIO 1
# 8 habitaciones?
datos.query('bedrooms==8').shape

# Numero minimo y maximos de habitaciones

habitaciones = datos['bedrooms']

habitaciones.min()
habitaciones.max()

# Nueva columna que sea la relación precio/planta

datos['precio_planta']=datos['price']/datos['floors']

# EJERCICIO 2
# Precio de la casa de la fila 256
datos.loc[256,'price']

#Numero de habitaciones de la fila 215 a 222

datos.loc[215:222,'bedrooms']

# Selección aleatoria del 15% del DF

sample = datos.sample(frac=0.15)

# Filtra los registros con 3 o 4 habitaciones y precio menos a 300000 euros

sample.query('bedrooms in (3,4) and price < 300000')

#Ejercicio 3

v = [['caracteristicas','caracteristicas','caracteristicas','caracteristicas','caracteristicas','caracteristicas',
    'caracteristicas','caracteristicas','caracteristicas','caracteristicas','caracteristicas','caracteristicas',
    'caracteristicas','caracteristicas', 'localizacion', 'localizacion', 'localizacion', 'localizacion', 
    'caracteristicas'],
     ['date', 'price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot',
       'floors', 'waterfront', 'view', 'condition', 'sqft_above',
       'sqft_basement', 'yr_built', 'yr_renovated', 'street', 'city',
       'statezip', 'country', 'price_by_floor']]

tuplas = list(zip(*v))
m = pa.MultiIndex.from_tuples(tuplas)
datos.columns=m
datos.sort_index(level=0,axis=1,inplace=True)

# EJERCICIO 4
# Convierte la columna date a tipo fecha
datos2 = pa.read_csv('house.csv')
datos2['date'] = pa.to_datetime(datos2['date'],yearfirst=True)

# Generar 3 nuevas columnas extrayendo el año mes y dia

datos2['year']=datos2['date'].dt.year
datos2['month']=datos2['date'].dt.month
datos2['day']=datos2['date'].dt.day

# Precio medio por mes
datos2.set_index(datos2['date']).resample('1M')['price'].mean()

# Nueva columna date2 que le sume 20 dias a la columna date
deltatime = pa.Timedelta('20 days')
datos2['date2'] = datos2['date']+deltatime 