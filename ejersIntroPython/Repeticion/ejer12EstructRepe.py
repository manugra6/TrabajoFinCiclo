#Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, 
#si al final de cada mes deposita cantidades variables de dinero; 
# además, se quiere saber cuánto lleva ahorrado cada mes.

aco=0
try:
    for i in range(1,13):
        dinero=int(input("Cuanto dinero desea insertar el mes "+str(i)+"?: "))
        aco=dinero+aco
    print("Dinero ahorrado en 1 año: "+str(aco))    
except:
    print("Excepcion")
    