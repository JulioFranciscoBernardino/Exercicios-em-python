# 23) Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos
# para todos, mas especialmente para mulheres. Faça um programa que leia nome,
# sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo
# que:
# - Homens ganham 5% de desconto
# - Mulheres ganham 13% de desconto

def main():
    nome = input("Digite o nome do cliente: ")
    sexo = input("Digite o sexo do cliente (M/F): ")
    valor_compras = float(input("Digite o valor das compras: "))

    if sexo == "M" or sexo == "m":
        desconto = 0.05
        valor_com_desconto = valor_compras - (valor_compras * desconto)
        print(f"O desconto aplicado foi de 5%: {valor_com_desconto}") 
    else:
        desconto = 0.13
        valor_com_desconto = valor_compras - (valor_compras * desconto)
        print(f"O desconto aplicado foi de 13%: {valor_com_desconto}") 

if __name__ == "__main__":
    main()