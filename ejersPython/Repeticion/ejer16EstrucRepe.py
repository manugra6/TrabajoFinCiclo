#Una empresa les paga a sus empleados con base en las horas trabajadas en
#la semana. Realice un algoritmo para determinar el sueldo semanal de N 
#trabajadores y, además, calcule cuánto pagó la empresa por los 
#N empleados.
import random

aco=0
n_empleados = int(input("Inserte el numero de empleados de la empresa "))

for i in range(1,n_empleados+1):
    horas = random.randint(20,40)
    sueldo = horas*10
    print("Al empleado nº"+str(i)+" le pagan: "+str(sueldo))
    aco=sueldo+aco

print("La empresa tendra que pagar: "+str(aco))