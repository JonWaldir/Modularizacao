#Declaração de variaveis
n1 = 0
n2 = 0
n3 = 0
n4 = 0
#Inicio
def ordem():
    global n1,n2,n3,n4
    n4 = int(input('Digite o n4: '))
    if n4 > n3 :
        print(n1,n2,n3,n4)
    elif n4 > n2:
        print(n1,n2,n4,n3)
    elif n4 > n1:
        print(n1,n4,n2,n3)
    else:
        print(n4,n1,n2,n3)

def main():
    global n1,n2,n3,n4
    while True:
        n1 = int(input('Digite o n1: '))
        n2 = int(input('Digite o n2: '))
        n3 = int(input('Digite o n3: '))
        if n1 <= n2 <= n3 :
            break
        print('Digite em ordem crescente os 3 valores!')
    ordem()

if __name__ == "__main__":
    main()
#Fim
