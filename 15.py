#15) Crie um programa que leia o número de dias trabalhados em um mês e mostre o
#salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25
#por hora trabalhada.

def main ():
    dias = tempo_trabalhado()
    salario = calculo(dias)
    imprime_salario(salario)

def tempo_trabalhado():
    dias = int(input("Quantos dias você trabalhou? "))
    return dias

def calculo(dias):
    salario = dias * 25.00
    return salario

def imprime_salario(salario):
    print(f'O salario a ser repassado ao funcionário é de R${salario}')
    
if __name__ == '__main__':
    main()