# TALLER ENTRADAS - PROCESOS - SALIDAS LENGUAJE PYTHON

'''
01) Pregunta 

Ingresar por teclado y por separado en dos variables, sus nombres y apellidos respectivamente, 
mostrar en orden contrario al que se ingresaron, es decir apellidos y nombres, Ejm; 

*********** ANALISIS **************
ENTRADA: JHON JAIRO 
         OROZCO DAVILA
SALIDA => OROZCO DAVILA JHON JAIRO

'''

# 01 INICIALIZAR VARIABLES
nombre = " "       #  Variable TEXTO  SE USA "", Variable #  se usa 0
apellidos = ""

# 02 ENTRADAS
nombre = input("Ingresa tu Nombre: ")
apellidos = input("Ingresa tu Apellidos: ")

# 03 PROCESOS
salida = (f"{apellidos} {nombre}")

# 04 SALIDA

input(salida)


