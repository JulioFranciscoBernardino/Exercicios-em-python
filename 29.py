# 29) Desenvolva um programa que leia o nome de um funcionário, seu salário,
# quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de
# acordo com a tabela a seguir:
# - Até 3 anos de empresa: aumento de 3%
# - entre 3 e 10 anos: aumento de 12.5%
# - 10 anos ou mais: aumento de 20%

def main():
    nome = input("Digite o nome do funcionario: ")
    salario = float(input("Digite o salário do funcionario: "))
    anos = int(input("Digite quanto anos o funcionario está na empresa: "))

    if anos < 3:
        salario = salario + (salario * 0.03)
        print(f"O funcionario {nome} recebera {salario} que são 3% de aumento")
    elif anos == 3 and anos <= 10:
        salario = salario + (salario * 0.125)
        print(f"O funcionario {nome} recebera {salario} que são 12.5% de aumento")
    else:
        salario = salario + (salario * 0.2)
        print(f"O funcionario {nome} recebera {salario} que são 20% de aumento")


if __name__ == "__main__":
    main()