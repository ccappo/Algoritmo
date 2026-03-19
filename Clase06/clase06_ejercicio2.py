# Leer la edad y el nombre de una persona
# Determinar su franja etarea de acuerdo
# a esta escala
# De 0-13:  INFANTE
# De 14-17: ADOLESCENTE
# De 18-64: ADULTA
# De 65 en adelante: ADULTA DE LA TERCERA EDAD

# Imprimir el mensaje "La persona con nombre <nombre> es <franja>"

# var
#   edad  : numerico
#   nombre, franja : cadena
# inicio
#   imprimir("Nombre: "); leer(nombre)
#   imprimir("Edad :"); leer(Edad)
#
#   si edad >= 0 entonces
#      si edad <= 13 entonces
#         franja = "INFANTE"
#      sino si edad <= 17 entonces
#         franja = "ADOLESCENTE"
#      sino si edad <= 64 entonces
#         franja = "ADULTA"
#      sino 
#         franja = "ADULTA DE LA TERCERA EDAD"
#      fin-si
#      imprimir("La persona con nombre ", nombre, "es ", franja)
#   sino
#      imprimir("La edad debe ser mayor o igual a cero")
#   fin-si
# fin
edad = int(input("Edad : "))
nombre = input("Nombre : ")

if edad >= 0 :
    if edad <= 13:
        franja = "INFANTE"
    elif edad <= 17:
        franja = "ADOLESCENTE"
    elif edad <= 64:
        franja = "ADULTA"
    else:
        franja = "ADULTA TERCERA EDAD"
    print(f'La persona {nombre} es {franja}')
else:
    print('La edad debe ser mayor a cero')

    
