# Crie um código que recebe do usuário uma frase e retorna a frase cifrada de acordo com o sistema Zenit-Polar: https://pt.wikipedia.org/wiki/Zenit_Polar

# Ao executar o programa, ele deve solicitar para o usuário escrever uma frase e então o programa imprime a frase cifrada. Por exemplo:

# python3 cifra.py
# Digite uma frase a ser cifrada: Exercício de python
# Oxotcácae do zyrhel

# Envie um arquivo com o seguinte nome:

# ex_1_<NOME_COMPLETO_COM_UNDERLINE>.txt

# Por exemplo, eu entregaria o seguinte arquivo:

# ex_1_Yuri_Alexandre_Aoto.txt

def main():
    frase = obtem_frase()
    frase_cifrada = cifra_frase(frase)
    imprime_frase_cifrada(frase_cifrada)

def obtem_frase():
    frase = input("Digite uma frase a ser cifrada: ")

    print(f'A frase a ser cifrada é: {frase}')
    print('----------------------------------')

    return frase

def cifra_frase(frase):
    zenit, polar = 'zenit', 'polar'
    mensagem_cifrada = ''

    for letra in frase: #faz o loop na frase inteira
        if letra in zenit:
            indice = zenit.find(letra)
            mensagem_cifrada += polar[indice]
        elif letra in polar:
            indice = polar.find(letra)
            mensagem_cifrada += zenit[indice]
        else:
            mensagem_cifrada += letra

    return mensagem_cifrada

def imprime_frase_cifrada(frase_cifrada):
    print(f'A frase cifrada é: {frase_cifrada}')


if  __name__ == "__main__":
    main()
