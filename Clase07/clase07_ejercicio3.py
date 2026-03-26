# Leer una serie de numeros enteror mayores o igual a cero
# contar la cantidad de numeros leidos

# la serie termina cuando se lee un número negativo

# var
#   n  : numerico
#   cnt: numerico
# inicio
#   leer(n)
#   cnt = 0
#   mientras n >= 0 entonces
#      cnt = cnt + 1
#      leer(n)
#   fin-mientras
#  
#   imprimir("La cantidad de leidos fue", cnt)
# fin

n= int(input())

cnt= 0

while n >= 0:
    cnt +=1
    n= int(input())

print("La cantidad de leidos fue:", cnt)