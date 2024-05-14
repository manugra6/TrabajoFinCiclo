# Series

## Usando un Numpy array
```python
#Con un numpy array
valores = np.array([1,2,3,4,5])
serie = pd.Series(valores)
0    1
1    2
2    3
3    4
4    5

RangeIndex(start=0, stop=5, step=1)
serie = pd.Series(valores, index = ['a','b','c','d','e'])
a    1
b    2
c    3
d    4
e    5

dtype: int64
serie.index
Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
```

## Diccionario(Mapa) de Python

```python
d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
serie = pd.Series(d)
a    1
b    2
c    3
d    4
e    5
dtype: int64

#Si usamos el diccionario, y además especificamos un indice, los valores se ordenan según el indice ordenado
serie = pd.Series(d, index = ['b','c','a','e','d'])
b    2
c    3
a    1
e    5
d    4
dtype: int64

#La serie actúa de manera muy similar a un numpy array y es un argumento válido para la mayoría de las funciones NumPy.
np.sum(serie)
15

np.max(serie)
5

#Podemos consultar los valores especificando un valor del indice. También podemos consultar el tipo de la serie con _dtype_ y convertirlo a un numpy array con la función _to_numpy()_

serie['b']
2

serie[0]
2

array = serie.to_numpy()
array([2, 3, 1, 5, 4])

#También podemos interpretar el tipo Serie de pandas como un diccionario python, de manera que podemos tanto consultar, como añadir nuevos pares clave-valor a la misma.

serie['e']
5
serie['f'] = 6

b    2
c    3
a    1
e    5
d    4
f    6
dtype: int64

'e' in serie
True

'h' in serie
False

#Y como diccionario que se puede considerar, podemos pedir sus claves y sus valores
serie.keys()
Index(['b', 'c', 'a', 'e', 'd', 'f'], dtype='object')
serie.values
array([2, 3, 1, 5, 4, 6])

#Cuando hemos trabajado con matrices NumPy, normalmente no era necesario recorrer valor a valor la misma para aplicar una operación. Lo mismo ocurre cuando se trabaja con Series en pandas.

serie * 2

Out[35]:

b     4
c     6
a     2
e    10
d     8
f    12
dtype: int64

serie.keys()
Index(['b', 'c', 'a', 'e', 'd', 'f'], dtype='object')
serie2 = pd.Series(np.random.randint(0,10,6), index = ['b', 'c', 'a', 'e', 'd', 'f'])

b    2
c    4
a    0
e    7
d    4
f    8
dtype: int64

serie + serie2
b     4
c     7
a     1
e    12
d     8
f    14
dtype: int64

#Si algun indice no coincide, se almacena un NaN
serie2['g'] = 10

serie + serie2

a     1.0
b     4.0
c     7.0
d     8.0
e    12.0
f    14.0
g     NaN
dtype: float64
```

# DataFrame

## Usando diccionario de series

```python
l = [{'col1': 1, 'col2' : 4}, {'col1': 2, 'col2' : 3},  
     {'col1': 3, 'col2' : 2}, {'col1': 4, 'col2' : 1, 'col3' : 3}]

df = pd.DataFrame(l, index = ['a','b','c','e'])

||col1|col2|col3|
|---|---|---|---|
|a|1|4|NaN|
|b|2|3|NaN|
|c|3|2|NaN|
|e|4|1|3.0|

# Recupero la columna con []
df['col2']

# Asignando valores a una columna sumando otras
f['col4'] = df['col1'] + df['col2']
df
||col1|col2|col3|col4|
|---|---|---|---|---|
|a|1|4|NaN|5|
|b|2|3|NaN|5|
|c|3|2|NaN|5|
|e|4|1|3.0|5|

# Elimino columnas con del
del df['col3']

# Insertar columna
df.insert(0, 'col0', df['col4'] + df['col2'])

# Crear columa
df = df.assign(col3 = 3)
```

# Lectura y escritura

## Lectura

```python
# CSV
dataset = pd.read_csv(data_path / 'dataset.csv', sep = ',')
dataset.head()

||Number|City|Gender|Age|Income|Illness|
|---|---|---|---|---|---|---|
|0|1|Dallas|Male|41|40367.0|No|
|1|2|Dallas|Male|54|45084.0|No|
|2|3|Dallas|Male|42|52483.0|No|
|3|4|Dallas|Male|40|40941.0|No|
|4|5|Dallas|Male|46|50289.0|No|

pd.read_csv(data_path / 'dataset.csv', sep = ',', usecols=['Gender','Age']).head()
||Gender|Age|
|---|---|---|
|0|Male|41|
|1|Male|54|
|2|Male|42|
|3|Male|40|
|4|Male|46|

# JSON
dataset.head(100).to_json(data_path / 'dataset_records.json', orient='records')
ds = pd.read_json(data_path / 'dataset_index.json', orient='index')
ds.head()

ds = pd.read_json(data_path / 'dataset_index.json', orient='index')
ds.head()
||Number|City|Gender|Age|Income|Illness|
|---|---|---|---|---|---|---|
|0|1|Dallas|Male|41|40367|No|
|1|2|Dallas|Male|54|45084|No|
|2|3|Dallas|Male|42|52483|No|
|3|4|Dallas|Male|40|40941|No|
|4|5|Dallas|Male|46|50289|No|
```

