import math

def Leer_fraccion():
    n1 = int(input("Escriba el primer número: "))
    n2 = int(input("Escriba el segundo número: "))

    return Simplificar_fraccion(n1, n2)

def Escribir_fraccion(numerador,denominador):
    if denominador==1:
        print(numerador)
    else:
        print(f"{int(numerador)}/{int(denominador)}")

def Simplificar_fraccion(numerador,denominador):
    mcd = math.gcd(int(numerador),int(denominador))
    
    nume=numerador/mcd
    denom=denominador/mcd
    
    return nume,denom

def Sumar_fracciones (n1,d1,n2,d2):
    numerador=n1*d2 + d1*n2
    denominador= d1*d2
    numerador, denominador = Simplificar_fraccion(numerador, denominador)
    return numerador, denominador

def Restar_fracciones (n1,d1,n2,d2):
    numerador=n1*d2 - d1*n2
    denominador= d1*d2
    numerador, denominador = Simplificar_fraccion(numerador, denominador)
    return numerador, denominador

def Multiplicar_fracciones (n1,d1,n2,d2):
    numerador=n1*n2
    denominador= d1*d2
    numerador, denominador = Simplificar_fraccion(numerador, denominador)
    return numerador, denominador

def Dividir_fracciones (n1,d1,n2,d2):
    numerador=n1*d2 + d1*n2
    denominador= d1*d2
    numerador, denominador = Simplificar_fraccion(numerador, denominador)
    return numerador, denominador

n1,d1=Leer_fraccion()
n2,d2=Leer_fraccion()

Escribir_fraccion(*Sumar_fracciones(n1,d1,n2,d2))