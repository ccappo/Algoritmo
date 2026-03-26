# Imprimir el promedio de los primeros N numeros pares

# var
#   N        : numerico
#  cnt, suma : numerico
# inicio
#   leer(N)
#   si N > 0 entonces
#      cnt = 0
#      suma = 0
#      mientras cnt < N hacer
#          cnt = cnt + 1
#          suma = suma + cnt*2 
#      imprimir("El promedio es", suma/cnt)
#   sino
#      imprimir("N debe ser mayor o igual que 1")
#   fin-mientras
# fin 

N = int(input("Cantidad de números pares :"))

if N > 0:
    cnt  = 0   # cantidad de números pares
    suma = 0   # para acumular la suma
    while cnt < N:       
        cnt      +=1         # cuento 
        suma     += cnt * 2  # genero el par y acumulo (1*2=2,2*2=4,3*2=6,..)
    print("El promedio es ", suma/cnt) # imprimo el promedio
else:
    print("N debe ser mayor o igual que 1")   
