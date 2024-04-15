#Se quiere realizar un programa que lea por teclado las 5 notas obtenidas
#por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar 
#todas las notas, la nota media, la nota más alta que ha sacado y la menor.
notas=[]

for i in range(0,5):
    nota= int(input("Inserte nota: "))
    while nota<0 or nota>10:
        nota= int(input("Numero incorrecto, vuelva a insertar nota: "))
    notas.append(nota)

suma=sum(notas)
media=suma/len(notas)
print ("Notas del alumno: "+ str(notas))
print ("Suma del alumno: "+ str(suma))
print ("Media del alumno: "+ str(media))
