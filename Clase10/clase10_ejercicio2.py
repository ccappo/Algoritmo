# Leer una serie de numeros enteros mayores a cero y 
# determina la cantidad de números primos 
# La serie termina cuando se lee un numero negativo o cero.
#
# sub es_primo(n : numerico) retorna numerico
# var
#   f : numerico
#   esp : logico
# inicio
#   esp = True
#   desde f=2 hasta entero(n/2)+1 hacer
#      si ( n == 1 ) entonces
#          retorna False // caso especial, el 1 no es primo
#      fin-si 
#      si ( n % f == 0 ) entonces
#          esp = False
#          salir  // rompe el ciclo abruptamente 
#      fin-si
#   fin-desde
#   retorna esp
# fin

# // programa principal
# var
#   n, cnt_primos : numerico
# inicio
#   leer(n)
#   cnt_primos = 0
#   mientras n > 0 hacer
#      si ( es_primo(n)) entonces
#         cnt_primos = cnt_primos + 1
#      fin-si
#      leer(n)
#   fin-mientras
#   imprimir('La cantidad de primos es ', cnt_primos)
# fin 

def es_primo(n) -> bool : 
     if n == 1: # caso especial, el uno no es primo
          return False
     for f in range(2,n//2 + 1):
          if n % f == 0:
               return False
     return True 

n = int(input())
cnt_primos = 0

while n > 0 :
     if es_primo(n):
          cnt_primos += 1
     n = int(input())

print(f'La cantidad de primos es {cnt_primos}')