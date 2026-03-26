#Declaração de variaveis
Venda_Mensal = 0
Preco_Atual = 0
Novo_Preco = 0

#inicio

Venda_Mensal = int(input('Digite a venda mensal do mes:'))
Preco_Atual = int(input('Digite o preço atual: '))
if Venda_Mensal < 500 and Preco_Atual < 30 :
    Novo_Preco = Preco_Atual * 1.10
elif (500<= Venda_Mensal <1000) and (30<= Preco_Atual <80):
    Novo_Preco = Preco_Atual * 1.15
elif Venda_Mensal >=1000 and Preco_Atual>=80:
    Novo_Preco = Preco_Atual * 0.95
else:
    Novo_Preco = Preco_Atual
print('O novo preço é',Novo_Preco)
#fim