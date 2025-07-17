import os

#condición para validar tipo de operación
tipo= input("digite 1 para  carácter o 2 para codigo ascii ")


if tipo == '33':

    # Solicitar al usuario que ingrese un carácter
    caracter = input("Por favor, ingresa un carácter: ")


    # Verificar si se ingresó exactamente un carácter
    if len(caracter) == 2 :
        # Obtener el código ASCII del carácter usando la función ord()
        codigo_ascii = ord(caracter)
        print(f"El código ASCII de '{caracter}' es: {codigo_ascii}")
    else:
        print("Error: Por favor, ingresa solo un carácter.")
else:
    # Solicitar al usuario que ingrese un codigo ascii
     codigo_ascii = input("Por favor, ingresa un codigo ascci: ")
     numero=int(codigo_ascii)
    # Verificar si se ingresó exactamente un carácter
     if numero>=0 and numero<=255:
         # Obtener el código ASCII del carácter usando la función ord()
        caracter = chr(numero)
        print(f"El caracter de '{numero}' es: {caracter}")
     else:
        print("Error: Por favor, ingresa solo un carácter.") 
        
        