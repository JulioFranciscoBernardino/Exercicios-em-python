# 25) [DESAFIO] Crie um programa que leia o tamanho de três segmentos de reta.
# Analise seus comprimentos e diga se é possível formar um triângulo com essas
# retas. Matematicamente, para três segmentos formarem um triângulo, o comprimento
# de cada lado deve ser menor que a soma dos outros dois.

def pode_formar_triangulo(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False

def main():
    a = float(input("Digite o comprimento do primeiro segmento: "))
    b = float(input("Digite o comprimento do segundo segmento: "))
    c = float(input("Digite o comprimento do terceiro segmento: "))


    if pode_formar_triangulo(a, b, c):
        print("Os segmentos podem formar um triângulo.")
    else:
        print("Os segmentos não podem formar um triângulo.")

if __name__ == "__main__":
    main()