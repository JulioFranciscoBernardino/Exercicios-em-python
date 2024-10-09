# 11) Desenvolva uma lógica que leia os valores de A, B e C de uma equação do
# segundo grau e mostre o valor de Delta.

def main():
    A, B, C = valores_adq()
    delta =  calculo_delta(A, B, C)
    imprime_delta(delta)
    
    
def valores_adq():
    A = int(input('Digite o valor de A'))
    B = int(input('Digite o valor de B'))
    C = int(input('Digite o valor de C'))
    return A, B, C


def calculo_delta(A, B, C):
    delta = pow(B, 2) - 4 * A * C
    return delta
    
    
def imprime_delta(delta):
    print(f'O delta da equação do 2º é {delta}')
    
if __name__ == "__main__":
    main()