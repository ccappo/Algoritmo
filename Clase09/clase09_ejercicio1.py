# Dada una cadena leida por teclado, convertirla a maýusculas, sin usar ninguna
# función auxilar (upper).  
#
#

# var
#   s: cadena
#   sm: cadena
#   k : numerico
# inicio
#   leer(s)
#   sm =  ""
#   desde k = 1 hasta strlen(s) hacer 
#      si s[k] >= "a" and s[k] <= "z" entonces
#          sm = sm + ascii(ord(s[k])-ord("a")+ord("A"))
#      sino
#          sm = sm + s[k]
#      fin-si
#
#  fin-desde
# fin 
s  = input("Cadena:")
sm = "" 

for k in range(len(s)):
  if s[k] >= "a" and s[k] <= "z" :
     sm += chr(ord(s[k])-ord("a")+ord("A"))
  else:
     sm += s[k]

print(sm)
