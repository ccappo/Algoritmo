# Dado el puntaje final determinar la nota de un alumno
# de acuerdo a la siguiente escala
# 0-59  : UNO
# 60-69 : DOS
# 70-79 : TRES
# 80-90 : CUATRO
# 91-100: CINCO

# Validar que el puntaje se encuentre entre 0 y 100


# var
#    puntaje : numerico
# inicio
#    leer(puntaje)
#    si puntaje >=0 and puntaje <= 100:
#        si puntaje <= 59 entonces
#           imprimir("UNO")
#        sino si puntaje <= 69 entonces
#           imprimir("DOS")
#        sino si puntaje <= 79 entonces
#           imprimir("TRES")
#        sino si puntaje <= 90 entonces
#           imprimir("CUATRO")
#        sino
#           imprimir("CINCO")
#        fin-si
#    sino
#        imprimir("El puntaje debe estar entre 0 y 100")
#    fin-si
# fin

puntaje= int(input("Puntaje: "))

if puntaje >= 0 and puntaje <= 100:

    if puntaje <= 59:
         print("UNO")
    elif puntaje <= 69:
         print("DOS")
    elif puntaje <= 79:
         print("TRES")
    elif puntaje <= 90:
         print("CUATRO")
    else:
         print("CINCO")
else:
    print("Puntaje debe ser >= 0 y <= 100")

