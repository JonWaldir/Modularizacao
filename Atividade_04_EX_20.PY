import math
#Declaração de variaveis 

a = 0 
b = 0
c = 0 
delta = 0
x1 = 0
x2 = 0

#Inicio.

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de C '))
delta = (b**2) - (4*a*c)

if delta < 0 :
    print('Nâo possui raizes reais')
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print('A raiz de x1 é ' , x1)
    print('A raiz de x2 é: ',x2)
#Fim