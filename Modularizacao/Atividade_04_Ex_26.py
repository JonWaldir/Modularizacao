#declaração de variaveis
n1 = 0
n2 = 0
maior = 0
menor = 0
# declaração de variaveis

def main():
    global n1,n2
    n1 = int(input('Digite um numero 1:'))
    n2 = int(input('Digite o numero 2: '))
    verificaDivisao()
    
def verificaDivisao():
    global n1,n2,maior,menor
    if n1 == n2:
        print('Sao iguais digite diferente ')
    elif n1 > n2:
        maior = n1
        menor = n2
    else:
        maior =n2
        menor =n1
    if maior % menor==0:
        print('o MAIOR E DIVISEL PELO MENOR')
    else:
        print('nao e divisivel')
if __name__ == "__main__":
    main()