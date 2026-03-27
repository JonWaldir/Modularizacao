# declaração de variáveis
n1 = 0
n2 = 0

# inicio
def verificamaior():
    global n1,n2
    if n1 == n2:
        print('Os números sao iguais')
    elif n1 > n2:
        print(' o maior numero é : ', n1)

    else:
        print('O maior numero é ', n2)
    
def main():
    global n1,n2
    n1 =  int(input('Digite um numero: '))
    n2 = int(input('digite outro numero: '))
    verificamaior()

if __name__ == "__main__":

    main()

# fim