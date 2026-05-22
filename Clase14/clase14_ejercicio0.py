# Ejercicio 2 de la diapositiva de arreglos n-dimensionales
# Encontrar el minimax de una matriz

# Falta el pseudocódigo
# var
#    M               : matriz[10,20] numerico
#    f,c,max,minimax : numerico
# inicio
#    // leer los datos
#    desde f=1 hasta alen(M) hacer
#       desde c=1 hasta alen(M[f]) hacer
#            leer(A[f,c])
#       fin-desde
#    fin-desde
#
#    desde c=1 hasta alen(M[1]) hacer
#       max = M[1,c]
#       desde f=2 hasta alen(M) hacer
#            si ( M[f,c] > max) entonces
#                max = M[f,c]
#            fin-si
#       fin-desde
#       si ( c == 1 ) entonces
#           minimax = max
#       sino si ( max < minimax )
#           minimax = max
#       fin-si
#   fin-desde
#
#   imprimir('El minimax es:', minimax)
#
# fin

nfila = 10
ncol  = 20

# inicializar la matriz de 10x20
M = []
for k in range(nfila):
    M.append([0]*ncol)

# leer la matriz
for f in range(len(M)):
    for c in range(len(M[f])):
        M[f][c] = int(input(f'M[{f},{c}]='))

# Esto se debe descomentar para realizar una prueba rápida
# M = [
#       [ 1,40,60,10,15],
#       [40,20,30,30,25],
#       [30,25,40,40,35],
#       [20,30,20,50,45],
#       [10,40,30,60,55],
#       [40,30,20,10,50],
#       [60,50,20,80,65]
# ]
minimax = 0
for c in range(len(M[0])):
    max = M[0][c]
    for f in range(1,len(M)):
        if M[f][c] > max:
            max = M[f][c]
    if c == 1:
        minimax = max
    elif max < minimax:
        minimax = max

print(f'Minimax = {minimax}')
