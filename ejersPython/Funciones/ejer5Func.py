def calcularMaxMin (nums):
    maximo = max(nums)
    minimo = min(nums)
    print(f"Maximo: {maximo}  Minimo: {minimo}")
    
numeros=[]
for i in range(5):
    num=int(input("Introduzca numero: "))
    numeros.append(num)
    
calcularMaxMin(numeros) 
