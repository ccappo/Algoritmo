# Leer un numero N (entero) y
# determinar con un mensaje si es par o impar

# var
#   N : numerico
# inicio
#   leer(N)
#
#   si N % 2 == 0 entonces
#      imprimir("Es par")
#   sino
#      imprimir("Es impar")
#   fin-si
# fin

N = int(input())

if N % 2 == 0:
   print('Es par')
else:
   print('Es impar')
