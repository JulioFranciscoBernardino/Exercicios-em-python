#5) Faça um programa que leia as duas notas de um aluno em uma matéria e mostre
#na tela a sua média na disciplina.
#Ex:
#Nota 1: 4.5
#Nota 2: 8.5
#A média entre 4.5 e 8.5 é igual a 6.5

def main():
    num1 = float(input('Digite o valor da 1º nota: '))
    num2 = float(input('Digite o valor da 2º nota: '))
    soma = (num1 + num2) / 2
    print(f'A media deste aluno foi de {soma:.1f}')
    
main()