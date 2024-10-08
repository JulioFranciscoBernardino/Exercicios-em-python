def main():
    dias, km = pega_info()
    valor = calculo(dias, km)
    imprime_conta(valor)
    
def pega_info():
    dias = int(input("Quantos dias o veiculo foi alugado?: "))
    km = float(input("Quantos KM o veiculo alugado percorreu?: "))
    return dias, km

def calculo(dias, km):
    val1 = dias * 90
    val = km * 0.20
    valor = val1 + val
    return valor

def imprime_conta(valor):
    print(f'O valor a pagar do aluguel é de R${valor}')
        
if __name__ == '__main__':
    main()