# 18) Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade
# dela e depois mostre se ela pode ou não votar.

def votar(idade):
    if idade >= 16:
        print('Já pode votar, mas é opcional')
    elif idade >= 18 and  idade <= 70:
        print('Pode votar, mas é obrigatorio')
    elif idade < 16:
        print('Não pode votar')
    else:
        print('Votar não é mais obrigatorio')

def main():
    ano = int(input('Digite o  ano de nascimento: '))
    idade = 2024 - ano
    votar(idade)


if  __name__ == "__main__":
    main()
