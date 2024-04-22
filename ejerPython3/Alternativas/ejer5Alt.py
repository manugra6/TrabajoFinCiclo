año = int(input("Introduzca el numero de un año: "))

if año%4==0 and (año%100!=0 or año%400==0):
    print("Es año bisiesto")
else:
    print("no es bisiesto")