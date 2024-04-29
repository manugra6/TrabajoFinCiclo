import numpy as np
import numpy.ma as ma

# Ejer 1

impar = np.arange(1,100,2)
nomb_completo=np.array({"Manuel", "Graña", "Malvido"})
fechas = np.arange('2020-01-01','2020-02-04',dtype='datetime64[D]') 

# Ejer 2: Recupera los últimos 10 elementos del array de impares
impar[:len(impar)-11:-1]

#Ejercicio 3 Recorre el array de fechas, y genera un nuevo numpy array 
# que contenga unicamente los días laborales

fechas[np.is_busday(fechas)]

# Ejer 4: Generar matriz propuesta, de que tipos es? Mascara a numeros 
# mayores o iguales a 10

matriz = np.matrix('10 1 8 4 ; 3 7 2 1 ; 0 2 20 12')
print(matriz.dtype)

mask = matriz is ma.masked==True

#Ejercicio 5
#Crea dos fechas, la primera de ellas será tu fecha de nacimiento, y la segunda, la de un familiar o amigo tuyo.
#-¿Qué diferencia en horas hay entre las dos fechas?
#-¿Cual sería tu fecha de nacimiento si hubieras nacido 236 horas antes?

nacimiento = np.datetime64('2001-10-12')
nacOtro = np.datetime64('2001-04-20')

difference = nacimiento-nacOtro
print(np.timedelta64(difference,'h'))

antes = np.timedelta64(236,'h')
nac_nuevo = nacimiento-antes
print(nac_nuevo)
