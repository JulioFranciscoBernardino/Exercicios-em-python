# 24) Faça um algoritmo que pergunte a distância que um passageiro deseja
# percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para
# viagens até 200Km e R$0.45 para viagens mais longas.

def main():
    distancia = float(input("Qual é a distância que você deseja percorrer em Km? "))
    if distancia <= 200:
        preco = distancia * 0.50
        print(f"R${preco}")
    else:
        preco = distancia * 0.45
        print(f"R${preco}")

if __name__ == "__main__":
    main()