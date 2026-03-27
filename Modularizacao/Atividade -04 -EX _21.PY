# #Declaração de variaveis 
# n1 = 0
# n2 = 0
# n3 = 0
# n4 = 0
# media = 0 

# #Inicio.
# n1 = float(input('Digite a nota 1:'))
# n2 = float(input('Digite a nota 2:'))
# n3 = float(input('Digite a nota 3:'))
# n4 = float(input('Digite a nota 4:'))

# media = (n1 + n2 + n3 + n4) /4
# if media < 3 :
#     print('Retido')
# elif media >= 3 and  media <6 :
#     print('Exame')
# else:
#     print('Aprovado')

# #Fim.
#Declaração de variaveis
soma = 0 
nota = 0
i = 0
#inicio
def calculanota():
    global soma
    media = soma /4
    print('Media = ', media)
    if media <3:
        print('RETIDO')
    elif 3<= media <6:
        print('EXAME')
    else:
        print('Aprovado')

def main():
    global i,nota,soma
    for i in range(1,5,1):

        while True:
            nota = float(input(f'Digite a nota {i} (0 a 10):'))
            if  0<= nota <= 10:
                break
            else:
                print('Erro nota invalida digite sua nota de 0 a 10!')
        soma += nota
    calculanota()

if __name__ == "__main__":
    main()

#fim