# Algoritmo - Sección MJ - 2026
# -----------------------------
# Algoritmo que dado el radio de una esfera
# imprime su volumen

import math

r = float(input('El radio es: '))

v = 4/3 * math.pi * r**3

print(f'El volumen es {v}')
