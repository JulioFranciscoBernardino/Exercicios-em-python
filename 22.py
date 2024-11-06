# 22) Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua
# situação em relação ao alistamento militar.
# - Se estiver antes dos 18 anos, mostre em quantos anos faltam para o
# alistamento.
# - Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do
# alistamento.

from  datetime import datetime



def calculo(ano):
    ano_atual = datetime.now().year
    idade = ano_atual - ano
    if idade < 18:
        anos_faltando = 18 - idade
        print(f'Você ainda tem {idade} anos. Faltam {anos_faltando} anos para o alistamento.')
    elif idade >= 18:
        anos_passados = idade - 18
        print(f'f"Você tem {idade} anos. Já se passaram {anos_passados} anos desde o alistamento.')

        
def main():
    ano = int(input('Digite o ano de nacimento: '))
    calculo(ano)





if __name__ == '__main__':
    main()