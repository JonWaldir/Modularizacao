#Declaração de variaveis 
n1 = 0
n2  = 0

#inicio
def ordenamento():
    global n1,n2
    if n1 == n2 :
        print("Sao iguais")
    elif n1 > n2 :
        print('em ordem crescente:',n2,',',n1)
    else:
        print('Em crescente : ',n1,',',n2)
def main():
    global n1,n2
    n1 = int(input('Digite o n1 :'))
    n2 = int(input('Digite o n2: '))
    ordenamento()
if __name__ == "__main__":
    main()

#fim 