#Declaração de variaveis
temp_minutos = 0
distancia_total = 0
extensao = 0
volta = 0
vms = 0
kmh = 0
#inicio

temp_minutos = int(input('Digite o tempo do percurso em minutos:'))
extensao = int(input('Digite a extensao em metros:'))
volta = int(input('Digite o numero de voltas:'))

distancia_total = (extensao* volta)
vms = extensao / (temp_minutos*60)
kmh = vms * 3.6
print('A velocidade em km/h é',kmh)