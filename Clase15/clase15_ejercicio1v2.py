# Leer los datos de un archivo con el siguiente formato
# cedula, apellido, nombre, fechanac, sexo

# Ejemplo:
# 2929922,Perez,Juan,01021980,M

# Imprimir el resumen de cantidades de Mujeres y Hombres
# por mes de esta forma
# MES  FEM   MASC   
# ---  ----  ----
# ENE  ##    ##
# FEB  ##    ##
# ..   ..    ..
# DIC  ##    ##
# ---  ----  ----
# TOT  ###   ### 

# Adicional planteado en clase
# -----------------------------
# Luego imprimir este resumen por apellido
# Por cada Inicial del APellido indicar la frecuencia (solo si es > 0)
# Inicial Cnt
# ------  ---
#   A      #
#   B      #
#   C      #
#   ...
#   Z      #

import os
from dataclasses import dataclass

@dataclass
class CntMes:
   cntF : int
   cntM : int

@dataclass
class CntInicial:
   inicial: str
   cnt    : int

# Funciones

def imprimir_cabecera():
   print(f'MES\tFEM \tMASC')
   print(f'---\t----\t----')

def procesar_registro(linea):
   cedula, apellido, nombre, fechanac, sexo = linea.strip().split(',')
 
   m = int(fechanac.strip()[2:4]) # obtener el mes de la fecha
   
   if sexo == 'F':
      meses[m-1].cntF += 1
   elif sexo == 'M':
      meses[m-1].cntM += 1
   else:
      raise Exception('Sexo debe ser M o F')

   # procesar la inicial
   inicial = apellido[0].upper()

   # Busco en la lista de iniciales
   # si existe la inicial, aumento la cantidad
   # si no existe, creo un nuevo registro con la inicial
   #               y agrego a la lista de iniciales
   existe = False
   for k in range(len(iniciales)):
      if iniciales[k].inicial == inicial:
          iniciales[k].cnt += 1
          existe = True
          break
   if not existe:
      # agrego una nueva inicial
      iniciales.append(CntInicial(inicial,1))

def imprimir_resumen():
   nomb_mes = ['ENE', 'FEB', 'MAR', 'ABR', 'MAY', 'JUN', 'JUL', 'AGO','SEP', 'OCT', 'NOV', 'DIC']
   imprimir_cabecera()

   total_f = 0
   total_m = 0

   for mes in range(12):
       total_f += meses[mes].cntF
       total_m += meses[mes].cntM
       print(f'{nomb_mes[mes]:3}\t{meses[mes].cntF:<4}\t{meses[mes].cntM:<4}')
   
   print(f'---\t----\t----')
   print(f'TOT\t{total_f:<4}\t{total_m:<4}')

   # ordenar usando utilitario de Python

   # iniciales.sort(key=lambda i : i.inicial)

   # ordenar iniciales, antes de imprimir
   # utiliza un algoritmo sencillo de ordenaciona (por seleccion)
   for i in range(len(iniciales)):
      menor = i
      for j in range(i+1,len(iniciales)):
         if iniciales[j].inicial < iniciales[menor].inicial:
            menor = j
      tmp = iniciales[i] 
      iniciales[i] = iniciales[menor]
      iniciales[menor]= tmp

   # imprimo las iniciales y sus cantidades
   print('Inicial\tCnt')
   print('-------\t---')
   for inicial in iniciales:
      print(inicial.inicial, '\t', inicial.cnt)
# Programa Principal
nombre_archivo = 'datos.txt'

# creamos la estructura de informacion
# matriz de 12 filas y 2 columnas 
# fila = mes 
# columna 0: FEM  columna 1: MASC

iniciales = [] # acumular por iniciales del apellido

meses = [] # vector de Registro de tipo CntMes

for _ in range(12):
   meses.append(CntMes(0,0))

if os.path.exists(nombre_archivo):
   archivo = open(nombre_archivo, encoding='utf-8',mode='rt')

   for linea in archivo:
       procesar_registro(linea)

   imprimir_resumen()

   archivo.close()
else:
   print(f'Archivo {nombre_archivo} NO existe')

