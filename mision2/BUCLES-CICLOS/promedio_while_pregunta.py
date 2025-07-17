'''
CON BUCLES


'''

numero = 0
suma = 0
contador = 0
respuesta = 0

respuesta = input("CONTINUAR (SI/NO): ") [0].lower()

while respuesta == 's' :
    numero = int(input("INGRESE NUMERO (POSITIVOO PARA SALIR): "))

    if numero >= 0:
        suma = suma + numero
        contador += 1
    respuesta = input("CONTINUAR (SI/NO): ") [0].lower()
# variable de control debe ser actualizada antes de volcer al bucle



# salida tiempo total

promedio = suma / contador 
    
print(promedio)





