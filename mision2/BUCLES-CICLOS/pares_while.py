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

contador = 1

while(contador <=n):
    par = contador *2
    print(par)
    contador = contador +1

    suma += par

print(f"sumatoria de pares: {suma}")




