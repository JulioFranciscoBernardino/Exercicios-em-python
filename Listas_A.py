def obter_numeros():
    """Obtém números do usuário até que ele digite "Fim".

    Retorna:
        Uma lista de números digitados pelo usuário.
    """
    numeros = []
    while True:
        
        numero = input("Digite um número ou digite 'Fim' para terminar: ")
        if numero == "Fim":
            break
        
        try:
            numeros.append(float(numero))
        except ValueError:
            print("Dado invalido. Por favor, digite um número.")
    
    return numeros

def calcular_estatisticas(numeros):
    """Calcula a média, o valor maior e o menor de uma lista de números.

    Args:
        numeros: Uma lista de números.

    Retorna:
        A média, o valor maior e o menor.
    """
    media = sum(numeros) / len(numeros)
    maximo = max(numeros)
    minimo = min(numeros)

    return media, maximo, minimo

def exibir_resultados(numeros, media, maximo, minimo):
    """Exibe os números, a média, o valor máximo e o mínimo.

    Args:
        numeros: Uma lista de números.
        media: A média dos números.
        maior: O valor maior dos números.
        menor: O valor menor dos números.
    """
    print("Os números são:")
    print(", ".join(f"{n:.1f}" for n in sorted(numeros)))
    print(f"O menor é {minimo:.1f} e o maior é {maximo:.1f}")
    print(f"A média é {media:.1f}")

if __name__ == "__main__":
    numeros = obter_numeros()
    media, maximo, minimo = calcular_estatisticas(numeros)
    exibir_resultados(numeros, media, maximo, minimo)