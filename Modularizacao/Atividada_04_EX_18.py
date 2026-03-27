#Declaração de variaveis
n1 = 0
n2 = 0
diferenca = 0
#inicio
def calcularDiferenca():
    global n1,n2,diferenca
    if n1 == n2:
        print('Os numeros sao iguais')
    elif n1 > n2:
        diferenca = n1 - n2
        print('a diferenca do maior numero ',n1,'e do menor ',n2,'é ',diferenca)
    else:
        diferenca = n2 - n1
        print('a diferenca do maior numero',n1,' e do menor',n2, ' e ',diferenca)

def main():
    global n1,n2
    n1 = int(input('Digite um numero:'))
    n2 = int(input('Digite outro numero: '))
    calcularDiferenca()
if __name__ == "__main__":
    main()

#fim