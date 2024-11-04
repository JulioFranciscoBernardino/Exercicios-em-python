# 17) Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse
# 80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba
# o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.

def multado(velocidade):
    if  velocidade > 80:
        multa = (velocidade - 80) * 5
        print(f'O veiculo foi multado em R${multa:.2f} por ultrapassar o limite de velocidade')
    elif velocidade < 40:
        print('O veiculo está a baixo da velocidade minima da via')
    else:
        print('O veiculo está dentro do limite de velocidade')


def main():
    velocidade  = int(input("Qual a velocidade do carro? "))
    multado(velocidade)


if  __name__ == "__main__":
    main()
