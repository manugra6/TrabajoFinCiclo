#Crea un programa python que lea una cadena de caracteres y muestre la siguiente información:

# La primera letra de cada palabra. Por ejemplo, si recibe Universal Serial Bus debe devolver USB.
# Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, 
#  si recibe república argentina debe devolver República Argentina.
# Las palabras que comiencen con la letra A. Por ejemplo, si recibe Antes de ayer debe devolver 
#  Antes ayer.

cadena = input("Escriba cadena: ")

lista = cadena.split(" ")
listaCapitalize=[]
porA=[]
for cad in lista:
    print(cad[0], end=" ")
    listaCapitalize.append(cad.capitalize())
    if cad[0]=='a' or cad[0]=='A':
        porA.append(cad)
print("\n")    
print(' '.join(listaCapitalize)+"\n")
print(' '.join(porA))    
    

