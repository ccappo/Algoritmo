# Algoritmo - Sección MJ - 2026
# -----------------------------
# Algoritmo que dado el radio de una esfera
# imprime su volumen

# En Pseudocódigo
# var 
#   r, v : numerico
# const
#   PI = 3.14
# inicio
#   leer(r)
#   v = 4/3 * PI * r^3
#   imprimir("El volumen es ", v)
# fin 
import math

r = float(input('El radio es: '))

v = 4/3 * math.pi * r**3

print(f'El volumen es {v}')
