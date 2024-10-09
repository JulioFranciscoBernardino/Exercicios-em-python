
#3) Crie um programa que leia o nome e o salário de um funcionário, mostrando no
#final uma mensagem.
#Ex:
#Nome do Funcionário: Maria do Carmo
#Salário: 1850,45
#O funcionário Maria do Carmo tem um salário de R$1850,45 em Junho.

def main():
    nome = input('Digite o nome do funcionário: ')
    salario = float(input('Digite o salario do funcionário: '))
    print('O funcionário', nome, 'tem o salário de R$', salario,)
    
main()