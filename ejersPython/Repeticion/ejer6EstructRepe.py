#Escribir un programa que imprima todos los números 
#pares entre dos números que se le pidan al usuario.

n1 = int(input("Valor del primer numero: "))
n2 = int(input("Valor del segundo numero: "))

for i in range(n1,n2):
    if i%2==0:
        print(i)
        

