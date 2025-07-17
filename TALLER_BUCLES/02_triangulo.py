contador=0
equilatero=0
isoceles=0
escaleno=0
def indicarTriangulo(lado1,lado2,lado3):
    if lado1==lado2 and lado1==lado3:
        return 1


def pedeirLados():
    lado1 = float(input("LADO 1: "))
    lado2 = float(input("LADO 2: "))
    lado3 = float(input("LADO 3: "))
    indicarTriangulo(lado1,lado2,lado3)
    

n=int(input("Números de triángulos="))
while(contador<n):
    contador+=1
    #print(contador)
    pedeirLados()
print('EQUILATERO ',equilatero )
print('ESCALENO ',escaleno )
print(' ISOSCELES ',isoceles)
