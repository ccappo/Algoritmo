# Ejercicio parecido al Primer Parcial con Subrutina
#
# Leer una serie de números enteros entre 1000 y 10000
# Imprimir la cantidad de múltiplos de 19 que existen.
# Para determinar si es múltiplo de 19, utilizar
# el método del primero parcial pero convertido a
# subrutina
# La serie termina cuando se lee 999.
# ------------------------------------------------
#sub es_multiplo_19 ( n : numerico) retorna numerico
#var
#   d : numerico
#inicio
#   mientras n > 19 entonces
#     d = n % 10
#     n = entero(n/10)
#     n = n + d*2
#   fin-mientras
#   si (n == 19) entonces
#     retorna True
#   sino
#     retorna False
#   fin-si
#fin


# //Programa principal
# var
#   n : numerico
#   multiplos : numerico
# inicio
#   leer(n)
#   mientras n != 999 entonces
#      si ( n >= 1000 and n <= 10000) entonces 
#         si ( es_multiplo_19(n)) entonces
#            multiplos = multiplos + 1
#         fin-si
#      fin-si
#      leer(n)
#   fin-mientras
#   imprimir('La cantidad de multiplos de 19 es ', multiplos)
# fin