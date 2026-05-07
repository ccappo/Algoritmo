##//Dada 100 notas de estudiantes como maximo, encontrar
##//la desviacion estandar
##
##var
##   A :  vector[100] numerico
##   k,suma,promedio,ds: numerico
##inicio   
##
##   // leer los valores
##   
##   desde i=1 hasta alen(A) hacer 
##        leer(A[i])
##   fin-desde
##   
##   // calcular el promedio
##   suma = 0
##   desde i=1 hasta alen(A) hacer 
##        suma = suma + A[i]
##   fin-desde
##   
##   promedio = suma / alen(A)
##   
##   // calcular la varianza y desv estand.
##   suma = 0
##   desde i=1 hasta alen(A) hacer 
##        suma = suma + (A[i] - promedio)^2
##   fin-desde
##   
##   ds = sqrt(suma / alen(A))
##   
##   imprimir("La desv. estandar es ",ds)
##fin

# Calcular la desviacion estandard

# A es numerico(entero) y de 10 elementos
import math

from array import array

N = 100 # nro de notas 

A=array('I') # creamos un arreglo vacio
for i in range(N):
    A.append(int(input(f'A[{i}]='))) # vamos agregando

# opcion usando listas
#A = [0]*N   # creamos un arreglo con N posiciones en 0
#for i in range(len(A)):
#   A[i] = int(input(f'A[{i}]=')) # colocamos el valor leido en la posicion i

# valores estáticos usando lista
#A = [75,60,50,20,30,40,50,17,26,13]

# valores estáticos usando array
#A = array("I",[75,60,50,20,30,40,50,17,26,13])

# promedio

suma= 0
for i in range(len(A)):
    suma += A[i]

promedio = suma/len(A)

# calcula la varianza y ds

suma= 0
for i in range(len(A)):
    suma += (A[i]-promedio)**2

ds = math.sqrt(suma/len(A))

print(f'La DS es {ds} y el promedio es {promedio}')




