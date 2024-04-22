#Dada una lista de cadenas, pide una cadenena por teclado e indica si está en la lista, indica cuantas 
#veces aparece en la lista, lee otra cadena y sustituye la primera por la segunda en la lista, 
#y por último borra la cadena de la lista

cadenas = ["nando","como","lonsez","lechero","asturiano","como"]

cad = input("Inserte cadena para ver si está en la lista: ")

if cad in cadenas:
    print("La cadena se encuentra en la lista")
else:
    print("La cadena no está")
    
num = len(cadenas)
print(f"La cadena se encuentra: {cadenas.count(cad)} veces")

cad2 = input("Inserte cadena a sustituir: ")

for i in (0,num):
    posicion = cadenas.index(cad)
    cadenas[posicion]=cad2
print(cadenas)