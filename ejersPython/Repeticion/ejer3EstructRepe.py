#Algoritmo que pida números hasta que se introduzca un cero. 
# Debe imprimir la suma y la media de todos los números introducidos.
su=0
cont=0
media=0

n=int(input("Introduzca un numero (0 si quiere salir) "))
while n!=0:
    su=su+n
    cont=cont+1
    n=int(input("Introduzca un numero (0 si quiere salir) "))

if cont>0:
    
    media=su/cont
else:
    media=0

print("Suma: ",su)
print("Media: ",media)