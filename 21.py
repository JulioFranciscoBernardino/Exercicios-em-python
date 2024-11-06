# 21) Faça um algoritmo que leia um determinado ano e mostre se ele é ou não
# BISSEXTO.

def main():
    ano = int(input('Digite o que deseja descobir se é bissexto: '))
    if ano % 4 == 0:
        print(f'O ano {ano} é bissexto')
    else:
        print(f'O ano {ano} não é bissexto')

if __name__ == '__main__':
    main()
    