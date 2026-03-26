#Declaração de variaveis
Hfim = 0
Mfim = 0
inicioMim = 0
inicioHora = 0
diferenca = 0
HRduracao = 0
MinDuracao = 0
total_inicio = 0
total_fim = 0

#inicio

while True:
    inicioHora = int(input('Digite em que horas foi inciado o jogo: '))
    inicioMim = int(input('Digite os minutos tambem em foi inicado:'))
    if 0<=inicioHora <=23 and 0<=inicioMim<59:
        break
    else:
        print('Digite novamente!')
while True:
    Hfim = int(input('Digite em que horas foi finalizado o jogo: '))
    Mfim = int(input('Digite os minutos tambem em foi finalizado:'))
    if 0<= Hfim <=23 and 0<= Mfim <=59:
        break
    else:
        print('Digite novamente!')
total_inicio = (inicioHora * 60) + inicioMim
total_fim = (Hfim * 60 ) + Mfim

diferenca = total_fim - total_inicio
if diferenca <0 :
    diferenca = diferenca + 1440 #quantidades de minutos em um dia
    HRduracao =  diferenca // 60
    MinDuracao = diferenca % 60
else:
    HRduracao = diferenca // 60
    MinDuracao = diferenca %60
print('o total de horas foi ', HRduracao, ':',MinDuracao)




#Fim