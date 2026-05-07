# Leer 100 números e imprimir cuantos son múltiplos de 2,3,5,7,11,13,19 y 23
#
# var 
#  A          : vector[100] numerico
#  contadores : vector[*] numerico
#  factores   : vector[*] numerico = {de 2,3,5,7,11,13,19 y 23}
#  k,f        : numerico

#  // leer los datos
#  desde k=1 hasta alen(A) hacer
#    leer(A[k])
#  fin-desde

#  // dimensionar contadores de acuerdo a la cantidad
#  // de factores que se debe verificar
#  dim(contadores, alen(factores))

#  // contamos, recorriendo cada elemento de A y verificando
#  // con cada factor en a lista de factores
#  desde k=1 hasta alen(A) hacer
#     desde f=1 hasta alen(factores) hacer
#        si ( A[k] % factores[f] == 0   ) entonces
#             contadores[f] = contadores[f] + 1
#        fin-si
#     fin-desde
#  fin-desde
#  
#  //imprimir los contadores de cada factor
#  desde f=1 hasta alen(factores) hacer
#     imprimir(factores[k],":", contadores[f], "\n")
#  fin-desde
# fin  
from array import array

# Funcion que recibe la lista de contadores
# y factores e imprime la salida
# Es para mostrar como se puede pasar
# listas como parámetros
def imprimirSalida(C,F):
  # imprimir contadores
  for f in range(len(C)):
     print(f'{F[f]}:{C[f]}')

N = 100
A = array('I', [0] * N)

factores = array('I')

factores = array('I',[2,3,5,7,11,13,19,23])
contadores = array("I", [0] * len(factores))

# leer los datos
for k in range(len(A)):
    A[k] = int(input(f'A[{k}]:'))

# Comentar la lectura y descomentar esto para realizar
# una verificación más rápida de los resultados
#A = array('I', [50,60,70,45,62,27,89,76,16])
          
for k in range(len(A)):
    for f in range(len(factores)):
        if A[k] % factores[f] == 0:
            contadores[f] += 1

# imprimir contadores
#for f in range(len(contadores)):
#    print(f'{factores[f]}:{contadores[f]}')
imprimirSalida(contadores,factores)


