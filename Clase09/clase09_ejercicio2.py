# Dada una cadena, generar otra pero invertida e imprimirla.
# No usas slicing en caso de Python, cuya solucion simplemente es <cad>[::-1]

#  var
#    cad, cadinv : cadena
#  inicio
#    leer(cad)
#    desde k=strlen(s) hasta 1 paso -1 hacer
#        cadinv = cadinv + s[k]
#    fin-desde
#    imprimir(cadinv)
#  fin


cad = input('Ingrese una cadena')
cadinv = ""

# Misma solucion pero con range
#
# for k in range(len(cad)-1,-1,-1):
#    cadinv += cad[k]

k=len(cad)-1

while k > 0:
    cadinv += cad[k]
    k = k - 1


print(cadinv)
