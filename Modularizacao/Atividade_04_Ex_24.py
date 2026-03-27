#Declaração de variaveis
n1 = 0
#inicio
def main():
    global n1
    n1 = int(input('Digite um numero:'))
    verifica()

def verifica():
    global n1
    if n1%2==0 and n1%3==0:
        print('E possivel dividir por 2 e 3')
    else:
        print('Não e possivel dividir por 2 e 3 ao mesmo tempo')
if __name__ == "__main__":
    main()
#fim