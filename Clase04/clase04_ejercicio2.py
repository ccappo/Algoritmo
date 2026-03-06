# Dados los lados de un triangulo calcular
# la superficie utilizando la fórmula de semiperímetro

# Pseudocodigo

# var
#   a,b,c,sup,s : numerico
# inicio
#   leer(a,b,c)
#   s   = (a+b+c)/2
#   sup = (s*(s-a)*(s-b)*(s-c))^0.5
#   imprimir("La superficie es: ", sup)
# fin

import math

a=float(input("Lado a:"))
b=float(input("Lado b:"))
c=float(input("Lado c:"))

s = (a+b+c)/2
sup = math.sqrt(s*(s-a)*(s-b)*(s-c))

print(f'La superficie es: {sup}')






