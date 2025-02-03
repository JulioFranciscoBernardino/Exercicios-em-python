# 27) Crie um programa que leia duas notas de um aluno e calcule a sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média até 4.9: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

def main():
    
    loop = [1, 2]
    soma = 0
    for loop in loop:
        nota = float(input(f"Digite a nota {loop}º: "))
        soma = soma + nota

    media = soma / 2

    if media < 4.9:
        print("O alunos está reprovado")
    elif media <= 6.9:
        print("O alunos está de recuperação")
    else:
        print("O aluno está aprovado")

if __name__ == "__main__":
    main()