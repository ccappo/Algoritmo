# Leer una cadena cad y un caracter c
# Retornar la posicion de la primera ocurrencia de c en cad
# En caso de que no exista c en cad, retornar -1
# 
# sub posicion_caracter( cad, c : cadena ) retorna numerico
# var
#   k : numerico
# inicio
#   desde k=1 hasta strlen(cad) hacer
#      si ( cad[k] == c) entonces
#          salir 
#      fin-si
#   fin-desde
#   si ( k <= strlen(cad)) entonces
#      retornar k
#   sino
#      retornar -1
#   fin-si
# fin

# var
#    s,c : cadena
#    p : numerico
# inicio
#    leer(s,c)
#    p = posicion_caracter(s,c) 
#    si ( p != -1 ) entonces
#       imprimir('Primera posición del caracter ', c, 'en',s, ' es ',p )
#    sino
#       imprimir('No se encuentra el caracter')
#    fin
# fin

def posicion_caracter ( cad, c ) -> int :
    for k in range(len(cad)):
        if cad[k] == c :
            break
    if k < len(cad) and cad[k] == c:
        return k
    else:
        return -1

s = input('Cadena:')
c   = input('Caracter a buscar')

p  = posicion_caracter(s,c)

if p != -1 :
    print(f'Primera posicion de {c} en {s} es {p}')
else:
    print('No existe el caracter')

