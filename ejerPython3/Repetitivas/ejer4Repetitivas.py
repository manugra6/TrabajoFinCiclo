#Crea una aplicación que permita adivinar un número. En primer lugar la aplicación solicita un número 
#entero por teclado. A continuación va pidiendo números y va respondiendo si el número a adivinar es 
#mayor o menor que el introducido. El programa termina cuando se acierta el número.

numero = int(input("Inserte un numero: "))
adivinar = int(input("Intenta adivinar el numero introducido: "))
while adivinar!=numero:
    if adivinar<numero:
        print("El numero es mayor que el que ha puesto")
    elif adivinar>numero:
        print("El número que ha insertado es menor que el que intenta adivianr")
    adivinar=int(input("Error, intentelo de nuevo: "))
        
print("Ha acertado el numero")