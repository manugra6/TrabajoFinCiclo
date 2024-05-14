# Operaciones básicas

```python
data.head() # Enseña la tabla desde el principio
data.tail() # Enseña la tabla desde el final
data.shape() # 
data.dtypes() # tipos de datos en cada columna
data.describe() #descripcion de las columnas
data.mean() # media de cada columna
data.median() #mediana
data.['columna'].value_counts(dropna=false,normalise=true) #cuenta el numero de valores que se encuentran en una columna
data.sort_values(by='columna', ascending=True, inplace=False)

# QCUT y Cut
pa.qcut(data['columna'],q=5) # crea segmentos del mismo tamaño
pa.cut(data['columna'],bins=3) # cut crea segmentos definidos por nosotros

# Ordenar el DataFrame por el valor de la columna
data.sort_values(by = 'bedrooms', ascending = True, inplace=False).head()

#Copy
_=data.query('condicion a filtrar')
data2 = _.copy(deep=false)
```

# DataFrames

```python
# Ejemplo creación
df = pd.DataFrame({'col1':[1,2,3,4],
                   'col2':[444,555,666,444],
                   'col3':['abc','def','ghi','xyz']})
# Buscar datos
df.loc['G1'] #se obtienen todos los datos del index G1
df.loc['G1'].loc[1].loc['A'] # datos de index G1, subindex 1 columna A

# Indices
df.set_index('States', inplace = True) # setea una columna com indicesç
df.reset_index() # convierte el indice a columna

# Fechas
df = pd.DataFrame({
    'Nombre': ['Alicia','Pedro','Carlos'],
    'Fecha_nacimiento': ['10/25/2005','10/29/2002','01/01/2001']
})
df['Fecha_nacimiento'] = pd.to_datetime(df['Fecha_nacimiento'])

df['anyo_nacimiento'] = df['Fecha_nacimiento'].map(lambda x: x.strftime('%Y'))#esto añade el año como columna
```
# Datos missing

```python
# numerod de NAs de cada columna
data.isna().sum()
#cuenta el numero de valores que se encuentran en una columna, incluye los nulos
data.['columna'].value_counts(dropna=false) 
# filtra los valores que son na true y no los añade
data['columna'].notna() 

#hace la media sin saltarse los minimos sirve tambien con el minimo, el maximo...
data['columna'].mean(skipna=False) 

b=data['columna'].fillna(value = -1) # rellena los valores missing en la columna

# axis = 'index' elimina todas las filas con algun nan
data.dropna(axis = 'index', how = 'any').shape
  
# axis = 'columns' elimina todas las columnas con algun nan 
data.dropna(axis = 'columns', how = 'any').shape
```

# Operaciones

```python
# Concatenar dataframes (mismas columnas diferentes indices)
df = pd.concat([df1, df2], axis = 0) // df1.append(df2, ignore_index=True).head()
# (Mismos indices diferentes columnas)
df = pd.concat([df1, df2], axis = 1)
# Merge como un JOIN
df = df1.merge(df2, how = 'left', left_on = 'city', right_on = 'city')
```

# Tablas pivotantes

```python
# Son tablas que resumen los contenidos de otra misma
# se pueden agrupar en una variable
_ = df.pivot(index='date', columns='variable', values='value')
# o en varias
_ = df.pivot(index=['date', 'variable'], columns='variable2', values='value')

# stack(), reduce el numero de columnas
stack = _.stack().to_frame()
# unstack(), Mueve uno de los indices a columna (pasa de fila a columna)
stack.unstack(level = 0)
stack.unstack(level=['date','variable'])

# melt: La función melt nos sirve para convertir el nombre de varias variables en el dominio de una sola
data_cal.melt(id_vars=['nombre','apellido'])

#La función pivot_table() se puede utilizar para crear tablas dinámicas.
pd.pivot_table(data = df, index = 'date', columns='variable', values = 'value')
  
pd.pivot_table(data = df, index = ['date', 'variable2'], columns='variable', values = 'value')
#Con agregaciones y calculos: 
pd.pivot_table(data = df, index = 'date', columns='variable2', values = 'value', aggfunc='mean')
```

# Agrupaciones

```python
#- Dividir los datos en grupos según algunos criterios.
#- Aplicar una función a cada grupo de forma independiente.
#- Combinar los resultados en una estructura de datos.
g = data.groupby('condition')
# se puede agrupar en varias creando un multiindex
g = data.groupby(['condition','waterfront'])['price'].mean()
df.groupby(['Company','Person']).sum()
#En lugar de agrupar por una columna, también es posible agrupar por un valor del indice.
dfg.groupby(level=1)['price'].mean()
# Asi se puede saber la media de un grupo entero
df.groupby('Company').mean()
df.groupby('Company').mean().loc['FB'] #o para un dato en concreto

#max y min
df.groupby('Person').max()
df.groupby('Person').min()

#AGREGACIONES: 
data.groupby('condition').agg({
    'price' : 'mean',
    'bathrooms' : 'median',
    'waterfront' : 'max',
    'floors' : 'min'
})
#También se puede aplicar distintas operaciones a la misma columna agregada
agrupacion = data.groupby('condition').agg({
    'price' : [np.mean, np.min, np.max],
    'bathrooms' : 'median',
    'waterfront' : np.max,
    'floors' : ['min', 'max']
})

#También se puede usar el método apply para personalizar una función.
def media_mayores_1millon(x):
    return np.mean(x[x > 1_000_000])

data[['price','condition']].groupby('condition')['price'].apply(media_mayores_1millon)
```

# Visualización

```python
# Gráfico de lineas:
df[['price']].plot(figsize = (20, 8))

# Gráfico de barras: 
df[['bathrooms']].plot(kind = 'bar', figsize = (20, 8))
df[['bathrooms', 'floors']].plot(kind = 'bar', figsize = (20, 8))

# Gráfico de puntos
df.plot(kind = 'scatter', x = 'yr_built', y = 'sqft_above', figsize = (10, 8))

# Grafico de cajas
df[['bathrooms', 'floors']].plot(kind = 'box', figsize = (10, 8))
df['price'].plot(kind = 'box', figsize = (10, 8))

# Gráfico de tarta
df['condition'].value_counts(normalize = True).plot(kind = 'pie', figsize = (10, 8), legend = True)
```