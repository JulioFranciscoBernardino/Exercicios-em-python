# 26) Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando
# na tela uma das mensagens abaixo:
# - O primeiro valor é o maior
# - O segundo valor é o maior
# - Não existe valor maior, os dois são iguais

def main():
    num1 = int(input("Digite o 1º numero: "))
    num2 = int(input("Digite o 2º numero: "))
    
    if num1 > num2:
        print(f"{num1} é maior que {num2}")
    elif num2 > num1:
        print(f"{num2} é maior que {num1}")
    else:
        print("São iguais")

if __name__ == "__main__":
    main()