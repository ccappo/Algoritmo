# Leer 100 numeros e imprimir la cantidad
# de elementos mayores, menores e iguales al promedio
#
# // Subrutina que recibe un arreglo numerico y retorna
# // el promedio (media) del valore de sus elementos 
# sub promedioArreglo(A : vector[*] numerico) retorna numerico
# var
#    k, suma : numerico
# inicio
#    suma = 0
#    desde k=1 hasta alen(A) hacer 
#       suma = suma + A[k]
#    fin-desde
#    retorna suma/alen(A)
# fin
#
# var
#   A : vector[100] numerico
#   cnt_mayor, cnt_menor, cnt_igual, prom : numerico
# inicio
#   // leer los valores
#   desde k=1 hasta alen(A) hacer
#      leer(A[k])
#   fin-desde
# 
#   prom = promedioVector(A)
# 
#   desde k=1 hasta alen(A) hacer
#      si ( A[k] == prom ) entonces
#         cnt_igual = cnt_igual + 1
#      sino si ( A[k] > prom )
#         cnt_mayor = cnt_mayor + 1
#      sino
#         cnt_menor = cnt_menor + 1
#      fin-si
#   fin-desde 
# 
#   imprimir("Cnt. Mayores a", prom, ":", cnt_mayor)
#   imprimir("Cnt. Menores a", prom, ":",cnt_menor)
#   imprimir("Cnt. Iguales a", prom, ":",cnt_igual)
# fin

# Desarrollo de Python usando listas

def promedioVector(A: list) -> float :
    ''' 
       Calcula el promedio de una lista de números recibido como parámetro

       :param A : lista de numeros enteros
       :return  : el promedio de los elementos 
    '''
    suma = 0
    for e in A:
        suma += e
    return suma/len(A)

A: list[int] = [0] * 10  # Una lista de 100 numeros

# lectura de los datos
for k in range(len(A)):
    A[k] = int(input(f'A[{k}]:'))

# calcular el promedio

cnt_mayor = 0
cnt_menor = 0
cnt_igual = 0

prom: float = promedioVector(A)

for e in A :
    if e == prom :
        cnt_igual += 1
    elif e > prom:
        cnt_mayor += 1
    else:
        cnt_menor += 1

print(f'Cantidad de mayores a {prom}: {cnt_mayor}')
print(f'Cantidad de menores a {prom}: {cnt_menor}')
print(f'Cantidad de iguales a {prom}: {cnt_igual}')