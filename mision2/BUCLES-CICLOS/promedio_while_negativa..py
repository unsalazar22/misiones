'''
CON BUCLES


'''

numero = 0
suma = 0
contador = 0


while numero >= 0:
    numero = int(input("INGRESE NUMERO (NEGATIVO PARA SALIR): "))

    if numero >- 0:
        suma = suma + numero
        contador += 1


# salida tiempo total

promedio = suma / contador 
    
print(promedio)





