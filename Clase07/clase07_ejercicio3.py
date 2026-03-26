# Leer una serie de numeros enteror mayores o igual a cero
# contar la cantidad de numeros leidos

# la serie termina cuando se lee un número negativo

n= int(input())

cnt= 0

while n >= 0:
    cnt +=1
    n= int(input())

print("La cantidad de leidos fue:", cnt)