#Ingreso de numero y ordenamiento ASCENDENTE, DESCENDENTE, MAXIMO, MINIMO

numero= int(input("Ingrese un numero por favor"))
numeros=  []

for i  in range(numero):
    num = int (input(f"num{i+1} :"))
    numeros.append(num)

numeros.sort()
print(numeros)
numeros.sort(reverse = True)
print(numeros)
  
print(f"Maximo: {max(numeros)}")
  