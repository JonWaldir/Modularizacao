
#incio
def SaldoFinal(sel,saldo):

   if sel == 1 :
      saldo = saldo*1.03
      print('Esse sera seu valor final optando pela poupança: ', saldo)
   else:
      saldo = saldo * 1.05
      print('Esse sera seu valor final optando pela redna fixa :',saldo)
      
def main():
   while True:
      escolha =  int(input('Digite 1 se quiser para poupança ou 2 para renda fixa:'))
      if escolha == 1 or escolha == 2:
         break
      else:
         print('Digite 1 ou 2!')
   valorN = float(input('Digite o valor que quer depositar (r$):'))
   SaldoFinal(escolha,valorN)

if __name__=="__main__":
   main()
#fim