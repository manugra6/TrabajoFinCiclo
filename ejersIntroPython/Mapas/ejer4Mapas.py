#Codifica un programa en python que nos permita guardar los nombres de 
#los alumnos de una clase y las notas que han obtenido.
#Cada alumno puede tener distinta cantidad de notas. Guarda la información
#en un diccionario cuya claves serán los nombres de los alumnos y 
#los valores serán listas con las notas de cada alumno.

#El programa pedirá el número de alumnos que vamos a introducir,
#pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos 
#un número negativo. Al final el programa nos mostrará la lista de 
#alumnos y la nota media obtenida por cada uno de ellos. 
#Nota: si se introduce el nombre de un alumno que ya existe el 
#programa nos dará un error.

clase = {}

num=int(input("Inserte numero de alumnos: "))
for i in range(num):
    nombre=input("Inserte nombre del alumno: ")
    while nombre in clase:
        nombre=input("Inserte otro nombre del alumno: ")
        print("El nombre del alumno ya existe")
        
    notas=[]
    while True:
        nota = float(input("Inserte nota (negativa para terminar): "))
        if nota<0:
            break
        notas.append(nota)
    clase[nombre]=notas
    
    for nombre,notas in clase.items():
        media = sum(notas)/len(notas)
        print(f"{nombre}: Notas: {notas}, Media {media:.2f}")
        
    
        