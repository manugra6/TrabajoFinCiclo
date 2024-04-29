import numpy as np

# array = np.array([44, 28,  8, 34, 34, 26, 32, 12, 28,  6, 19, 12, 46, 20, 20, 49, 18,
#        19, 15, 15, 43,  3, 17, 33, 27, 10, 18,  2,  3,  3, 35, 35, 21, 17,
#        36, 31, 16, 27,  6, 46, 29, 25, 26, 48, 30, 19, 18,  1, 43, 10, 32,
#        15, 32, 30, 40, 41, 11, 46, 39,  5, 40,  1, 26, 10, 18, 26, 25, 25,
#        21, 30, 12, 46,  1, 43,  1,  3, 26, 24,  0, 36, 34,  7, 26, 25, 41,
#        22,  1, 16, 43,  1, 46, 14, 17, 39, 12,  9, 42, 48,  9, 45, 47, 32,
#        15,  6, 40, 18,  6, 13, 35,  8, 46, 48, 26, 23, 12, 29, 21,  6,  3,
#        22, 27, 16, 27, 10, 28, 23,  5, 24, 17, 43, 25, 11, 38, 40, 32, 42,
#        27, 32,  6, 16, 18, 10, 18, 34, 34,  3,  4,  5,  4,  0, 35, 30,  9,
#        16, 32, 46,  7, 10, 20, 13, 48,  8, 27, 27, 27, 16, 17, 12, 35, 31,
#        21, 29, 15, 49, 14, 22, 18,  0, 13, 14, 39, 30,  4, 48,  1, 19, 33,
#        39,  9,  0, 24,  6, 12, 24, 29, 16, 11, 12, 13, 11])

# np.median(array)
# np.average(array)

# np.quantile(array,0,5)

# np.percentile(array,25)
# np.percentile(array,50) #Lo mismo que la mediana

# np.std(array)

# np.var(array)

import numpy as np

arr_int = np.array([1, 2, 3, 4])
print(arr_int)  # int64 (dependiendo del sistema puede variar)

arr_float = np.array([1.0, 2.5, 3.7])
print(arr_float)

arr_bool = np.array([True, False, True])
print(arr_bool)  # bool

arr_str = np.array(['hola', 'mundo'])
print(arr_str)