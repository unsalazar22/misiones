"""
Costo salario por horas
Una empresa paga a sus empleados una tarifa fija de $10.000 por hora, más un
recargo del 100% por cada hora adicional.
Crea una función que represente el pago total del empleado según el total de
horas trabajadas.

"""

'''
#7 ejercicio  7		
		
  """ANALISIS	""""	
ENTRADAS
	HORAS
PROCESO
       TARIFA = 10.000
       PAGO = HORAS * TARIFA
SALIDA  
       PAGO

'''

#1 Funciones
def calcularPago (horas):
        return horas * TARIFA

TARIFA = 10000
horas = int(input("Horas "))

pago = calcularPago(horas) 

print(pago)

