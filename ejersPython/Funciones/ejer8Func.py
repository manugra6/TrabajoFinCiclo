def factorial (num):
    if num==0 or num==1:
        return 1
    else:
        return num * factorial(num-1)
    
num=int(input("Introduce un numero para el calculo de su factorial: "))
resultado = factorial(num)
print(f"El factorial de {num} es: {resultado}")