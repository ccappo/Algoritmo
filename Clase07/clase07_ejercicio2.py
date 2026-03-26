# Leer un numero positivo (>0) y calcular su raiz cuadrada

# Si es negativo volver a leer

# var
#   n : numerico
# inicio
#   imprimir("Ingrese un nro > 0");leer(n)
#
#   mientras n <= 0 hacer
#       imprimir("Favor Ingrese un nro > 0")
#       leer(n)
#   fin-mientras
#
#   imprimir("La raiz cuadra es ", sqrt(n))
#
# fin

import math

n = float(input("Ingrese un nro > 0: "))

while n <= 0 :
   n = float(input("Favor Ingrese un nro > 0: "))

print(f"La raiz es {math.sqrt(n)}")
