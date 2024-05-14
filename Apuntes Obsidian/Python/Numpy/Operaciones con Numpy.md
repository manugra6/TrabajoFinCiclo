# Rutinas de creación de arrays

## Formstring

- Matriz inicializada a partir de datos de texto

```python
np.fromstring('1 2 3 4' , sep = ' ')
```

## Arange

- Array de valores numéricos pasados por rango al que se le puede dar un intervalo: 
```python
np.arange(1,10,2) => array([1, 3, 5, 7, 9])
np.arange(10,1,-2) => array([10,  8,  6,  4,  2])
```

## Creación de matrices

```python
# diag - Extrae la diagonal de una matriz o array de dos dimensiones
a = np.eye(N = 4)

# diagflat - Crea una matriz bidimensional con la entrada usada como diagonal.
np.diagflat(v = [1,2,3,4], k = 0)
```

# Manipulación de arrays

## Dimensiones del array

```python
# shape - Recuperas la dimension
a.shape => (2,4)

# reshape - Modificar la dimension
a.reshape((4,2))
```

## Unión de arrays

```python
# concatenate - Une un conjunto de arrays por filas o columnas
np.concatenate((a,b), axis = 0)

# stack - Parecido a join, pero genera un nuevo indice
np.stack(arrays=(a,b), axis = 0)
```

## División de arrays

```python
# split - Divide un array en varios
np.split(a, [3, 5, 10, 16])

[array([0, 1, 2]),
 array([3, 4]),
 array([5, 6, 7, 8, 9]),
 array([10, 11, 12, 13, 14, 15]),
 array([16, 17, 18, 19])]
```

## Añadir y eliminar elementos

```python 
# insert - Inserta elementos en una posicion del array
np.insert(a, obj=4, values=[5,6])
array([1, 2, 3, 4, 5, 6])

np.insert(a, obj=1, values=[5,6])
array([1, 5, 6, 2, 3, 4])

# append - Inserta elementos al final del array
np.append(a, [5,6])

# delete - Elimina un elemento del array(el indice que se le pasa)
np.delete(a, obj = 3)

# trim_zeros - Elimina los 0s al inicio y el final del array
a = np.array([0, 0, 0, 0, 1, 2, 3, 4, 0, 0])
np.trim_zeros(a)

# unique - Deja los elementos unicos del array
a = np.array([1,1,1,1,2,2,2,2,3,3,3,3])
np.unique(a)
```

# Operaciones con cadenas

```python
# add - Devuelve la concatenación de cadenas de elementos para dos matrices de str o unicode.
np.char.add(a,b)
array(['AD', 'BE', 'CF'], dtype='<U2')

# multiply - Devuelve (a * i), es decir, concatenación múltiple de cadenas, por elementos.
np.char.multiply(a, [2,3,4])
array(['AA', 'BBB', 'CCCC'], dtype='<U4')

# capitalize - Devuelve una copia de a con solo el primer carácter de cada elemento en mayúscula.
np.char.capitalize(nombres)
array(['Maria', 'Antonio', 'Francisco'], dtype='<U9')

# replace - Devuelve un array después de reemplazar los caracteres
np.char.replace(nombres, 'mar', 'sof')
array(['sofia', 'antonio', 'francisco'], dtype='<U9')

# split - Para cada elemento de a, devuelve una lista de las palabras de la cadena, utilizando sep como cadena delimitadora.
nombre = np.array(['Mi nombre es Abraham Requena'])
np.char.split(nombre, sep=' ')
array([list(['Mi', 'nombre', 'es', 'Abraham', 'Requena'])], dtype=object)
```

## Comparaciones

```python
# equal - Valores iguales
np.char.equal(a,b)
array([False,  True, False])

# greater_equal . Compara el mayor o igual a nivel cadena. A < B, o F > C
np.char.greater_equal(a,b)
array([False,  True, False])

# less_equal
np.char.less_equal(a,b)
array([ True,  True,  True])
```

## Información sobre la cadena

```python 
# endswith - Devuelve True si la palabra acaba en el char que definimos
c = np.array(['Hola', 'Adios'])
np.char.endswith(c, suffix='ios')
array([False,  True])

# startswith - Devuelve True si la palabra comienza en el char que definimos
np.char.startswith(c, prefix='Ad')
array([False,  True])

# islower - Devuelve True si todos los caracteres están en minusculas
c = np.array(['HOLA', 'adios'])
np.char.islower(c)
array([False,  True])
# islower - Devuelve True si todos los caracteres están en mayusculas
c = np.array(['HOLA', 'adios'])
np.char.isupper(c)
array([ True, False])
# isdigit - Devuelve True si todos los elementos son numericos
c = np.array(['HOLA', 'adios', '123'])
np.char.isdigit(c)
array([False, False,  True])
```

# Algebra lineal

```python 
# Producto matricial de dos matrices
np.dot(a, b)
array([[ 8, 10],[ 5,  8]])

# vdot - Devuelve el producto escalar de dos vectores.
np.vdot(a,b)
17
El calculo de arriba sería: 3*2 + 2*2 + 1*1 + 3*2 = 17

# inner - Producto interno de dos matrices.
a = np.arange(6).reshape((2,3))
b = np.arange(3)

np.inner(a, b)

Out[29]:

array([ 5, 14])

El calculo sería:
- 0 x 0 + 1 x 1 + 2 x 2 = 5
- 3 x 0 + 4 x 1 + 5 x 1 = 14

# matrix_power - Eleve una matriz cuadrada a la potencia (entera) n.
m = np.array([[2,3], [1,4]])
np.linalg.matrix_power(m, 2)
array([[ 7, 18],
       [ 6, 19]])

#La matriz m^2 es igual a el producto escalar de m x m. Podemos comprobar el resultado con _np.dot_
np.dot(m,m)
array([[ 7, 18],
       [ 6, 19]])
       
# eig - Calcula los valores propios y los vectores propios rectos de una matriz cuadrada
m = np.diag([4,3,2,1])
array([[4, 0, 0, 0],
       [0, 3, 0, 0],
       [0, 0, 2, 0],
       [0, 0, 0, 1]])

np.linalg.eig(m)
(array([4., 3., 2., 1.]),
 array([[1., 0., 0., 0.],
        [0., 1., 0., 0.],
        [0., 0., 1., 0.],
        [0., 0., 0., 1.]]))

# det - Calcula el determinante de una matriz.
np.linalg.det(m)
24.000000000000004

# solve - Resuelve una ecuación con matrices
x = np.linalg.solve(a, b)
```

# Funciones lógicas

```python
# all - Comprueba si todos los elementos de una matriz o array cumplen una condicion
a = np.array([2,3,4,5])
np.all(a < 10)
True

# any - Comprueba si algún elemento de una matriz o array cumplen una condicion

a = np.array([2,3,4,5])
np.any(a < 0)
False

# logical_and : Función lógica and. Devuelve True si todas las comprobaciones son ciertas
np.logical_and(a > 2, a < 4)
array([False,  True, False, False])

# logical_or : Función lógica or. Devuelve True si alguna de las comprobaciones son ciertas
np.logical_or(a > 2, a < 4)
array([ True,  True,  True,  True])

# Devuelve True si todas las diferencia en valor absoluto es menor a la tolerancia.
np.allclose([1e10,1e-7], [1.00001e10,1.000001e-7], rtol=0.00001)
True

#isclose - Igual, pero valor a valor
np.isclose([1e10,1e-7], [1.001e10,1.000001e-7], rtol=0.00001)
array([False,  True])

#equal - Verdadero si dos arrays o matrices son iguales en cuanto a dimensiones y valores
np.array_equal(np.array([1,2,3]), np.array([1,2,3]))
True

np.array_equal(np.array([1,2,3]), np.array([1,2,3,4]))
False

# greater - Devuelve True si el valor es mayor.
np.greater(np.array([1,2,3]), np.array([3,2,1]))
array([False, False,  True])

np.greater_equal(np.array([1,2,3]), np.array([3,2,1]))
array([False,  True,  True])

# less y less_equal funcionan igual.
np.less(np.array([1,2,3]), np.array([3,2,1]))
array([ True, False, False])

np.less_equal(np.array([1,2,3]), np.array([3,2,1]))
array([ True,  True, False])

```

# Funciones matemáticas

## Redondeo

```python
# round - Redonde un número a las cifras que definamos
array = np.array([1.435, 13.1435, 4.916])
np.round(array, 2)
array([ 1.44, 13.14,  4.92])

# floor - Devuelve el suelo - el número entero pequeño más cercano
np.floor(array)
array([ 1., 13.,  4.])

# Devuelve el techo - el siguiente número entero
np.ceil(array)
array([ 2., 14.,  5.])
```

## Sumas y productos

```python
# prod - Devuelve el producto de los elementos de la matriz sobre un eje dado
b = np.array([2,3,4])
np.prod(b)
24

b = np.array([[2,3,4],[2,2,2]])
np.prod(b, axis = 0)
array([4, 6, 8])

np.prod(b, axis = 1)
array([24,  8])

# sum - Mismo funcionamiento que prod, pero en este caso realizando la suma
np.sum(b)
15

np.sum(b, axis = 0)
array([4, 5, 6])

np.sum(b, axis = 1)
array([9, 6])
```

## Exponentes y logaritmos

```python
#exp - Calcula el exponencial de todos los elementos en la matriz de entrada.
np.exp(b)
array([[ 7.3890561 , 20.08553692, 54.59815003],
       [ 7.3890561 ,  7.3890561 ,  7.3890561 ]])

El exponencial se calcula como el número e elevado al escalar. Es decir, es equivalente a:

In [141]:

np.power(np.e, b)

Out[141]:

array([[ 7.3890561 , 20.08553692, 54.59815003],
       [ 7.3890561 ,  7.3890561 ,  7.3890561 ]])

#Para el cálculo de logaritmos tenemos las opciones:

#log: base e
p = np.power(np.e, b)
np.log(p)
array([[2., 3., 4.],
       [2., 2., 2.]])

#log10: base 10
np.log10(b)
array([[0.30103   , 0.47712125, 0.60205999],
       [0.30103   , 0.30103   , 0.30103   ]])

np.power(10, np.log10(b))
array([[2., 3., 4.],
       [2., 2., 2.]])
       
#log2: base 2
p.log2(b)
array([[1.       , 1.5849625, 2.       ],
       [1.       , 1.       , 1.       ]])

np.power(2, np.log2(b))
array([[2., 3., 4.],
       [2., 2., 2.]])
```

## Operaciones Aritméticas

```python
# Suma
np.add(a,b)

# Resta
np.subtract(a,b)

# Multiplicacion
np.multiply(a,b)

# Division
np.divide(a,b)

# Isinf sustituye los valores inf por el valor que le demos
d[np.isinf(d)] = 0
```

# Funciones estadísticas

## Orden

```python
# min y max devuelven los valores minimos y maximos de un array
print("Min", np.min(a))
print("Max", np.max(a))

np.min(b, axis = 1) # Axis 1 por filas
np.min(b, axis = 0) # Axis 0 por columnas

# percentile - Calcule el percentil q-ésimo de los datos a lo largo del eje especificado.
np.percentile(b, q = 11)

# Idem para el quantil. 
np.quantile(b, q = 0.25)

```

## Medias y varianzas

```python
# median - Calcula la mediana (valor central)
np.median(b)
50.0
np.median(np.array([1,2,0,100,200,300,50]))
50.0

# average o media (con pesos)
a = np.array([1,2,3,4])
np.average(a)
2.5
np.average(a, weights=[2,2,1,1])
2.1666666666666665
#La cuenta sería: avg = sum(a * pesos) / sum(pesos)
#1 x 2 + 2 x 2 + 3 x 1 + 4 x 1 = 13 → 13 / 6 = 2.16

# mean - Practicamente idéntico
np.mean(b, axis = 0) # Media por columnas
array([4.5, 5.5, 6.5])

np.mean(b, axis = 1) # Media por filas
array([ 1.,  4.,  7., 10.])

# std - Desviacion estándar
np.std(b, axis = 0)
array([3.35410197, 3.35410197, 3.35410197])

np.std(b)
3.452052529534663

# var - Varianza
np.var(b, axis = 1)
```