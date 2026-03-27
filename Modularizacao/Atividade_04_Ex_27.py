
#inicio


def calculaKM(tempo,ext,vol):
    distancia_total = (ext* vol)
    vms = distancia_total / (tempo*60)
    kmh = vms * 3.6
    print(f"A velocidade em km/h é {kmh:.2f}")
    

def main():
    
    temp_minutos = int(input('Digite o tempo do percurso em minutos:'))
    extensao = int(input('Digite a extensao em metros:'))
    volta = int(input('Digite o numero de voltas:'))
    calculaKM(temp_minutos,extensao,volta)
if __name__ == "__main__":
    main()
# fim