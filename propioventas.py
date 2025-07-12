"""
CALCULAR LA VENTA TRIMESTRAL DE 1 UN PRODUCTO INGRESANDO LA CANTIDAD VENDIDA POR MES.

ANALISIS:
        ENTRADAS: precioProducto
                  cantiMes1
                  cantiMes2
                  cantiMes3
                  
        PROCESO:
                mes1 = cantiMes1 * precioProducto, 
                mes2 = cantiMes2 * precioProducto, 
                mes3 = cantiMes3 * precioProducto
                totalTrimestre = mes1 + mes2 + mes3
        SALIDA:
                mes1
                mes2
                mes3
                totalTrimestre

"""
import os
#1. reservar e inicializar variables
producto = 1000
cantiMes1 = 0
cantiMes2 = 0
cantiMes3 = 0
#2. Entradas por teclado con input
cantiMes1 = int(input("INGRESE CANTIDAD VENDIDA MES 1: "))
cantiMes2 = int(input("INGRESE CANTIDAD VENDIDA MES 2: "))
cantiMes3 = int(input("INGRESE CANTIDAD VENDIDA MES 3: "))
os.system("cls")
print("*** VENTAS TRIMESTRE ***")
print("-" * 50)

#3. Procesos

print(f"MES UNO: {cantiMes1} x {producto} = {cantiMes1*producto}")
print(f"MES DOS: {cantiMes2} x {producto} = {cantiMes2*producto}")
print(f"MES TRES: {cantiMes3} x {producto} = {cantiMes3*producto}")
print("-" * 50)

print(f"TOTAL TRIMESTRE: {cantiMes1 * producto} + {cantiMes2 * producto} + {cantiMes3 * producto} = {(cantiMes1 + cantiMes2 + cantiMes3) * producto}")
print("-" * 50)


