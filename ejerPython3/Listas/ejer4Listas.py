#Dado una lista, hacer un programa que indique si está ordenada o no.

lista=[1,9,5,8,4]
lista2=sorted(lista)

if lista==lista2:
    print("La lista está ordenada")
else:
    print("La lista NO está ordenada")
