#Declaração de variaveis
escolha = 0
valorN = 0
#incio

while True:
    escolha =  int(input('Digite 1 se quiser para poupança ou 2 para renda fixa:'))
    if escolha == 1 or escolha == 2:
     break
    else:
       print('Digite 1 ou 2!')
valorN = float(input('Digite o valor que quer depositar (r$):'))
if escolha == 1 :
   valorN = valorN*1.03
   print('Esse sera seu valor final optando pela poupança: ', valorN)
else:
   valorN = valorN * 1.05
   print('Esse sera seu valor final optando pela redna fixa :',valorN)


#fim