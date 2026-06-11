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

import os
from dataclasses import dataclass

@dataclass
class CntMes:
   cntF : int
   cntM : int
   
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
 
# Programa Principal
nombre_archivo = 'datos.txt'

# creamos la estructura de informacion
# matriz de 12 filas y 2 columnas 
# fila = mes 
# columna 0: FEM  columna 1: MASC

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

