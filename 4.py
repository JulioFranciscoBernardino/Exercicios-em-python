#4) Desenvolva um algoritmo que leia dois números inteiros e mostre o somatório
#entre eles.
#Ex:
#Digite um valor: 8
#Digite outro valor: 5
#A soma entre 8 e 5 é igual a 13.

def main():
    num1 = int(input('Digite o 1º numero: '))
    num2 = int(input('Digite o 2º numero: '))
    soma = num1 + num2
    print('A soma dos numeros é: ', soma)

main()