# // Considere que lee los datos de precios
# // de productos de varios supermercados 
# // Se requiere realizar un resumen de los precios
# // de esta manera
# //
# // 
# // +-----------+-----------------+-----------------+----
# // |           |      S6         |      Stock      |
# // |           +-----------------+-----------------+----  
# // | Producto  | P.May  | P. Min | P.May  | P. Min |
# // +-----------+-----------------+-----------------+----
# // | papa      |  5000  |  6000  |        |        |
# // | tomate    | 15000  | 16500  |        |        |
# // | zanahoria |  8000  |  9000  |  7000  |  7800  |
# // | locote    |        |        |  7800  |  9200  |
# // +-----------+--------+--------+--------+--------+----

# // Se tienen productos fijos y supermercados fijos
# // Se lee de una lista que contiene: producto, supermercado, precio mayoritario y precio minoritario
# // Se deja de leer cuando alguno de los precios es menor o igual cero
# //
# // Ejemplo de datos a leer
# // -----------------------
# // papa,s6,5000,6000
# // tomate,s6,15000,16500
# // locote,s6,8000,9000
# // zanahoria,stock,7000,7800
# // locote,stock,7800,9200
# // tomate,arete,14500,18000
# // ...
# // fin,fin,0,0
# //

# sub buscarProducto( p : cadena ) retorna numerico
# var
#   k : numerico
# inicio
#   desde k=1 hasta alen(productos) hacer
#     si ( productos[k] == p ) entonces
#        retorna k
#     fin-si
#   fin-desde
#   retorna -1
# fin
#
# sub buscarSupermercado( s : cadena ) retorna numerico
# var
#   k : numerico
# inicio
#   desde k=1 hasta alen(supermercados) hacer
#     si ( supermercados[k] == s ) entonces
#        retorna k
#     fin-si
#   fin-desde
#   retorna -1
# fin
#
# var
#   precios       : matriz[4,7,2] numerico
#   productos     : vector[4] cadena = {'papa','cebolla','locote','tomate'}
#   supermercados : vector[7] cadena = {'s6','stock','arete'..}
#   p,s           : cadena
#   pmay,pmin,pos_producto,pos_super : numerico
# inicio
#   leer(p,s,pmay,pmin)
#  
#   // condicion de salida, uno de los precios es menor o igual a 0
#   mientras ( pmay > 0 and pmin > 0 ) hacer
#     
#     pos_producto = buscarProducto(p)
#     pos_super    = buscarSupermercado(p)
#
#     si ( pos_super <> -1 and pos_producto <> -1 ) entonces
#        precios[pos_producto,pos_super,1] = pmay
#        precios[pos_producto,pos_super,2] = pmin
#     fin-si // si es un dato que no esta registrado, se ignora
#	 
#     leer(p,s,pmay,pmin)
#	 
#   fin-mientras
#  
#   // imprimir la tabla
#  
#   imprimir(strdup("+-----------",alen(supermercados)+1,"+\n")
#   imprimir("|            +")
#   desde k=1 hasta alen(supermercados) hacer
#      imprimir("|", supermercados[k],"|") 
#   fin-desde
#   imprimir("\n")
#   imprimir("|            +")
#   imprimir(strdup("+-----------",alen(supermercados)+1,"+\n")
#  
#   imprimir("|  Producto  ")
#   desde k=1 hasta alen(supermercados) hacer
#     imprimir("|  P.May |   P.Min ") 
#   fin-desde
#  
#   imprimir("|\n")
#   imprimir("|            +")
#   imprimir(strdup("+-----------",alen(supermercados)+1,"\n")
#  
#  
#   desde k=1 hasta alen(precios) hacer
#      imprimir("|",productos[k],"|")
#      desde j=1 hasta alen(supermercados) hacer
#        imprimir("|",precios[k,j,1],"|",precios[k,j,2])
#      fin-desde
#      imprimir("|\n")
#   fin-desde
#  
#   imprimir(strdup("+-----------",alen(supermercados)+1,"\n")
#
# fin
   