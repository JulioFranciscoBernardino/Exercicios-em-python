#7) Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a
#sua terça parte.
#Ex:
#Digite um número: 3.5
#O dobro de 3.5 é 7.0
#A terça parte de 3.5 é 1.16666

def main():
    num = float(input('Digite um número: '))
    dobro = num * 2
    terceira_parte = num / 3
    print(f"O dobro de {num} é {dobro:.2f}")
    print(f"A terça parte de {num} é {terceira_parte:.4f}")
    
if __name__ == "__main__":
    main()