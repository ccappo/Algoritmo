# Imprimir los primeros 100 numeros enteros empezando del 1.
# de la forma: 1 2 3 4 5 .. 100
# Se lee N al principio

# var
#   N : numerico
# inicio
#   N = 1
#   mientras N <= 100 hacer
#      imprimir(N, " ")
#      N = N + 1
#   fin-mientras
# fin

N = 1

while N <= 100:
    print(f'{N}', end=" ")
    N += 1


