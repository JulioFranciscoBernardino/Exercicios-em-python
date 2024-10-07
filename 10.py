def main():
    l, a = pega_dados()
    area, tinta = trata_dados(l, a)
    imprime_dados(area, tinta)


def pega_dados():
    largura = float(input('Digite a Largura da parede em METROS: '))
    Altura = float(input('Digite a Altura da parede em METROS: '))
    return largura, Altura


def trata_dados(largura, altura):
    area = largura * altura
    tinta = area / 2
    return area, tinta


def imprime_dados(area, tinta):
    print(f'A area da parede é de {area: .2f} m²')
    print(f'E a quantidade de tintas necessárias para o serviço é de{tinta: .3f} litros')
        

if __name__ == "__main__":
    main()