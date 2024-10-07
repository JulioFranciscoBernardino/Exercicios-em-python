def main():
    real = pega_valor()
    dolar = transformer(real)
    imprime_dolar(dolar)


def pega_valor():
    real = float(input('Digite quantos reais você possui: '))
    return real


def transformer(real):
    dolar = real / 5.45
    return dolar


def imprime_dolar(dolar):
    print(f'A quantidade do câmbio trocado é ${dolar: .2f}') 

if __name__ == "__main__":
    main()