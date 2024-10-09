#6) Faça um programa que leia um número inteiro e mostre o seu antecessor e seu
#sucessor.
#Ex:
#Digite um número: 9
#O antecessor de 9 é 8
#O sucessor de 9 é 10

def main():
    num = int(input('Digite um número inteiro positivo: '))
    print(f'O sucessor de', num, 'é', num + 1)
    print(f'O antecessor de', num, 'é', num - 1)
    
main()