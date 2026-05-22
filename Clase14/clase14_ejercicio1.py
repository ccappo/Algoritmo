# Ejercicio 2 del ejercitario de la Parte B de la Unidad VI
# Construir una subrutina que retorne la minima distancia entre tres puntos 
# en el plano. Debe recibir como parámetros
# Se debe diseñar como registro.

# tipos
#   TPunto : registro {
#                       x, y : numerico
#                     }
#
# sub min ( x, y : numerico) retorna numerico
# inicio
#    si ( x < y ) entonces
#       retorna x
#    sino
#       retorna y
#    fin-si
# fin

# // Calcula la distancia euclidiana entre dos puntos
# sub distancia ( pt1, pt2 : TPunto) retorna numerico
# inicio
#    retorna sqrt((pt1.x - pt2.x)^2 + (pt1.y - pt2.y)^2 )
# fin

# sub mininadistancia( pt1, pt2, pt3 : TPunto) retorna numerico
# var
#   d1, d2, d3 : numerico
# inicio
#   d1 = distancia(pt1, pt2)
#   d2 = distancia(pt1, pt3)
#   d3 = distancia(pt2, pt3)
#
#   retorna min(min(d1,d2),d3)
#
# fin

# // programa principal
# var
#    pt1, pt2, pt3 : TPunto
# inicio
#    leer(pt1)
#    leer(pt2)
#    leer(pt3)
#    
#    imprimir('La mininima distancia es:', minimadistancia(pt1,pt2,pt3))
# fin

# ===============================================================
from dataclasses import dataclass
import math

@dataclass
class TPunto:
     x : int
     y : int


def distancia ( pt1, pt2) -> float :
     if isinstance(pt1, TPunto) and isinstance(pt2, TPunto):
          return math.sqrt((pt1.x - pt2.x)**2 + (pt1.y - pt2.y)**2)
     else:
          raise Exception('Tipos incorrectos') # genera un error si no son los tipos correctos 

def minimadistancia(pt1,pt2,pt3) -> float:
     if isinstance(pt1, TPunto) and isinstance(pt2, TPunto) and isinstance(pt3, TPunto):
          d1 = distancia(pt1,pt2)
          d2 = distancia(pt1,pt3)
          
