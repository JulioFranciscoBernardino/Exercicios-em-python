# 19) Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua
# média e mostre na tela. No final, analise a média e mostre se o aluno teve ou
# não um bom aproveitamento (se ficou acima da média 7.0).
def pega_nota():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    return nota1, nota2

def calculo(n1, n2):
    media = (n1 + n2) / 2
    if media  >= 7:
        print('Este aluno ficou acima da media')
    elif media >= 6:
        print('Este aluno ficou abaixo da media, mas está aprovado')
    elif media <= 4:
        print('Este aluno ficou abaixo da media e está reprovado')

def main():
    nota1, nota2 = pega_nota()
    calculo(nota1, nota2)


if  __name__ == "__main__":
    main()

