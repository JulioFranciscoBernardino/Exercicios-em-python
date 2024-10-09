# 13) Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o
# seu novo salário, com 15% de aumento.

def main():
    salario = pega_salario()
    calculo = aumento_salario(salario)
    imprime_aumento(calculo)    
    
def pega_salario():
    salario = float(input('Digite o salário do funcionário em R$'))
    return salario

def aumento_salario(salario):
    aumento = salario + (salario * 0.15)
    return aumento
    
def imprime_aumento(aumento):
    print(f'O aumento do salário em 15% é de {aumento}')

if __name__ == '__main__':
    main()