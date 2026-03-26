# Leer una serie de numeros mayores o igual a cero
# Imprimir los dos máximos, el promedio y la cantidad
# de números leidos

# var
#   n : numerico
#   max1,max2 : numerico
#   cnt, suma : numerico
# inicio
#   max1 = -1
#   max2 = -1
#   suma = 0
#   cnt = 0
# 
#   leer(n)
#   
#   mientras n >=0 hacer
#       cnt  = cnt + 1
#       suma = suma + n	  
# 	  si n > max1 entonces
# 	     max2 = max1
# 		 max1 = n
# 	  sino si n > max2 entonces
# 	     max2 = n
# 	  fin-si
# 	  leer(n)
#   fin=mientras
#   imprimir("Max 1 =", max1, " Max 2 =", max2)
#   imprimir("Promedio = ", suma/cnt, " Cantidad = ", cnt)
# fin

max1 = -1
max2 = -1
cnt  = 0
suma = 0

n = int(input("n="))

while n >= 0:
    suma += n
    cnt += 1

    if n > max1:
        max2 = max1
        max1 = n
    elif n > max2:
        max2 = n
    
    n = int(input("n="))

print(f'El max1 = {max1}, el max2 = {max2}, el promedio {suma/cnt:.2f} y se leyeron {cnt} números')
    

 
