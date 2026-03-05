# Algoritmo - Sección MJ - 2026
# -----------------------------
# Algoritmo que lee tres variables enteras a, b y c
# e imprime a**b**c

# Pseudocódigo
# var
#   a,b,c,r  : numerico
# inicio
#   leer(a,b,c)
#   r = a^b^c
#   imprimir("El resultado es ", r)
# fin

a= int(input("El valor de a:"))
b= int(input("El valor de b:"))
c= int(input("El valor de c:"))

r = a**b**c

print(f'El resultado de {a}**{b}**{c}={r}')
    

