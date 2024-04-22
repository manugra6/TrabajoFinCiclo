#Escribe un programa que diga si un número introducido por teclado es o no primo. Un número primo es
#aquel que sólo es divisible entre él mismo y la unidad.

numero=int(input("Introduzca numero: "))
esPrimo=True
divisibleEntre=[]
for cont in range(2,numero):
    if numero%cont==0:
        divisibleEntre.append(cont)
        esPrimo=False
        
if esPrimo and numero==0:
    print("El numero es 0")
elif esPrimo:
    print("El numero es primo")
else: 
    print("El numero no es primo")
    print(f"Es divisible entre : {divisibleEntre}")