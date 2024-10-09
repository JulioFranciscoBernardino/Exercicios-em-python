# 8) Desenvolva um programa que leia uma distância em metros e mostre os valores
# relativos em outras medidas.
# Ex:
# Digite uma distância em metros: 185.72
# A distância de 85.7m corresponde a:
# 0.18572Km
# 1.8572Hm
# 18.572Dam
# 1857.2dm
# 18572.0cm
# 185720.0mm


def main():
    distancia = pega_distancia()
    distancia_tratada(distancia)
    
def pega_distancia():
    distancia = float(input('Digite a distância em metros: '))
    return distancia

def distancia_tratada(distancia_mt):
    print(f'A distância em CM é:', distancia_mt * 100)
    print(f'A distancia em MM é:', distancia_mt * 1000)
    print(f'A distância em KM é: ', distancia_mt / 1000)
    print(f'A distância em DM é: ', distancia_mt * 10)
    
if __name__ == '__main__':
    main()
    
    