# Dado los puntos en un archivo, imprimir
# todos los puntos que tienen la menor distancia entre ellos

# Ejercicio planteado en la diapositiva

import math
from dataclasses import dataclass
import os

@dataclass
class Punto:
    x : float
    y : float

def distanciaEuclidiana ( pt1, pt2 ):
    if isinstance(pt1,Punto) and isinstance(pt2,Punto):
        return math.sqrt((pt1.x - pt2.x)**2 +  (pt1.y - pt2.y)**2)
    else:
        raise Exception('Se espera tipo Punto')

def procesarRegistro(linea):
     #print(linea,end='')
     x,y = linea.strip().split(' ')
     puntos.append(Punto(float(x),float(y)))

def menorDistancia():
    if len(puntos) >= 2:
        min_dist = distanciaEuclidiana(puntos[0],puntos[1])

        for i in range(len(puntos)):
            for j in range(i+1,len(puntos)):
                d = distanciaEuclidiana(puntos[i],puntos[j])
                #print(f'Distancia entre {puntos[i]} y {puntos[j]} = {d}')
                if d < min_dist:
                    min_dist = d
        print(f'Menor distancia = {min_dist}')
        for i in range(len(puntos)):
            for j in range(i+1,len(puntos)):
                d = distanciaEuclidiana(puntos[i],puntos[j])
                if d == min_dist:
                   print(f'Distancia entre {puntos[i]} y {puntos[j]} = {d}')    
    else:
        raise Exception('Se necesitan al menos dos puntos')

puntos = [] 

nombre_archivo = 'puntos.txt'

if os.path.exists(nombre_archivo):

   archivo = open(nombre_archivo)

   for linea in archivo:
       procesarRegistro(linea)

   menorDistancia()

   archivo.close()
else:
    print(f'No existe el archivo {nombre_archivo}')
   

