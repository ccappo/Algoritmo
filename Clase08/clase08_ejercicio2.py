# Leer una cadena S e imprimirla toda en mayúsculas.  
# Utilizar la propiedad de posicionamiento en la tabla ASCII de los 
# caracteres.(chr() y ord()).

#var
#  s, sm : cadena
#  k     : numérico
#inicio
#  imprimir(“Cadena:”);leer(s)
#  sm = "" 
#
#  desde k=1 hasta strlen(s) hacer 
#    si s[k] >= "a" and s[k] <= "z" entonces
#     sm = sm + ascii(ord(s[k])-ord("a")+ord("A"))
#    sino
#     sm = sm + s[k]
#    fin-si
#  fin-desde
#  imprimir(sm)
#fin


s  = input("Cadena:")
sm = "" 

for k in range(len(s)):
  if s[k] >= "a" and s[k] <= "z" :
     sm += chr(ord(s[k])-ord("a")+ord("A"))
  else:
     sm += s[k]

print(sm)
