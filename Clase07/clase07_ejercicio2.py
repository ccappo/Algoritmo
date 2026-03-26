# Leer un numero positivo (>0) y calcular su raiz cuadrada

# Si es negativo volver a leer

import math

n = float(input("Ingrese un nro > 0: "))

while n <= 0 :
   n = float(input("Favor Ingrese un nro > 0: "))

print(f"La raiz es {math.sqrt(n)}")
