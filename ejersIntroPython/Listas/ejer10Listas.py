#Diseñar el algoritmo correspondiente a un programa, que:

    #Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
    #Carga la tabla con valores numéricos enteros.
    #Suma todos los elementos de cada fila y todos los elementos de 
    # cada columna visualizando los resultados en pantalla.
import random

tabla =[]

for i in range(0,5):
    fila=[]
    for j in range(0,5):
        n=random.randint(1,5)
        fila.append(n)
    tabla.append(fila)
    
for fila in tabla:
    print(fila)

          
print("Suma de cada fila: ")
for i in tabla:
    sumFila = sum(i)
    print(f"Suma fila: {sumFila}")
    
print("Suma de cada columna: ")
for j in range(5):
    sumCol=sum(fila[j] for fila in tabla)
    print(f"Suma columna {j + 1}: {sumCol}")  