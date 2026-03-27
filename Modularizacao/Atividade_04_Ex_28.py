#Declaração de variaveis
VendaM = 0
Patual = 0
Novo_Preco = 0

#inicio
def VerificaDesconto(VendaM,Patual):
    if VendaM < 500 and Patual < 30 :
        Novo_Preco = Patual * 1.10
    elif (500<= VendaM <1000) and (30<= Patual <80):
        Novo_Preco = Patual * 1.15
    elif VendaM >=1000 and Patual>=80:
        Novo_Preco = Patual * 0.95
    else:
        Novo_Preco = Patual
    print('O novo preço é',Novo_Preco)
    
def main():
    Venda_Mensal = int(input('Digite a venda mensal do mes:'))
    Preco_Atual = int(input('Digite o preço atual: '))
    VerificaDesconto(Venda_Mensal,Preco_Atual)

if __name__=="__main__":
    main()
#fim