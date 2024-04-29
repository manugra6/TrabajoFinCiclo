import numpy as np

#Ejercicio 1
# -¿Hay algún valor múltiplo de 7?

nums = np.array([2, 5, 4, 2, 49, 34, 59, 21,45, 6, 105])
np.any(nums % 7==0)

# -Devuelve un array con todos los nº menores de 40 o que sean múltiplos de 7

result = nums[np.logical_or(nums%7==0, nums<40)]

#Ejercicio 2
#Usando el array resultado del ejercicio anterior, calcula:

# -El producto de todos sus valores

prod = np.prod(result)

#Convierte el array el una matriz 3x3 y realiza la suma por filas

tres=result.reshape(3,3)

#Calcula el log10 de cada elemento de la matriz que acabas de crear

np.log10(tres)

#Ejercicio 3
# Haciendo uso de la matriz 3x3 creada en el ejercicio anterior y del siguiente array a, calcule:

#La suma de la matriz más el vector
a = np.array([0,3,5])
np.add(tres,a)

#La división de ambos. ¿qué ocurre? Modifique el valor extraño por 0.
div=np.divide(tres,a)
div[np.isinf(div)]=0

#El valor máximo de la matriz resultado de la división. ¿y por filas? ¿y por columnas?
np.max(div)
np.max(div, axis=0)#filas
np.max(div, axis=1)#columnas

#Ejercicio 4

array = np.array([44, 28,  8, 34, 34, 26, 32, 12, 28,  6, 19, 12, 46, 20, 20, 49, 18,
       19, 15, 15, 43,  3, 17, 33, 27, 10, 18,  2,  3,  3, 35, 35, 21, 17,
       36, 31, 16, 27,  6, 46, 29, 25, 26, 48, 30, 19, 18,  1, 43, 10, 32,
       15, 32, 30, 40, 41, 11, 46, 39,  5, 40,  1, 26, 10, 18, 26, 25, 25,
       21, 30, 12, 46,  1, 43,  1,  3, 26, 24,  0, 36, 34,  7, 26, 25, 41,
       22,  1, 16, 43,  1, 46, 14, 17, 39, 12,  9, 42, 48,  9, 45, 47, 32,
       15,  6, 40, 18,  6, 13, 35,  8, 46, 48, 26, 23, 12, 29, 21,  6,  3,
       22, 27, 16, 27, 10, 28, 23,  5, 24, 17, 43, 25, 11, 38, 40, 32, 42,
       27, 32,  6, 16, 18, 10, 18, 34, 34,  3,  4,  5,  4,  0, 35, 30,  9,
       16, 32, 46,  7, 10, 20, 13, 48,  8, 27, 27, 27, 16, 17, 12, 35, 31,
       21, 29, 15, 49, 14, 22, 18,  0, 13, 14, 39, 30,  4, 48,  1, 19, 33,
       39,  9,  0, 24,  6, 12, 24, 29, 16, 11, 12, 13, 11])

# Valor medio y mediano
np.median(array)
np.average(array)

# ¿Qué valor se encuentra en el tercer cuártil?
np.quantile(array,0,5)

# ¿Qué valor se encuentra en el percentil 25? ¿y en el 50? ¿con qué valor coincide este último?
np.percentile(array,25)
np.percentile(array,50) #Lo mismo que la mediana

# ¿Cuál es la desviación estándar y la varianza del conjunto de datos?
np.std(array)

np.var(array)