#Imprimir los primeros N numeros enteros empezando en uno con sus cuadrados
#de la forma
#1^2 = 1
#2^2 = 2
#.
#.
#n^2 = ..
# Se lee N al principio

# var
#   N : numerico
#   k : numerico
# inicio
#   leer(N)
#   k = 1
#   mientras k <= n hacer
#      imprimir(k,"^2 =", k^2)
#      k = k + 1
#   fin-mientras
# fin

n = int(input())

k = 1

while k <= n:
    print(f'{k}^2 = {k**2}')
    k += 1


