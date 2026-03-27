import math
#Declaração de variaveis 

a = 0 
b = 0
c = 0 

#Inicio.
def bashkara():
    global a,b,c
    delta = (b**2) - (4*a*c)

    if delta < 0 :
        print('Nâo possui raizes reais')
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print('A raiz de x1 é ' , x1)
        print('A raiz de x2 é: ',x2)    
        
def main():
    global a,b,c
    a = float(input('Digite o valor de a: '))
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de C '))
    bashkara()

if __name__ =="__main__":
    main()
#Fim