'''
IMPRIMIR LOS PRIMERO N NEMERO PARES

ANALISIS
   ENTRADA: n
   PROCESO: par = contador * 2
   SALIDA: par


'''
par = 0
n = 0

n = int(input("CUANTOS PARES: "))

# BUCLE  VARIABLE CONTROL INICIA EN UN VALOR
#  VARIABLE CONTROL es comparada con el valor final
#  VARIABLE CONTROL debe ser incrementada

for contador in range (1 , n+1, 1):
    par = contador *2
    print(par)

    suma += par

    # salida en tiempo total

    print(f"SUMATORIA DE PARES: {suma}")

    





