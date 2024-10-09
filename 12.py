# 12) Crie um programa que leia o preço de um produto, calcule e mostre o seu
# PREÇO PROMOCIONAL, com 5% de desconto.

def main ():
    valor = pega_dado()
    calculo = calculo_desconto(valor)
    imprime_valor_com_desconto(calculo)

def pega_dado():
    valor = float(input('Digite o valor do produto em REAIS para aplicar 5% de desconto: R$'))
    return valor

def calculo_desconto(valor):
    deconto = valor - (valor * 0.05)
    return deconto

def imprime_valor_com_desconto(calculo):
    print(f'O valor do produto com desconto de 5% é: {calculo}')


if __name__ == '__main__':
    main()